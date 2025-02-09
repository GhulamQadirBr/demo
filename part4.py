import pandas as pd
import matplotlib.pyplot as mpl
import streamlit as st

# Load data
file_path = r"D:\sindh_bus_tracker\Copy of Bus_Timing_Routes(1).xlsx"
df = pd.read_excel(file_path)

# Data Preprocessing
df.columns = ["Route_Name", "Point_Numbers", "Bus_Type", "Morning_Departure", "Evening_Departure"]
df["Morning_Departure"] = pd.to_datetime(df["Morning_Departure"], format="%H:%M:%S").dt.strftime("%H:%M")
df["Evening_Departure"] = pd.to_datetime(df["Evening_Departure"], format="%H:%M:%S").dt.strftime("%H:%M")

# Display Data
st.title("Sindh Bus Tracker")
st.write("### Bus Routes Data Overview")
st.dataframe(df.head())

# Bus Count by Type
st.write("### Count of Buses by Type")
bus_count = df["Bus_Type"].value_counts()
st.bar_chart(bus_count)

# Earliest and Latest Departure Times
st.write("### Earliest and Latest Bus Departures")
st.write(f"Earliest Morning Bus: {df['Morning_Departure'].min()}")
st.write(f"Latest Evening Bus: {df['Evening_Departure'].max()}")

# Routes Overview
st.write("### Total Routes")
route = df["Route_Name"].unique()
st.write(f"Total Routes: {len(route)}")
st.write(f"Routes: {route}")

# Pie Chart for Bus Types
st.write("### Bus Type Distribution")
fig, ax = mpl.subplots(figsize=(10, 6))
bus_count.plot(kind='pie', color='pink', ax=ax, autopct='%1.1f%%')
ax.set_ylabel('')
st.pyplot(fig)

# Scatter Plot for Morning and Evening Departure Times
st.write("### Morning and Evening Departure Times")
fig, ax = mpl.subplots(figsize=(8, 6))
ax.scatter(df["Morning_Departure"], [1] * len(df), label="Morning_Departure", color='black', alpha=0.5)
ax.scatter(df["Evening_Departure"], [1] * len(df), label="Evening_Departure", color='orange', alpha=0.5)
ax.set_title("Morning and Evening Departure Times")
ax.set_xlabel("Time")
ax.set_yticks([])
ax.legend()
st.pyplot(fig)

# Distribution of Routes
st.write("### Distribution of Routes Covered")
route_counts = df["Route_Name"].value_counts()
fig, ax = mpl.subplots(figsize=(8, 8))
route_counts.plot(kind='pie', autopct='%1.1f%%', colors=mpl.cm.Paired.colors, startangle=90, ax=ax)
ax.set_ylabel('')
st.pyplot(fig)

# Top 5 Busiest Routes
st.write("### Top 5 Busiest Routes")
busiest_routes = df["Route_Name"].value_counts()
st.write(busiest_routes.head())

# Bar Chart for Top 10 Busiest Routes
st.write("### Top 10 Busiest Bus Routes")
fig, ax = mpl.subplots(figsize=(10, 6))
busiest_routes.head(10).plot(kind='bar', color='green', ax=ax)
ax.set_xlabel("Route Name")
ax.set_ylabel("Number of Buses")
ax.set_xticklabels(busiest_routes.head(10).index, rotation=45)
st.pyplot(fig)
