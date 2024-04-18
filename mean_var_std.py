import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    array = np.array(list).reshape(3,3)
    calculations = {
      'mean': [[array[:,0].mean(), array[:,1].mean(), array[:,2].mean()],
               [array[0,:].mean(), array[1,:].mean(), array[2,:].mean()],
                array.mean()],
      'variance': [[array[:,0].var(), array[:,1].var(), array[:,2].var()],
               [array[0,:].var(), array[1,:].var(), array[2,:].var()],
                array.var()],
      'standard deviation': [[array[:,0].std(), array[:,1].std(), array[:,2].std()],
               [array[0,:].std(), array[1,:].std(), array[2,:].std()],
                array.std()],
      'max': [[array[:,0].max(), array[:,1].max(), array[:,2].max()],
               [array[0,:].max(), array[1,:].max(), array[2,:].max()],
                array.max()],
      'min': [[array[:,0].min(), array[:,1].min(), array[:,2].min()],
               [array[0,:].min(), array[1,:].min(), array[2,:].min()],
                array.min()],
      'sum': [[array[:,0].sum(), array[:,1].sum(), array[:,2].sum()],
               [array[0,:].sum(), array[1,:].sum(), array[2,:].sum()],
                array.sum()]
    }
    
    
    return calculations