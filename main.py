from read_csv import read_csv
import logging
from pmi_process import get_frequency,get_all_words
from csv_writer import csv_writer
logging.basicConfig(level=logging.DEBUG)
path = '/Users/charilie/Desktop/PMI/l1.csv'
if __name__ == '__main__':
    labelset=read_csv(path)
    logging.debug(labelset)
    dict_all = get_all_words(path) #所有词的字典
    res_list = get_frequency(path, '疑似财务风险', dict_all)
    csv_writer('pmi_dict.csv',res_list,'疑似财务风险')

