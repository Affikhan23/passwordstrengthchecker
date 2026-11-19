
import pandas as pd

# Take user information
name = input("Enter your name: ")

sleep = float(input("How many hours did you sleep? "))
water = float(input("How much water did you drink (litres)? "))
steps = int(input("How many steps did you walk today? "))
exercise = int(input("How many minutes did you exercise? "))

# Check health
print("\n===== DAILY HEALTH REPORT =====")
print("Name:", name)

if sleep >= 7:
    print("Sleep: Good")
else:
    print("Sleep: Need more rest")

if water >= 2:
    print("Water Intake: Good")
else:
    print("Water Intake: Drink more water")

if steps >= 5000:
    print("Walking: Good")
else:
    print("Walking: Try walking more")

if exercise >= 30:
    print("Exercise: Good")
else:
    print("Exercise: Try some physical activity")

# Store data using Pandas
data = {
    "Name": [name],
    "Sleep Hours": [sleep],
    "Water Litres": [water],
    "Steps": [steps],
    "Exercise Minutes": [exercise]
}

df = pd.DataFrame(data)

print("\n===== HEALTH DATA =====")
print(df)

# Save data in CSV file
df.to_csv("health_data.csv", index=False)

print("\nYour health data has been saved!")
