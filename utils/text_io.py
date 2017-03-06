import zipfile
import tensorflow as tf
from os import listdir
from os.path import isfile, join


def read_from_file(file_pass, is_zipped = False):
    if is_zipped:
        with zipfile.ZipFile(file_pass) as f:
            return tf.compat.as_str(f.read(f.namelist()[0]))
    else:
        with open(file_pass, 'r') as f:
            return tf.compat.as_str(f.read())


def append_to_file(file_pass, text):
    with open(file_pass, 'a') as f:
        f.write('\n')
        f.write(text)
        f.close()


def clear_file(file_pass):
    open(file_pass, 'w').close()


def read_dir(dir):
    return [f for f in listdir(dir) if isfile(join(dir, f))]

