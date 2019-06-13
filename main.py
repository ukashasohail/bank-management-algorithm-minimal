#input for operation or create account
x = int(input("Press 1 for operation \nPress 2 to create account: "))

#nested arrays to store  data
data = [[1000, 500], [1001, 900], [1002, 1500],[1003,5000],[1004,3000]]

#checking user's choice
if x == 1:

    choice = int(input("""\nEnter 1 to deposit amount, \n2 to withdraw amount, \n3 for transfer : """))

    if choice == 1:
        #input of account number and amount
        account_number = int(input("Enter account number: "))
        amount = int(input("Enter amount to deposit: "))

        #for loop to iterate over nested array
        for i in data:
            #check if 0th index of nested array = account number
            if i[0] == account_number:
                #add amount
                i[1] = i[1] + amount

    elif choice == 2:
        account_number = int(input("Enter account number: "))
        amount = int(input("Enter amount to withdraw: "))
        for i in data:
            if i[0] == account_number:
                if i[1]>amount:
                    i[1] = i[1] - amount
                else:
                    print("You don't have enough amount in your account.")

    else:
        dep_account_number = int(input("Enter your account number: "))
        rec_account_number = int(input("Enter reciever's account number: "))
        amount = int(input("Enter amount to transfer: "))

        for i in data:
            if i[0] == dep_account_number:
                if i[1]>amount:
                    i[1] = i[1] - amount
                else:
                    print("You don't have enough amount in your account.")
        for j in data:
            if j[0] == rec_account_number:
                j[1] = j[1] + amount

elif x == 2:
    amount = int(input("Enter the amount you want to deposit: "))
    
    highest = 0
    for i in data:
        if i[0]>highest:
            highest = i[0]

    data.append([i[0]+1,amount])
 
print(data)
