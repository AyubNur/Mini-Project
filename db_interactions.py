
from ast import If
from tkinter import END
import pymysql
import os
from dotenv import load_dotenv
from Utilities_used import *


load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
def establish_connection():
    connection= pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = database
    )
    cursor=connection.cursor()
    return connection,cursor



def load_data_products():
    connection,cursor=establish_connection()
    
    cursor.execute("SELECT * FROM product_table");
    product_table=cursor.fetchall()
    products_list=[]
   
    for row in product_table:
        product_dict = { 'product_id': row[0], 'product_name': row[1], 'price': row[2] }
        products_list.append(product_dict)
    
    connection.commit()
    cursor.close()
    return products_list

def load_data_couriers():
    connection,cursor=establish_connection()
    
    cursor.execute("SELECT * FROM courier_table");
    courier_table=cursor.fetchall()
    courier_list=[]

    for row in courier_table:
        courier_dict = { 'courier_id': row[0], 'courier_name': row[1], 'courier_number': row[2] }
        courier_list.append(courier_dict)
    
    connection.commit()
    cursor.close()
    return courier_list


def load_data_orders():
    connection,cursor=establish_connection()
    
    cursor.execute("SELECT * FROM order_table");
    order_table=cursor.fetchall()
    order_list=[]

    for row in order_table:
        order_dict = { 'order_id': row[0], 'customer_name': row[1], 'customer_address': row[2],'customer_phonenumber': row[3],'courier': row[4],'status': row[5],'items': row[6]}
        order_list.append(order_dict)
    
    connection.commit()
    cursor.close()
    return order_list












#2
def write_data_new_products():
    connection,cursor=establish_connection()
    product_name_input=input('new product name ')
    product_price_input=float(input('new product price '))

    sql = f"INSERT INTO product_table (name, price) VALUES (\'{product_name_input}\',{product_price_input})"

    cursor.execute(sql)
    connection.commit()

    # select from product
    cursor.execute("SELECT * FROM product_table");
    product_table=cursor.fetchall()
   
    for row in product_table:
        product_dict = { 'product_id': row[0], 'product_name': row[1], 'price': row[2] }
        print(product_dict)
    cursor.close()

    
#3
def write_data_update_products():
    connection,cursor=establish_connection()
    
    cursor.execute("SELECT * FROM product_table");
    product_table=cursor.fetchall()
   
    # for row in product_table:
    #     product_dict = { 'product_id': row[0], 'product_name': row[1], 'price': row[2] }
    #     product_list=[]
    #     product_list.append(product_dict)


    user_input_product_id=int(input('product id of the product you want to change '))
    # cursor.execute("SELECT * FROM product_table WHERE product_id=user_input_")
    
    user_input_product_name=input('what do you want to add ')
    user_input_product_price=float(input('how much does it cost'))
    # product_list[user_input_product_id]['name']=user_input_product_name
    # product_list[user_input_product_id]['price']=user_input_product_price

    sql = f"UPDATE product_table SET name = '{user_input_product_name}', price = {user_input_product_price} WHERE product_id = {user_input_product_id}"

    cursor.execute(sql)
    connection.commit()

    cursor.close()
    
    

 

#4
def write_data_delete_product():
    #for count,value in enumerate(product_list):
                #print (count,value)
    connection,cursor=establish_connection()
    

    choice_delete_product=int(input('what product do you want delete '))
   

    sql=f"DELETE FROM product_table WHERE product_id={choice_delete_product}"

    cursor.execute(sql)
    connection.commit()
    cursor.close()



#2 new courier
def write_data_new_courier():
    connection,cursor=establish_connection()
    
    
    courier_name_input=input('new courier name ')
    courier_number_input=float(input('new courier number '))

   

    sql = f"INSERT INTO courier_table (name, number) VALUES (\'{courier_name_input}\',{courier_number_input})"

    cursor.execute(sql)
    connection.commit()
    
    cursor.close()

   
#3
def write_data_update_courier():
    #for count,value in enumerate(courier_list):
        #print (count,value)
    connection,cursor=establish_connection()
    
    user_input_courier_id=int(input('which courier do you want to change '))
    user_input_courier_name=input('what do you want the name to be ')
    user_input_courier_price=int(input('couriers number'))
  


    sql = f"UPDATE courier_table SET name = '{user_input_courier_name}', number = {user_input_courier_price} WHERE courier_id = {user_input_courier_id}"

    cursor.execute(sql)
    connection.commit()
    cursor.close()

    


#4 courier
def write_data_delete_courier():
    #indexed_list(courier_list)
    connection,cursor=establish_connection()
    

    choice_delete_courier=int(input('type in courier index of which courier you to want delete?'))
       

    sql=f"DELETE FROM courier_table WHERE courier_id={choice_delete_courier}"

    cursor.execute(sql)
    connection.commit()
    cursor.close()




#2 new order
def write_data_new_order(courier_list):
    connection,cursor=establish_connection()
    
    customer_name_input=input('what is your name ')
    customer_address_input=input('what is your address ')
    customer_phone_number_input=input('what is your phone number ')
    customer_items_input=input('what items are in the order')
    
    for count,value in enumerate(courier_list):
                        print (count,value)

    courier_chosen=input('select courier by selecting courier id ')
    
    
    sql = f"INSERT INTO order_table (customer_name,customer_address,customer_phonenumber,courier,status,items) VALUES (\'{customer_name_input}\',\'{customer_address_input}\',{customer_phone_number_input},{courier_chosen},'Preparing', \'{customer_items_input}\')"

    cursor.execute(sql)
    connection.commit()
    cursor.close()

    cursor.close()

    


  
    

#3 order update existing
def write_data_update_order_status():
    connection,cursor=establish_connection()
    # indexed_list(order_list)
    order_list=load_data_orders()
    print(order_list)
    user_input_order_id=int(input('input for order index value '))
    #print('order status list with index values')
    user_input_order_status=int(input('input for order status '))
    # if user_input_order_status==0:
    #         order_list[user_input_order_id]['status']='Preparing' 
    # if user_input_order_status==1:
    #         order_list[user_input_order_id]['status']='On the way'
            
    # if user_input_order_status==2:
    #         order_list[user_input_order_id]['status']='Delivered'

    sql=f'''UPDATE order_table SET status = CASE
    WHEN  '{user_input_order_status}'=0 THEN 'Preparing'
    WHEN  '{user_input_order_status}'=1 THEN 'On the way'
    WHEN  '{user_input_order_status}'=2 THEN 'Delivered'
    END WHERE order_id={user_input_order_id}'''

    


    # sql=f"UPDATE order_table SET status = If ('{user_input_order_status}'=0,'Preparing' OR '{user_input_order_status}'=1,'On the way' OR '{user_input_order_status}'=2,'Delivered') WHERE order_id={user_input_order_id}"
    # # SET col_Z = IF(col_A = 4 OR col_B = 4, 4, NULL)
    # # WHERE id = "001"
    
    # indexed_list(order_list)
    
    

    # sql = f"UPDATE order_table SET status = '{user_input_order_status}' WHERE order_id = {user_input_order_id}"

    cursor.execute(sql)
    connection.commit()
    cursor.close()

    # return order_list


#4 order
def write_data_update_existing_order(order_status,courier_list,product_list):
    connection,cursor=establish_connection()

    user_input_order_id=int(input('input for order id '))
    
    user_input_updated_name=input('input new name ')
    user_input_updated_address=input('input new address ')
    user_input_updated_phonenumber=int(input('input new phone number '))
    
    indexed_list(courier_list)
    user_input_updated_courier=int(input('input new courier '))
    indexed_list(order_status)
    user_input_order_status=int(input('input new status '))
    product_list=load_data_products()
    print(product_list)
    user_input_order_items=input('update the items')

    # order_list[user_input_order_id]['customer_name']=user_input_updated_name
    # order_list[user_input_order_id]['customer_address']=user_input_updated_address
    # order_list[user_input_order_id]['customer_phonenumber']=user_input_updated_phonenumber
    
    indexed_list(courier_list)

    # order_list[user_input_order_id]['courier']=user_input_updated_courier
    # if user_input_order_status==0:
    #         order_list[user_input_order_id]['status']='Preparing' 
    # if user_input_order_status==1:
    #         order_list[user_input_order_id]['status']='On the way'
            
    # if user_input_order_status==2:
    #         order_list[user_input_order_id]['status']='Delivered'
    # order_list[user_input_order_id]['items']=user_input_order_items


    sql = f'''UPDATE order_table SET customer_name = '{user_input_updated_name}', customer_address='{user_input_updated_address}' ,customer_phonenumber = {user_input_updated_phonenumber},courier = {user_input_updated_courier}, items='{user_input_order_items}',status = CASE
    WHEN  '{user_input_order_status}'=0 THEN 'Preparing'
    WHEN  '{user_input_order_status}'=1 THEN 'On the way'
    WHEN  '{user_input_order_status}'=2 THEN 'Delivered' END WHERE order_id = {user_input_order_id}'''

    cursor.execute(sql)
    connection.commit()
    cursor.close()





def write_data_delete_order():
    #indexed_list(courier_list)
    connection,cursor=establish_connection()
    

    choice_delete_order=int(input('type in order index of which order you to want delete?'))
    # del order_list[choice_delete_order]    

    sql=f"DELETE FROM order_table WHERE order_id={choice_delete_order}"

    cursor.execute(sql)
    connection.commit()
    cursor.close()





