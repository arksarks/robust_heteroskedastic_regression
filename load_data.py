# -*- coding: utf-8 -*-
# pylint: disable=C0103
"""
@author: Karthik Iyer
"""
import glob
import pandas as pd

def load_data():
    
    print "Loading Data ..,"
    data = {file_: pd.read_csv(file_) for file_ in glob.glob('*.csv')}
    file_names = data.keys()
    print "Finished Loading Data!"
    return data, file_names