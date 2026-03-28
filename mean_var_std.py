import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    mat = np.array(list).reshape(3,3)

    calculations = {
        "mean": [
            mat.mean(axis=0).tolist(),
            mat.mean(axis=1).tolist(),
            float(mat.flatten().mean())
        ],
        "variance": [
            mat.var(axis=0).tolist(),
            mat.var(axis=1).tolist(),
            float(mat.flatten().var())
        ],
        'standard deviation': [
            mat.std(axis=0).tolist(),
            mat.std(axis=1).tolist(),
            float(mat.flatten().std())
        ],
        'max': [
            mat.max(axis=0).tolist(),
            mat.max(axis=1).tolist(),
            float(mat.flatten().max())
        ],
        'min': [
            mat.min(axis=0).tolist(),
            mat.min(axis=1).tolist(),
            float(mat.flatten().min())
        ],
        'sum': [
            mat.sum(axis=0).tolist(),
            mat.sum(axis=1).tolist(),
            float(mat.flatten().sum())
        ]
    }

    return calculations
