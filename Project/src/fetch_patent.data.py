# Placeholder: Replace with real patent data extraction via PatentsView or USPTO XML parsing
import pandas as pd

def load_patent_activity(file_path):
    df = pd.read_csv(file_path)
    # Columns: ['date', 'company', 'num_patents', 'num_categories', 'num_new_categories']
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df