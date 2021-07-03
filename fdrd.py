def interest(fdamount , percent , duration):
    fdcal = fdamount*percent/100
    fdcal2 = fdcal/365 * duration
    print("FD interest: " , fdcal2)

def interestrd(rdamount , percent , duration):
    rdcal = rdamount*percent/100
    rdcal2 = rdcal/12 * duration
    print("RD interest: " , rdcal2)

def interestsb(sbamount , percent , duration):
    sbcal = sbamount*percent/100
    sbcal2 = sbcal/365 * duration
    print("SB interest: " , sbcal2)



print("Enter Deposit Schemes : FD , RD , SB")
a = input()


if a == "FD":
    print("Enter FD Principal value: ")
    fdamount = input()
    fdamount = int(fdamount)

    print("Enter your FD Duration : ")
    duration = input()
    duration = int(duration)

    print("Enter your Age : ")
    age = input()
    age = int(age)

    if fdamount <= 10000000 :
        if duration > 7 and duration < 14 and  age < 60:
            percent = 4.50
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 15 and duration < 29 and  age < 60 :
            percent = 4.75
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 30 and duration < 45 and  age < 60 :
            percent = 5.50
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 45 and duration < 60 and  age < 60 :
            percent = 7
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 61 and duration < 184 and  age < 60 :
            percent = 7.50
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 185 and duration < 365 and  age < 60 :
            percent = 7
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 7 and duration < 14 and  age > 60:
            percent = 5
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 15 and duration < 29 and  age > 60 :
            percent = 5.25
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 30 and duration < 45 and  age > 60 :
            percent = 6.0
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 45 and duration < 60 and  age > 60 :
            percent = 7.5
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 61 and duration < 184 and  age > 60 :
            percent = 8.0
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 185 and duration < 365 and  age > 60 :
            percent = 8.50
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 365 :
            print("Two options: \n")
            print("1. Tax Savings FD \n")
            print("2. Exit \n\n")
            x = input("Select 1 / 2 to know more Details : ")
            if x == '1' :
                print("This scheme is for 3 Years Lock-in period")
                print("Get upto Rs 1.5 lakh a year tax deduction undret Section 80C Provisions\n")
                y = input('Do you want to proceed Y/N : ')
                if y == 'Y' :
                    percent = 10.0
                    fdcal3 = interest(fdamount , percent , duration)

                elif y == 'N' :
                    print("Exiting !!!")
                    exit()

            elif x == '2' :
                print("Exiting !!!!")
                exit()





    elif fdamount > 10000000 :

        if duration > 7 and duration < 14 :
            percent = 5
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 15 and duration < 29 :
            percent = 5.25
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 30 and duration < 45 :
            percent = 6.0
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 45 and duration < 60 :
            percent = 7.5
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 61 and duration < 184 :
            percent = 8.0
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 185 and duration < 365  :
            percent = 8.50
            fdcal3 = interest(fdamount , percent , duration)

        elif duration > 365 :
            print("Maximum Duration is 365 days only !!!")
            exit()



    else :
        print("Enter Correct Value")

elif a == "SB" :
    print("Enter SB Principal value: ")
    sbamount = input()
    sbamount = int(sbamount)

    print("Enter your SB Duration : ")
    duration = input()
    duration = int(duration)

    sbtype = input("Type of Account Normal / NRI: ")
    if sbtype == "Normal":
        percent = 4
        sbcal3 = interestrd(sbamount , percent , duration)

    elif t == "NRI" :
        percent = 8
        sbcal3 = interestrd(sbamount , percent , duration)



elif a == "RD" :
    print("Enter RD Principal value: ")
    rdamount = input()
    rdamount = int(rdamount)

    print("Enter your RD Duration : ")
    duration = input()
    duration = int(duration)

    print("Enter your Age : ")
    age = input()
    age = int(age)

    if duration <= 6 and age < 60:
            percent = 7.50
            rdcal3 = interestrd(rdamount , percent , duration)

    elif duration <= 9 and age < 60 :
            percent = 7.75
            rdcal3 = interestrd(rdamount , percent , duration)

    elif duration <= 12 and age < 60 :
            percent = 8.0
            rdcal3 = interestrd(rdamount , percent , duration)

    elif duration <= 15 and age < 60 :
            percent = 8.25
            rdcal3 = interestrd(rdamount , percent , duration)

    elif duration <= 18 and age < 60 :
            percent = 8.50
            rdcal3 = interestrd(rdamount , percent , duration)

    elif duration <= 21 and age < 60 :
            percent = 8.75
            rdcal3 = interestrd(rdamount , percent , duration)

    elif duration <= 6 and age > 60:
            percent = 8.0
            rdcal3 = interestrd(rdamount , percent , duration)

    elif duration <= 9 and age > 60 :
            percent = 8.35
            rdcal3 = interestrd(rdamount , percent , duration)

    elif duration <= 12 and age > 60 :
            percent = 8.50
            rdcal3 = interestrd(rdamount , percent , duration)

    elif duration <= 15 and age > 60 :
            percent = 8.75
            rdcal3 = interestrd(rdamount , percent , duration)

    elif duration <= 18 and age > 60 :
            percent = 9.0
            rdcal3 = interestrd(rdamount , percent , duration)

    elif duration <= 21 and age > 60 :
            percent = 9.25
            rdcal3 = interestrd(rdamount , percent , duration)
