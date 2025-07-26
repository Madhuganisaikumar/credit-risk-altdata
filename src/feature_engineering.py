def engineer_features(df):
    df['engagement'] = df['posts_per_day'] * df['likes_per_post']
    df['payment_ratio'] = df['on_time_payments'] / (df['late_payments'] + 1)
    df['usage_index'] = df['data_used_gb'] + df['call_minutes'] / 60
    return df
