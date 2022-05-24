# from itertools import count
import os

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
main_menu_message='press [0] to exit app, press [1] for product menu, press [2] for courier menu'
product_menu_message="[0] to return to main menu,\n[1] to show product list,\n[2] to create a new product,\n[3] to update existing product,\n[4] to delete a product\n"
courier_menu_message='[0] to return to main menu,\n[1] to print courier list,\n[2] to create a new courier,\n[3] to update existing courier,\n[4] to delete a courier\n'

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
            
           

     


product_list,courier_list=load_data()

main_menu()