import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#LOADING THE DATASETS#
drivers = pd.read_csv("data/drivers.csv")
results = pd.read_csv("data/results.csv")
races = pd.read_csv("data/races.csv")


#MERGING THE DATASETS#
data = results.merge(drivers, on="driverId")
data = data.merge(races, on="raceId")


#CREATE DRIVER's NAME COLOUMN#
data["driver_name"] = data["forename"] + " " + data["surname"]


# TOP 10 DRIVERS BY TOTAL POINTS#
driver_points = data.groupby("driver_name")["points"].sum().sort_values(ascending=False).head(10)

print("Top 10 Drivers by Total Points")
print(driver_points)

plt.figure(figsize=(10,5))
driver_points.plot(kind="bar")
sns.set(style="darkgrid")

plt.title("Top 10 Drivers by Total Points")
plt.xlabel("Driver")
plt.ylabel("Total Points")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# AVERAGE FINISHING POSITION OF DRIVERS#
avg_position = data.groupby("driver_name")["positionOrder"].mean().sort_values().head(10)

print("\nTop Drivers by Average Finishing Position")
print(avg_position)

plt.figure(figsize=(10,5))
avg_position.plot(kind="bar")
sns.set(style="darkgrid")

plt.title("Top Drivers by Average Finishing Position")
plt.xlabel("Driver")
plt.ylabel("Average Position")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# POSITION GAIN DURING RACE #
data["position_gain"] = data["grid"] - data["positionOrder"]

gain = data.groupby("driver_name")["position_gain"].mean().sort_values(ascending=False).head(10)

print("\nDrivers Who Gain Most Positions During Races")
print(gain)

plt.figure(figsize=(10,5))
gain.plot(kind="bar")
sns.set(style="darkgrid")

plt.title("Drivers Who Gain Most Positions During Races")
plt.xlabel("Driver")
plt.ylabel("Average Position Gain")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# POINTS DISTRIBUTION FOR TOP DRIVERS#
top_drivers = driver_points.index

plt.figure(figsize=(10,6))

sns.boxplot(
    data=data[data["driver_name"].isin(top_drivers)],
    x="driver_name",
    y="points"
)
sns.set(style="darkgrid")
plt.title("Points Distribution for Top Drivers")
plt.xlabel("Driver")
plt.ylabel("Points")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


