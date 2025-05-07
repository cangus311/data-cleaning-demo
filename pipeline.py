import pandas as pd

def read_data(filepath):
    return pd.read_csv(filepath) # loads file as a dataframe
      # return function is here so that we can work with it


def clean_data(df):
    df = df.dropna()  # drop rows with actual NaN
    df = df[df['email'].str.strip() != '']  # remove rows where email is an empty string
    df = df.copy()  # makes a new copy of the dataframe
    df['name'] = df['name'].str.strip()
    return df


def save_data(df, filepath):
    df.to_csv(filepath, index=False) #index is part of pandas, this says don't include the index in the output file

if __name__ == '__main__':  # this is how the file is named when run in this script
    df = read_data('raw_users.csv')   #calls read_data function
    cleaned_df = clean_data(df)       # calls clean_data function
    save_data(cleaned_df, 'cleaned_users.csv')    # calls save_data function, saves result to new file
