import pandas as pd
df=pd.read_csv("./tesla-stock-price.csv")
reversed_df=df.dropna(subset=['date'])
reversed_df=reversed_df[::-1]
reversed_df.to_csv('new-tela-stock-prices.csv',index=False)