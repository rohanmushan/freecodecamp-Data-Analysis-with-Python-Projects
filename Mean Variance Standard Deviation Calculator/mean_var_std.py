import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  
  matrix = np.array(list).reshape((3,3))

  calculations = {}

  calculations['mean'] = [matrix.mean(axis=0).tolist(), 
                        matrix.mean(axis=1).tolist(),
                        matrix.mean()]
  
  calculations['variance'] = [matrix.var(axis=0).tolist(), 
                          matrix.var(axis=1).tolist(),
                          matrix.var()]

  calculations['standard deviation'] = [matrix.std(axis=0).tolist(), 
                        matrix.std(axis=1).tolist(),
                        matrix.std()]

  calculations['max'] = [matrix.max(axis=0).tolist(), 
                        matrix.max(axis=1).tolist(),
                        matrix.max()]

  calculations['min'] = [matrix.min(axis=0).tolist(), 
                        matrix.min(axis=1).tolist(),
                        matrix.min()]

  calculations['sum'] = [matrix.sum(axis=0).tolist(), 
                        matrix.sum(axis=1).tolist(),
                        matrix.sum()]

  return calculations