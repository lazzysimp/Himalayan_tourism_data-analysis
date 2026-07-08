#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_excel("Himalayan_Tourism.xlsx")


# In[3]:


df.shape


# In[4]:


df.head(20)


# In[5]:


df.info()


# In[6]:


pd.isnull(df).sum()


# In[7]:


df.columns


# In[8]:


df.describe()


# In[9]:


print("Total Tourists:", df["Tourists"].sum())

print("Total Revenue (Crores):", round(df["Revenue_Crore"].sum(),2))

print("Average Stay(Days):", round(df["Avg_Stay_Days"].mean(),2))

print("Average Hotel Occupancy(%):", round(df["Hotel_Occupancy_%"].mean(),2))

print("Average Satisfaction:", round(df["Satisfaction"].mean(),2))


# In[10]:


# answers should we expand the business

tourists = df.groupby("Year")["Tourists"].sum()

plt.figure(figsize=(8,5))

plt.plot(tourists.index,
         tourists.values,
         marker='o',
         linewidth=3)

plt.title("Tourism Growth (2021-2025)")

plt.ylabel("Total Tourists")

plt.grid(alpha=.3)

plt.show()


# In[11]:


#at what pace the tourists are increasing for future planning

tourists_by_year = df.groupby("Year")["Tourists"].sum().sort_index()

plt.figure(figsize=(8,6))

bars = plt.bar(tourists_by_year.index.astype(str),
               tourists_by_year.values)

plt.xlabel("Year")
plt.ylabel("Total Tourists")
plt.title("Total Tourists by Year")

plt.ticklabel_format(style='plain', axis='y')

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f'{bar.get_height():,.0f}',
        ha='center',
        va='bottom',
        fontsize=9
    )

plt.tight_layout()
plt.show()


# In[12]:


#at what month the business should advertis more

month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

plt.figure(figsize=(10,6))

for year in sorted(df["Year"].unique()):
    monthly = (
        df[df["Year"] == year]
          .groupby("Month")["Tourists"]
          .sum()
          .reindex(month_order)
    )

    plt.plot(monthly.index, monthly.values, marker='o', label=year)

plt.title("Monthly Tourist Trend (2021–2025)")
plt.xlabel("Month")
plt.ylabel("Tourists")
plt.legend(title="Year")
plt.grid(True)

plt.show()


# In[13]:


# Identify the states that attract the highest number of tourists.

state = df.groupby("State")["Tourists"].sum().sort_values(ascending=False)

bars = plt.bar(state.index, state.values)

plt.title("Tourist Preference by State")
plt.xlabel("State")
plt.ylabel("Tourists")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 100000,
        f"{int(bar.get_height()):,}",
        ha="center"
    )
    
plt.ticklabel_format(style='plain', axis='y')

plt.tight_layout()

plt.show()


# In[14]:


#most popular adventure destinations to help the company design and promote adventure tour packages.

adv=df.groupby("Destination")["Adventure_Tourists"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(16,10))

bars = plt.bar(adv.index, adv.values)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height()*1.01,
        f"{int(bar.get_height()):,}",
        ha="center",
        fontsize=12
    )
    
plt.ticklabel_format(style='plain', axis='y')

plt.xticks(rotation=45, fontsize=16)

plt.yticks(fontsize=14)

plt.title("Top Adventure Destinations",fontsize=15)

plt.grid()

plt.tight_layout()

plt.show()


# In[15]:


#Destinations preferred by foreign tourists

foreign = df.groupby("Destination")["Foreign_Tourists"].sum()

foreign = foreign.sort_values(ascending=False).head(6)

plt.figure(figsize=(7,7))

plt.pie(foreign.values,
        labels=foreign.index,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Top Destinations Preferred by Foreign Tourists")

plt.show()


# In[16]:


# average stay duration to plan the bookings and advance hotel booking blocks

stay = df.groupby("Destination")["Avg_Stay_Days"].mean()
stay = stay.sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))

plt.hlines(y=stay.index,
           xmin=0,
           xmax=stay.values)

plt.plot(stay.values,
         stay.index,
         "o")

plt.title("Average Stay Duration by Destination")
plt.xlabel("Average Stay (Days)")

plt.show()


# In[ ]:




