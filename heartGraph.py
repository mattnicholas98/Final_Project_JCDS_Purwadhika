import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./datasets/heart.csv')
# print(df)

plt.style.use('seaborn')

# all the data visualization graphs based on the csv file to see the trend of the symptoms that are causing the heart diseases
# ============== GRAPH 1 =========================

# plt.title('Age based on Serum Cholestoral', fontsize=20)
# plt.scatter(df['age'], df['chol'], color = 'k')
# plt.xlabel('Age')
# plt.ylabel('Serum Cholestoral')
# z1 = np.polyfit(df['age'], df['chol'], 1)
# p1 = np.poly1d(z1)
# plt.plot(df['age'], p1(df['age']), 'r--')
# plt.grid(True)
# plt.savefig('static/graph1.png', facecolor='#ADD8E6', edgecolor='#ADD8E6')

# ============= GRAPH 2 ====================

# targett = df['target'].values.tolist()
# countA = targett.count(1)
# countB = targett.count(0)
# summaryList = [countA, countB]

# plt.title('The Target Data', fontsize=20)
# plt.pie(summaryList, labels=['WITH heart disease', 'NO heart disease'], autopct='%.1f%%',
#         textprops={'fontsize': 12}, shadow=True, startangle=90, colors='yb')
# plt.legend(summaryList)
# plt.savefig('static/graph2.png', facecolor='#ADD8E6', edgecolor='#ADD8E6')

# ============= GRAPH 3 =============================

# plt.title('Age vs Max Heart Rate', fontsize=20)
# plt.scatter(df['age'], df['thalach'], color = 'k')
# plt.xlabel('Age')
# plt.ylabel('Max Heart Rate')
# z2 = np.polyfit(df['age'], df['thalach'], 1)
# p2 = np.poly1d(z2)
# plt.plot(df['age'], p2(df['age']), 'r--')
# plt.grid(True)
# plt.savefig('static/graph3.png', facecolor='#ADD8E6', edgecolor='#ADD8E6')

# ================= GRAPH 4 =============================

# plt.title('Amount of gender differences', fontsize=20)
# sns.countplot(x = 'sex', data = df, palette = "mako_r")
# plt.xlabel("0 = Female; 1 = Male")
# plt.savefig('static/graph4.png', facecolor='#ADD8E6', edgecolor='#ADD8E6')

# ================= GRAPH 5 =============================

# youngAges = df[(df['age'] >= 29) & (df['age'] < 40)]
# middleAges = df[(df['age'] >= 40) & (df['age'] < 55)]
# oldAges = df[(df['age'] > 55)]

# plt.title('Age States', fontsize=20)
# plt.pie([len(youngAges), len(middleAges), len(oldAges)],
#     labels = ['Young ages','Middle ages','Old ages'], explode = [0.1, 0.1, 0.1],
#     colors = ['b', 'g', 'yellow'], startangle=50, autopct='%.1f%%', textprops={'fontsize': 12})

# plt.savefig('static/graph5.png', facecolor='#ADD8E6', edgecolor='#ADD8E6')

# ================ GRAPH 6 ====================================

# pd.crosstab(df['age'], df['target']).plot(kind="bar")
# plt.title('Heart Disease Frequency for Ages', fontsize=20)
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.savefig('static/graph6.png', facecolor='#ADD8E6', edgecolor='#ADD8E6')

# ==================== GRAPH 7 ========================

# plt.scatter(x = df['age'][df['target'] == 1], 
#     y = df['thalach'][(df['target'] == 1)], color='r')

# plt.scatter(x = df['age'][df['target'] == 0], 
#     y = df['thalach'][(df['target'] == 0)], color='b')

# plt.title('Max. Heart Rate based on Age', fontsize=20)
# plt.legend(['Disease', 'NO Disease'])
# plt.xlabel('Age')
# plt.ylabel('Maximum Heart Rate')
# plt.savefig('static/graph7.png', facecolor='#ADD8E6', edgecolor='#ADD8E6')

# ======================= GRAPH 8 =======================

# pd.crosstab(df['slope'], df['target']).plot(kind="bar", color='yk')
# plt.title('Heart Disease Frequency for Slope', fontsize=20)
# plt.xlabel('The Slope of The Peak Exercise ST Segment ')
# plt.xticks(rotation = 0)
# plt.ylabel('Frequency')
# plt.savefig('static/graph8.png', facecolor='#ADD8E6', edgecolor='#ADD8E6')

# ======================== GRAPH 9 ========================

# pd.crosstab(df['fbs'], df['target']).plot(kind="bar", color='br')
# plt.title('Heart Disease Frequency According To FBS', fontsize=20)
# plt.xlabel('Fasting Blood Sugar > 120 mg/dl \n(0 = False; 1 = True)')
# plt.xticks(rotation = 0)
# plt.legend(["NO Disease", "Disease"])
# plt.ylabel('Frequency of Disease or NOT')
# plt.savefig('static/graph9.png', facecolor='#ADD8E6', edgecolor='#ADD8E6')

# ======================== GRAPH 10 ========================

# pd.crosstab(df['cp'], df['target']).plot(kind="bar", color='yb')
# plt.title('Heart Disease Frequency According To Chest Pain Type', fontsize=20)
# plt.xlabel('Chest Pain Type')
# plt.xticks(rotation = 0)
# plt.ylabel('Frequency of Disease or NOT')
# plt.savefig('static/graph10.png', facecolor='#ADD8E6', edgecolor='#ADD8E6')

# ========================= GRAPH 11 ==============================

# shown for presentation purpose only
plt.figure(figsize=(10,10))
sns.heatmap(df.corr(), annot=True, fmt='.1f')     # thalach, CP, slope
plt.savefig('static/graph11.png')