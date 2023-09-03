import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

#read the text file which contains all languages
with open('pageviews-20180503-000000.txt',encoding='utf-8') as f:
    contents = f.readlines()
    lst00 = []
    for i in range(len(contents)):
        lst00.append(contents[i].strip().split(' '))

#convert lst00 to dataframe
df00 = pd.DataFrame(lst00,columns=['languageWithWebsite','article_name','views','page_size'])

#split all languages to view the first element of languages without a following character are wikipedia projects
languages = df00.languageWithWebsite.str.split(".")
sublist =[]
sublist2 = []
for language in languages:
    sublist.append(language[0])
    try:
        sublist2.append(language[1])
    except:
        sublist2.append(np.NAN)

#Add sublist to the dataframe
df00['language'] = sublist
df00['website'] = sublist2
df00['website'].fillna('p',inplace=True)
views = []
size = []

#convert each element from str to int
for v in df00['views']:
    views.append(int(v))
for s in df00['page_size']:
    size.append(int(s))
df00['views'] = views
df00['page_size'] = size

#***********************************************************************************************************************
#Part 1
# This chart shows the relation between the (the views of the main page) and languages (which the data connected by the language without the extention that shows where the page located)

temp00 = df00[df00['article_name']=='Main_Page']
x = np.unique(temp00.language)
y = temp00.groupby('language').sum().reset_index()['views']
fig,ax = plt.subplots(figsize=(12,10))
plt.bar(x,y)
plt.xticks( rotation=90, fontsize=10)
for i in range(len(x)):
    if y[i]>4500:
        plt.text(i, y[i]//60, y[i], color='green', fontsize=10)
    else:
        plt.text(i,y[i]+50,y[i],color = 'green',fontsize = 9)
plt.ylim([0,4500])
plt.title('The number of views of the \" Main_Page \" for all languages:')
plt.legend(['00:00'],title = 'Time')
plt.xlabel('Languages')
plt.ylabel('Views')
plt.yticks(fontsize = 12)
plt.show()

#**********************************************************************************************************************
#Part 2
#read the text file which contains all languages

with open('pageviews-20180503-120000.txt',encoding='utf-8') as f:
    contents = f.readlines()
    lst12 = []
    for i in range(len(contents)):
        lst12.append(contents[i].strip().split(' '))

#convert lst12 to dataframe
df12 = pd.DataFrame(lst12,columns=['languageWithWebsite','article_name','views','page_size'])

#split all languages to view the first element of languages without a following character are wikipedia projects
languages = df12.languageWithWebsite.str.split(".")
sublist =[]
for language in languages:
    sublist.append(language[0])

#Add sublist to the dataframe
df12['language'] = sublist
views = []
size = []

#convert each element from str to int
for v in df12['views']:
    try:
        views.append(int(v))
    except:
        views.append(v)
for s in df12['page_size']:
    try:
        size.append(int(s))
    except:
        size.append(s)
df12['views'] = views
df12['page_size'] = size

temp00 = df00[df00['article_name']=='Main_Page']
temp12 = df12[df12['article_name']=='Main_Page']
group00 = temp00.groupby('language')['views'].sum()
group12 = temp12.groupby('language')['views'].sum()
l = ['en','es','ar','de','ja','fr']

x = np.arange(len(l))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()

data1 = ax.bar(x - width/2,group00[l], width, label='00:00')
data2 = ax.bar(x + width/2,group12[l], width, label='12:00')

ax.bar_label(data1, padding=3,color = 'red')
ax.bar_label(data2, padding=3,color = 'red')

ax.text(0-width*3, group00['en']//320, group00['en'], color='red', fontsize=10)
ax.text(0+width, group12['en']//870, int(group12['en']), color='red', fontsize=10)

plt.ylim([0,1000])
plt.ylabel('Views')
plt.xlabel('Languages')
ax.set_title('Number of Views for the \' Main_Page \' on (3/5/2018) :')
ax.set_xticks(x)
ax.set_xticklabels(l)
ax.legend(title = 'Time')
plt.show()

#**********************************************************************************************************************
#Part 3

fig,ax = plt.subplots(figsize=(12,10))
temp = df00.groupby('website').sum()['views']
l = ['Wikinews','Wikivoyage','Wikiversity','MediaWiki','Wikiquote','FoundationWiki','Wikisource','Wikibooks','WikidataWiki','WikipediaZeroSite','Wiktionary','wikipedia','Wikimedia']
ex = [0.4,0.36,0.32,0.28,0.24,0.2,0.16,0.12,0.08,0.04,0,0,0]
plt.pie(sorted(temp),labels=l,autopct='%1.2f%%',startangle=270,explode=ex)
plt.legend()
plt.title('The Percentage of the views for each website:')
plt.show()

#**********************************************************************************************************************
#Part 4

en = df00[df00['language']=='en']
words = en['article_name'].str.split('_')
slist = []
for word in words:
    slist.append(word[0])
labels = ['What','When','Where','How','Which','Why','Who']
counts = pd.DataFrame(slist).value_counts()[labels]

fig, ax = plt.subplots()

data = ax.bar(labels,counts,width=0.4)
plt.title('The Number of Websites start with WH-Question Words\nin English language')
plt.xlabel('WH-Question Words')
plt.ylabel('Number of Articles')
plt.legend(['00:00'],title = 'Time')
plt.bar_label(data,color = 'green')
plt.show()

#**********************************************************************************************************************
#Part 5

en = df00[df00['language']=='en']
words = en['article_name'].str.split('_')
slist = []
for word in words:
    slist.append(word[0])
labels = ['What','When','Where','How','Which','Why','Who']
counts = pd.DataFrame(slist).value_counts()[labels]

en2 = df12[df12['language']=='en']
words2 = en2['article_name'].str.split('_')
slist2 = []
for word in words2:
    slist2.append(word[0])

counts2 = pd.DataFrame(slist2).value_counts()[labels]

plt.plot(labels,counts)
plt.plot(labels,counts2)
plt.legend(labels = ['00:00','12:00'])
plt.title('Relation between number of articles start with WH-Question Words\nat different time on the same day')
plt.xlabel('WH-Question Words')
plt.ylabel('Number of Articles')
plt.show()



