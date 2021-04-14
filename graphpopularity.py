import pandas as pd
import numpy as np

def loading():
    fl = open("baby-names-by-state.csv", "r")
    df = pd.read_csv(fl)
    return df

def filter_name():
    pass

def create_graph():
    pass

if __name__=="main":
    df = loading()