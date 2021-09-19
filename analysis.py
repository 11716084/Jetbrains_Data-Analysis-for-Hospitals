import pandas as pd
import matplotlib. pyplot as plt
pd.set_option('display.max_columns', 8)

a = pd.read_csv("test/general.csv")
b = pd.read_csv("test/prenatal.csv")
c = pd.read_csv("test/sports.csv")

b = b.rename(columns={"Sex": "gender",
                      "HOSPITAL": "hospital"})
c = c.rename(columns={"Male/female": "gender",
                      "Hospital": "hospital"})

# print(a[0:20])
# print(b[0:20])
# print(c[0:20])
s = pd.concat([a, b, c], ignore_index=True)

s = s.drop(columns=['Unnamed: 0'])
s = s.dropna(axis=0, how='all')

s["gender"].replace({"female": "f", "man": "m", "woman": "f", "male": "m"}, inplace=True)
s['gender'] = s['gender'].where(s['gender'].notna(), 'f')

s.update(
    s[['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']].fillna(0))

s[['age']].plot(kind='hist', bins=[0, 15, 35, 55, 70, 80])
plt.savefig('name_of_the_pic.jpg', bbox_inches='tight')
plt.show()
print("The answer to the 1st question: 15 - 35")

s.diagnosis.value_counts(sort=False).plot.pie()
plt.savefig('pie.jpg', bbox_inches='tight')
plt.show()
print("The answer to the 2nd question: pregnancy")


s.diagnosis.value_counts(sort=False).plot.pie()
plt.savefig('because.jpg', bbox_inches='tight')
plt.show()
print("The answer to the 3rd question: It's because fgfgfg")

# print(f"The answer to the 1st question is {s['hospital'].value_counts().idxmax()}")  # 1
#
# patients_in_general = s.loc[(s['hospital'] == 'general')]
# pat_in_gen_suffer_from_stomach = s.loc[(s['hospital'] == 'general') & (s['diagnosis'] == 'stomach')]  # 2
# i = (len(pat_in_gen_suffer_from_stomach)/len(patients_in_general))  # 2
# print(f"The answer to the 2nd question is {round(i, 3)}")  # 2
#
# patients_sports = s.loc[(s['hospital'] == 'sports')]  # 3
# pat_in_sports_dislocation = s.loc[(s['hospital'] == 'sports') & (s['diagnosis'] == 'dislocation')]  # 3
# h = len(pat_in_sports_dislocation)/len(patients_sports)  # 3
# print(f"The answer to the 3rd question is {round(h, 3)}")  # 3
#
# median_general = (s.loc[(s['hospital'] == 'general'), 'age'].median())  # 4
# median_sport = (s.loc[(s['hospital'] == 'sports'), 'age'].median())  # 4
# x = median_general-median_sport  # 4
# print(f"The answer to the 4th question is {x}")  # 4
#
# blood_general = len(s.loc[(s['hospital'] == 'general') & (s['blood_test'] == 't')])
# blood_sport = len(s.loc[(s['hospital'] == 'sport') & (s['blood_test'] == 't')])
# blood_prenatal = len(s.loc[(s['hospital'] == 'prenatal') & (s['blood_test'] == 't')])
# if blood_general > blood_sport and blood_general > blood_prenatal:
#     print(f"The answer to the 5th question is {'general'}, {blood_general} blood tests")
# elif blood_prenatal > blood_sport and blood_prenatal > blood_general:
#     print(f"The answer to the 5th question is {'prenatal'}, {blood_prenatal} blood tests")
# elif blood_sport > blood_prenatal and blood_sport > blood_general:
#     print(f"The answer to the 5th question is {'sport'}, {blood_sport} blood tests")
