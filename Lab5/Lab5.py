import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 25))

#1
x_1 = np.arange(-5, 5, 0.01)
y_1 = (x_1 + 1) / (x_1 ** 2 - 2)
y_2 = x_1 * np.log2(x_1 ** 2)

plt.subplot(5, 2, 1)
plt.plot(x_1, y_1, "r-", x_1, y_2, "g--")

#2
x_2 = np.arange(0, 8 * np.pi, 0.01)
y_3 = np.sin(1.5 * x_2)
y_4 = np.cos(x_2 / 2)

plt.subplot(5, 2, 3)
plt.plot(x_2, y_3)
plt.subplot(5, 2, 4)
plt.plot(x_2, y_4)

#3a

#alternative: data module
df1 = pd.read_csv('date_climatice_2016.csv')
df1.pop("LAT")
df1.pop("LON")
df1.pop("R24")
df1 = df1.astype({
    "DATCLIM":"datetime64[ns]",
    "CODST":"category"})
df2 = pd.read_csv('statii_meteo.csv')
df2 = df2.rename(columns={"ID": "CODST", "Nume": "NUME"})
df1 = df2.merge(df1, on='CODST')
#alternative: data module

x_3 = df1.query("NUME == 'Botosani'")["DATCLIM"]
y_5 = df1.query("NUME == 'Botosani'")["TMIN"]
y_6 = df1.query("NUME == 'Botosani'")["TMED"]
y_7 = df1.query("NUME == 'Botosani'")["TMAX"]

plt.subplot(5, 2, 5)
plt.plot(x_3, y_5, x_3, y_6, x_3, y_7)
plt.xlabel("DATCLIM")
plt.ylabel("Temperaturi")
plt.title("Grafic 3a")
plt.legend(["TMIN", "TMED", "TMAX"])
plt.tight_layout()

#3b
df1_3b = df1[["CODST", "NUME", "TMIN"]].groupby("CODST").min()
y_3b = df1_3b["NUME"]
x_3b = df1_3b["TMIN"]

plt.subplot(5, 2, 7)
plt.barh(y_3b, x_3b)
plt.xlabel("TMIN")
plt.ylabel("NUME")
plt.title("Grafic 3b")
plt.tight_layout()

#3c
df1_3c = df1[["CODST", "NUME", "ALT", "TMIN"]].groupby("CODST").min()
x_3c = df1_3c["ALT"]
y_3c = df1_3c["TMIN"]

plt.subplot(5, 2, 9)
plt.scatter(x_3c, y_3c)
x_3c.reset_index(drop = True, inplace = True)
y_3c.reset_index(drop = True, inplace = True)
for i, annotation in enumerate(df1_3c["NUME"]):
    plt.annotate(annotation,
                 (x_3c[i], y_3c[i]),
                 textcoords="offset points",
                 xytext=(5,5),
                 ha="center")
plt.xlabel("ALT")
plt.ylabel("TMIN")
plt.title("Grafic 3c")
plt.grid()
plt.tight_layout()

plt.show()





