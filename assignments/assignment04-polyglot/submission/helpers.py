import pandas as pd


def summarise_bmi(df):
    d = df.dropna(subset=["BMI", "IncomeGroup"])
    out = (d.groupby(["IncomeGroup", "Gender"])["BMI"]
             .agg(n="count", mean_bmi="mean", sd_bmi="std", median_bmi="median")
             .round(2).reset_index()
             .sort_values(["IncomeGroup", "Gender"]))
    return out

def summarise_bmi(df):
    d = df.dropna(subset=["BMI", "IncomeGroup"])
    out = (d.groupby(["IncomeGroup", "Gender"])["BMI"]
             .agg(n="count", mean_bmi="mean", sd_bmi="std", median_bmi="median")
             .round(2).reset_index()
             .sort_values(["IncomeGroup", "Gender"]))
    return out