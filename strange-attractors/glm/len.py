def sqdist(v):
  s = 0
  for i in range(0, len(v)):
    s += v[i] * v[i]
  
  return s