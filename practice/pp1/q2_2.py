import numpy as np
import matplotlib.pyplot as plt

MAX_ITER = int(1e+4)

def gen_X_path(k, n, p):
    X = np.array([k])
    for i in range(1, MAX_ITER):
        outcome = 1 if np.random.uniform(0, 1) <= p else -1
        if X[i - 1] + outcome >= n:
            X = np.append(X, X[i - 1] + outcome)
            return X
        elif X[i - 1] + outcome <= 0:
            X = np.append(X, X[i - 1] + outcome)
            return X

        X = np.append(X, X[i - 1] + outcome)

    return X

k = 40
n = 60
p = 0.5

for k in range(5):
    path_X = gen_X_path(k, n, p)
    plt.plot(range(len(path_X)), path_X, label=f"X_n Path #{k}")

plt.legend(loc="best")
plt.show()
