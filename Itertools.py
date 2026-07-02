from itertools import combinations

features = ['age','income','score']
print(list(combinations(features, 2)))