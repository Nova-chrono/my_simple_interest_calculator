print("Novachrono's Simple Interest Calculator")


def calculator():
    
    print("What do you want to solve?")
    cal = input("Enter \"I\" for Interest, \"P\" for Principal, \"R\" for Rate(%), \"T\" for Time(years): ")
    # print(cal)
    cal = cal.lower()
    # print(cal)
    cal_pick = ["i", "p", "r", "t"]
    valid = False
    
    while not valid:
        while cal not in cal_pick:
            print("Invalid input!")
            cal = input("Enter \"I\" for Interest, \"P\" for Principal, \"R\" for Rate(%), \"T\" for Time(years): ")
            cal = cal.lower()

        if cal == "i":
            try:
                P = float(input("Principal: "))
                R = float(input("Rate: "))
                T = float(input("Time: "))
                valid = True
                I = (P * R * T) / 100
                print("Interest = ", I)
            except:
                print("Please input only digits greater than zero.")

        elif cal == "p":
            try:
                I = float(input("Interest: "))
                R = float(input("Rate: "))
                T = float(input("Time: "))
                valid = True
                P = (I * 100) / (R * T)
                print("Principal = ", P)
            except:
                print("Please input only digits greater than zero.")

        elif cal == "r":
            try:
                I = float(input("Interest: "))
                P = float(input("Principal: "))
                T = float(input("Time: "))
                valid = True
                R = (I * 100) / (P * T)
                print("Rate = ", R, "%")
            except:
                print("Please input only digits greater than zero.")

        else:
            try:
                I = float(input("Interest: "))
                P = float(input("Principal: "))
                R = float(input("rate: "))
                valid = True
                T = (I * 100) / (P * R)
                if T < float(2):
                    print("Time = ", T, "year")
                else:
                    print("Time = ", T, "years")
            except:
                print("Please input only digits greater than zero.")
        

calculator()
