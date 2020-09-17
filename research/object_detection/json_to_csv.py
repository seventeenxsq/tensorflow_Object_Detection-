# -*- coding: utf-8 -*-
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
 
#用于改变当前工作目录到指定的路径。
#os.chdir('/home/xuyifang/Desktop/API/research/data_prepare/train/')
os.chdir('/home/xuyifang/Desktop/image/')
 
#图片路径
#path = '/home/xuyifang/Desktop/API/research/data_prepare/train'
path = '/home/xuyifang/Desktop/image/test'
 
def json_to_csv(path):
    counter = 0
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        counter = counter + 1
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
			
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    print(xml_df)
    print('执行',counter,'次！')
    return xml_df
 
 
def txt_to_csv():

    list_data=[]
    for line in open("foo.txt"): 
        print line, 



def main():
    image_path = path
    xml_df = json_to_csv(image_path)
#    xml_df.to_csv('arthritis_test.csv', index=None)
    xml_df.to_csv('arthritis_test.csv', index=None)
    print('Successfully converted xml to csv.')
 
 
main()