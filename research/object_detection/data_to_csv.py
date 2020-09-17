# json_to_csv.py
# -*- coding: utf-8 -*-

import os, sys
# glob是一个可以用* ? []来匹配寻找文件的模块
import glob
import pandas as pd
import json



# 将txt文件中的数据转过来
def txt_to_csv(_path, _out_file):  #参数是json文件的路径，输出csv文件的路径
    # 这个list装载json数据集的那些标签
    json_list = []

    # dict_keys(['info', 'lincenses', 'images', 'type', 'annotations', 'categories'])
    # {'area': 120552.21823795195, 'iscrowd': 0, 'image_id': 'd2a8747107a0', 'bbox': [768.23616, 165.66984, 454.79423999999983, 265.0698], 'category_id': 101}
    
    f = open(_path)               # 返回一个文件对象 
    line = f.readline()          # 调用文件的 readline()方法 
    while line: 
        element=line[:-1].split(' ')
        filename=element[0].split('/')[-1]
        # label是一个列表
        labels=element[1].split(',')
        values=(
            filename,
            1920,1080,
            labels[-1],
            labels[0],
            labels[1],
            labels[2],
            labels[3]
        )
        json_list.append(values)
        line = f.readline() 
 
    f.close()

    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    # ataFrame的单元格可以存放数值、字符串等，这和excel表很像，同时DataFrame可以设置列名columns与行名index。
    xml_df = pd.DataFrame(json_list, columns=column_name)
    # pd的DataFrame对象可以调用to_csv文件（保存文件名）
    xml_df.to_csv(_out_file, index=None)
    print('Successfully converted to csv.')


if __name__ == '__main__':
    # convert
    txt_to_csv("train_label.txt","data.csv")