import psycopg2
from datetime import datetime
from input_validation import (
    get_valid_name,
    get_valid_age,
    get_valid_sex,
    get_valid_weight,
    get_valid_height,
    get_valid_activity,
    get_valid_goal,
)

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def calculate_bmr(weight, height_cm, age, sex):
    if sex == "male":
        bmr = 10 * weight + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height_cm - 5 * age - 161
    return bmr

def calculate_tdee(bmr, activity_level):
    if activity_level == "sedentary":
        return bmr * 1.2
    elif activity_level == "light":
        return bmr * 1.375
    elif activity_level == "moderate":
        return bmr * 1.55
    elif activity_level == "active":
        return bmr * 1.725
    elif activity_level == "very_active":
        return bmr * 1.9

def calculate_goal_calories(tdee, goal):
    if goal == "lose":
        return max(tdee - 500, 1200)
    elif goal == "maintain":
        return tdee
    elif goal == "gain":
        return tdee + 300

def save_to_database(name, age, sex, weight, height, activity, goal, bmi, bmi_label, bmr, tdee, calories):
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="bmi_project",
            user="postgres",
            password="YOUR-PA$$WORD",
            port="5432"
        )

        cur = conn.cursor()

        query = """
        INSERT INTO bmi_records
        (name, age, sex, weight_kg, height_cm, activity_level, goal, bmi, bmi_label, bmr, tdee, goal_calories, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            name, age, sex, weight, height, activity, goal,
            round(bmi, 2), bmi_label, round(bmr, 2),
            round(tdee, 2), round(calories, 2), datetime.now()
        )

        cur.execute(query, values)
        conn.commit()

        print("\nData saved in database successfully")

        cur.close()
        conn.close()

    except Exception as e:
        print("\nError saving to database:", e)

print("=== BMI AND CALORIE CALCULATOR ===")

name = get_valid_name()
age = get_valid_age()
sex = get_valid_sex()
weight = get_valid_weight()
height = get_valid_height()
activity = get_valid_activity()
goal = get_valid_goal()

bmi = calculate_bmi(weight, height)
bmi_label = bmi_category(bmi)
bmr = calculate_bmr(weight, height, age, sex)
tdee = calculate_tdee(bmr, activity)
goal_calories = calculate_goal_calories(tdee, goal)

print("\n=== RESULTS ===")
print("Name:", name)
print("Age:", age)
print("Sex:", sex)
print("BMI:", round(bmi, 2))
print("BMI Category:", bmi_label)
print("BMR:", round(bmr, 2), "kcal/day")
print("TDEE:", round(tdee, 2), "kcal/day")
print("Calories for your goal:", round(goal_calories, 2), "kcal/day")

save_to_database(name, age, sex, weight, height, activity, goal, bmi, bmi_label, bmr, tdee, goal_calories)
