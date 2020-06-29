import csv
def read_csv(path):
    '''
    读取csv中标签的数量.
    :param path:
    :return:
    '''
    with open(path,'r') as csvfile:
        reader=csv.DictReader(csvfile)
        label_set = set()
        for line in reader:
            label_set.add(line['label2'])
        return label_set
