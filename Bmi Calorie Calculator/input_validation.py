def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name != "":
            return name
        else:
            print("Name cannot be empty")

def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0 and age < 120:
                return age
            else:
                print("Please enter a valid age")
        except:
            print("Please enter a number")

def get_valid_sex():
    while True:
        sex = input("Enter your sex (male/female): ").strip().lower()
        if sex == "male" or sex == "female":
            return sex
        else:
            print("Invalid option. Please type male or female")

def get_valid_weight():
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            if weight > 0 and weight < 500:
                return weight
            else:
                print("Please enter a valid weight")
        except:
            print("Please enter a valid number")

def get_valid_height():
    while True:
        try:
            height = float(input("Enter your height in cm: "))
            if height > 0 and height < 300:
                return height
            else:
                print("Please enter a valid height")
        except:
            print("Please enter a valid number")

def get_valid_activity():
    while True:
        print("Options: sedentary, light, moderate, active, very_active")
        activity = input("Enter your activity level: ").strip().lower()

        if activity in ["sedentary", "light", "moderate", "active", "very_active"]:
            return activity
        else:
            print("Invalid activity level. Try again")

def get_valid_goal():
    while True:
        goal = input("Enter your goal (lose, maintain, gain): ").strip().lower()

        if goal in ["lose", "maintain", "gain"]:
            return goal
        else:
            print("Invalid goal. Try again")
