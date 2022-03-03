import pandas as pd


def create_db(db_name):
    df = pd.DataFrame(columns=["name", "mood"])
    df.to_csv(db_name, index=False)