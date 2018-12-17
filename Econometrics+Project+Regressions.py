
# coding: utf-8

# In[392]:

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats
from sklearn import linear_model
get_ipython().magic('matplotlib inline')


# In[502]:

# OBP, OBP Against, SLG, and SLG Against 1999-2003 Seasons
batting99_03=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/1999-2003_Seasons_Team_Compiled_Batting.csv')
batting99_03


# In[22]:

batting.dtypes


# In[395]:

clf = linear_model.Lasso(alpha=0.1)
clf.fit([[0,0], [1, 1], [2, 2]], [0, 1, 2])
print(clf.coef_, clf.intercept_)


# In[382]:

# regression model #1 -  OBP and OBP Against
results=smf.ols('Win_per ~ OBP + OBP_Against', data=batting99_03).fit().summary()
print(results)


# In[381]:




# In[56]:

# regression model #2 - SLG and SLG Against
#print(smf.ols('Win_per ~ SLG + SLG_Against', data=batting99_03).fit().summary())


# In[384]:

batting99_03['OBP_restricted']=batting99_03['OBP']-batting99_03['OBP_Against']
batting99_03['SLG_restricted']=batting99_03['SLG']-batting99_03['SLG_Against']
batting14_18['OBP_restricted']=batting14_18['OBP']-batting14_18['OBP_Against']
batting14_18['SLG_restricted']=batting14_18['SLG']-batting14_18['SLG_Against']


# In[74]:

# regression model #3 - OBP/OBP Against and SLG/SLG Against
#print(smf.ols('Win_per ~ OBP + OBP_Against + SLG + SLG_Against', data=batting99_03).fit().summary())


# In[387]:

# regression model 4 - equal coefficients
results = smf.ols('Win_per ~ OBP_restricted + SLG_restricted', data=batting99_03).fit()
print(results.summary())


# In[388]:

hyp = 'OBP_restricted = SLG_restricted'
results.f_test(hyp)


# In[59]:

# OBP, OBP Against, SLG, and SLG Against 2014-2018 Seasons
batting14_18 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2014-2018_Seasons_Team_Batting_Compiled.csv')
#batting14_18


# In[60]:

# regression model #1 -  OBP and OBP Against
#print(smf.ols('Win_per ~ OBP + OBP_Against', data=batting14_18).fit().summary())


# In[64]:

# regression model #2 - SLG and SLG Against
#print(smf.ols('Win_per ~ SLG + SLG_Against', data=batting14_18).fit().summary())


# In[76]:

# regression model #3 - OBP/OBP Against and SLG/SLG Against
#print(smf.ols('Win_per ~ OBP + OBP_Against + SLG + SLG_Against', data=batting14_18).fit().summary())


# In[389]:

# regression model 4 - equal coefficients
results2 = smf.ols('Win_per ~ OBP_restricted + SLG_restricted', data=batting14_18).fit()
print(results2.summary())


# In[390]:

hyp = 'OBP_restricted = SLG_restricted'
results2.f_test(hyp)


# In[307]:

# Salaries 2000 Seasons
Salary_Batting00 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2000F.csv')
#Salary_Batting00


# In[ ]:




# In[176]:

print(Salary_Batting00['salary'].mean(),Salary_Batting00['salary'].median(),Salary_Batting00['salary'].quantile([.1, .9]))


# In[169]:

b=Salary_Batting00['salary'].median()
b


# In[175]:

c=Salary_Batting00['salary'].quantile([.1, .9])
c


# In[151]:

#Salaries 2001 Seasons
Salary_Batting01 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2001F.csv')
#Salary_Batting01


# In[149]:

#Salary_Batting01['PlayerID'].value_counts()


# In[137]:

print(Salary_Batting01['Salary'].mean(), Salary_Batting01['Salary'].median(), Salary_Batting01['Salary'].quantile([.1, .9]))


# In[150]:

#Salaries 2002 Seasons
Salary_Batting02 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2002F.csv')
#Salary_Batting02


# In[152]:

#Salary_Batting02['playerID'].value_counts()


# In[143]:

print([Salary_Batting02['salary'].mean(),Salary_Batting02['salary'].median(),Salary_Batting02['salary'].quantile([.1, .9])]) 


# In[180]:

#Salaries 2003 Seasons
Salary_Batting03 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2003F.csv')
#Salary_Batting03


# In[154]:

#Salary_Batting03['playerID'].value_counts()


# In[153]:

print([Salary_Batting03['salary'].mean(),Salary_Batting03['salary'].median(),Salary_Batting03['salary'].quantile([.1, .9])]) 


# In[177]:

#Salaries 2004 Season
Salary_Batting04 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2004F.csv')
#Salary_Batting04


# In[160]:

print([Salary_Batting04['salary'].mean(),Salary_Batting04['salary'].median(),Salary_Batting04['salary'].quantile([.1, .9])]) 


# In[212]:

#Salaries 2012 Season
Salary_Batting12 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2012F.csv')
#Salary_Batting12


# In[211]:

Salary_Batting12['salary'].mean(),Salary_Batting12['salary'].median(),Salary_Batting12['salary'].quantile([.1, .9])


# In[214]:

#Salaries 2013 Season
Salary_Batting13 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2013F.csv')
#Salary_Batting13


# In[213]:

Salary_Batting13['salary'].mean(),Salary_Batting13['salary'].median(),Salary_Batting13['salary'].quantile([.1, .9])


# In[216]:

#Salaries 2014 Season
Salary_Batting14 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2014F.csv')
#Salary_Batting14


# In[215]:

Salary_Batting14['salary'].mean(),Salary_Batting14['salary'].median(),Salary_Batting14['salary'].quantile([.1, .9])


# In[219]:

#Salaries 2015 Season
Salary_Batting15 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2015F.csv')
#Salary_Batting15


# In[218]:

Salary_Batting15['salary'].mean(),Salary_Batting15['salary'].median(),Salary_Batting15['salary'].quantile([.1, .9])


# In[442]:

#Salaries 2016 Season
Salary_Batting16 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2016F.csv')
#Salary_Batting16


# In[221]:

Salary_Batting16['salary'].mean(),Salary_Batting16['salary'].median(),Salary_Batting16['salary'].quantile([.1, .9])


# In[275]:

#2000 Season Average Salaries Across Position Groups and Home Runs
HR25_00=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2000_%3E25HR.csv')
HR14_00=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2000_%3C14HR.csv')
FB_00=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2000_First.csv')
IF_00=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2000_Infielders.csv')
OF_00=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2000_OF.csv')
C_00=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2000_Catchers.csv')


# In[279]:

print(HR25_00['salary'].mean(),HR14_00['salary'].mean(),FB_00['salary'].mean(),IF_00['salary'].mean(),OF_00['salary'].mean(),C_00['salary'].mean())


# In[374]:

#2001 Season Average Salaries Across Position Groups and Home Runs
HR25_01=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2001_%3E25HR.csv')
HR14_01=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2001_%3C14HR.csv')
FB_01=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2001_First.csv')
IF_01=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2001_Infielders.csv')
OF_01=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2001_OF.csv')
C_01=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2001_Catchers.csv')


# In[375]:

print(HR25_01['Salary'].mean(), HR14_01['Salary'].mean(), FB_01['Salary'].mean(),IF_01['Salary'].mean(), OF_01['Salary'].mean(), C_01['Salary'].mean())


# In[282]:

#2002 Season Average Salaries Across Position Groups and Home Runs
HR25_02=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2002_%3E25HR.csv')
HR14_02=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2002_%3C14HR.csv')
FB_02=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2002_First.csv')
IF_02=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2002_Infielders.csv')
OF_02=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2002_OF.csv')
C_02=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2002_Catchers.csv')


# In[283]:

print(HR25_02['salary'].mean(),HR14_02['salary'].mean(),FB_02['salary'].mean(),IF_02['salary'].mean(),OF_02['salary'].mean(),C_02['salary'].mean())


# In[376]:

#2003 Season Average Salaries Across Position Groups and Home Runs
HR25_03=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2003_%3E25HR.csv')
HR14_03=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2003_%3C14HR.csv')
FB_03=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2003_First.csv')
IF_03=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2003_Infielders.csv')
OF_03=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2003_OF.csv')
C_03=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2003_Catchers.csv')


# In[377]:

print(HR25_03['salary'].mean(),HR14_03['salary'].mean(),FB_03['salary'].mean(),IF_03['salary'].mean(),OF_03['salary'].mean(),C_03['salary'].mean())


# In[278]:

#2004 Season Average Salaries Across Position Groups and Home Runs
HR25_04=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2004_%3E25HR.csv')
HR14_04=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2004_%3C14HR.csv')
FB_04=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2004_First.csv')
IF_04=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2004_Infielders.csv')
OF_04=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2004_OF.csv')
C_04=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2004_Catchers.csv')


# In[285]:

print(HR25_04['salary'].mean(),HR14_04['salary'].mean(),FB_04['salary'].mean(),IF_04['salary'].mean(),OF_04['salary'].mean(),C_04['salary'].mean())


# In[224]:

#2012 Season Average Salaries Across Position Groups and Home Runs
HR25_12=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2012_%3E25HR.csv')
HR14_12=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2012_%3C14HR.csv')
FB_12=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2012_First.csv')
IF_12=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2012_Infielders.csv')
OF_12=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2012_Outfielders.csv')
C_12=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2012_Catchers.csv')


# In[ ]:




# In[229]:

print(HR25_12['salary'].mean(),HR14_12['salary'].mean(),FB_12['salary'].mean(),IF_12['salary'].mean(),OF_12['salary'].mean(),C_12['salary'].mean())


# In[230]:

#2013 Season Average Salaries Across Position Groups and Home Runs
HR25_13=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2013_%3E25HR.csv')
HR14_13=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2013_%3C14HR.csv')
FB_13=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2013_First.csv')
IF_13=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2013_Infielders.csv')
OF_13=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2013_Outfielders.csv')
C_13=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2013_Catchers.csv')


# In[231]:

print(HR25_13['salary'].mean(),HR14_13['salary'].mean(),FB_13['salary'].mean(),IF_13['salary'].mean(),OF_13['salary'].mean(),C_13['salary'].mean())


# In[232]:

#2014 Season Average Salaries Across Position Groups and Home Runs
HR25_14=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2014_%3E25HR.csv')
HR14_14=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2014_%3C14HR.csv')
FB_14=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2014_First.csv')
IF_14=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2014_Infielders.csv')
OF_14=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2014_Outfielders.csv')
C_14=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2014_Catchers.csv')


# In[233]:

print(HR25_14['salary'].mean(),HR14_14['salary'].mean(),FB_14['salary'].mean(),IF_14['salary'].mean(),OF_14['salary'].mean(),C_14['salary'].mean())


# In[234]:

#2015 Season Average Salaries Across Position Groups and Home Runs
HR25_15=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2015_%3E25HR.csv')
HR14_15=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2015_%3C14HR.csv')
FB_15=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2015_First.csv')
IF_15=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2015_Infielders.csv')
OF_15=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2015_Outfielders.csv')
C_15=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2015_Catchers.csv')


# In[235]:

print(HR25_15['salary'].mean(),HR14_15['salary'].mean(),FB_15['salary'].mean(),IF_15['salary'].mean(),OF_15['salary'].mean(),C_15['salary'].mean())


# In[271]:

#2016 Season Average Salaries Across Position Groups and Home Runs
HR25_16=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2016_%3E25HR.csv')
HR14_16=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2016_%3C14HR.csv')
FB_16=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2016_First.csv')
IF_16=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2016_Infielders.csv')
OF_16=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2016_Outfielders.csv')
C_16=pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2016_Catchers.csv')


# In[274]:

print(HR25_16['salary'].mean(),HR14_16['salary'].mean(),FB_16['salary'].mean(),IF_16['salary'].mean(),OF_16['salary'].mean(),C_16['salary'].mean())


# In[503]:

#2000-2004 Salary Regressions
Salary00_04 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2000-2004.csv')
Salary00_04 = Salary00_04.rename(columns={'Free Agency':'Free_Agency'})
Salary00_04


# In[467]:

#print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Arbitration + Free_Agency', data=Salary00_04).fit().summary())


# In[462]:

print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary00_04).fit().summary())


# In[472]:

#2000-2003 Salary Regression
Salary00_03 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2000-2003_F.csv')
Salary00_03 = Salary00_03.rename(columns={'Free Agency':'Free_Agency'})
#Salary00_03


# In[470]:

#print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Arbitration + Free_Agency', data=Salary00_03).fit().summary())


# In[471]:

print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary00_03).fit().summary())


# In[473]:

#2000 Individual Regression
Salary00 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2000_F.csv')
Salary00 = Salary00.rename(columns={'Free Agency':'Free_Agency'})
#print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Arbitration + Free_Agency', data=Salary00).fit().summary())


# In[474]:

print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary00).fit().summary())


# In[491]:

#print(Salary00['OBP'].std()*6.5188, Salary00['SLG'].std()*1.6710)
print(Salary00['OBP'].std()*3.461, Salary00['SLG'].std()*2.821)


# In[475]:

#2001 Individual Regression
Salary01 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2001_F.csv')
Salary01 = Salary01.rename(columns={'Free Agency':'Free_Agency'})
#print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Arbitration + Free_Agency', data=Salary01).fit().summary())


# In[476]:

print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary01).fit().summary())


# In[492]:

#print(Salary01['OBP'].std()*2.5237, Salary01['SLG'].std()*2.9841)
print(Salary01['OBP'].std()*1.7544, Salary01['SLG'].std()*3.1919)


# In[477]:

#2002 Individual Regression
Salary02 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2002_F.csv')
Salary02 = Salary02.rename(columns={'Free Agency':'Free_Agency'})
#print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Arbitration + Free_Agency', data=Salary02).fit().summary())


# In[493]:

#print(Salary02['OBP'].std()*4.6524, Salary02['SLG'].std()*1.4325)
print(Salary02['OBP'].std()*2.3213, Salary02['SLG'].std()*1.7359)


# In[479]:

print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary02).fit().summary())


# In[480]:

#2003 Individual Regression
Salary03 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2003_F.csv')
Salary03 = Salary03.rename(columns={'Free Agency':'Free_Agency'})
#print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Arbitration + Free_Agency', data=Salary03).fit().summary())


# In[481]:

print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary03).fit().summary())


# In[495]:

#print(Salary03['OBP'].std()*5.7531, Salary03['SLG'].std()*1.3597)
print(Salary03['OBP'].std()*2.1428, Salary03['SLG'].std()*2.5751)


# In[482]:

#2004 Individual Regression
Salary04 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2004_F.csv')
Salary04 = Salary04.rename(columns={'Free Agency':'Free_Agency'})
#print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Arbitration + Free_Agency', data=Salary04).fit().summary())


# In[483]:

print(smf.ols(' np.log(Salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary04).fit().summary())


# In[496]:

#print(Salary04['OBP'].std()*5.8847, Salary04['SLG'].std()*2.1283)
print(Salary04['OBP'].std()*3.8168, Salary04['SLG'].std()*2.5215)


# In[504]:

#2012-2016 Salary Regressions
Salary12_16 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2012-2016.csv')
Salary12_16


# In[505]:

print(smf.ols(' np.log(salary) ~ OBP + SLG + PA + Catcher + Infielder', data=Salary12_16).fit().summary())


# In[465]:

print(smf.ols(' np.log(salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary12_16).fit().summary())


# In[486]:

#2012-2015 Salary Regressions
Salary12_15 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2012-2015_F.csv')
print(smf.ols(' np.log(salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary12_15).fit().summary())


# In[485]:

#2012 Salary Regressions
Salary12 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2012_F.csv')
print(smf.ols(' np.log(salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary12).fit().summary())


# In[497]:

print(Salary12['OBP'].std()*1.4389, Salary12['SLG'].std()*2.1953)


# In[487]:

#2013 Salary Regressions
Salary13 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2013_F.csv')
print(smf.ols(' np.log(salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary13).fit().summary())


# In[498]:

print(Salary13['OBP'].std()*1.7212, Salary13['SLG'].std()*2.5168)


# In[488]:

#2014 Salary Regressions
Salary14 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2014_F.csv')
print(smf.ols(' np.log(salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary14).fit().summary())


# In[499]:

print(Salary14['OBP'].std()*3.3596, Salary14['SLG'].std()*2.0284)


# In[489]:

#2015 Salary Regressions
Salary15 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2015_F.csv')
print(smf.ols(' np.log(salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary15).fit().summary())


# In[500]:

print(Salary15['OBP'].std()*3.3653, Salary15['SLG'].std()*0.3954)


# In[490]:

#2016 Salary Regressions
Salary16 = pd.read_csv('https://raw.githubusercontent.com/ajgarber20/Econometrics-Project/master/2016_F.csv')
print(smf.ols(' np.log(salary) ~ OBP + SLG + PA + Catcher + Infielder + Age_Dummy', data=Salary16).fit().summary())


# In[501]:

print(Salary16['OBP'].std()*2.5063, Salary16['SLG'].std()*0.6202)


# In[ ]:



