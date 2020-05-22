import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",passwd='asusv8200',database='dailybudget')

cursor=db.cursor()

def list_all(*args):
    cursor.execute("select {} from {} join {} group by {} order by {} asc".format(*args))
    data_list_all=cursor.fetchall()
    return data_list_all
    # for i in data_list_all:
    #     print(i)
def list_table(*args):
    cursor.execute("select {} from {}".format(*args))
    data_list_all = cursor.fetchall()

    for i in data_list_all:
        return i

def insert_data(table,arguments,values): #Arguments and values must be comma separeted.
    cursor.execute("insert into {} ({}) values({})".format(table,arguments,values))
    db.commit()

def insert_t_date_budget(sql_date_insert,budget):
    sql1="insert into t_date(day,month,year) values({})".format(sql_date_insert)
    cursor.execute(sql1)

    sql2="insert into budget(idbudget,budget) values('{}',{})".format(int(cursor.lastrowid),budget)
    cursor.execute(sql2)

    db.commit()


def ai_truncate(table): # to use before insert statement into t_date in order to reset ai to 1
    sql='alter table {} auto_increment=1'.format(table)
    cursor.execute(sql)
    db.commit()

def delete_all(table):

    sql='delete from {}'.format(table)
    cursor.execute(sql)
    db.commit()

def delete_specific(table,*condition):

    sql='delete from {} where {}={}'.format(table,*condition)
    cursor.execute(sql)
    db.commit()

def count():
    sql="select count(idt_date) from t_date"
    cursor.execute(sql)
    rows=cursor.fetchall()
    for i in rows[0]:
        return i ## type integer

def same_entry_check(day,month):
    sql="select day,month from t_date where day={} and month={}".format(day,month)
    cursor.execute(sql)
    res=cursor.fetchall()
    return res

def update_budgetdata(day,month,new_amount):
    sql1="select idt_date from t_date where day={} and month={}".format(day,month)
    cursor.execute(sql1)
    idt_date=cursor.fetchall()

    _idt_date = [item for t in idt_date for item in t]
    id_table=None
    for i in _idt_date:
        id_table= i # returns an integer value.



    sql2="update budget set budget = {} where idbudget = {}".format(new_amount,id_table)
    cursor.execute(sql2)
    db.commit()

def b_amount():
    sql="select budget from budget"
    cursor.execute(sql)
    budget_amount=cursor.fetchall()
    return budget_amount

def print_days():
    sql="select day from t_date order by t_date.day asc"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

    #for i in rows:
    #    return i  ## type integer

def b_amount_sorted(): # sorted by date, to get correct day, amount correspondance.
    sql="select budget from t_date join budget where idt_date = idbudget group by day order by t_date.day asc"
    cursor.execute(sql)
    budget_sorted=cursor.fetchall()
    return budget_sorted

def close_connection():
    db.close()

#delete_all('t_date')

#ai_truncate('t_date')

#insert_data('t_date','day,month,year','04,05,2020')
#print(list_all('*','t_date','budget'))
#insert_t_date_budget('17,05,2020','11')


#print(list_all('day,month,year,budget','t_date','budget where idt_date=idbudget'))
#
# am=list_all('day,month,year,budget','t_date','budget where idt_date=idbudget')
# print(am[0][2])


#print(list_table('*','t_date'))
#insert_t_date_budget('06,05,2020','20')
#insert_t_date_budget('07,05,2020','12')

#print(count())
#days=count()


#days = count()


#print(days)



#
#
#
# self.y nin yerine koyacagin amountlari liste halinde yaz:
# y:  [11.45, 14.29, 14.29, 14.29, 17.62, 17.62, 23.08, 34.48]
#
# data=b_amount()
#
# out=[item for t in data for item in t]
# print(out)
# Yukardakinin aynisi
# l=[]
# for item in data:
#     for t in item:
#         l.append(t)
#         #print(l)
# print(l)


#db.close()