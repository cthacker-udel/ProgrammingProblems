import psycopg2

def postgres_test(dbname, user, host, password):
    try:
        conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}' connect_timeout=1".format(dbname, user, host, password))
        cursor = conn.cursor()
        rows = cursor.fetchall()

        for table in rows:
            print(table)
        conn.close()
        print("connected!")
    except:
        print("Did not connect")


if __name__ == '__main__':
    dbname = ''
    user = ''
    password = ''
    host=''
    postgres_test(dbname, user, host, password)
