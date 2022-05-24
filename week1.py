from itertools import count
import os
welcome_message = "Hi! Welcome to the Coffee Club"
product_list = ["Tea", "Coffee", "Chai", "Hot Chocolate", "Milkshake"]
main_menu_message='press [0] to exit app, press [1] for product menu '
product_menu_message="[0] to return to main menu,\n[1] to show product list,\n[2] to create a new product,\n[3] update existing product,\n[4] delete a product\n"



print(welcome_message)
print(main_menu_message)

def main_menu():
    user_input_main_menu = int(input())
    if user_input_main_menu==0:
        print("Exit the app \n")
        exit()
    else: 
        # print(product_menu_message)
        product_menu()


def product_menu():
    while True:
        user_options = int(input(product_menu_message))
        if user_options == 0:
            print("Return to main menu.\n")
            print(main_menu_message)
            main_menu()
            
            
        elif user_options == 1:
            os.system('cls')
           
            print(product_list)
        elif user_options==2:
            print('create new product\n')
            product_list.append(input('enter your new product here\n'))
            print(product_list)
        
        elif user_options==3:
            for count,value in enumerate(product_list):
                print (count,value)
            choice1=int(input('what product do you want to change '))
            choice2=input('what do you want to add ')
            product_list[choice1]=choice2

        elif user_options==4:
            for count,value in enumerate(product_list):
                print (count,value)
            choice1=int(input('what product do you want delete '))
            del product_list[choice1]     
            
          

main_menu()