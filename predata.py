# -*- coding: UTF-8 -*-
import config
from pylog import Pylog
from jsonutil import JsonUtil
import os
import csv
from database import DataBase

class Predata:
    def __init__(self):
        pass

    def get_data(self):
        mode = config.get_config("mode", "mode")
        if mode == "normal":
            return self.get_JsonList()
        elif mode == "upload":
            return self.upload_data()
        elif mode == "verifygame":
            return self.get_gameid()


    #获取json list
    def get_JsonList(self):
        runfile = config.get_config("normal", "runfile")
        jsonlist = []
        if runfile == "allfile":
            pathDir = os.listdir("./InterfaceJson")
            # 遍历文件夹中所有文件
            for allDir in pathDir:
                # 读取文件中json
                jsons = JsonUtil().load("./InterfaceJson/" + allDir)
                Pylog.info("导入接口文件：" + allDir)
                for key in jsons:
                    jsonlist.append({key: jsons[key]})
            return jsonlist
        else:
            jsons = JsonUtil().load("./InterfaceJson/" + runfile)
            Pylog.info("导入接口文件：" + runfile)
            for key in jsons:
                jsonlist.append({key: jsons[key]})
            return jsonlist

    #获取上传文件list
    def upload_data(self):
        lists = []
        src = config.get_config("upload", "src")
        pathDir = os.listdir(src)
        for allDir in pathDir:
            child = os.path.join('%s%s' % (src + "/", allDir))
            lists.append(child)
        return lists

    def get_gameid(self):
        step = config.get_config("verifygame","step")
        game = config.get_config("verifygame","game")
        urlfile = config.get_config("verifygame", "urlfile")
        if step == "1":
            switch ={"MG":"10001","AG":"10022","BBIN":"10012"}
            sql = "select game_id from t_owner_game where game_provider_id = "+switch[game]
            ids = DataBase().inquire_data(sql,"cms")
            Pylog.info(game+"id个数： "+ str(len(ids)))
            return ids

        elif step == "2":
            with open(urlfile+'/'+game+'.csv','r') as var_file:
                reader = csv.reader(var_file)
                rows = [{row[0]:row[1]} for row in reader]
                Pylog.info(game + "url个数： " + str(len(rows)))
            return rows

if __name__ == "__main__":
    s = Predata().get_data()
    print(s)
