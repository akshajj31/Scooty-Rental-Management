import random

global no_of_scooties, no_of_bikes, rental_time

def reserve_two_wheeler_time(reservation_time, scooties_available, bikes_available):
    ans = input("Do you have a license? ").lower()
    if ans != "yes":
        print("You cannot rent a two-wheeler without a license.")
        return scooties_available, bikes_available

    choice = input("What do you want to rent? Bike or scooty: ").lower()
    if choice == "scooty":
        if scooties_available == 0:
            print("No scooties available at this time.")
            return scooties_available, bikes_available

        no_of_scooties = min(int(input(f"Enter the number of scooties you want to rent (max {scooties_available}): ")), scooties_available)
        scooties_available -= no_of_scooties
        print(f"{no_of_scooties} scooties reserved for {reservation_time} hours.")
        return scooties_available, bikes_available

    elif choice == "bike":
        if bikes_available == 0:
            print("No bikes available at this time.")
            return scooties_available, bikes_available

        no_of_bikes = min(int(input(f"Enter the number of bikes you want to rent (max {bikes_available}): ")), bikes_available)
        bikes_available -= no_of_bikes
        print(f"{no_of_bikes} bikes reserved for {reservation_time} hours.")
        return scooties_available, bikes_available

    else:
        print("Invalid choice.")
        return scooties_available, bikes_available

def total_price(no_of_scooties, no_of_bikes, rental_time):
    price_scooty = 50  # per hour price
    total1 = no_of_scooties * price_scooty * rental_time

    price_bike = 100  # per hour price
    total2 = no_of_bikes * price_bike * rental_time

    Total = total1 + total2
    print(f"Total price is {Total}")

def main():
    scooties_available = random.randint(0, 5)
    bikes_available = random.randint(0, 5)

    print("Welcome to Hills Two-Wheeler Rentals\n")

    while True:
        i = int(input('''1 Display stock\n2 Rent a two-wheeler\n3 Price\n4 Exit\n>> '''))

        if i == 1:
            print(f"Scooties available: {scooties_available}")
            print(f"Bikes available: {bikes_available}")

        elif i == 2:
            reservation_time = int(input("Enter the time you would like to reserve a vehicle for: "))
            scooties_available, bikes_available = reserve_two_wheeler_time(reservation_time, scooties_available, bikes_available)

        elif i == 3:
            total_price(no_of_scooties, no_of_bikes, rental_time)

        elif i == 4:
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
