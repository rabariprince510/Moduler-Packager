
import datetime
import time
import math
import random
import uuid

def create_file(filename):
    f = open(filename, "w")
    f.close()
    print("File created successfully!")

def write_to_file(filename, text):
    f = open(filename, "w")
    f.write(text)
    f.close()
    print("Data written successfully!")

def read_from_file(filename):
    try:
        f = open(filename, "r")
        content = f.read()
        f.close()
        print("File Content:")
        print(content)
    except FileNotFoundError:
        print("Error: File not found!")

def append_to_file(filename, text):
    f = open(filename, "a")
    f.write("\n" + text)
    f.close()
    print("Data appended successfully!")


# ==============================================================================
# 1. DATETIME AND TIME OPERATIONS
# ==============================================================================

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        
        choice = input("\n ~ Enter your choice: ")
        
        if choice == "1":
            now = datetime.datetime.now()
            print(f"\nCurrent Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print("----------------------------------")
            
        elif choice == "2":
            d1_str = input("\n Enter the first date (YYYY-MM-DD): ")
            d2_str = input("\n Enter the second date (YYYY-MM-DD): ")
            d1 = datetime.datetime.strptime(d1_str, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(d2_str, "%Y-%m-%d")
            diff = abs((d2 - d1).days)
            print(f"\n Difference: {diff} days")
            print("---------------------------------")
            
        elif choice == "3":
            now = datetime.datetime.now()
            print(f"\n Formatted Date: {now.strftime('%A, %d %B %Y')}")
            print("---------------------------------")
            
        elif choice == "4":
            input("\n Press Enter to START stopwatch...")
            start = time.time()
            input("\n Press Enter to STOP stopwatch...")
            end = time.time()
            print(f"\n Elapsed time: {round(end - start, 2)} seconds")
            print("---------------------------------")
            
        elif choice == "5":
            secs = int(input("\n Enter countdown time in seconds: "))
            while secs > 0:
                print(f"\n Time remaining: {secs} seconds", end="\r")
                time.sleep(1)
                secs -= 1
            print("\n\n Time's up!")
            print("---------------------------------")
            
        elif choice == "6":
            break
        else:
            print("\n ~~ Invalid choice, please try later.")


# ==============================================================================
# 2. MATHEMATICAL OPERATIONS
# ==============================================================================

def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        
        choice = input("\n ~ Enter your choice: ")
        
        if choice == "1":
            num = int(input("\n Enter a number: "))
            print(f"\n Factorial: {math.factorial(num)}")
            print("----------------------------------")
            
        elif choice == "2":
            p = float(input("\n Enter principal amount: "))
            r = float(input("\n Enter rate of interest (in %): "))
            t = float(input("\n Enter time (in years): "))
            ci = p * math.pow((1 + r / 100), t)
            print(f"\n Compound Interest: {ci:.2f}")
            print("----------------------------------")
            
        elif choice == "3":
            angle = float(input("\n Enter angle in degrees: "))
            rad = math.radians(angle)
            print(f"\n sin({angle}): {math.sin(rad):.4f}")
            print(f"\n cos({angle}): {math.cos(rad):.4f}")
            print(f"\n tan({angle}): {math.tan(rad):.4f}")
            print("----------------------------------")
            
        elif choice == "4":
            print("a. Circle")
            print("b. Rectangle")
            shape = input("Select shape (a/b): ")
            if shape == "a":
                radius = float(input("\n Enter radius: "))
                print(f"\n Area of Circle: {math.pi * radius * radius:.2f}")
            elif shape == "b":
                l = float(input("\n Enter length: "))
                w = float(input("\n Enter width: "))
                print(f"\n Area of Rectangle: {l * w:.2f}")
            print("----------------------------------")
            
        elif choice == "5":
            break
        else:
            print("\n ~~ Invalid choice, please try again.")


# ==============================================================================
# 3. RANDOM DATA GENERATION
# ==============================================================================

def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        
        choice = input("\n ~ Enter your choice: ")
        
        if choice == "1":
            low = int(input("\n Enter lower limit: "))
            high = int(input("\n Enter upper limit: "))
            print(f"\n Random Number: {random.randint(low, high)}")
            print("-----------------------------------")
            
        elif choice == "2":
            size = int(input("\n Enter list size: "))
            random_list = [random.randint(1, 100) for _ in range(size)]
            print(f"\n Generated List: {random_list}")
            print("-----------------------------------")
            
        elif choice == "3":
            length = int(input("\n Enter password length: "))
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
            password = "".join(random.choice(chars) for _ in range(length))
            print(f"\n Generated Password: {password}")
            print("-----------------------------------")
            
        elif choice == "4":
            otp = random.randint(100000, 999999)
            print(f"\n Generated Random OTP: {otp}")
            print("----------------------------------")
            
        elif choice == "5":
            break
        else:
            print("\n ~~Invalid choice, please try later.")


# ==============================================================================
# 4. UUID GENERATION
# ==============================================================================

def uuid_menu():
    print("\nGenerate Unique Identifiers:")
    generated_uuid = uuid.uuid4()
    print(f"Generated UUID: {generated_uuid}")
    print("-----------------------------------")


# ==============================================================================
# 5. FILE OPERATIONS MENU
# ==============================================================================

def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        
        choice = input(" ~ Enter your choice: ")
        
        if choice == "1":
            fname = input("\n Enter file name: ")
            create_file(fname)
            print("-----------------------------------")
            
        elif choice == "2":
            fname = input("\n Enter file name: ")
            data = input("\n Enter data to write: ")
            write_to_file(fname, data)
            print("-----------------------------------")
            
        elif choice == "3":
            fname = input("\n Enter file name: ")
            read_from_file(fname)
            print("------------------------------------")
            
        elif choice == "4":
            fname = input("\n Enter file name: ")
            data = input("\n Enter data to append: ")
            append_to_file(fname, data)
            print("------------------------------------")
            
        elif choice == "5":
            break
        else:
            print("\n ~~Invalid choice, please try again.")


# ==============================================================================
# 6. DYNAMIC MODULE EXPLORATION USING dir()
# ==============================================================================

def explore_module():
    print("\nExplore Module Attributes:")
    mod_name = input("Enter module name to explore: ").strip()
    
    modules = {
        "datetime": datetime,
        "time": time,
        "math": math,
        "random": random,
        "uuid": uuid
    }
    
    if mod_name in modules:
        attributes = dir(modules[mod_name])
        print(f"\n Available Attributes in {mod_name} module:")
        print(attributes[:10], "...]")  # Displays sample attributes neatly
    else:
        print(f"\n Module '{mod_name}' is not pre-imported.")
    print("------------------------------------------------")


# ==============================================================================
# MAIN INTERFACE CONTROL
# ==============================================================================

def main():
    while True:
        print("\n===================================")
        print("Welcome to Multi-Utility Toolkit")
        print("===================================")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("===================================")
        
        choice = input("~ Enter your choice: ")
        
        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            print("\n===================================")
            print("\n Thank you for using the Multi-Utility Toolkit!")
            print("\n If you need help please visit again..!")
            print("\n Goodbye..!!")
            print("===================================")
            break
        else:
            print("Invalid selection! Please choose between 1 and 7.")

if __name__ == "__main__":
    main()
