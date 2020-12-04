import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss
import zignor
import timeit

sns.set_style("darkgrid")

def get_truncated_normal(mean=0, sd=1, low=0, upp=1):
    return ss.truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

def BuildGaussian(mean=0.5, sd=0.15, low=0, upp=1, number=300000):
    x = np.linspace(0, 1, number)
    mu = 0
    sigma = 1

    y_pdf = ss.norm.pdf(x, mean, sd)  # the normal pdf
    y_cdf = ss.norm.cdf(x, mean, sd)  # the normal cdf

    plt.plot(x, y_pdf, label='pdf')
    plt.plot(x, y_cdf, label='cdf')
    plt.legend()
    plt.show()

    X = get_truncated_normal(mean, sd, low, upp)

    plt.figure(figsize=(14,10))
    sns.distplot(X.rvs(number), bins=100, color='red',
               kde_kws={"color": "b", "lw": 2, "label": 'Gaussian Distribution'})
    plt.show()




def BuildUniform(lower=10, upper=20, number=1000000):
    uniform_distribution = ss.uniform(loc=lower, scale=upper - lower)
    x = np.linspace(uniform_distribution.ppf(0), uniform_distribution.ppf(1), number)

    y_pdf = uniform_distribution.pdf(x)
    y_cdf = uniform_distribution.cdf(x)

    plt.plot(x, y_pdf, label='pdf')
    plt.plot(x, y_cdf, label='cdf')
    plt.show()

    data_uniform = ss.uniform.rvs(size=number, loc=lower, scale=upper - lower)

    plt.figure(figsize=(14, 10))
    sns.distplot(data_uniform, bins=100, color='red', norm_hist=False,
                 kde_kws={"color": "b", "lw": 2, "label": 'Uniform Distribution'})

    plt.show()



def BuildExponential(scale=0.0001, loc=0.2, number=1000000):
    x = np.linspace(0, 1, number)
    mu = 0
    sigma = loc

    y_pdf = ss.expon.pdf(x, mu, sigma)  # the normal pdf
    y_cdf = ss.expon.cdf(x, mu, sigma)  # the normal cdf

    plt.plot(x, y_pdf, label='pdf')
    plt.plot(x, y_cdf, label='cdf')
    plt.legend()
    plt.show()

    data_expon = ss.expon.rvs(scale, loc, number)

    plt.figure(figsize=(14, 10))
    plt.xlim(0, 1)
    sns.distplot(data_expon, bins=400, color='red', norm_hist=False,
                 kde_kws={"color": "b", "lw": 2, "label": 'Exponential Distribution'})

    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Enter numbers')
    BuildUniform(lower=int(input()), upper=int(input()))

    BuildExponential()

    BuildGaussian()  # normal


    numbers = 500000  # 50 миллионов

    start = timeit.default_timer()
    norm1 = zignor.randn(numbers)
    stop = timeit.default_timer()

    start1 = timeit.default_timer()
    u1 = np.random.random(numbers)
    u2 = np.random.random(numbers)
    z1 = np.sqrt(-2.0 * np.log(u1)) * np.cos(2 * np.pi * u2)
    z2 = np.sqrt(-2.0 * np.log(u1)) * np.sin(2 * np.pi * u2)
    stop1 = timeit.default_timer()

    print('Execution time of ziggurat algorithm: {}'.format(stop - start))
    print('Execution time of box-muller algorithm: {}'.format(stop1 - start1))

    f, axes = plt.subplots(1, 2)
    sns.distplot(norm1, ax=axes[0])
    sns.distplot(z2, ax=axes[1])
    plt.show()


