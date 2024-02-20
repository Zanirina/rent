from rent_service.buildings import Building
from rent_service.users import User, RentGivers, RentSeekers
from rent_service.house import House
import json


# The following two functions are needed to log in to an existing account
def load_users_from_file(filename):
    try:
        with open(filename, "r") as json_file:
            users_data = json.load(json_file)
        return users_data
    except FileNotFoundError:
        return {}


def checkIn(login, password, q):
    with open(q, 'r') as file:
        data = json.load(file)
    users = data.get('users', [])

    for user in users:
        if user.get('login') == login and user.get('password') == password:
            if user.get('utype' =="Rent-giver"):
                rentg1= RentGivers(RentGivers, user.get("login", []), user.get("name", []), user.get("surname", []),
                              user.get("phonenumber", []), user.get("password", []))
            elif user.get('utype' =="Rent-seeker"):
                rents1=RentSeekers(RentSeekers, user.get("login", []), user.get("name", []), user.get("surname", []),
                              user.get("phonenumber", []), user.get("password", []))

            #User.toString(user)
            return True
    print("Invalid password or login")
    return False


# Load users from a JSON file named "perinfo.json"
users_data = load_users_from_file("C:\\Users\\22208\PycharmProjects\As4\\rent_service\perinfo.json")

# Create sample house and apartment objects
house1 = House("RastyLake 34", 11, "House", 270000, 4, 98)
apart1 = House("Parori", 22, "Apartment", 160000, 1, 35)

# Login Prompt
loginin = input("Enter a login: ")
passin = input("Enter a password: ")

# usertype = users_data.load
# print(usertype)
# Main Menu Loop
while checkIn(loginin, passin, "C:\\Users\\22208\PycharmProjects\As4\\rent_service\perinfo.json") == True:
    print("---MENU:")
    print("1. Affordable housing for rent")
    print("2. Create an ad for rental housing")
    print("3. Personal account ")
    print("4. Favorites ")
    print("5. Create add")
    print("---------------------------------------")
    choice = int(input("Enter your choice: "))
    print("---------------------------------------")

    if choice == 1:
        print('Select the type of building:')
        print("1. Apartments\n2. Houses")
        print("---------------------------------------")
        choicetyp = int(input("Enter your choice: "))
        print("---------------------------------------")

        if choicetyp == 1:
            apart1.toString()
        elif choicetyp == 2:
            house1.toString()
# elif choice == 2:
#   create()
    elif choice == 3:
        RentSeekers.toString(RentSeekers)
        RentGivers.toString(rent)


# elif choice == 4:
#     showfav()
