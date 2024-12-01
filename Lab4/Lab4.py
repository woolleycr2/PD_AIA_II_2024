import pandas as pd

#1
df1 = pd.read_csv("date_climatice_2016.csv")
print(df1)

#2
df1.pop("LAT")
df1.pop("LON")
df1.pop("R24")

#3
df1 = df1.astype({
    "DATCLIM" : "datetime64[ns]",
    "CODST" : "category"})
df1.info()

#4
df2 = pd.read_csv("statii_meteo.csv")
print(df2)

#5
df2 = df2.rename(columns={"ID": "CODST", "Nume": "NUME"})

#6
df1 = df2.merge(df1, on="CODST")

#7
mean_TMED = df1["TMED"].mean()
print(mean_TMED)
max_TMAX = df1["TMAX"].max()
print(max_TMAX, df1.query("TMAX == @max_TMAX")["NUME"])
min_TMIN = df1["TMIN"].min()
print(min_TMIN, df1.query("TMIN == @min_TMIN")["NUME"])

#8a
date_statistice = df1[["NUME", "ALT", "TMIN"]].groupby("NUME").min()

#8b
date_statistice = date_statistice.merge(df1[["NUME", "TMED"]].groupby("NUME").mean(), on="NUME")

#8c
date_statistice = date_statistice.merge(df1[["NUME", "TMAX"]].groupby("NUME").max(), on="NUME")

#8d
print(date_statistice)

#9
print(date_statistice.corr())