import pandas as pd

file_path = "buses_routes.xlsx"
df = pd.read_excel(r"D:\sindh_bus_tracker\Copy of Bus_Timing_Routes(1).xlsx")

df.columns = ["Route_Name", "Point_Numbers", "Bus_Type", "Morning_Departure", "Evening_Departure"]


df["Morning_Departure"] = pd.to_datetime(df["Morning_Departure"], format="%H:%M:%S").dt.strftime("%H:%M")
df["Evening_Departure"] = pd.to_datetime(df["Evening_Departure"], format="%H:%M:%S").dt.strftime("%H:%M")
# print(df.head())

bus__count=df["Bus_Type"].value_counts()
print(bus__count)

print("earliest Morning_bus:",df["Morning_Departure"].min())
print("latest Evening_bus:",df["Evening_Departure"].max())

route=df["Route_Name"].unique()
print("total routes:",len(route))
print("routes:",route)