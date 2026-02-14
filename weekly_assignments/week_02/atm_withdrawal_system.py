def atm():
    bal = 10000
    print("Balance:", bal)
    while True:
        try:
            x = input("Enter amount or type exit: ")
            if x.lower() == "exit":
                print("Final balance:", bal)
                break
            amt = float(x)            
            if amt <= 0:
                raise ValueError            
            if amt > bal:
                raise ValueError            
            bal = bal - amt            
            print("Withdrawal successful")
            print("Remaining balance:", bal)
        except ValueError:
            print("Invalid amount")
        except:
            print("Enter numbers only")
atm()
