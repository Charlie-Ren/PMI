from read_csv import read_csv
import logging
import argparse
from pmi_process import get_frequency,get_all_frequency
from csv_writer import csv_writer
import csv
import synonyms
logging.basicConfig(level=logging.DEBUG)
path = '/Users/charilie/Desktop/PMI/l1.csv'
if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("--dict",dest="dict",action="store_true",default=False)
    parser.add_argument("--enlarge", dest="enlarge", action="store_true", default=False)
    args=parser.parse_args()
    if args.dict:
        labelset = read_csv(path)
        logging.debug(labelset)
        dict_all = get_all_frequency(path)  # 所有词的字典
        for label in labelset:
            res_list = get_frequency(path, label, dict_all)
            csv_writer('pmi_dict_l1.csv', res_list, label)
    if args.enlarge:
        dict_path="pmi_dict_l1.csv"
        output_path="l1_enlarged_dict.csv"
        with open(dict_path,'r',encoding='utf-8-sig') as csvfile: #完美解决ufeff
            reader=csv.DictReader(csvfile)
            for line in reader:
                word=line['word']
                word_label=line['label']
                word_list=synonyms.nearby(word)[0]
                csv_writer(output_path,word_list,word_label)#把每个同义词都写进去



