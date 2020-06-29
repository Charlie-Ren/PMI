import csv
def csv_writer(path,list,label):
    with open(path,'a+') as csvfile:
        fieldname=['word','label']
        writer=csv.DictWriter(csvfile,fieldnames=fieldname)
        for word in list:
            dict={'word':word,'label':label}
            writer.writerow(dict)