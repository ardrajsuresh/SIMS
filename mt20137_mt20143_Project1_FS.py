# SALES AND INVENTORY MANAGEMENT SYSTEM
import pandas as pd   
import pdfkit as pdf #for creating bill in pdf format
import  sys #for exit
import getpass #for password
df=pd.read_csv("Book1.csv") #file containing inventory data

def SIMS(): # Main Node containing the sales and admin nodes
    def _admin() : #Admin Node handles all functions related to inventory management
        def add_item() : # This node is used to add new items to the inventory

            df=pd.read_csv("Book1.csv")
            new_item=input("Enter the name of item:")
            filt=(df['item']==new_item) #Compares the entered item with existing item
            checklist=df[filt].values.tolist() #returns all the true values
            if checklist : #Checking whether the item already exists in the inventory
                print("This Item already exist in stock!!\n",df[filt])
                up_quantity=input("Enter the Quantity to be Added :") 
                Quant = int(df.loc[filt,'Quantity']) #Returns the quantity available in the inventory
                df.loc[filt,'Quantity']=Quant+int(up_quantity) #More quantity added
                print(df)
                df.to_csv("Book1.csv",index=False) #The updated dataframe is copied back to the file
            else: #if the item is a new item, all the data has to be entered
                new_quantity=input("Enter the quantity of items:")
                new_price=input("Enter the price of item:")
                new_code=input("Enter the code for the item:")
                new_weight=input("Enter the weight for the item:")
                new_manufacturer=input("Enter the manufacturer for the item:") 
                df = df.append({'item': new_item,'Quantity': new_quantity,'price': new_price,'code': new_code,'Weight': new_weight,'Manufacturer': new_manufacturer}, ignore_index=True)
            df.to_csv("Book1.csv",index=False) #The new item is appened into the dataframe and the changes are copied back to the file

        def print_inventory(): #This node prints the items and details in the inventory
            df=pd.read_csv("Book1.csv")
            print("The Current position of the stock is given below")
            print(df)
        def password() : #This node is used for authentication of the admin user
            print("You need to authorise if you want access to admin panel ")
            adminpass="akshat" #Password
        
            attempt=3 #After three wrong attempts the user is denied entry into the admin section
            while (attempt>0) :
                passw= getpass.getpass(prompt='Enter the password : ')

                if(passw==adminpass):
                    return True 
                else :
                    print('Please try again: Attempts remaining',attempt-1)
                    print("You Entered : ",passw)
                    attempt=attempt-1
            return False

        def update_existing(): #This node is used for updating the inventory details
            def update_prices(): #This node updates prices of exisitng items in the inventory
                df=pd.read_csv("Book1.csv")
                print(df)
                serch=input("Enter code of item whose prices is to be updated:")
                filt=(df['code']==serch) #returns the item in the inventory
                checklist=df[filt].values.tolist() #returns all values as true or false
                if checklist : #selecting thr true value
                    print("You want to modify this item\n",df[filt])
                    up_price=input("Enter the new price")
                    df.loc[filt,'price']=int(up_price) #changeing the price of the particular item
                    print(df)
                else :
                    print("The Item is not found")
                df.to_csv("Book1.csv",index=False) #The updation made is copied to the file
            def update_inventory(): #to delete an item from the inventory
                df=pd.read_csv("Book1.csv")
                delrow=input('Enter the code of item you want to remove:')
                print(df)
                try:
                    ind = int(df[df['code']==delrow].index[0]) #finding the item form inventory
                    print(ind)
                    df.drop(ind,inplace=True) #deletion of that particular row
                    print(df)
                    df.to_csv("Book1.csv",index=False) #The updation made is copied to the file
                except: #exeption handling if the user enters a wrong choice
                    print('You have not entered a valid product')
            selc1=input("1:Delete Item from Stock\n 2:Update Prices") #the two functionalities present in update_existing_inventory
            if(int(selc1)==1):
                update_inventory()
            elif(int(selc1)==2):
                update_prices()
            else:
                print("Enter correct choice")

        auth=password() #password verification
        flow=True #for the proper code flow
        if auth is False :
            sys.exit("You have exceeded maximum Attempts ") #deny access to unauthorised people
        else :

            print("Welcome to Admin Panel\n Select the option you want to perform")
        
            while flow is True: # Interface to each functionalities
                print("1:Print inventory report")
                print("2:Add New Items")
                print("3:Update Existing Inventory")

                selc=input("Enter the Number corresponding to the operation you want to perform ")
                if(int(selc)==1):
                    print_inventory()
                elif(int(selc)==3):
                    update_existing()
                elif(int(selc)==2):
                    add_item()
                else:
                    print("Enter Valid Choice")
                check1=input("1: To continue else Exit") #For going back to SIMS Console
                if int(check1) == 1:
                    flow=True
                else:
                    flow=False
        return
    
    def sales(): #Sales section involves all functions related to sales
    
        def search_items(): #This node allows the user to check if an item is there or not
            df=pd.read_csv("Book1.csv") # The file where all the inventory data is stored
            find = input("Enter the item to search for:")
            val = (df['item']==find) #finds out the item from the stock
            item = df[val].values.tolist() #returns true and false for all values
            if item: #if the item exists, its details are printed
                print(item)
            else:
                print("Such an Item Do Not Exit!")
            return

        def product_sales(): #This node handles all sales activities

            def update_stock_qty(item,qty): #This node updates stock quantity each time an item is added to the bill
                df=pd.read_csv("Book1.csv")
                val = (df['item']==item)
                thing = df[val].values.tolist() #finding item from stock
                if thing: #if it exists in the stock
                    Quant = int(df.loc[val,'Quantity']) #returns quantity present inside that
                    Quant = Quant - int(qty) #subtscts the sold quantity from the available quantity
                    df.loc[val,'Quantity'] = Quant #new quantity is updated
                df.to_csv("Book1.csv",index=False) #The updation made is copied to the file

            def modify_current_sale_record(df2): #This node helps in modification of current bill
                print("The current bill is as follows:")
                print(df2)
                print("You can make the following changes") #The options available
                print("1. Add an Item")
                print("2. Remove an item ")
                print("3. Change Quantity of an item") 
                say = int(input("Enter your requirement:"))

                if say == 1: #to add and item
                    find = input("Enter item code:")
                    qty = input("Enter Quantity:")
                    val = (df['code']==find) #the item is found from the inventory
                    thing = df[val].values.tolist()
                    if thing:
                        print(thing)
                        update_stock_qty(thing[0][0],qty) #The stock is updated now(ie, deletion)
                        money = int(qty)*thing[0][2] #Calculate total money according to the quantity purchased
                        df2=df2.append({'item': thing[0][0],'Quantity': qty,'price': money,'code': thing[0][3],'Weight': thing[0][4],'Manufacturer': thing[0][5]},ignore_index=True)
                        print(df2) #df2 holds the bill. The changes in the bill is appended into df2
                elif say == 2: #to remove an item
                    rem = input("Enter item code:")
                    ind = int(df2[df2['code']==rem].index[0]) #the item is found from the bill
                    print(ind)
                    df2.drop(ind,inplace=True) #that row is deleted
                    print(df2)
                elif say == 3: #to change the quantity of an item
                    edit = input("Enter item code:")
                    new_qty = input("Enter quantity:")
                    new_val =(df2['code']==edit) #The item is found 
                    new_thing = df2[new_val].values.tolist() # retuns all true and falise values
                    if new_thing:
                        print(new_thing)
                        old_qty = int(df2.loc[new_val,'Quantity']) #exisitng qty added in the bill is found
                        df2.loc[new_val,'Quantity'] = int(new_qty) #new qty is updated
                        price = df2.loc[new_val,'price'] #old prince is found
                        new_price1 = int(new_qty)*price #new price is changed according the number of items
                        new_price = new_price1/old_qty
                        df2.loc[new_val,'price'] = new_price #new price is updated
                        print(df2)
                else:
                    print("You Entered wrong choice!")
                df2.to_csv("bill.csv",index=False) #The updation made is copied to the bill file
                df2.to_csv('record.csv', mode='a', header=False,index=False2) #The updation made is copied to the file
        
            def generate_current_sale_record(): #In this node the actual billing happens
                df=pd.read_csv("Book1.csv")
                n = 0 #while loop counter
                df2 = pd.DataFrame(columns=['item','Quantity','price','code','Weight','Manufacturer']) #empty dataframe in order to store bill details
                while(n == 0):
                    find = input("Enter item code:")
                    qty = input("Enter Quantity:")
                    val = (df['code']==find) #entered item is found from stock
                    thing = df[val].values.tolist() 
                    print(thing) #it is displayed as list
                    update_stock_qty(thing[0][0],qty) #The stock is updated
                    money = int(qty)*thing[0][2] #the amount according to the qty sold is calculated
                    df2=df2.append({'item': thing[0][0],'Quantity': qty,'price': money,'code': thing[0][3],'Weight': thing[0][4],'Manufacturer': thing[0][5]},ignore_index=True) #The item is appended into the bill dataframe
                    n = int(input("Want to shop more? Enter 0, else enter 1:")) #checking condition for adding more items
                print(df2) #the bill is printed
                say = int(input("Enter 0 if you want to modify the bill, else enter 1"))
                if say == 0:
                    modify_current_sale_record(df2) #for modifications of the bill
                else:
                    df2.to_csv("bill.csv",index=False) #The Bill dataframe is copied into the file
                    df2.to_csv('record.csv', mode='a', header=False,index=False) #For sales record keeping, the sold items are appended into the sales record record.csv each time a customer is served
                    return
            generate_current_sale_record()
            
        def print_invoice(): #This node generates the invoice as pdf file and copied the bill into the memory
            df3=pd.read_csv("bill.csv") #the bill file
            print(df3)
            total_price = df3['price'].sum() #Total price to be paid is calculated and displayed
            print("Total Amount to be paid: Rs",total_price)
    
            df3.to_html("bill.html") #first the dataframe is concverted into an html file
            pdf.from_file("bill.html",'bills.pdf') #this html file is then converted into a pdf
            return
    
        def print_sales_report(): #this node prints the sales report 
            df5 = pd.read_csv("record.csv") #sales record copied into the record.csv is read
            g=df5.groupby('item') #this groups all the the items with same name
            print(g.sum()) #sum of each item is printed

        choice = 1
        while choice: #for the interface to go to different sections
            print("WELCOME TO THE SALES SECTION> PLEASE CHOOSE THE OPTION:")
            print("1. Search items:")
            print("2. Product Sales:")
            print("3. Print Invoice:")
            print("4. Print Sales Report:")

            choice = int(input("Enter your choice:"))

            if choice==1:
                search_items()
            elif choice==2:
                product_sales()
            elif choice==3:
                print_invoice()
            elif choice==4:
                print_sales_report()
            else:
                choice = int(input("Enter proper value:"))
        return
    
    option = 1
    while option:
        print("WELCOME TO SALES AND INVENTORY MANAGEMENT SYSTEM") #The main console of SIMS
        print("1.ADMIN SECTION")
        print("2.SALES SECTION")
    
        option = int(input("Enter Your Choice:"))
        if option == 1:
            _admin()
        elif option == 2:
            sales()
        else:
            option=int(input("Please Enter a valid option"))

SIMS()