import pandas as pd

def load_and_merge_data():
    sm = pd.read_csv('data/social_media.csv')
    mu = pd.read_csv('data/mobile_usage.csv')
    up = pd.read_csv('data/utility_payments.csv')
    target = pd.read_csv('data/loan_status.csv')
    
    data = sm.merge(mu, on='id').merge(up, on='id').merge(target, on='id')
    return data
