import numpy as np
L = 4
llista = [1, 2, 3, 4, 5, 6]
pista = []
for e in llista:
  n = 10**e
  dades = L * (np.random.rand(n, 2))
  inside_circle = (dades**2).sum(axis=1) <= L**2
  pi = [4*(inside_circle.sum()/n)]
  pista.append(pi)
print(pista)



