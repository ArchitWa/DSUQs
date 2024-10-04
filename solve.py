import pandas as pd

df = pd.read_csv('data.csv')


# 1. How many students prefer to study at night? 

c = sum([1 for i in range(len(df)) if df.loc[i, 'Preferred_Study_Time'] == 'Night'])
print(c)
print()

# 2. What percentage of students spend at least 90 minutes on social media and work a part time job? 
# Please provide your answer rounded to three decimal places.

d = sum([1 for i in range(len(df)) if df.loc[i, 'Social_Media_Use_mins'] >= 90 and df.loc[i, 'Part_Time_Job'] == 'Yes'])
print(round(d/len(df)*100, 3))
print()

# 3. Which hobby is associated with the lowest average stress levels among students? Please provide the hobby and the associated 
# average stress level rounded to three decimal places.

hobbies = df['Hobbies'].unique()

for hobby in hobbies:
    avg = df[df['Hobbies'] == hobby]["Stress_Level"].mean()
    print(hobby, round(avg, 3))
print()

# 4. What student had the highest median GPA across 11th grade, 12th grade, and college? Please provide the student's ID 
# number and their median GPA rounded to three decimal places.

df['Median_GPA'] = df[['Eleventh_Grade_GPA', 'Twelfth_Grade_GPA', 'College_GPA']].median(axis=1)
max_gpa = df['Median_GPA'].max()
student_id = df[df['Median_GPA'] == max_gpa]['Student_ID'].values[0]

print(student_id, round(max_gpa, 3))
print()

# 5. 1. Your friend who commutes from Pasadena to UCLA often blames the long drive for their tanking GPA. As a skeptical data scientist,
#  this compels you to investigate whether there truly exists a relationship between commute time and academic performance. Formulate a 
# claim on this possible relationship and analyze any trends or patterns in the data that would support your claim. Be sure to discuss any 
# limitations or factors in the dataset that may affect the validity of your results.

import matplotlib.pyplot as plt
import seaborn as sns

df['Commute_Time_mins'] = df['Commute_Time_mins'].astype(int)
df['College_GPA'] = df['College_GPA'].astype(float)


# plot with commute time and college GPA but also with daily study time/
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Commute_Time_mins', y='College_GPA', data=df, hue='Daily_Study_Time_mins')
plt.title('Commute Time vs College GPA')
plt.xlabel('Commute Time (mins)')
plt.ylabel('College GPA')
plt.show()

# plot with Social Media Use  and Study Time
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Social_Media_Use_mins', y='Daily_Study_Time_mins', data=df)
plt.title('Social Media Use vs Daily Study Time ')
plt.xlabel('Social Media Use (mins)')
plt.ylabel('College GPA')
plt.show()

# 6. Many people say that "cash is king" and believe that having a higher economic status is associated with better outcomes in one's 
# academic, professional, and personal life. To what degree, if any, does the data support this ideology? Use evidence from the dataset 
# to build your answer. Make sure to thoroughly explain your reasoning and note any potential drawbacks to your approach


# plot with Financial Status and College GPA
plt.figure(figsize=(10, 6))
sns.boxplot(x='Financial_Status', y='College_GPA', data=df)
plt.title('Financial Status vs College GPA')
plt.xlabel('Financial Status')
plt.ylabel('College GPA')
plt.show()

# plot with Financial Status and Average GPA
plt.figure(figsize=(10, 6))
sns.boxplot(x='Financial_Status', y='Average_GPA', data=df)
plt.title('Financial Status vs Average GPA')
plt.xlabel('Financial Status')
plt.ylabel('Average GPA')
plt.show()

# plot with Financial Status and Height
plt.figure(figsize=(10, 6))
sns.boxplot(x='Financial_Status', y='Height_cm', data=df)
plt.title('Financial Status vs Height')
plt.xlabel('Financial Status')
plt.ylabel('Height')
plt.show()

# plot with Financial Status and Weight
plt.figure(figsize=(10, 6))
sns.boxplot(x='Financial_Status', y='Weight_kg', data=df)
plt.title('Financial Status vs Weight')
plt.xlabel('Financial Status')
plt.ylabel('Weight')
plt.show()

# plot with Financial Status and Stress Level
plt.figure(figsize=(10, 6))
sns.boxplot(x='Financial_Status', y='Stress_Level', data=df)
plt.title('Financial Status vs Stress Level')
plt.xlabel('Financial Status')
plt.ylabel('Stress Level')
plt.show()


