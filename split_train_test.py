import glob
import os
from shutil import copy
from random import shuffle
import pandas as pd
import xml.etree.ElementTree as ET


def split_xml():
    path = 'samples/gull'
    train_path = os.path.join(path, 'positive_xml', 'train')
    test_path = os.path.join(path, 'positive_xml', 'test')

    os.makedirs(train_path, exist_ok=True)
    os.makedirs(test_path, exist_ok=True)

    filelist = glob.glob(path + '/positive_xml/full/*.xml')
    shuffle(filelist)

    for i, filename in enumerate(filelist):
        if i % 3 == 0:
            copy(filename, os.path.join(test_path, os.path.basename(filename)))
            print(i, ' Test ', filename)
        else:
            copy(filename, os.path.join(train_path, os.path.basename(filename)))
            print(i, ' Train ', filename)


def xml_to_csv(train_or_test):
    path = os.path.join(os.getcwd(), 'samples/gull/positive_xml', train_or_test)
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
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
    xml_df.to_csv('{train_or_test}_gull_labels.csv'.format(train_or_test=train_or_test), index=None)

split_xml()
xml_to_csv('train')
xml_to_csv('test')
