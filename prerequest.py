from pylog import Pylog
from httprequest import HttpRequest
import config
import re
import json
import csv
import time

class PreRequest:
    def __init__(self):
        self.httpRequest = HttpRequest()

    def request(self,data):
        mode = config.get_config("mode", "mode")
        if mode == "upload":
            self.upload(data)
        elif mode == "normal":
            self.normal(data)
        elif mode == "verifygame":
            if config.get_config("verifygame","step") == "1":
                self.verify_1(data)
            elif config.get_config("verifygame","step") == "2":
                self.verify_2(data)


    def normal(self,jsondata):
        Pylog.info("".join(jsondata.keys()) + ": 开始测试")
        for k,v in jsondata.items():
            url = "http://" + config.get_config("normal","url")+ v["url"]
            method = v["method"]
            data = v["data"]
            self.reps = self.httpRequest.post(url=url, data=data) if method == "POST" else  self.httpRequest.get(url=url, data=data)
            Pylog.debug("Request Body:" + str(self.reps.request.body))
            Pylog.debug("Response:" + self.reps.text)

    def upload(self,filename=None):
        Pylog.info(filename + ": 开始上载")
        try:
            src = config.get_config("upload", "src")
            savefile = config.get_config("upload","savefile")
            savename = re.findall('E:/OtherFile/(.*)', src, re.S)[0]
            idfile = savefile + savename + '.csv'
            url = "http://img.will888.cn/photo/upload"
            files = {'pic': open(filename, 'rb')}
            self.reps = self.httpRequest.upload(url=url, files = files)
            Pylog.debug("Response:" + self.reps.text)
            pic = json.loads(self.reps.content)
            #CSV写入
            csvfile = open(idfile,'a',encoding='utf8',newline='')
            writer = csv.writer(csvfile)
            picId = pic["picid"]
            picname = re.findall(src+'/(.*)', filename, re.S)
            writer.writerow([picname[0], picId])
            csvfile.close()
        except Exception  as e:
            Pylog.error(e)

    def verify_1(self, data):
        game = config.get_config("verifygame","game")
        urlfile = config.get_config("verifygame","urlfile")
        Pylog.info(data)
        datas = {"id":data}
        self.httpRequest.headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                    "Authorization": "MAuth-870fc3d727723a7410d2c0fa15154072cdb9300e9a54f89e09b9a27d32f852a44fd07348ae46208298303f281bcdc9a9079fa0b79310115038b4071b44edbe42-MAuth",
                                    "X-APP-ID": "20"}
        url = "http://" + config.get_config("normal", "url") + "/v1/config/kd/game/start"
        self.reps = self.httpRequest.post(url=url, data=datas)
        Pylog.debug("Request Body:" + str(self.reps.request.body))
        Pylog.debug("Response:" + self.reps.text)

        csvfile = open(urlfile+'/'+game+'.csv','a',encoding='utf8',newline='')
        writer = csv.writer(csvfile)
        #正则表达式
        gameurl = re.findall("action='(.*)'>        </form>", self.reps.text, re.S)
        writer.writerow([data, gameurl[0]])
        csvfile.close()

    def verify_2(self,data):
        Pylog.info(list(data.keys())[0])
        game_id = list(data.keys())[0]
        game_url = data[game_id]
        self.httpRequest.headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                    "Authorization": "MAuth-870fc3d727723a7410d2c0fa15154072cdb9300e9a54f89e09b9a27d32f852a44fd07348ae46208298303f281bcdc9a9079fa0b79310115038b4071b44edbe42-MAuth",
                                    "X-APP-ID": "20"}
        self.reps = self.httpRequest.get(url=game_url)
        Pylog.debug("Request Body:" + str(self.reps.request.body))
        # Pylog.debug("Response:" + self.reps.text)


if __name__ == "__main__":
    PreRequest().request({"业主站点信息": {
		"url": "/v1/cms/site/getinfo",
		"method": "GET",
		"data": {}
    }})