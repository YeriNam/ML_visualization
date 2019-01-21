from scipy.cluster import hierarchy as hc
from scipy.stats import spearmanr as sp

trainx=pd.DataFrame()
train_cols = list(['Breed1','Breed2','State','Age','PhotoAmt','dominant_pixel_frac', 'dominant_score', 'vertex_x', 'vertex_y','Dog','Cat', 'label_score', 'RescuerID'] + ['svd_{}'.format(i) for i in range(10)])
trainx=train[train_cols]

trainq=pd.DataFrame()
trainq=train[train_cols]
br=train['Breed1'].astype(int)
trainq['Dog']=np.logical_and(
        train['Type']==1,np.logical_or(
                train['Breed1']!='307',np.logical_and(
                        train['Type']==1,train['Breed2']!='307')))
trainq['Cat']=np.logical_and(train['Type']==2,np.logical_or(br<264, br>266))

#264 265 266
corr=np.round(sp(trainq).correlation,4)
corr_condensed=hc.distance.squareform(1-corr)
z=hc.linkage(corr_condensed, method='average')
fig=plt.figure(figsize=(16,10))
dendrogram=hc.dendrogram(z,labels=trainx.columns,orientation='left', leaf_font_size=16)
plt.show()


trainx['AdoptionSpeed']=target
