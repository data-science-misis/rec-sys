import pandas as pd

DATASET_FILE_PATH = '../data/dataset.plk'
POPULAR_WINES_DATASET_FILE_PATH = '../data/sorted_popular_wines.plk'

df = pd.read_pickle(DATASET_FILE_PATH)
df['id'] = df.index

popular_wines = pd.read_pickle(POPULAR_WINES_DATASET_FILE_PATH)
popular_wines['id'] = popular_wines.index


def database():
    return df


def popular():
    return popular_wines
