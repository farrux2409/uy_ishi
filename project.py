import psycopg2

host = 'localhost'
user = 'postgres'
password = '123'
database = 'n42'
port = 5432

connection = psycopg2.connect(host=host,
                              user=user,
                              password=password,
                              database=database,
                              port=port)
cur = connection.cursor()

# example for drop table
# delete_table_query = '''
# drop table if exists costumers;
# '''
# cur.execute(delete_table_query)
# connection.commit()
# #
# update_table_query = '''
# update costumers
# set costumer_name = 'Jane'
# where costumer_id  = 3
# '''
# cur.execute(update_table_query)
# connection.commit()

# example for insert
# insert_query = '''
#     insert into costumers(costumer_name,costumer_email,gender)
#       values('John','ziyodulla@gmail.com','Male')
# '''
# cur.execute(insert_query)
# connection.commit()

# example for select
# select_costumers = '''
#
# select * from costumers order by gender;
#
#
#
#
# '''
# cur.execute(select_costumers)
# for i in cur.fetchall():
#     print(i)
