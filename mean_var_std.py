import numpy as np

def calculate(list):
    mat = np.array(list).reshape(3,3)
    calculations = {
        "mean": [ mat.mean(), mat.mean(axis=1), mat.flatten().mean() ]
    }


    return calculations
