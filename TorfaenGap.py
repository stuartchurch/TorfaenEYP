import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import streamlit as st

@st.cache
def load_data():
    data = pd.read_csv('TorfaenEI.csv')
    return data

df = load_data()

#df = pd.read_csv('TorfaenEI.csv')
df = df.dropna( how='any', subset=['Minimum age in months', 'Maximum age in months'])
df=df.sort_values(['Primary Domain/Need','Minimum age in months']) 
size=df['Intervention Name'].count()

#add new column for colour and make black by default
df['Colour']='Red'

lookupDict = {'Vulnerable families': 'Red', 
	'Additional learning needs': 'Blue',
	'Physical development and health': 'Green',
	'Social and emotional': 'Brown',
	'Cognitive development/Education': 'Grey',	
	'Speech, language and communication': 'Violet'}

mask = df['Primary Domain/Need'].isin(lookupDict.keys())
df.loc[mask, 'Colour'] = df.loc[mask, 'Primary Domain/Need'].map(lookupDict)

st.title("Torfaen Early Years Provision")

services = pd.DataFrame(df['Primary Domain/Need'].unique())
services.loc[-1] = ['Show All']  # adding a row
services.index = services.index + 1  # shifting index
services = services.sort_index()  # sorting by index

unitarspec = pd.DataFrame(df['Universal/Targeted/Specialist'].unique())
unitarspec.loc[-1] = ['Show All']  # adding a row
unitarspec.index = unitarspec.index + 1  # shifting index
unitarspec = unitarspec.sort_index()  # sorting by index

#Select a Service
servicearea = st.selectbox('Select a Domain/Need:', services)
unitarspec = st.selectbox('Select whether Universal, Targeted or Specialist:', unitarspec)

st.image('key.png')

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
plt.hlines(y=df['Intervention Name'], xmin=df['Minimum age in months'], xmax=df['Maximum age in months'], color=df['Colour'], alpha=0.6)
plt.scatter(df['Minimum age in months'], df['Intervention Name'], color='black', alpha=1)
plt.scatter(df['Maximum age in months'], df['Intervention Name'], color='black', alpha=1)

plt.xlabel('Age (Months)')
plt.ylabel('Intervention Name')

st.pyplot(figure)


	
