import numpy as np

def calculate(list):
    mat = np.array(list).reshape(3,3)
    calculations = {
        "mean": [ mat.mean(axis=0), mat.mean(axis=1), mat.flatten().mean() ],
        "variance": [ mat.var(axis=0), mat.var(axis=1), mat.flatten().var() ],
        'standard deviation': [ mat.std(axis=0), mat.std(axis=1), mat.flatten().std() ],
        'max': [ mat.max(axis=0), mat.max(axis=1), mat.flatten().max() ],
        'min': [ mat.min(axis=0), mat.min(axis=1), mat.flatten().min() ],
        'sum': [ mat.sum(axis=0), mat.sum(axis=1), mat.flatten().sum() ]
    }

    return calculations
