## some useful commands related to pandas.dataframe 

#eliminate some columns by its name
df.drop(['B', 'C'], axis=1) 

# merging dataframes 
df = pd.merge(left=ratings, right=parking, on="placeID", how="left")

#complex indexing 
midx = pd.MultiIndex(levels=[['lama', 'cow', 'falcon'],
['speed', 'weight', 'length']],
...                      labels=[[0, 0, 0, 1, 1, 1, 2, 2, 2],
...                              [0, 1, 2, 0, 1, 2, 0, 1, 2]])
