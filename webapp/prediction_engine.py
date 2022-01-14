import pandas as pd

from data_provider import database, popular

MAX_RECOMMENDATION_COUNT = 100


def predict_popular(k=10):
    n = min(k, MAX_RECOMMENDATION_COUNT)

    return popular()[:n]


def get_user_ids():
    return database()['user_id'].unique().tolist()


def predict_collaborative_filtering(user_id, k=10):
    return pd.DataFrame()
