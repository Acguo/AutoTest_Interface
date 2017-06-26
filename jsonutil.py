# -*- coding: UTF-8 -*-
import json

class JsonUtil:
    def __init__(self):
        pass

    #生成json文件
    def store(self,data=None,file=None):
        with open(file, 'w') as json_file:
            json_file.write(data)
            json_file.close()

    #读取json文件
    def load(self,file=None):
        with open(file,encoding='UTF-8') as json_file:
            data = json.load(json_file)
            return data

    #比较json字段
    def cmp_dict(self,src_data, dst_data):
        assert type(src_data) == type(dst_data), "type: '{}' != '{}'".format(type(src_data), type(dst_data))
        if isinstance(src_data, dict):
            assert len(src_data) == len(dst_data), "dict len: '{}' != '{}'".format(len(src_data), len(dst_data))
            for key in src_data:
                assert key in dst_data
                self.cmp_dict(src_data[key], dst_data[key])
        elif isinstance(src_data, list):
            assert len(src_data) == len(dst_data), "list len: '{}' != '{}'".format(len(src_data), len(dst_data))
            # src_data.sort(key=lambda x: (x["dict_no_type_id"], x["bet_count"]))
            # dst_data.sort(key=lambda x: (x["dict_no_type_id"], x["bet_count"]))
            for src_list, dst_list in zip(src_data, dst_data):
                self.cmp_dict(src_list, dst_list)
        else:
            assert src_data == dst_data, "value '{}' != '{}'".format(src_data, dst_data)

if __name__ == "__main__":
    pass