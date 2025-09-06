from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
import numpy as np
import pandas as pd
# from utils.constants import CLIENT_ID, SECRET

CLIENT_ID = "Enter your client ID"
SECRET = "Enter your secret key"
OUTPUT_PATH = "/opt/airflow/data/output"


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    # Connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    
    # Extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    
    
    # transformation
    post_df = transform_data(post_df)
    # loading to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df, file_path)

    return file_path
    
    
    # Loading to CSV