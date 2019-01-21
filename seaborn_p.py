##https://seaborn.pydata.org/tutorial/categorical.html
## train ,target is given 
## create this file to practice a usage of seaborn library 

target.value_counts().sort_index().plot('barh', color='teal');
plt.title('Adoption speed classes counts');

import seaborn as sns
Trainq=pd.DataFrame()
Trainq['Type'] = train['Type'].apply(lambda x: 'Dog' if x == 1 else 'Cat')
Trainq['speed']=target
plt.figure(figsize=(10, 6));
sns.countplot(x='speed ', data=Trainq, hue='Type');
plt.title('Number of cats and dogs of each speed');

 

import seaborn as sns
Trainq=pd.DataFrame()
Trainq=train
Trainq['speed']=target
plt.figure(figsize=(10, 6));
sns.countplot(x='Color1', data=Trainq, hue='Type');
plt.title('the number of cats and dogs per color1 ');


plt.figure(figsize = (10, 6))
plt.title('Distribution of pets age (log scale)');
TX_dog=pd.DataFrame()
TX_cat=pd.DataFrame()
TX_dog=Trainq.loc[Trainq['Type']==1]
TX_cat=Trainq.loc[Trainq['Type']==2]
np.log1p(TX_dog['Age']).plot('hist', label='dog');
np.log1p(TX_cat['Age']).plot('hist', label='cat');

plt.legend();
