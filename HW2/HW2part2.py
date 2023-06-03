import pandas as pd


def calculate_average():
    df = pd.read_csv('hw.csv')
    result = df.sum()/df.shape[0]
    print(result)
    return result

calculate_average()


