from operator import index
import pandas as pd


def create_db(db_name):
    df = pd.DataFrame(columns=["name", "mood"])
    df.to_csv(db_name, index=False)


def write_to_db(db_name, name, mood):
    df = pd.read_csv(db_name)
    df['name'] = name
    df['mood'] = mood
    df.to_csv(db_name, index=False)
