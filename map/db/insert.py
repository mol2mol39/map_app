import psycopg2
from psycopg2.extras import execute_values
import csv

conn = psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'.format( 
                user="postgres",        #ユーザ
                password="postgres",  #パスワード
                host="map-db",       #ホスト名
                port="5432",            #ポート
                dbname="postgres"))    #データベース名

cur = conn.cursor()

def insert_data_from_csv(table_name, csv_path, column_mapping={}):
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = []
        data = []
        for i, row in enumerate(reader):
            if i == 0:
                header = row
            else:
                data.append(row)

        no_use_columns = []
        if column_mapping:
            new_header = []
            for i, col in enumerate(header):
                if col in column_mapping:
                    new_header.append(column_mapping[col])
                else:
                    no_use_columns.append(i)
            column_text = ','.join(new_header)
        else:
            column_text = ','.join(header)

        query = "INSERT INTO {table} ({columns}) VALUES %s;".format(table=table_name, columns=column_text)
        params = []
        for row in data:
            param = [col for i, col in enumerate(row) if i not in no_use_columns]
            params.append(tuple(param))
        
        ret = execute_values(cur, query, params, page_size=len(params))
        conn.commit()
        cur.close()
        conn.close()

if __name__ == '__main__':
    table_name = 'countries'
    csv_path = 'db/data/country/country_code.csv'
    column_mapping = {
        '国・地域名': 'jp_name',
        'ISO 3166-1における英語名': 'en_name',
        'numeric': 'numeric_code',
        'alpha-3': 'id',
        'alpha-2': 'alpha2',
        '場所': 'area',
        '各行政区分': 'administrative_division'
    }
    insert_data_from_csv(table_name, csv_path, column_mapping)