import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

df = pd.read_csv('Droplets.csv', delimiter=',', nrows=10778, skiprows=[1])

x = df['MeanAlignedFAM'];
y = df['MeanAlignedTAMRA']
 
g = sns.jointplot(x=df["MeanAlignedFAM"], y=df["MeanAlignedTAMRA"], data=df)

g.ax_joint.legend_.remove()

plt.show() 