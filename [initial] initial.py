import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df2023 = pd.read_csv('2023.csv').copy()
df2022 = pd.read_csv('2022.csv').copy()
df2021 = pd.read_csv('2021.csv').copy()

#어떤 열이 있는 지 확인
#df2023.info()
df2023 = df2023.drop(['upperwhisker','lowerwhisker','Standard error of ladder score','Explained by: Log GDP per capita','Explained by: Social support','Explained by: Healthy life expectancy','Explained by: Freedom to make life choices','Explained by: Generosity','Explained by: Perceptions of corruption'],axis=1)
df2023.columns = ['country','score','GDP','support','health','freedom','generosity','corruption','score_dystopia','dystopia_residual']

#Dystopia - 한국은 97위에 랭크되어 있다.
df2023_dystopia = df2023.sort_values('dystopia_residual', ascending =False)
df2023_dystopia = df2023_dystopia.reset_index(drop='True')
print(df2023_dystopia[['country','dystopia_residual']])
