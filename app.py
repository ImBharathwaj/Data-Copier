import pandas as pd
import os
from read import get_json_reader
from write import load_db_table


def main():
    pass

def orders_db():
    BASE_DIR = '/home/bharathwaj/Code/DE-Sandbox/Data-Copier/retail_db_json/'
    table_name = 'orders'
    file_name = os.listdir(f'{BASE_DIR}{table_name}')

    # if os.listdir(f'{BASE_DIR}{table_name}'):
    fp = f'{BASE_DIR}{table_name}/{file_name[0]}'

    conn = 'postgresql://postgres:root@localhost:5432/retail_db'
    json_reader = pd.read_json(fp, lines=True, chunksize=1000)

    for df in json_reader:
        min_key = df['order_id'].min()
        max_key = df['order_id'].max()
        df.to_sql(table_name, conn, if_exists='append', index=False)
        print(f'Processed {table_name} with in the range odd {min_key} and {max_key}')


if __name__ == '__main__':
    main()
