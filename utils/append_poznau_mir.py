import utils.text_io as io
import re


FILES_DIR = 'datasets/raw_poznau_mir'
TARGET = 'datasets/dataset_1.txt'

files = io.read_dir(FILES_DIR)

print('Reading files: ', files)

io.clear_file(TARGET)

for file in files:
    text = io.read_from_file(FILES_DIR + '/' + file)
    text = re.sub('\[.*?\]', ' ', text)
    text = re.sub('(\[|\(|\]|\)|\{|\})', ' ', text)
    text = re.sub('Взято из Флибусты, http(.*?)\n', ' ', text)
    text = re.sub('(,|\.|\?|!)', ' ', text)
    text = re.sub('image l: href = "#\w+\.?\w+"', ' ', text)
    text = re.sub('("|\'|«)', ' ', text)
    text = re.sub(' - ', ' ', text)
    b = str.encode(text)
    text = b.decode('utf-8').lower()
    io.append_to_file(TARGET, text)
