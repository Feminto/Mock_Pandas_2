import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # this would give the product id that were sold outisde the date range we are interested in
    condition = sales[((sales['sale_date'] < '2019-01-01') | (sales['sale_date'] > '2019-03-31'))][['product_id']]
    
    # this give the unique product_ids from our sales table
    df = sales[['product_id']].drop_duplicates()

    # filtering out the product ids from sales table which falls within the data range of interest
    df = df[~df['product_id'].isin(condition['product_id'])]

    # joining the final list of product_id/s with product table to capture the product name
    result = df.merge(product, on = 'product_id', how = 'inner')

    return result[['product_id','product_name']]