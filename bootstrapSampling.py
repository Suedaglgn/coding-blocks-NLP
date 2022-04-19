from sklearn.utils import resample


def bootstrap_oversampling(dataframe, multiply_with):
    n_iterations = 5
    n_size = int(len(dataframe)) * multiply_with

    for i in range(n_iterations):
        r1 = resample(dataframe, n_samples=n_size)
    return r1