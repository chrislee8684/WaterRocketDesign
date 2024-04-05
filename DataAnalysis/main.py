# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Intake data as a data frame
df = pd.read_csv('raw_rocket_data.ods')
print(df.head())

# Altitude vs. Time
plt.figure(figsize=(10, 6))
plt.plot(df['Time (ms)'], df['Altitude'], marker='o', linestyle='-', color='b')
plt.title('Altitude vs. Time')
plt.xlabel('Time (ms)')
plt.ylabel('Altitude (m)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show('Alt-vs-Time')

# Z-accel vs. Time
plt.figure(figsize=(10, 6))
plt.plot(df['Time (ms)'], df['Z-accel'], marker='o', linestyle='-', color='b')
plt.title('Z-accel vs. Time')
plt.xlabel('Time (ms)')
plt.ylabel('Z-accel (m/s)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show('Z-accel-vs-Time')

# Temperature vs. Altitude
plt.figure(figsize=(10, 6))
plt.plot(df['Altitude'], df['Temperature'], marker='o', linestyle='-', color='b')
plt.title('Temperature vs. Altitude')
plt.xlabel('Altitude')
plt.ylabel('Temperature')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show('Temperature-vs-Altitude')

# Pressure vs. Altitude
plt.figure(figsize=(10, 6))
plt.plot(df['Altitude'], df['Pressure'], marker='o', linestyle='-', color='b')
plt.title('Z-accel vs. Altitude')
plt.xlabel('Altitude')
plt.ylabel('Pressure')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show('Pressure-vs-Altitude')

# Humidity vs. Altitude
plt.figure(figsize=(10, 6))
plt.plot(df['Altitude'], df['Humidity'], marker='o', linestyle='-', color='b')
plt.title('Humidity vs. Altitude')
plt.xlabel('Altitude')
plt.ylabel('Humidity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show('Humidity-vs-Altitude')

# Pairplot
sns.pairplot(df)
plt.show('Pairplot')