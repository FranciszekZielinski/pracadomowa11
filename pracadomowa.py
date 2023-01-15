import numpy as np

dane = np.load('ex3_data.npy')


nowe_dane = dane[~np.isnan(dane).any(axis = 1)]


ile_wierszy = dane.shape[0] - nowe_dane.shape[0]
print(ile_wierszy)

for i in range(dane.shape[1]):
    print (f'{i} : {np.sum(np.isnan(dane[:,i]))}')

#for column in dane.T:
 #   print(f'{column} : {np.sum(np.isnan(column))}')
