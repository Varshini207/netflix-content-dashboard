import pandas as pd

def clean_data():
    df = pd.read_csv('../data/netflix_titles.csv')
    
    # 1. Fill missing values
    df['country'] = df['country'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('No Cast')
    
    # 2. Extract Year from date_added
    df['date_added'] = pd.to_datetime(df['date_added'].str.strip())
    df['year_added'] = df['date_added'].dt.year.fillna(0).astype(int)
    
    # 3. Save for the API to use
    df.to_csv('../data/cleaned_netflix.csv', index=False)
    print("Data Cleaned and Saved!")

if __name__ == "__main__":
    clean_data()