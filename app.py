import csv

import os


from db_interactions import *
from Utilities_used import *

#import db_interactions as dbi   (later on change to dbi.functioncall ie dbi.write_new)


#app messages
welcome_message = "Hi! Welcome to the Coffee Club"
main_menu_message='press [0] to exit app, press [1] for product menu, press [2] for courier menu, press [3] for orders menu'
product_menu_message="[0] to return to main menu,\n[1] to show product list,\n[2] to create a new product,\n[3] to update existing product,\n[4] to delete a product\n"
courier_menu_message='[0] to return to main menu,\n[1] to print courier list,\n[2] to create a new courier,\n[3] to update existing courier,\n[4] to delete a courier\n'
orders_menu_message='[0] to return to main menu,\n[1] to print orders dictionary,\n[2] to create a new order,\n[3] update order status,\n[4] to update existing order,\n[5] to delete an order\n'
print(welcome_message)

#empty lists
# order_list=[]
order_status=['Preparing','Out for delivery','Delivered']
# product_list=[]

# courier_list=[]



#loading data to read




#writing data

def main_menu():
    while True:
        
        user_input_main_menu = int(input(f'{main_menu_message} : '))
        if user_input_main_menu==0:
            print(product_list)
            print(courier_list)
            print("--------------------------------------------")
            # write_data(product_list,courier_list)
              
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
            product_list=load_data_products()
            print(product_list)
           
        elif user_options==2:
            print('create new product\n')
            product_list=write_data_new_products()
            
        
        elif user_options==3:
            product_list=load_data_products()
            print(product_list)

           
            product_list=write_data_update_products()
            # print(product_list)

        elif user_options==4:
            product_list=load_data_products()
            print(product_list)
            product_list=write_data_delete_product()
            product_list=load_data_products()
            print(product_list)




def couriers_menu():
    
    while True:
        user_input_courier=int(input(courier_menu_message))
        if user_input_courier==0:
            print("Return to main menu.\n")
            
            return

        elif user_input_courier== 1:
                os.system('cls')
                courier_list=load_data_couriers()
                print(courier_list)  
               
        elif user_input_courier==2:
                print('create new courier\n')

                courier_list=write_data_new_courier()
                courier_list=load_data_couriers()
                print(courier_list)     
                

        elif user_input_courier==3:
                courier_list=load_data_couriers()
                print(courier_list)     
                
                courier_list=write_data_update_courier()
                courier_list=load_data_couriers()
                print(courier_list)
        elif user_input_courier==4:
                courier_list=load_data_couriers()
                print(courier_list)  
                write_data_delete_courier()
                os.system('cls')
                courier_list=load_data_couriers()
                print(courier_list)  








def orders_menu():
    while True:
        user_input_order_menu=int(input(orders_menu_message))
        if user_input_order_menu==0:
            main_menu()
        elif user_input_order_menu==1:
            order_list=load_data_orders()
            print(order_list)
        elif user_input_order_menu==2:
            order_list=load_data_orders()
            order_list=write_data_new_order(courier_list)
            order_list=load_data_orders()
            print(order_list)
  
                
        elif user_input_order_menu==3:
            order_list=load_data_orders()
            print(order_list)
            # indexed_list(order_list)
            order_list=write_data_update_order_status()
            # order_list=load_data_orders()
            order_list=load_data_orders()
            print(order_list)
                    
            # indexed_list(order_list)
            

            
            

           
        
        elif user_input_order_menu==4:
            #print('orders list with index value')
            # indexed_list(order_list)
            order_list=load_data_orders()
            print(order_list)
            #input('input for order index value')
            write_data_update_existing_order(order_status,courier_list,product_list)
            order_list=load_data_orders()
            
            print(order_list)

            
         

        
        
        elif user_input_order_menu==5:
            print('orders list with index value ')
            order_list=load_data_orders()
            print(order_list)
            #delete order at index of order list
            write_data_delete_order()
            order_list=load_data_orders()
            print(order_list)





        

product_list=load_data_products()
courier_list=load_data_couriers()
order_list=load_data_orders()

main_menu()

