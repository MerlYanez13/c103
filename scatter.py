import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
bargraph=px.scatter(df,x='Population',y='Per capita',size='Percentage', color='Country')
bargraph.show()