def dot(u, v):
  """
  Dot product of 2 N dimensional vectors.
  """
  s = 0
  for i in range(0, len(u)):
    s += u[i] * v[i]
  
  return s