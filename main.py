#Bus Reservation System
#0=available, 1=booked
seats=[0]*41

while True:
    print("\n---Bus Seat Reservation System---")
    print("1. Show all Seats")
    print("2. Book a seat")
    print("3. Exit")
    choice=int(input("Enter your choice:" ))
    if choice==1:
     for i in range(1,41):
         if seats[i]==0:
            print(f"seats{i}:Available")
         else:
            print(f"seats{i}:Booked")
    elif choice==2:
        seat=int(input("Enter seat number(1-40):"))
        if seats[seat] == 0:
            seats[seat] = 1
            print("Seat booked successfully!")
        else:
            print("Seat already booked.")
    elif choice == 3:
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice!Please try again.")
    
