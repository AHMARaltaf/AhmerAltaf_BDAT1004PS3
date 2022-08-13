#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[1]:


import pandas as pndss #Importing libraries
import numpy as nampi #Importing libraries

users = pndss.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep = '|')
#reading the csv file which is seperated by '|' and storing in variable name users
users
#printing the variable users


# In[2]:


users.groupby('occupation').age.mean()
#grouping the variable users here based on average of age of various occupation type


# In[72]:


# Step 5
def sex_determine(s): #defining a method to filter our different genders where if male, then returning 1 else 0
    if s == 'M':
        return 1
    if s == 'F':
        return 0

users['gender_reveal'] = users['gender'].apply(sex_determine)
#storing data based on gender revealed in the previous step

a = users.groupby('occupation').gender_reveal.sum() / users.occupation.value_counts()
#getting the %age factor based on the occupation

a.sort_values(ascending = False)
#printing the values based on descending sorting


# In[4]:


#Step 6
users.groupby('occupation').age.agg(['min', 'max'])
#grouping the variable users here based on maximum and minimum age of that particular occupation


# In[5]:


#Step 7
users.groupby(['occupation','gender']).mean('age')
#grouping the variable users here based on user id, age and gender reveal done earlier where male = 1 and female = 0.


# In[6]:


#Step 8
sex_type_occupation = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})
#grouping the variable users here based on occupation and gender with the count
total_cnt = users.groupby(['occupation']).count()
#storing the total count of each occupation in this variable
occ_sex = sex_type_occupation.div(total_cnt, level = "occupation")
occ_sex.loc[:, 'gender']
#printing the values from the variable, value is splitted on the base of
gender


# # Question 2

# In[7]:


import pandas as pndss #Importing libraries
import numpy as nampi #Importing libraries
euro12 = pndss.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv')
#Reading the data from the GITHUB file and storing in variable - euro12 
euro12.head
#printing the top rows of the data from euro12


# In[8]:


#Step 4
euro12.Goals #printing the data based on the goals from the dataset


# In[9]:


#Step 5
euro12.Team.nunique()
#printing the unique count of teams from the dataset


# In[10]:


#Step 6
euro12.info()
#defining the dataset or the variable which has all the data


# In[12]:


#Step 7
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
#storing the data in a variable based on the teams with less red cards and yellow cards
discipline.head
#printing the top rows of the variable to show results


# In[13]:


#Step 8
discipline.sort_values(['Red Cards','Yellow Cards'], ascending=[True,True])
#printing the data after sorting it based on Red Cards first and then on yellow cards


# In[14]:


#Step 9
discipline['Yellow Cards'].mean()
#printing the mean value of yellow cards given


# In[16]:


#Step 10
euro12[euro12['Goals'] > 6]
#Filtering the data based on the teams who scored more than 6 goals


# In[17]:


#Step 11
euro12[euro12.Team.str.startswith('G')]
#printing the values after filterting the teams which start with the letter "G"


# In[18]:


#Step 12
euro12.head(7)
#printing the top 7 rows of the data stored in the variable


# In[20]:


#Step 13
euro12.iloc[:, :-3]
#printing all the data here with all rows and columns, except the last 3 columns


# In[21]:


#Step 14
euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]
#printing the data with a filter of three countries according to thier shooting accuracy


# # Question 3

# In[23]:


import pandas as pndss #Importing libraries
import numpy as nampi #Importing libraries
sequel_1 = pndss.Series(nampi.random.randint(1,5,100)) 
#creating a series - 1 with a random number from 1 to 4
sequel_2 = pndss.Series(nampi.random.randint(1,4,100)) 
#creating a series - 2 with a random number from 1 to 3
sequel_3 = pndss.Series(nampi.random.randint(10000, 30001, 100)) 
#creating a series - 3 with a random number from 10,000 to 30,000
daata_freme_1 = pndss.DataFrame(sequel_1, columns=['random_numbers 1-4']) 
#creating dataframe for first series
daata_freme_2 = pndss.DataFrame(sequel_2, columns=['random_numbers 1-3']) 
#creating dataframe for second series
daata_freme_3 = pndss.DataFrame(sequel_3, columns=['random_numbers 10,000 - 30,000']) 
#creating dataframe for third series
print(daata_freme_1, daata_freme_2, daata_freme_3)
#Priting all the data frames just created above


# In[24]:


#Step 3
join_series = pndss.concat([sequel_1, sequel_2, sequel_3], axis=1)
join_series.head()


# In[25]:


#Step 4
join_series.rename(columns = {0: 'bedrs', 1: 'bathrs', 2: 'price_sqr_meter'}, inplace=True)
#renaming first three columns with the desired names
join_series.head()
#printing the top data from the variable


# In[26]:


#Step 5
bigcolumn = pndss.concat([sequel_1, sequel_2, sequel_3])
#concatenating the values of three different series in a new viariable
bigcolumn = bigcolumn.to_frame()
#Converting the data from the variable into a dataframe
bigcolumn
#printing the dataframe


# In[27]:


len(bigcolumn)
#Answer: Length of dataframe is more than 90, hence it is not true


# In[28]:


bigcolumn.reset_index(drop=True, inplace=True)
#resetting the index of the dataframe using reset_index command
bigcolumn
#printing the dataframe so that we are able to see the index going from 0 to 299


# # Question 4

# In[2]:


import pandas as pndss #Importing library
import datetime #Importing library
data = 'wind_ahmer.txt' #storing the data in a new variable called data
data = pndss.read_csv(data, sep = "\s+", parse_dates = [[0,1,2]]) 
#Reading the data and storing it seperated by enter
data.head()
#printing the top data using head command


# In[3]:


#Step 4
def modify_year(x): #Creating a method to fix the year of the data
  year = x.year - 100 if x.year > 1989 else x.year # Equating a formulae to fix the year of the dataset based on some conditions
  return datetime.date(year, x.month, x.day) #Returning the fixed dates

data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(modify_year)
#making changes using the method to the actual data 
data.head()
#printing the data with fixed year


# In[58]:


#Step 5
data["Yr_Mo_Dy"] = pndss.to_datetime(data["Yr_Mo_Dy"])
data = data.set_index('Yr_Mo_Dy')
#setting the new index and format to the data using set_index function
data.head()
#printing the top rows of the data using the head command


# In[59]:


#Step 6
data.isnull().sum()
#printing the count of data with null values


# In[60]:


#Step 7
data.notnull().sum()
#printing the count of data where value is not null


# In[61]:


#Step 8
data.sum().sum() / data.notna().sum().sum()
#Calculating the mean windspeeds of the windspeeds over all the locations and all the times


# In[70]:


#Step 9
loc_stats = pndss.DataFrame() 
#creating a dataframe 
loc_stats = data.describe(percentiles=[])
#we are describing the data and printing mean, std, man and min.
loc_stats


# In[63]:


#Step 10
day_stats = pndss.DataFrame()
#Creating a dataframe
day_stats['Minimum'] = data.min(axis = 1) 
#Defining the Minimum column
day_stats['Maximum'] = data.max(axis = 1)  
#Defining the Maximum column
day_stats['Mean'] = data.mean(axis = 1)
#Defining the Mean column
day_stats['standard deviations'] = data.std(axis = 1) 
#Defining the std column
day_stats.head()
#printing the dataframe


# In[64]:


#Step 11
data.loc[data.index.month == 1].mean()
#getting the data for the january month using the .index.month command and then taking the mean for all the categories


# In[65]:


#Step 12
data.groupby(data.index.to_period('A')).mean()
#Grouping the data based on period = annual(A)


# In[66]:


#Step 13
data.groupby(data.index.to_period('M')).mean()
#Grouping the data based on period = monthly(M)


# In[67]:


#Step 14
data.groupby(data.index.to_period('W')).mean()
#Grouping the data based on period = weekly(W)


# In[71]:


#Step 15
weekly = data.resample('W').agg(['min','max','mean','std'])
#Reshaping the data for each category based on these fields: Minimum, Maximum, Mean and Standard Deviaion
weekly.loc[weekly.index[1:53], "RPT":"MAL"] .head(12)
#Printing the data of 1-52 weeks starting from January 2 1961


# # Question 6

# In[29]:


import pandas as pndss #Importing libraries
import numpy as nampi #Importing libraries
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as ps3_plot #Importing the plotting library
USA_shaadi_Div_Rate = pndss.read_csv('us-marriages-divorces-1867-2014_ahmer_ps_3.csv')
#Reading the data from CSV files stored in my Jupitor Home page directory
years = USA_shaadi_Div_Rate['Year'].values
#storing the year data in years which is getting retrived from the dataset
shaadi_rate_per_capita = USA_shaadi_Div_Rate['Marriages_per_1000'].values
#storing the marriage per 1000 data in the new variable which is getting retrived from the dataset
divorce_rate_per_capita = USA_shaadi_Div_Rate['Divorces_per_1000'].values
#storing the divorce per 1000 data in the new variable which is getting retrived from the dataset


# In[30]:


ps3_plot.figure()
#plotting the graph
ps3_plot.plot(years, shaadi_rate_per_capita,label='Marriages_per_Capita')
#defining the data with a label
ps3_plot.plot(years, divorce_rate_per_capita,label='Divorces_per_Capita')
#defining the data with a label
ps3_plot.legend()


# # Question 7

# In[31]:


import pandas as pndss #Importing libraries
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as ps3_plot #Importing libraries for platting graphs
import numpy as nampi #Importing libraries


USA_shaadi_Div_Rate = pndss.read_csv('us-marriages-divorces-1867-2014_ahmer_ps_3.csv')
#Reading the data from CSV files stored in my Jupitor Home page directory
USA_shaadi_Div_Rate = USA_shaadi_Div_Rate[
    USA_shaadi_Div_Rate['Year'].apply(lambda x: x in [1900, 1950, 2000])]
years = USA_shaadi_Div_Rate['Year'].values
#storing the year data in years which is getting retrived from the dataset
shaadi_rate_per_capita = USA_shaadi_Div_Rate['Marriages_per_1000'].values
#storing the marriage per 1000 data in the new variable which is getting retrived from the dataset
divorce_rate_per_capita = USA_shaadi_Div_Rate['Divorces_per_1000'].values
#storing the divorce per 1000 data in the new variable which is getting retrived from the dataset
ps3_plot.figure()
#plotting the graoh
ps3_plot.bar(years, shaadi_rate_per_capita, 
        color='blue',
        width=3.4,
        align='center',
        label='Marriages per capita')
#additing label, colour and formating to the data
ps3_plot.bar(years, divorce_rate_per_capita,
        color='red',
        width=5.4,
        align='center',
        label='Divorces per capita')
#additing label, colour and formating to the data
ps3_plot.legend()


# # Question 8

# In[32]:


import pandas as pndss #Importing libraries

hollywood_hero_dead = pndss.read_csv('actor_kill_counts_ahmer_ps_3.csv')
#Reading the data from CSV files stored in my Jupitor Home page directory
hollywood_hero_dead
#printing the data 


# In[37]:


import pandas as pndss #Importing libraries
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as ps3_plot #Importing library for graph ploting
import numpy as nampi #Importing libraries
hollywood_hero_dead = pndss.read_csv('actor_kill_counts_ahmer_ps_3.csv')
#Reading the data from CSV files stored in my Jupitor Home page directory
hero_naam = hollywood_hero_dead['Actor'].values #Creating a variable with data related to actors
total_kill = hollywood_hero_dead['Count'].values #Creating a variable with the total kill count from the dataset
hero_cat_list = pndss.DataFrame({'hero_naam': hero_naam,
                                'total_kill': total_kill})
#creating a dataframe of the above two variables just created
hero_cat_list.sort_values(by='total_kill', ascending=True)
#sorting the data based on the total kill
ps3_plot.figure()
#Plotting the graph
ps3_plot.barh(nampi.arange(len(hero_naam)), total_kill)
ps3_plot.yticks(nampi.arange(len(hero_naam)),
           ['actor_names {}'.format(x) for x in hero_naam])


# # Question 9 

# In[39]:


#Question 9 
romaaan_emp_region = pndss.read_csv("roman-emperor-reigns_ahmer_ps_3.csv")
#Reading the data from CSV files stored in my Jupitor Home page directory
romaaan_emp_region.head
#printing the top data of the data using head command


# In[40]:


dead_body_total= romaaan_emp_region.groupby(romaaan_emp_region["Cause_of_Death"]).Cause_of_Death.count()
#storing the data based on cause of death from the dataset
dead_body_total=list(dead_body_total)
#converting the data into a list
dead_body_total
#printing the list


# In[41]:


death_list=['Assassinated', 'Died in Captivity', 'Illness', 'Killed in battle', 'Natural causes', 'Possibly assassinated' ,'Suicide','Executed']


# In[50]:


ps3_plot.pie(dead_body_total, 
        labels = death_list,autopct = '%0.0f%%',
        colors=['blue', 'orange', 'red', 'green', 'yellow', 'purple', 'pink', 'grey'])
#defining the pie chart and different colours in which it will showcast the data
ps3_plot.show


# # Question 10

# In[54]:


ar_rev_and_doc_rev_compare = pndss.read_csv('arcade-revenue-vs-cs-doctorates_ahmer_ps3.csv')
#Reading the data from CSV files stored in my Jupitor Home page directory
ar_rev_and_doc_rev_compare.head(10)
#comparing the values for two columns for the year 2000-2009


# In[53]:


import seaborn as samandar #Importing libraries
samandar.lmplot(x='Total Arcade Revenue (billions)', y='Computer Science Doctorates Awarded (US)', data=ar_rev_and_doc_rev_compare, hue='Year', fit_reg=True).set(title='Total revenue earned vs the number of computer science Doctorates Awarded (US)')
#setting the graph name, axis names and the data to be plotted
ps3_plot.show()
#plotting the above defined graph


# # References

# #### 1 . www.google.com

# #### 2.https://www.python.org/

# #### 3 . Class Notes

# In[ ]:


4 . 

