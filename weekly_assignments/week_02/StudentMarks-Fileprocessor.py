def marks():
    total = 0
    count = 0
    invalid = 0
    try:
        f = open("mark.txt", "r")
        lines = f.readlines()
        if len(lines) == 0:
            raise ValueError
        for line in lines:
            try:
                parts = line.strip().split(",")
                if len(parts) != 2:
                    raise ValueError
                name = parts[0]
                m = float(parts[1])
                if m < 0:
                    raise ValueError
                print(name, ":", m)
                total = total + m
                count = count + 1
            except:
                print("Invalid record found")
                invalid = invalid + 1
        if count > 0:
            avg = total / count
            print("Average marks:", avg)
        else:
            print("No valid records")
        print("Valid records:", count)
        print("Invalid records:", invalid)
        f.close()
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("File is empty")
marks()