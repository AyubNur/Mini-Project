# from itertools import count
import os
from turtle import update

#------------------------------------------------------
# with open("Products.txt","w") as file1:
#     # print(file1.readlines())
#     product_list=file1.readlines()

# with open("Courier.txt","w") as file2:
#     # print(file2.readlines())
#     courier_list=file2.readlines()


# file=open("Products.txt","w")
# file=open("Courier.txt","w")
#-------------------------------------------------------
welcome_message = "Hi! Welcome to the Coffee Club"
main_menu_message='press [0] to exit app, press [1] for product menu, press [2] for courier menu, press [3] for orders menu'
product_menu_message="[0] to return to main menu,\n[1] to show product list,\n[2] to create a new product,\n[3] to update existing product,\n[4] to delete a product\n"
courier_menu_message='[0] to return to main menu,\n[1] to print courier list,\n[2] to create a new courier,\n[3] to update existing courier,\n[4] to delete a courier\n'
orders_menu_message='[0] to return to main menu,\n[1] to print orders dictionary,\n[2] to create a new order,\n[3] update order status,\n[4] to update existing order,\n[5] to delete an order\n'

order_list=[{"customer_name": "John Hamilton",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "courier": 2,
  "status": "Preparing"},{"customer_name": "David Bradley",
  "customer_address": "Gravesend, 75 Little Street, LONDON, E1 4RQ",
  "customer_phone": "0750498573",
  "courier": 3,
  "status": "Preparing"}]



order_status=['Preparing','Out for delivery','Delivered']



def indexed_list(a):
    for count,value in enumerate(a):
        print (count,value)
    
    


    

print(welcome_message)






# read data (load the data from the text files to the lists)
def load_data():
    #read data from Products.txt
    products_file=open('Products.txt')
    products_list=products_file.readlines()
    courier_file=open('Courier.txt')
    courier_list=courier_file.readlines()
    products_file.close()
    courier_file.close()
    return products_list,courier_list

#write data (write the data into the respective file)
def write_data(file_name,list):
    f=open(file_name,'w')
    for word in list:
        f.write(word)
    f.close()


def main_menu():
    while True:
        
        user_input_main_menu = int(input(f'{main_menu_message} : '))
        if user_input_main_menu==0:
            print(product_list)
            print(courier_list)
            print("--------------------------------------------")
            write_data('Products.txt',product_list)
            write_data('Courier.txt',courier_list)    
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
            product_list.append(input('enter your new product here\n')+'\n')
            print(product_list)
        
        elif user_options==3:
            for count,value in enumerate(product_list):
                print (count,value)
            choice1=int(input('what product do you want to change '))
            choice2=input('what do you want to add ')
            product_list[choice1]=choice2+'\n'

        elif user_options==4:
            for count,value in enumerate(product_list):
                print (count,value)
            choice1=int(input('what product do you want delete '))
            del product_list[choice1]    
            

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
                courier_list.append(input('enter your new courier here\n')+'\n')
                print(courier_list)
        elif user_input_courier==3:
                for count,value in enumerate(courier_list):
                    print (count,value)
                choice1=int(input('what courier number do you want to change '))
                choice2=input('what courier name do you want to add ')
                courier_list[choice1]=choice2+'\n'
        elif user_input_courier==4:
                for count,value in enumerate(courier_list):
                    print (count,value)
                choice1=int(input('what product do you want delete '))
                del courier_list[choice1]   
            
           

     
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
            for count,value in enumerate(courier_list):
                        print (count,value)
            courier_chosen=input('select courier by selecting courier index ')
            order={'customer_name':customer_name_input,'customer_address':customer_address_input,'customer_phone':customer_phone_number_input,'courier':courier_chosen,'status':'Preparing'}
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
           
            # user_input_order_key=int(input('type [customer_name] to update customer name, [customer_address] to update customer address, [customer_phone] to update customer phone number,'))
            user_input_updated_name=input('input new name ')
            user_input_updated_address=input('input new address ')
            user_input_updated_phonenumber=int(input('input new phone number '))
            
            indexed_list(courier_list)
            user_input_updated_courier=int(input('input new courier '))
            indexed_list(order_status)
            user_input_order_status=int(input('input new status '))

            
            # if user_input_updated_name or user_input_updated_courier or user_input_updated_address or user_input_updated_status or user_input_updated_phonenumber=='':
            #     return orders_menu()
            # elif user_input_updated_courier!=order_list[user_input_order_index]['courier'] or user_input_updated_status!=order_list[user_input_order_index]['status']:
            #     return orders_menu()
            # else:

            #update order status
            if user_input_order_status==0:
                   order_list[user_input_order_index]['status']='Preparing' 
            if user_input_order_status==1:
                    order_list[user_input_order_index]['status']='On the way'
                    
            if user_input_order_status==2:
                    order_list[user_input_order_index]['status']='Delivered'
            order_list[user_input_order_index]['customer_name ']=user_input_updated_name
            order_list[user_input_order_index]['customer_address ']=user_input_updated_address
            order_list[user_input_order_index]['customer_phone ']=user_input_updated_phonenumber
            
            a=courier_list[user_input_updated_courier]
            order_list[user_input_order_index]['courier ']=a
            # order_list[user_input_order_index]['status ']=user_input_updated_status
            # order_list[user_input_order_index]['courier ']=user_input_updated_courier

            # order_list[user_input_order_index]['courier ']=user_input_updated_courier



            # order_list[user_input_order_index]['courier']=user_input_updated_courier
            
            print(order_list)

            
            # #indent an if to say if blank dont update(return call) and else then retun
            #     if input=='':
            #         return
            #     else:
            #         update

        
        
        elif user_input_order_menu==5:
            print('orders list with index value ')
            for count,value in enumerate(order_list):
                    print (count,value)
            #delete order at index of order list
            choice1=int(input('what order do you want to delete '))
            del order_list[choice1]   



        # elif user_input_order_menu==6:
        #     print(indexed_order_list)




        


product_list,courier_list=load_data()

main_menu()

