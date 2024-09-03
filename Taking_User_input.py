# print("\n")
# # a = input("Enter your name : ")
# # print(a)
# print("\n")

# x = input("Enter first number : ")
# y = input("Enter second number : ")
# print(int(x) + int(y))
# print("\n")

# print("\n")
# number_of_days = int(input("Enter the number of days :  "))

# years = int(number_of_days / 365)
# weeks = int((number_of_days % 365) / 7)
# days = (number_of_days % 365) % 7

# print("\n")
# print(number_of_days, " = ", years, " years + ", weeks, " weeks + ", days, " days")
# print("\n")

class revision():

    def _init_(self):
        pass

    def fibonacci_series(self):
        print("\n")
        print("~~~~~~~~~~Fibonacci Series~~~~~~~~~~")
        a = 0
        b = 1
        mylist = []
        n = int(input("Enter the length of the list :  "))
        for i in range(n):
            mylist.append(a)
            a,b = b,a+b
        print(mylist)
        print("\n")

    def second_smallest_number(self):
        print("\n")
        print("~~~~~~~~~~Second smallest number~~~~~~~~~~")
        mylist = []
        l = int(input("Enter the length of the list :  "))
        print("\n")
        for i in range(l):
            num = int(input("Enter number :  "))
            mylist.append(num)
        print("Your list  = {}".format(mylist))
        print("\n")

        firstmin = secondmin = float('inf')
        for i in mylist:
            if i < firstmin:
                secondmin = firstmin
                firstmin = i
            elif firstmin < i < secondmin:
                secondmin = i
        print("Second smallest number of the list is  {}".format(secondmin))
        print("\n")

    def reverse_of_string(self):
        print("\n")
        print("~~~~~~~~~~Reverse of string~~~~~~~~~~")
        mystring = input("Enter the string :  ")
        print("\n")
        print("Reverse of this string is ", mystring[::-1])
        print("\n")

    def number_of_occurrences(self):
        print("\n")
        print("~~~~~~~~~~Number of occurrences~~~~~~~~~~")
        mylist = []
        l = int(input("Enter the length of the list :  "))
        print("\n")
        for i in range(l):
            num = int(input("Enter number :  "))
            mylist.append(num)
        print("\n")
        print("Your list = {}".format(mylist))
        print("\n")
        number_to_be_searched = int(input("Enter the number you have to search its occurrence :  "))
        match number_to_be_searched:
            case number_to_be_searched if number_to_be_searched not in mylist:
                print("Sorry, number not in the list, try again.")
                print("\n")
            case _:
                print("Number of occurrences of the number {}  = {}".format(number_to_be_searched, mylist.count(number_to_be_searched)))
                print("\n")
        
    def intersection(self):
        print("\n")
        print("~~~~~~~~~~Intersection of lists~~~~~~~~~~")
        print("Enter first list")
        mylist1 = []
        l = int(input("Enter the length of the list :  "))
        print("\n")
        for i in range(l):
            num = int(input("Enter number :  "))
            mylist1.append(num)
        print("\n")
        print("Your first list = {}".format(mylist1))
        print("\n")

        print("\n")
        print("Enter second list")
        print("\n")
        mylist2 = []
        len = int(input("Enter the length of the list :  "))
        print("\n")
        for i in range(len):
            num = int(input("Enter number :  "))
            mylist2.append(num)
        print("\n")
        print("Your second list = {}".format(mylist2))
        print("\n")

        common_elements = [num for num in mylist1 if num in mylist2]
        print("Result of intersecton of the two lists = {}".format(common_elements))
        print("\n")
    
    def number_of_days_calculation(self):
        print('\n')
        print("~~~~~~~~~~Number of days calculation~~~~~~~~~~")
        number_of_days = int(input("Enter the number of days :  "))
        print("\n")
        years = int(number_of_days / 365)
        weeks = int((number_of_days % 365) / 7)
        days = int((number_of_days % 365) % 7)
        print("{} number of days = {} years + {} weeks + {} days.".format(number_of_days,years,weeks,days))
        print("\n")

    def swappinf(self):
        print("\n")
        print("~~~~~~~~~~Swapping~~~~~~~~~~")
        a = int(input("Enter first number :  "))
        print("\n")
        b = int(input("Enter second number :  "))
        print("\n")
        a = a + b
        b = a - b
        a = a - b
        print("After swapping a = {} and b = {}".format(a,b))
        print("\n")

class Childish(revision):
    pass

Childish_obj = Childish()
Childish_obj.fibonacci_series()
Childish_obj.second_smallest_number()
Childish_obj.intersection()
Childish_obj.number_of_days_calculation()
Childish_obj.reverse_of_string()
Childish_obj.number_of_occurrences()


    
              



































