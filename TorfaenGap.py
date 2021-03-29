import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import streamlit as st


#Load data
df = pd.read_csv('TorfaenEI.csv')
df=df.sort_values(['Minimum age in months'], ascending = False) 
size=df['Intervention Name'].count()
st.title("Torfaen Early Intervention : Gap Analysis")

services = pd.DataFrame(df['Primary Domain/Need'].unique())
services.loc[-1] = ['Show All']  # adding a row
services.index = services.index + 1  # shifting index
services = services.sort_index()  # sorting by index

unitarspec = pd.DataFrame(df['Universal/Targeted/Specialist'].unique())
unitarspec.loc[-1] = ['Show All']  # adding a row
unitarspec.index = unitarspec.index + 1  # shifting index
unitarspec = unitarspec.sort_index()  # sorting by index

#Select a Service
servicearea = st.selectbox('Select a Theme/Area:', services)
unitarspec = st.selectbox('Select whether Universal, Targeted or Specialist:', unitarspec)

if (servicearea != 'Show All') & (unitarspec != 'Show All'):	
	df = df[(df['Primary Domain/Need']==servicearea) & (df['Universal/Targeted/Specialist']==unitarspec)]
	size=df['Intervention Name'].count()

if (servicearea != 'Show All') & (unitarspec == 'Show All'):	
	df = df[(df['Primary Domain/Need']==servicearea)]
	size=df['Intervention Name'].count()

if (servicearea == 'Show All') & (unitarspec != 'Show All'):	
	df = df[(df['Universal/Targeted/Specialist']==unitarspec)]
	size=df['Intervention Name'].count()
	
fig, ax = plt.subplots()
figure = plt.gcf()
figure.set_size_inches(8,(size/2))
plt.style.use('fivethirtyeight')
plt.hlines(y=df['Intervention Name'], xmin=df['Minimum age in months'], xmax=df['Maximum age in months'], color='green', alpha=0.6)
plt.scatter(df['Minimum age in months'], df['Intervention Name'], color='black', alpha=1)
plt.scatter(df['Maximum age in months'], df['Intervention Name'], color='black', alpha=1)

plt.xlabel('Age (Months)')
plt.ylabel('Intervention Name')

st.pyplot(figure)


	
	
	
