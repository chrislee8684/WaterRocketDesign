import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')
print(df.head())

# Altitude vs. Time
plt.figure(figsize=(10, 6))
plt.plot(df['Time (ms)'], df['Altitude'], marker='o', linestyle='-', color='b')
plt.title('Altitude vs. Time')
plt.xlabel('Time (ms)')
plt.ylabel('Altitude (m)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Alt-vs-Time')

# Z-accel vs. Time
plt.figure(figsize=(10, 6))
plt.plot(df['Time (ms)'], df['Z-accel'], marker='o', linestyle='-', color='b')
plt.title('Z-accel vs. Time')
plt.xlabel('Time (ms)')
plt.ylabel('Z-accel (m/s)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Z-accel-vs-Time')

# Temperature vs. Altitude
plt.figure(figsize=(10, 6))
plt.plot(df['Altitude'], df['Temperature'], marker='o', linestyle='-', color='b')
plt.title('Temperature vs. Altitude')
plt.xlabel('Altitude')
plt.ylabel('Temperature')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Temperature-vs-Altitude')

# Pressure vs. Altitude
plt.figure(figsize=(10, 6))
plt.plot(df['Altitude'], df['Pressure'], marker='o', linestyle='-', color='b')
plt.title('Z-accel vs. Altitude')
plt.xlabel('Altitude')
plt.ylabel('Pressure')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Pressure-vs-Altitude')

# Humidity vs. Altitude
plt.figure(figsize=(10, 6))
plt.plot(df['Altitude'], df['Humidity'], marker='o', linestyle='-', color='b')
plt.title('Humidity vs. Altitude')
plt.xlabel('Altitude')
plt.ylabel('Humidity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Humidity-vs-Altitude')

# Pairplot
sns.pairplot(df)
plt.savefig('Pairplot')