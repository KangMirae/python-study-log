import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    rs = orders.groupby('customer_number')['order_number'].count().reset_index()
    max_count = rs['order_number'].max()
    return rs[rs['order_number'] == max_count][['customer_number']]