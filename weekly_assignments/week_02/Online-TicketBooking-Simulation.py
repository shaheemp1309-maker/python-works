def booking():
    seats = 50
    print("Total seats available:", seats)
    while True:
        try:
            x = input("Enter number of tickets or type exit: ")
            if x.lower() == "exit":
                print("Booking stopped")
                break
            t = int(x)
            if t <= 0:
                raise Exception
            if t > seats:
                raise Exception
            seats = seats - t
            print("Booking successful")
            print("Remaining seats:", seats)
            if seats == 0:
                print("All seats are booked")
                break
        except ValueError:
            print("Enter numbers only")
        except Exception:
            print("Invalid ticket number")
booking()