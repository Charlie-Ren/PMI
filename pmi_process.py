import jieba
import csv
import math
import numpy as np

def get_all_words(path):
    with open(path, 'r') as csvfile:
        dict_all = {}
        reader = csv.DictReader(csvfile)
        for line in reader:
            sentence = line['text']
            word_list = list(jieba.cut(sentence,cut_all=True))
            for word in word_list:  # 先读取所有的字典并取出数值
                if word in dict_all:
                    dict_all[word] += 1
                else:
                    temp_dict = {word: 1}
                    dict_all.update(temp_dict)
    all_count = sum(dict_all.values())
    for key in dict_all:
        dict_all[key] = dict_all[key] / all_count  # 词出现的频率
    return dict_all


def get_frequency(path, label,dict_all):  # 根据label来算pmi的值
    with open(path, 'r') as csvfile:
        label_dict = {}
        reader = csv.DictReader(csvfile)
        for line in reader:
            if line['label2'] != label:
                continue
            else:
                sentence=line['text']
                word_list=list(jieba.cut(sentence,cut_all=True))
                for word in word_list:
                    if word in label_dict:
                        label_dict[word]+=1
                    else:
                        temp_dict={word:1}
                        label_dict.update(temp_dict)
                all_count=sum(label_dict.values())
                for key in label_dict:
                    temp_value=label_dict[key]
                    temp_value/=all_count
                    prob=dict_all[key]
                    temp_value/=prob #这个类下的概率除全部的概率
                    if(temp_value<=0): #排除所有为0的
                        label_dict[key]=-100
                        continue
                    temp_value=max((math.log(temp_value,2)),0)
                    label_dict[key]=temp_value
        res=sorted(label_dict.items(),key=lambda item:item[1],reverse=True)#按互信息大小排序, 此时是list
        res=res[:500]#每个取前500个词
        res_dict={}
        for l in res:
            res_dict[l[0]]=l[1]#再转为字典
        res_list=list(res_dict.keys())#只需要词,不需要keyword.
        print(res_list)
        return res_list
#dict_all=get_all_words('/Users/charilie/Desktop/PMI/l1.csv')
#res_dict=get_frequency('/Users/charilie/Desktop/PMI/l1.csv','疑似财务风险',dict_all)

