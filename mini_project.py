from math import prod
import os
from tkinter import W
from turtle import update
import csv

welcome_message = "Hi! Welcome to the Coffee Club"
main_menu_message='press [0] to exit app, press [1] for product menu, press [2] for courier menu, press [3] for orders menu'
product_menu_message="[0] to return to main menu,\n[1] to show product list,\n[2] to create a new product,\n[3] to update existing product,\n[4] to delete a product\n"
courier_menu_message='[0] to return to main menu,\n[1] to print courier list,\n[2] to create a new courier,\n[3] to update existing courier,\n[4] to delete a courier\n'
orders_menu_message='[0] to return to main menu,\n[1] to print orders dictionary,\n[2] to create a new order,\n[3] update order status,\n[4] to update existing order,\n[5] to delete an order\n'
print(welcome_message)

order_list=[]
order_status=['Preparing','Out for delivery','Delivered']
product_list=[]

courier_list=[]

def indexed_list(a):
    for count,value in enumerate(a):
        print (count,value)

def load_data():
    with open('products.csv', mode='r') as products_file:
        product_reader=csv.DictReader(products_file, delimiter=',')
        for row in product_reader:
            product_list.append(row)
    with open('courier.csv',mode='r') as couriers_file:
        courier_reader=csv.DictReader(couriers_file, delimiter=',')
        for row in courier_reader:
            courier_list.append(row)
    with open('order.csv', mode='r') as orders_file:
        orders_reader=csv.DictReader(orders_file, delimiter=',')
        for row in orders_reader:
            order_list.append(row)

    return product_list,courier_list,order_list

def write_data(product_list,courier_list):
    if len(product_list)>0:
        with open('products.csv', mode='w') as products_file:
            fieldnames = ['name','price']
            product_writer = csv.DictWriter(products_file, fieldnames=fieldnames)
    # instruct the writer to know to write the headers
            product_writer.writeheader()
            product_writer.writerows(product_list)
 # instruct the writer to write the row
    if len(courier_list)>0:
        with open('courier.csv', mode='w') as couriers_file:
            fieldnames = ['name','number']
            courier_writer = csv.DictWriter(couriers_file, fieldnames=fieldnames)
            courier_writer.writeheader()
            courier_writer.writerows(courier_list)
    if len(order_list)>0:
        with open('order.csv', mode='w') as orders_file:
            fieldnames = ['customer_name','customer_address','customer_phone','courier','status','items']
            order_writer = csv.DictWriter(orders_file, fieldnames=fieldnames)
            order_writer.writeheader()
            order_writer.writerows(order_list)

def main_menu():
    while True:
        
        user_input_main_menu = int(input(f'{main_menu_message} : '))
        if user_input_main_menu==0:
            print(product_list)
            print(courier_list)
            print("--------------------------------------------")
            write_data(product_list,courier_list)
              
            print("Exit the app \n")
            exit()
        elif user_input_main_menu==1:
            # print(product_menu_message)
            product_menu()
        elif user_input_main_menu==2:
                couriers_menu()
        elif user_input_main_menu==3:
                orders_menu()

def product_menu():
    
    while True:
        user_options = int(input(product_menu_message))
        if user_options == 0:
            print("Return to main menu.\n")
            return
            
        elif user_options == 1:
            os.system('cls')
            print(product_list)
           
        elif user_options==2:
            print('create new product\n')
            product_name_input=input('new product name ')
            product_price_input=float(input('new product price '))

            new_product={'name':product_name_input,'price':product_price_input}
            product_list.append(new_product)
            print(product_list)
        
        elif user_options==3:
            for count,value in enumerate(product_list):
                print (count,value)
            user_input_product_index=int(input('what product do you want to change '))
            user_input_product_name=input('what do you want to add ')
            user_input_product_price=float(input('how much does it cost'))
            product_list[user_input_product_index]['name']=user_input_product_name
            product_list[user_input_product_index]['price']=user_input_product_price
            print(product_list)

        elif user_options==4:
            for count,value in enumerate(product_list):
                print (count,value)
            choice_delete_product=int(input('what product do you want delete '))
            del product_list[choice_delete_product]    




def couriers_menu():
    
    while True:
        user_input_courier=int(input(courier_menu_message))
        if user_input_courier==0:
            print("Return to main menu.\n")
            
            return

        elif user_input_courier== 1:
                os.system('cls')
                print(courier_list)  
        elif user_input_courier==2:
                print('create new courier\n')
           
                courier_name_input=input('new courier name ')
                courier_number_input=int(input('new courier number '))

                new_courier={'name':courier_name_input,'number':courier_number_input}
                courier_list.append(new_courier)         
                print(courier_list)

        elif user_input_courier==3:
                for count,value in enumerate(courier_list):
                    print (count,value)
                
                user_input_courier_index=int(input('which courier do you want to change '))
                user_input_courier_name=input('what do you want the name to be ')
                user_input_courier_price=int(input('couriers number'))
                courier_list[user_input_courier_index]['name']=user_input_courier_name
                courier_list[user_input_courier_index]['number']=user_input_courier_price
                print(courier_list)
        elif user_input_courier==4:
                for count,value in enumerate(courier_list):
                    print (count,value)
                choice_delete_courier=int(input('which courier do you want delete? '))
                del courier_list[choice_delete_courier]    









def orders_menu():
    while True:
        user_input_order_menu=int(input(orders_menu_message))
        if user_input_order_menu==0:
            main_menu()
        elif user_input_order_menu==1:
            print(order_list)
        elif user_input_order_menu==2:
            customer_name_input=input('what is your name ')
            customer_address_input=input('what is your address ')
            customer_phone_number_input=input('what is your phone number ')
            customer_items_input=input('what items are in the order')
            for count,value in enumerate(courier_list):
                        print (count,value)
            courier_chosen=input('select courier by selecting courier index ')
            order={'customer_name':customer_name_input,'customer_address':customer_address_input,'customer_phone':customer_phone_number_input,'courier':courier_chosen,'status':'Preparing','items':customer_items_input}
            #append this order to orders list
            order_list.append(order)
            print(order_list)
        elif user_input_order_menu==3:
            #print('orders list with index value')
            indexed_list(order_list)
            user_input_order_index=int(input('input for order index value '))
            #print('order status list with index values')
            indexed_list(order_status)
          

            #update order status
            user_input_order_status=int(input('input for order status '))
            if user_input_order_status==0:
                   order_list[user_input_order_index]['status']='Preparing' 
            if user_input_order_status==1:
                    order_list[user_input_order_index]['status']='On the way'
                    
            if user_input_order_status==2:
                    order_list[user_input_order_index]['status']='Delivered'
                    
            indexed_list(order_list)
            

            
            

           
        
        elif user_input_order_menu==4:
            #print('orders list with index value')
            indexed_list(order_list)
            #input('input for order index value')
            user_input_order_index=int(input('input for order index '))
           
            user_input_updated_name=input('input new name ')
            user_input_updated_address=input('input new address ')
            user_input_updated_phonenumber=int(input('input new phone number '))
            
            indexed_list(courier_list)
            user_input_updated_courier=int(input('input new courier '))
            indexed_list(order_status)
            user_input_order_status=int(input('input new status '))

            
            
            user_input_order_items=input('update the items')

            order_list[user_input_order_index]['customer_name']=user_input_updated_name
            order_list[user_input_order_index]['customer_address']=user_input_updated_address
            order_list[user_input_order_index]['customer_phone']=user_input_updated_phonenumber
            
            indexed_list(courier_list)
            order_list[user_input_order_index]['courier']=user_input_updated_courier
            if user_input_order_status==0:
                   order_list[user_input_order_index]['status']='Preparing' 
            if user_input_order_status==1:
                    order_list[user_input_order_index]['status']='On the way'
                    
            if user_input_order_status==2:
                    order_list[user_input_order_index]['status']='Delivered'
            order_list[user_input_order_index]['items']=user_input_order_items
          
            
            print(order_list)

            
         

        
        
        elif user_input_order_menu==5:
            print('orders list with index value ')
            for count,value in enumerate(order_list):
                    print (count,value)
            #delete order at index of order list
            choice1=int(input('what order do you want to delete '))
            del order_list[choice1]   






        


product_list,courier_list,order_list=load_data()

main_menu()

