
class User:
    import json
    with open("C:\\Users\\22208\PycharmProjects\As4\\rent_service\perinfo.json", "r") as json_file:
        allusers = json.load(json_file)
    def __init__(self, login, name, surname, phonenumber, password):
        self.login = login
        self.name = name
        self.surname = surname
        self.phonenumber = phonenumber
        self.password = password

    @staticmethod
    def create_user_instance(user_data):
        if user_data['utype'] == 'Rent-giver':
            return RentGivers(**user_data)
        elif user_data['utype'] == 'Rent-seeker':
            return RentSeekers(**user_data)
        else:
            raise ValueError(f"Invalid user type: {user_data['utype']}")

    @staticmethod
    def toString(self):
        print(str(f"Username: {self.login}\nName and Surname: {self.name} {self.surname}"
                  f"\nPhone number: {self.phonenumber}"))

class RentGivers(User):
    def __init__(self, login, name, surname, phonenumber, password):
        super().__init__(login, name, surname, utype="Rent-giver", phonenumber=phonenumber, password=password)
        print('Hi gi')
        #self.property_list = property_list

    def add_property(self, property_details):
        self.property_list.append(property_details)

    def view_properties(self):
        for property_details in self.property_list:
            print(f"Property: {property_details}")


class RentSeekers(User):
    def __init__(self, login, name, surname, phonenumber, password):
        super().__init__(login, name, surname, utype="Rent-seeker", phonenumber=phonenumber, password=password)
        print('Hi See')
        #self.preferences = preferences

    def update_preferences(self, new_preferences):
        self.preferences = new_preferences

    def view_preferences(self):
        print(f"Preferences: {self.preferences}")
