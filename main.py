# Simple Railway Reservation System
TOTAL_SEATS = 50
available_seats = TOTAL_SEATS
bookings = {}

def check_availability():
    print("\nAvailable Seats:", available_seats)

def book_ticket():
    global available_seats

    if available_seats <= 0:
        print("\nNo seats available!")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")

    booking_id = "B" + str(len(bookings) + 1)

    bookings[booking_id] = {
        "name": name,
        "age": age
    }

    available_seats -= 1
    print("\nTicket Booked Successfully!")
    print("Booking ID:", booking_id)

def view_ticket():
    booking_id = input("Enter Booking ID: ")

    if booking_id in bookings:
        print("\nTicket Details:")
        print("Name:", bookings[booking_id]["name"])
        print("Age:", bookings[booking_id]["age"])
    else:
        print("\nInvalid Booking ID!")

def cancel_ticket():
    global available_seats

    booking_id = input("Enter Booking ID to cancel: ")

    if booking_id in bookings:
        del bookings[booking_id]
        available_seats += 1
        print("\nTicket Cancelled Successfully!")
    else:
        print("\nInvalid Booking ID!")

def menu():
    while True:
        print("\n--- Railway Reservation System ---")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_availability()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            view_ticket()
        elif choice == "4":
            cancel_ticket()
        elif choice == "5":
            print("\nThank You!")
            break
        else:
            print("\nInvalid Choice!")

menu()
