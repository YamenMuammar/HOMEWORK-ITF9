name = input("Enter your name : ")
age = input("Enter your age : ")
country = input("Enter your country : ")
city = input("Enter your city : ")
street = input("Enter your street : ")
information = []
first_dict = {
    "name" : f"{name}",
    "age" : f"{age}",
}
second_dict = {"address" : {
    "country" : f"{country}",
    "city" : f"{city}",
    "street" : f"{street}"
}

}
information.append(first_dict)
information.append(second_dict)
print(information)
