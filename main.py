import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('rentals.csv')
# print(df)
#
# print(df.head())

total_rental_days = df["days"].sum()
# print(total_rental_days)

average_rating = df["rating"].mean().round(2)

# print(average_rating)

most_rented_car = df["car"].mode()[0]

# print(most_rented_car)

each_rented_car = df["car"].value_counts()
# print(each_rented_car)

each_car_days = df.groupby('car')["days"].sum()

# print(each_car_days)

revenue = df["revenue"] =  df["days"] * df["price_per_day"]
most_money_car = df.groupby("car")["revenue"].sum()

print(df)

most_money_car.plot( kind="bar", color="skyblue", edgecolor="black")
plt.xlabel("Car")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()