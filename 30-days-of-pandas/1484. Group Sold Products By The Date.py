import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities.drop_duplicates(inplace=True)
    activities.sort_values(['sell_date', 'product'], inplace=True)
    rs = activities.groupby('sell_date')['product'].agg(['count', ','.join]).reset_index()
    rs.columns = ['sell_date', 'num_sold', 'products']
    return rs.sort_values('sell_date')