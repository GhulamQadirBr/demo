from part1 import df
import matplotlib.pyplot as mpl

bus_count=df["Bus_Type"].value_counts()
mpl.figure(figsize=(10,6))
bus_count.plot(kind='pie', color='pink')
mpl.title("Count of Buses by Type")
mpl.xlabel("Bus_Type")
mpl.ylabel("Count")
mpl.xticks(rotation=45)
# mpl.show()


mpl.figure(figsize=(8,6))
mpl.scatter(df["Morning_Departure"], [1] * len(df), label="Morning_Departure", color='black', alpha=0.5)
mpl.scatter(df["Evening_Departure"], [1] * len(df), label="Evening_Departure", color='orange', alpha=0.5)
mpl.title("Morning and Evening Departure Times")
mpl.xlabel("Time")
mpl.yticks([])  
mpl.legend()
# mpl.show()


route_counts = df["Route_Name"].value_counts()
mpl.figure(figsize=(8,8))
route_counts.plot(kind='pie', autopct='%1.1f%%', colors=mpl.cm.Paired.colors, startangle=90)
mpl.title("Distribution of Routes Covered")
mpl.ylabel("")
# mpl.show()

