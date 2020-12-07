import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(fname, place, val):
    
    df = pd.read_csv(fname, sep="|")
    df["base_de"] = pd.to_datetime(df["base_de"], format="%Y%m%d")
    
    group_df = df.groupby(["fclty_nm", "base_de"])[val].sum().unstack()
    # train_df = group_df.loc[place, :"2020-08-31"]
    train_df = group_df.loc[place, :"2020-08-31"]
    
    df = pd.DataFrame(train_df)

    return df

def day2month(df, place):

    return df[place].resample('MS').mean()

x = 1