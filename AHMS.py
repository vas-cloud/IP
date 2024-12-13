import random
import datetime
import matplotlib.pyplot as plt
import pandas as pd

# Global List Declaration
name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []
payment_mode = []

# Global Variable Declaration
i = 0

# Home Function
def Home():
    print("\t\t\t\tWELCOME To Dolphin Paradise\n")
    print("\t\t\t1 --> Booking")
    print("\t\t\t2 --> Rooms Information")
    print("\t\t\t3 --> Payment")
    print("\t\t\t4 --> Record")
    print("\t\t\t5 --> Data Analysis")
    print("\t\t\t0 --> Exit")
    
    ch = int(input("-> "))
    
    if ch == 1:
        Booking()
    elif ch == 2:
        Rooms_Info()
    elif ch == 3:
        Payment()
    elif ch == 4:
        Record()
    elif ch == 5:
        Data_Analysis()
    else:
        exit()

# Function to validate dates
def date(c):
    try:
        datetime.datetime(c[2], c[1], c[0])
    except ValueError:
        print("Invalid date\n")
        Booking()

# Booking Function
def Booking():
    global i
    print("\nBOOKING ROOMS\n")
    
    while True:
        n = input("Name: ")
        p1 = input("Phone No.: ")
        a = input("Address: ")
        
        if n and p1 and a:
            name.append(n)
            phno.append(p1)
            add.append(a)
            break
        else:
            print("Name, Phone No., and Address cannot be empty!")
    
    cii = input("Check-In (DD/MM/YYYY): ")
    checkin.append(cii)
    ci = list(map(int, cii.split('/')))
    date(ci)
    
    coo = input("Check-Out (DD/MM/YYYY): ")
    checkout.append(coo)
    co = list(map(int, coo.split('/')))
    date(co)
    
    d1 = datetime.datetime(ci[2], ci[1], ci[0])
    d2 = datetime.datetime(co[2], co[1], co[0])
    d = (d2 - d1).days
    day.append(d)
    
    print("\n----SELECT ROOM TYPE----")
    print("1. Standard Non-AC - Rs. 3500")
    print("2. Standard AC - Rs. 4000")
    print("3. 3-Bed Non-AC - Rs. 4500")
    print("4. 3-Bed AC - Rs. 5000")
    
    ch = int(input("-> "))
    
    if ch == 1:
        room.append('Standard Non-AC')
        price.append(3500)
    elif ch == 2:
        room.append('Standard AC')
        price.append(4000)
    elif ch == 3:
        room.append('3-Bed Non-AC')
        price.append(4500)
    elif ch == 4:
        room.append('3-Bed AC')
        price.append(5000)
    else:
        print("Invalid choice!")
        Booking()
    
    rn = random.randint(300, 340)
    cid = random.randint(10, 50)
    
    while rn in roomno or cid in custid:
        rn = random.randint(300, 340)
        cid = random.randint(10, 50)
    
    roomno.append(rn)
    custid.append(cid)
    rc.append(0)
    p.append(0)
    
    print("\n*** ROOM BOOKED SUCCESSFULLY ***")
    print("Room No.:", rn)
    print("Customer ID:", cid)
    
    i += 1
    Home()

# Room Information Function
def Rooms_Info():
    print("\nROOMS INFORMATION\n")
    print("1. Standard Non-AC")
    print("2. Standard AC")
    print("3. 3-Bed Non-AC")
    print("4. 3-Bed AC")
    input("\nPress Enter to return to Home... ")
    Home()

# Payment Function
def Payment():
    global i
    ph = input("\nEnter Phone Number: ")
    f = 0
    
    for n in range(i):
        if ph == phno[n] and p[n] == 0:
            f = 1
            print("\nPAYMENT MODE")
            print("1. Credit/Debit Card")
            print("2. UPI")
            print("3. Cash")
            mode = int(input("-> "))
            if mode == 1:
                payment_mode.append('Card')
            elif mode == 2:
                payment_mode.append('UPI')
            elif mode == 3:
                payment_mode.append('Cash')
            else:
                print("Invalid choice!")
                Payment()
            
            total = (price[n] * day[n]) + rc[n]
            print("\nAmount to Pay:", total)
            print("\nPayment Successful!")
            p[n] = 1
            roomno[n] = 0
            custid[n] = 0
            break
    if not f:
        print("No records found!")
    Home()

# Record Function
def Record():
    if phno:
        data = {
            "Name": name,
            "Phone No.": phno,
            "Address": add,
            "Check-In": checkin,
            "Check-Out": checkout,
            "Room Type": room,
            "Price": price,
            "Days": day,
            "Payment": ["Paid" if x == 1 else "Pending" for x in p]
        }
        df = pd.DataFrame(data)
        print("\nCUSTOMER RECORDS\n")
        print(df)
        df.to_csv("customer_records.csv", index=False)
        print("\nRecords exported to 'customer_records.csv'.")
    else:
        print("\nNo records found!")
    Home()

# Data Analysis Function
def Data_Analysis():
    if phno:
        plt.figure(figsize=(10, 6))
        
        # Room type analysis
        plt.subplot(1, 2, 1)
        plt.title("Room Types Booked")
        plt.pie([room.count(r) for r in set(room)], labels=set(room), autopct='%1.1f%%')
        
        # Payment mode analysis
        plt.subplot(1, 2, 2)
        plt.title("Payment Mode Distribution")
        plt.bar(list(set(payment_mode)), [payment_mode.count(pm) for pm in set(payment_mode)], color='skyblue')
        plt.xlabel("Payment Modes")
        plt.ylabel("Count")
        
        plt.tight_layout()
        plt.show()
    else:
        print("\nNo data available for analysis!")
    Home()

# Driver Code
Home()
