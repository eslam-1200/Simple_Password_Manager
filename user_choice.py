import queries

def any_else():
    print("===================================")
    print("Thanks for using our program Can we help more :D?")

def Choose():
    while True:


        lst = ["Add","Edit", "Check","Delete","Exit"]
        for i in lst:
            print(i)
        choice = input("Choose a service: ")


        if choice.lower() == "add":
            print("Please insert (Service , Email/Username , Password): ")
            data = []
            while len(data) <3:
                data.append(input(""))
            queries.add(data)
            print("Added successfully :)!")
            any_else()


        elif choice.lower() == "check":
            select_ser = input("Enter the service you want : ")
            queries.select(select_ser)
            any_else()


        elif choice.lower() == "edit":
            con = input("What service you want to change? ")
            while queries.Check_before_Edit(con):
                print("This service doesn't exist to be edited!")
                con = input("Try again!: ")

            print("Please insert (New Service name,New Email/Username ,New Password): ")
            ed_data = []
            while len(ed_data) < 3:
                ed_data.append(input(""))
            queries.edit(con,ed_data)
            print("Edited successfully :)!")
            any_else()


        elif choice.lower() == "delete":
            del_ser = input("Insert the service you want to delete: ")
            queries.delete(del_ser)
            any_else()


        elif choice.lower() == "exit":
            print("Hope you are satisfied :D")
            return


        else:
            print("====================================")
            print("This service is not available")
            print("try again :>")

