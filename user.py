import hashlib
from random import random, randint
from brta import BRTA
from ride_manager import uber
from vehicle import Car, Bike, Cng
license_authorithy = BRTA()


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_hash = hashlib.md5(password.encode()).hexdigest()
        with open('users.txt', 'w') as file:
            file.write(f'{email} {pwd_hash}')
        file.close()
        print(self.name, "user created")

    @staticmethod
    def login(email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]

        file.close()
        hased_password = hashlib.md5(password.encode()).hexdigest()
        if (hased_password == stored_password):
            print(' valid user')
        else:
            print(" in valid user")

        print("password found ", stored_password)


class Rider(User):
    def __init__(self, name, email, password, location, balance) -> None:
        self.location = location
        self.balance = balance
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self, destination):
        pass

    def start_a_trip(self, fare):
        self.balance -= fare


class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authorithy.validate_license(email, license)
        self.earning = 0

    def take_driving_test(self):
        result = license_authorithy.take_driving_test((self.email))
        if result == False:
            print('sorry you failed')
        else:
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            new_vehicle = None
            if (vehicle_type == 'car'):
                new_vehicle = Car(
                    vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            elif (vehicle_type == 'bike'):
                new_vehicle = Bike(
                    vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            else:
                new_vehicle = Cng(
                    vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            pass
        else:
            print("You are not a valid driver")

    def start_a_trip(self, destination, fare):
        self.earning += fare
        self.location = destination


rider1 = Rider("r1", "raone@gmail.com", 'pass', randint(0, 100), 5000)
