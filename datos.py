import math as mt
import numpy as np
with open("datosw.txt","r") as datos:
  ldata = []
  for i in datos:
    ldata.append(int(i))
  ldata = np.array(ldata)
  prom = ldata.mean()
  qt = []
  for a in ldata:
    d = (int(a)-prom)**2
    qt.append(int(d))
  suma = sum(qt)
  s = mt.sqrt((suma/(len(qt)-1)))
  print(s)