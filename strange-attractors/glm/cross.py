def cross(u, v):
  """
  return the cross product of 2 vectors.
  """
  dim = len(u)
  s = []
  for i in range(0, dim):
      if i == 0:
          j,k = 1,2
          s.append(u[j]*v[k] - u[k]*v[j])
      elif i == 1:
          j,k = 2,0
          s.append(u[j]*v[k] - u[k]*v[j])
      else:
          j,k = 0,1
          s.append(u[j]*v[k] - u[k]*v[j])
  return s