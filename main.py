import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


def ak(k, t):
    if t == 2: return 0
    s = integrate.quad(lambda x: f1(x) * np.cos(k * x / 2), 0, np.pi / 2)[0] * (1 / (2 * np.pi))
    if t == 1:
        s += integrate.quad(lambda x: f1(x) * np.cos(k * x / 2), -2 * np.pi, -3 * np.pi / 2)[0] * (1 / (2 * np.pi))
    else:
        s += integrate.quad(lambda x: f1(x) * np.cos(k * x / 2), -np.pi / 2, 0)[0] * (1 / (2 * np.pi))
    return s


def bk(k, t):
    if t == 3: return 0
    s = integrate.quad(lambda x: f1(x) * np.sin(k * x / 2), 0, np.pi / 2)[0] * (1 / (2 * np.pi))
    if t == 1:
        s += integrate.quad(lambda x: f1(x) * np.sin(k * x / 2), -2 * np.pi, -3 * np.pi / 2)[0] * (1 / (2 * np.pi))
    else:
        s += integrate.quad(lambda x: -f1(x) * np.sin(k * x / 2), -np.pi / 2, 0)[0] * (1 / (2 * np.pi))
    return s


def a0(t):
    s = integrate.quad(f1, 0, np.pi / 2)[0] * (1 / (2 * np.pi))
    if t == 1:
        s += integrate.quad(f1, -2 * np.pi, -3 * np.pi / 2)[0] * (1 / (2 * np.pi))
    else:
        s += integrate.quad(f1, -np.pi / 2, 0)[0] * (1 / (2 * np.pi)) * (-1) ** (t == 2)
    return s


def sigma(x, n, t):
    s = a0(t) / 2
    for k in range(1, n + 1):
        s += ak(k, t) * np.cos(k * x / 2) + bk(k, t) * np.sin(k * x / 2)
    return s


def f1(x):
    return np.cos(x)


def f2(x):
    return 0 + 0 * x


def draw(axis, x1, x2, x3, x4, g1, g2, g3, g4):
    axis.plot(x1, g1)
    axis.plot(x2, g2)
    axis.plot(x3, g3)
    axis.plot(x4, g4)


def main():
    # Input data
    t = int(input("Общий/по синусам/по косинусам(1, 2, 3): "))
    n = int(input("Количество слагаемых (1-100): "))

    # plots
    fig, ax = plt.subplots()
    x1 = np.arange(0, np.pi / 2, 0.01)
    x2 = np.arange(np.pi / 2, 2 * np.pi, 0.01)
    if t == 1:
        x3 = np.arange(-2 * np.pi, -3 * np.pi / 2, 0.01)
        x4 = np.arange(-3 * np.pi / 2, 0, 0.01)
        draw(ax, x1, x2, x3, x4, f1(x1), f2(x2), f1(x3), f2(x4))
    else:
        x3 = np.arange(-2 * np.pi, -np.pi / 2, 0.01)
        x4 = np.arange(-np.pi / 2, 0, 0.01)
        draw(ax, x1, x2, x3, x4, f1(x1), f2(x2), f2(x3), -f1(x4) if t == 2 else f1(x4))
    x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
    ax.plot(x, sigma(x, n, t))

    ax.set(xlabel="x", ylabel="y", title=f"График функции и ряд Фурье (n = {n}, " +
                                         f"{'общий' if t == 1 else ('по синусам' if t == 2 else 'по косинусам')})")
    ax.grid()
    plt.show()


main()
