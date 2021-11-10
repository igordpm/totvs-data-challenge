import pandas as pd

###
# This script serves as a sidefile to store user-functions generated in the notebooks.
# Functions will be added here as they are created.
###

def import_and_preprocess():
    """
    Import both .json files and preprocess them.
    
    The preprocessing step is thoroughly explained in the notebook `data_analysis.ipynb`.

    The output is: dataframe_of_churn_data, dataframe_of_orders_data

    Returns
    -------
    pandas.DataFrame, pandas.DataFrame
        Dataframes of preprocessed churn and orders data, respectively.
    """
    churn_data = pd.read_json('../data/challenge/is_churn.json', dtype={'last_purchase_date': 'datetime64'})
    churn_data.last_purchase_date = pd.to_datetime(churn_data.last_purchase_date.dt.date)
    churn_data = (
        churn_data
        .query("last_purchase_date > '2018-01-01'")
        .sort_values('last_purchase_date')   # added this line since chronology is important for churn prediction
        .reset_index(drop=True)
    )
    orders_data = pd.read_json('../data/challenge/orders.json')   # starts preprocessing of `orders_data`
    orders_data = (
        orders_data
        .query('customer_code in @churn_data.customer_code.unique()')
        .drop(columns=['branch_id'])
        .astype({'register_date': 'datetime64'})
        .sort_values('register_date')   # added this line since chronology is important for churn prediction
        .reset_index(drop=True)
    )
    return churn_data, orders_data

