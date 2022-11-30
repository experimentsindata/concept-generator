import pandas as pd
import nltk
from nltk.corpus import stopwords
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


# Specify url of the web page
source = urlopen('https://en.wikipedia.org/wiki/Yayoi_Kusama').read()

# Use beautiful soup to parse the text
soup = BeautifulSoup(source,'lxml')
text = ''
for paragraph in soup.find_all('p'):
    text += paragraph.text

# Clean text
text = re.sub(r'\[.*?\]+', '', text)
text = text.replace('\n', '')

#Save text to text
text_1 = text

#Lower case
text_1 = text_1.lower()

#remove numbers and punctuation, this is such an ugly solution, shoulf find a better one
text_1 = text_1.replace('1', '')
text_1 = text_1.replace('2', '')
text_1 = text_1.replace('3', '')
text_1 = text_1.replace('4', '')
text_1 = text_1.replace('5', '')
text_1 = text_1.replace('6', '')
text_1 = text_1.replace('7', '')
text_1 = text_1.replace('8', '')
text_1 = text_1.replace('9', '')
text_1 = text_1.replace('0', '')
text_1 = text_1.replace('.', '')
text_1 = text_1.replace(',', '')
text_1 = text_1.replace('!', '')
text_1 = text_1.replace('?', '')
text_1 = text_1.replace('"', '')
text_1 = text_1.replace('/', ' ')

#split text
data_subject1 = text_1.split()
data_stop_words = stopwords.words('english')

# Create the pandas DataFrame for subjects
df_subject1 = pd.DataFrame(data_subject1, columns=['col_subject'])
df_stop_words = pd.DataFrame(data_stop_words, columns=['col_words'])
df_extra_stops = pd.DataFrame(data_extra_stops, columns=['col_words'])

#remove duplicates
df_subject1.drop_duplicates(subset="col_subject",
                     keep=False, inplace=True)

#strip spaces
df_subject1['col_subject'].str.strip()
df_stop_words['col_words'].str.strip()

#Use mask to run text through stop word filter
mask1 = ~df_subject1.col_subject.isin(df_stop_words.col_words)
df_subject1 = df_subject1[mask1]

#quadruplicate webpage data
df_subject2 = df_subject1
df_subject3 = df_subject1
df_subject4 = df_subject1
df_subject5 = df_subject1

#shuffle dataframe orders to randomise
df_subject1 = df_subject1.sample(frac=1)
df_subject2 = df_subject2.sample(frac=1)
df_subject3 = df_subject3.sample(frac=1)
df_subject4 = df_subject4.sample(frac=1)
df_subject5 = df_subject5.sample(frac=1)

#set incremental index on data frames
df_subject1['index_incremental'] = range(1, len(df_subject1) + 1)
df_subject2['index_incremental'] = range(1, len(df_subject2) + 1)
df_subject3['index_incremental'] = range(1, len(df_subject3) + 1)
df_subject4['index_incremental'] = range(1, len(df_subject4) + 1)
df_subject5['index_incremental'] = range(1, len(df_subject5) + 1)

#join random frames together
data_first_join =  (pd.merge(df_subject1, df_subject2, left_on='index_incremental', right_on='index_incremental', how='left'))
data_second_join =  (pd.merge(data_first_join, df_subject3, left_on='index_incremental', right_on='index_incremental', how='left'))
data_third_join =  (pd.merge(data_second_join, df_subject4, left_on='index_incremental', right_on='index_incremental', how='left'))
data_fourth_join =  (pd.merge(data_third_join, df_subject5, left_on='index_incremental', right_on='index_incremental', how='left').drop('index_incremental', axis=1))

#show the output
print(data_fourth_join)
