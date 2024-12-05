import pandas as pd
import matplotlib.pyplot as plt
titanic = pd.read_csv('titanic.csv')

print(titanic.head())
print(titanic.tail())
print(titanic.describe())
print('=========================================')
plt.hist(titanic['Age'], color = 'blue', edgecolor = 'black',
           bins = int(180/5))
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
