# %%
# Aparencias(weather) : sol(sunny), nublado(cloudy), chuva(raining)
# Temperatura(temperature): -130 to 130 F
# Umidade(humidity): 0 to 100
# Vento(Wind): FALSO(FALSE), VERDADEIRO(TRUE)
# Jogar(play): sim/nao

# %%
import pandas as pd
import seaborn as srn
import statistics  as sts
import numpy as np

# %%
dataset = pd.read_csv("tempo.csv", sep=";")
dataset.head()

# %%
dataset.shape

# %%
dataset.columns = ["weather", "temperature", "humidity", "wind", "play"]

# %%
dataset.head()

# %%
dataset.isnull().sum()

# %%
dataset["humidity"].describe()
# %%
median = sts.median(dataset["humidity"])
median

# %%
dataset["humidity"].fillna(median, inplace=True)

# %%
dataset["humidity"].isnull().sum()

# %%
dataset.loc[(dataset["humidity"] > 100), "humidity"] = median

# %%
dataset.loc[(dataset["humidity"] > 100)]

# %%
dataset["wind"].describe()
# %%
mode = sts.mode(dataset["wind"])
mode

# %%
dataset.loc[pd.isna(dataset["wind"]), "wind"] = mode

# %%
dataset.loc[pd.isna(dataset["wind"])]

# %%
group = dataset.groupby(["weather"]).size()
group

# %%
dataset["weather"].replace("menos", "chuva", inplace=True)  

# %%
group = dataset.groupby(["weather"]).size()
group

# %%
dataset.head()

# %%
dataset["temperature"].describe()

# %%
median = sts.median(dataset["temperature"])
median

# %%
dataset.loc[(dataset["temperature"] > 100), "temperature"] = median

# %%
dataset["temperature"].describe()

# %%
group2 = dataset.groupby(["play"]).size()
group2



# %%
