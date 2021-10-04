import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
bargraph=px.bar(df,x='Country',y='InternetUsers')
bargraph.show()