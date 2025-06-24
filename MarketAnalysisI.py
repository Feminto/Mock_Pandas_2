import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    # capturing the buyer_id and item_id from orders table which falss within the year 2019
    order = orders[(orders['order_date'] >= '2019-01-01') & (orders['order_date'] <= '2019-12-31')][['buyer_id','item_id']]
    # taking the count of items for each user
    order = order.groupby('buyer_id')['item_id'].count().reset_index()
    # print(order)

    # joining the users table to capture all user_ids and their joining_date along with the count of items
    user = users.merge(order, left_on = 'user_id', right_on = 'buyer_id', how = 'left')

    df = user[['user_id','join_date','item_id']]
     # fill the NA values with 0 against the users who does not have any items in 2019
    df['item_id'].fillna(0, inplace = True)

    return df.rename(columns = {'user_id':'buyer_id','item_id':'orders_in_2019'})