#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests 
import pandas as pd 
from bs4 import BeautifulSoup 


# In[ ]:


# Downloading contents of the web page 
url = "https://en.wikipedia.org/wiki/College_admissions_in_the_United_States"
data = requests.get(url).text


# In[ ]:


soup = BeautifulSoup(data, 'html.parser')


# In[ ]:


print('Classes of each table: ')
for table in soup.find_all('table'):
    print(table.get('class'))


# In[ ]:


tables = soup.find_all('table')

table = soup.find('table', class_='wikitable')


# In[ ]:


df = pd.DataFrame(columns=['Admit Year', 'Apps', 'Admits', 'Enroll' 'Admit Rate', 'Admit: Enroll'])

for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')
    
    if(columns != []):
        admityear = columns[0].text.strip()
        Apps = columns[1].text.strip()
        Admits = columns[2].text.strip()
        Enroll = columns[3].text.strip()
        Admit_Rate = columns[4].text.strip()
        Admit_Enroll = columns[5].text.strip()
        
        df = df.append({'Admit Year': admityear, 'Apps': Apps, 'Admits': Admits, 'Enroll': Enroll, 'Admit Rate': Admit_Rate, 'Admit: Enroll' : Admit_Enroll}, ignore_index=True)    
        df.to_csv("schoolwikidata.csv", sep=',')


# In[ ]:


admission = pd.read_csv("wikidata.csv")
admissionchanges = pd.DataFrame(admission)
admissionchanges


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import csv

filename = 'wikidata.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    apps = []
    for row in reader:
        if row[1]=='':
            continue
        app = int(row[1])
        apps.append(app) 

  
#reading the database

data = pd.read_csv("wikidata.csv")
  
fig, ax = plt.subplots(dpi=150)
plt.plot(data['Admit Year'], apps, c = 'red' , marker = 'o', mfc = 'white')


# Adding Title to the Plot
plt.title("Application Numbers over the Last 20 Years")
  
# Setting the X and Y labels
plt.xlabel('Admit Year')
plt.ylabel('Applications in Millions')

  
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import csv

filename = 'wikidata.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    rates = []
    for row in reader:
        rate = float(row[2])
        rates.append(rate)

  
#reading the database

data = pd.read_csv("wikidata.csv")
  
fig, ax = plt.subplots(dpi=150)
plt.plot(data['Admit Year'], rates, c = 'blue' , marker = 'o', mfc = 'white')


# Adding Title to the Plot
plt.title("Students Admitted over the Last 20 Years")
  
# Setting the X and Y labels
plt.xlabel('Admission Year')
plt.ylabel('Student Admitted')

  
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import csv

filename = 'wikidata.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    rates = []
    for row in reader:
        rate = float(row[3])
        rates.append(rate)

  
#reading the database

data = pd.read_csv("wikidata.csv")
  
fig, ax = plt.subplots(dpi=150)
plt.plot(data['Admit Year'], rates, c = 'green' , marker = 'o', mfc = 'white')


# Adding Title to the Plot
plt.title("Students Enrolled over the Last 20 Years")
  
# Setting the X and Y labels
plt.xlabel('Admission Year')
plt.ylabel('Students Enrolled')

  
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import csv

filename = 'wikidata.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    rates = []
    for row in reader:
        rate = float(row[4])
        rates.append(rate)

  
#reading the database

data = pd.read_csv("wikidata.csv")
  
fig, ax = plt.subplots(dpi=150)
plt.plot(data['Admit Year'], rates, c = 'black' , marker = 'o', mfc = 'white')


# Adding Title to the Plot
plt.title("Admission Rate over the Last 20 Years")
  
# Setting the X and Y labels
plt.xlabel('Admission Year')
plt.ylabel('Admission Rate')

  
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import csv

filename = 'wikidata.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    rates = []
    for row in reader:
        rate = float(row[5])
        rates.append(rate)

  
#reading the database

data = pd.read_csv("wikidata.csv")
  
fig, ax = plt.subplots(dpi=150)
plt.plot(data['Admit Year'], rates, c = 'purple' , marker = 'o', mfc = 'white')


# Adding Title to the Plot
plt.title("Admission Enrollment Ratio the Last 20 Years")
  
# Setting the X and Y labels
plt.xlabel('Admission Year')
plt.ylabel('Admit: Enroll Ratio')

  
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

cost = pd.read_csv("schooldata.csv")
costchange = pd.DataFrame(cost)
costchange


# In[ ]:


fig, ax = plt.subplots(dpi=150)
costchange.plot(kind='line', x ='Year', marker = 'o',mfc ='white' ,ax=ax)
ax.set_xlabel("Year Change")
ax.set_ylabel("Price Change")
plt.title("Changes in Tuition over the last 20 years")

plt.show()


# In[ ]:




