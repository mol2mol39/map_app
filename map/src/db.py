import psycopg2

connector =  psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'.format( 
                user="postgres",        #ユーザ
                password="postgres",  #パスワード
                host="map-db",       #ホスト名
                port="5432",            #ポート
                dbname="postgres"))    #データベース名

print(connector)
cursor = connector.cursor()
    
cursor.execute("SELECT version();")
result = cursor.fetchone() 
    
print(result[0]+"に接続しています。")
