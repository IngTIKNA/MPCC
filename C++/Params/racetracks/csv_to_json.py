import pandas as pd 
import numpy as np 
import json 
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("address_mapFile")
args = parser.parse_args()

df = pd.read_csv(args.address_mapFile)
data = {}


data["X"]= np.array(df["X"]).tolist()
data["Y"]= np.array(df["Y"]).tolist()
data["X_i"]= np.array(df["X_inner"]).tolist()
data["Y_i"]= np.array(df["Y_inner"]).tolist()
data["X_o"]= np.array(df["X_outter"]).tolist()
data["Y_o"]= np.array(df["Y_outter"]).tolist()


with open( args.address_mapFile.split(".")[0] +'.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
