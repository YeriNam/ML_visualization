import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
from sklearn import manifold

#n_neighbors=5 #breed1? 
n_components= 2
mani_trainx=trainx[['MaturitySize','FurLength','Breed1','Vaccinated']]
Y = manifold.TSNE(n_components=n_components,init='pca',perplexity=50).fit_transform(mani_trainx)

fig = plt.figure(figsize=(15, 8))
#plt.suptitle("Manifold Learning with %i points, %i neighbors"
#             % (1000, n_neighbors), fontsize=14)

print("tsne")
ax = fig.add_subplot(257)
scale_x=1
scale_y=1
scale_z=1
#ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([scale_x, scale_y, scale_z, 1]))
ax.scatter(Y[:, 0], Y[:,1], c=target, cmap=plt.cm.Spectral)
#ax.view_init(4, -72)
plt.title("t-SNE")
#ax.xaxis.set_major_formatter(NullFormatter())
#ax.yaxis.set_major_formatter(NullFormatter())
#plt.axis('tight')


from sklearn.metrics import silhouette_score
silhouette_score (Y,target, metric='euclidean')
