import matplotlib.pyplot as plt 
import pandas as pd
import geopandas as gpd
import numpy as np
import streamlit as st


#Load data
df = pd.read_csv('/Users/stuartchurch/Tresors/Personal/DataSci/GitJupyter/TorfaenEi/TorfaenEI.csv')
df=df.sort_values(['ServiceArea','MinAgeMo']) 
size=df['ServiceName'].count()
st.title("Torfaen Early Intervention : Gap Analysis")

services = pd.DataFrame(df['ServiceArea'].unique())
services.loc[-1] = ['All Service Areas']  # adding a row
services.index = services.index + 1  # shifting index
services = services.sort_index()  # sorting by index

#st.write(services)

#Select a Service
servicearea = st.selectbox('Select a Service Area:', services)
st.subheader(servicearea)

fig, ax = plt.subplots()
figure = plt.gcf()
#figure.set_size_inches(8,12)


if servicearea != 'All Service Areas':	
	df = df[df['ServiceArea']==servicearea]
	size=df['ServiceName'].count()

figure.set_size_inches(8,(size/2))

	

#Programatically make colour dependent on Service Area
plt.style.use('fivethirtyeight')
plt.hlines(y=df['ServiceName'], xmin=df['MinAgeMo'], xmax=df['MaxAgeMo'], color=df['Color'], alpha=0.6)
plt.scatter(df['MinAgeMo'], df['ServiceName'], color=df['Color'], alpha=1)
plt.scatter(df['MaxAgeMo'], df['ServiceName'], color=df['Color'], alpha=1)

#ax.annotate('Social Services', xy=(0,0), xytext=(50, 'Gwent Safeguarding'), color = 'brown')

plt.xlabel('Age (Months)')
plt.ylabel('Service Name')

st.pyplot(figure)

	
	
	
	