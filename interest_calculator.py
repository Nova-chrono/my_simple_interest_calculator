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
                I = (P * R * T) / 100
                I = round(I, 2)
                valid = True
                print("Interest = ", I)
            except:
                print("Please input only digits greater than zero.")

        elif cal == "p":
            try:
                I = float(input("Interest: "))
                R = float(input("Rate: "))
                T = float(input("Time: "))
                P = (I * 100) / (R * T)
                P = round(P, 2)
                valid = True
                print("Principal = ", P)
            except:
                print("Please input only digits greater than zero.")

        elif cal == "r":
            try:
                I = float(input("Interest: "))
                P = float(input("Principal: "))
                T = float(input("Time: "))
                R = (I * 100) / (P * T)
                R = round(R, 2)
                valid = True
                print("Rate = ", R, "%")
            except:
                print("Please input only digits greater than zero.")

        else:
            try:
                I = float(input("Interest: "))
                P = float(input("Principal: "))
                R = float(input("rate: "))
                T = (I * 100) / (P * R)
                valid = True
                if T < float(1):
                    print("Time = ", T, "year")
                elif T == float(1):
                    print("Time = ", T, "year")
                else:
                    print("Time = ", T, "years")
            except:
                print("Please input only digits greater than zero.")
        

calculator()
