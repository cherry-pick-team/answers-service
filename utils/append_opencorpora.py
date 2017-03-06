import xml.etree.ElementTree as ET


XML_DIR = 'datasets/raw_opencorpora/annot.opcorpora.xml'
TARGET = 'datasets/dataset_3.txt'

tree = ET.parse(XML_DIR)
root = tree.getroot()


for child in root:
    print(child.tag, child.attrib)


import wikipedia