from part1 import df
from part2 import mpl
busiest_routes=df["Route_Name"].value_counts()
print("top 5 Busiest Routes")
print(busiest_routes.head())

mpl.figure(figsize=(10,6))
busiest_routes.head(10).plot(kind='bar', color='green')
mpl.title("Top 10 Busiest Bus Routes")
mpl.xlabel("Route Name")
mpl.ylabel("Number of Buses")
mpl.xticks(rotation=45)
mpl.show()

