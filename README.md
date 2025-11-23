# Problem Overview
The Bus Reservation System is a simple software application that allows users to check seat availability and book seats quickly and accurately. It displays 40 seats and clearly shows whether each one is available or already booked. Users can view all seats, select a seat to reserve, and receive instant confirmation.
This project automates the basic reservation process, reducing manual errors and saving time. It applies key programming concepts such as loops, conditionals, lists, modular design, and input validation. The system is easy to use, reliable, and can be enhanced in the future with additional features if needed.
# Features
View all 40 seats
Shows which seats are available/booked
Book any available seat
Prevents double-booking
Validates seat numbers (1–40)
Simple and clean menu interface
# Objective
The objective of this project is to automate the bus seat booking process and demonstrate the use of:
Loops
Lists
Conditional statements
Modular programming
Input validation
# tools used
programming language- python
Python IDE
# Functional requirements
1.	Seat display module
  i.	Show full seat(available/booked)
2.	Seat booking module
  i.	Accept the seat number for booking
  ii.	Check if the seat is free
 iii.	Update the reservation list
3.	Exit module
  i.	Allow the user to exit the program safely 
# Non-functional Requirements
1.	Must be user-friendly 
2.	Should validate seat numbers
3.	Avoid duplicate bookings
4.	Easy to modify and maintain
5.	fast response
# Algorithm
1.Start
2. Initialize 40 seats to available
3. Show menu
4. If user selects “Show Seats”, display seat status
5. If user selects “Book Seat”:
  Validate seat number
  If free → book it
  Else → show error
6. If user selects “Exit”, stop program
7. Repeat loop
Test No.	           Input            	Expected Output

  1               	Show seats	         Displays all seat status
  2            	Book seat 10	          Successfully booked
  3	          Book seat 10 again   	    Shows error: already booked
  4	          Seat number 0 or 45	      Shows error: invalid seat number
  5	         Menu choice invalid	        Shows “Invalid choice”
# How to Run
1. Install Python (if not installed)
2. Download or clone the repository
3. Open a terminal in project folder
4. Run:
  python main.py
# Future Enhancements
 Add cancellation feature
 Store data in file/database
 Add user login system
 Add GUI interface

7.	Should handle invalid inputs 
8.	Should not crash during normal use
