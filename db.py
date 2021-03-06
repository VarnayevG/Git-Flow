import pandas as pd


def create_db(db_name: str):
    """

    Creates database as a csv file
    with name and mood columns

    Parameters:
        db_name: database name

    """
    df = pd.DataFrame(columns=["name", "mood"])
    df.to_csv(db_name)


def write_to_db(db_name: str, name: str, mood: str):
    
    """

    Writes name and mood to database
    
    Parameters:
        db_name: database name
        name: person's name
        mood: person's mood
        
    """
    df = pd.read_csv(db_name)
    data = pd.DataFrame({"name": name, "mood": mood}, index=[0])
    df = pd.concat([df, data])
    df.to_csv(db_name)
