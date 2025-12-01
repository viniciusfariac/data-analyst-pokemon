def clear_data(df):
    df = df.copy()

    df["name"] = df["name"].str.title()
    
    df = df.drop_duplicates(subset="id")

    df = df.sort_values("id")

    print(df)
    return df