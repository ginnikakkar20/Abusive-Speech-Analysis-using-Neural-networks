import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
import seaborn as sns
import math
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl

mpl.style.use('seaborn')

# Plot confusion matrix for Like-Positive Score pair
pos_conf_arr = np.array([[134679,31339],[28357,140596]])
pos_df_cm = pd.DataFrame(pos_conf_arr, 
  index = [ 'Less positive', 'High positive'],
  columns = ['Less #likes', 'High #likes'])
fig = plt.figure()
plt.clf()
pos_cmap = sns.cubehelix_palette(n_colors=6, light= 0.9, as_cmap=True)
sns.set(font_scale=1.7)
res = sn.heatmap(pos_df_cm, annot=True, fmt='.2f', cmap=pos_cmap)
plt.yticks([0.5,1.5], [ 'Less positive', 'High positive'],va='center', rotation=90)
plt.title('Evaluation heatmap')
plt.savefig("figure1.pdf", format="pdf", bbox_inches='tight')

# Plot confusion matrix for Dislike-Negative Score pair
neg_conf_arr = np.array([[125229,50115],[36874,122753]])
df_neg_cm = pd.DataFrame(neg_conf_arr, 
  index = [ 'Less Negative', 'High Negative'],
  columns = ['Less #dislikes', 'High #dislikes'])
neg_fig = plt.figure()
plt.clf()
neg_cmap = sns.cubehelix_palette(n_colors=6, light= 0.9, as_cmap=True)
res = sn.heatmap(df_neg_cm, annot=True, fmt='.2f', cmap=neg_cmap)
plt.yticks([0.5,1.5], [ 'Less Negative', 'Higher Negative'],va='center', rotation=90)
plt.title('Evaluation heatmap')
plt.savefig("figure2.pdf", format="pdf", bbox_inches='tight')