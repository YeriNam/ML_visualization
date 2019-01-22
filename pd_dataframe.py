## some useful commands related to pandas.dataframe 

#eliminate some columns by its name
df.drop(['B', 'C'], axis=1) 

# merging dataframes 
df = pd.merge(left=ratings, right=parking, on="placeID", how="left")

#complex indexing 
midx = pd.MultiIndex(levels=[['lama', 'cow', 'falcon'],
                             ['speed', 'weight', 'length']],
                     labels=[[0, 0, 0, 1, 1, 1, 2, 2, 2],
                             [0, 1, 2, 0, 1, 2, 0, 1, 2]])
df = pd.DataFrame(index=midx, columns=['big', 'small'],
                  data=[[45, 30], [200, 100], [1.5, 1], [30, 20],
                        [250, 150], [1.5, 0.8], [320, 250],
                        [1, 0.8], [0.3,0.2]])

#groupby 
# Group by the parking_lot column
parking_group = df.groupby("parking_lot")

# Calculate the mean ratings
parking_group["service_rating"].mean()
