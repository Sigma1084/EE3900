from matplotlib import pyplot as plt

def main():
    N = 25
    X = [1, 1]
    for n in range(2, N+1):
        X.append(X[-1] + X[-2])
    plt.stem(range(N+1), X)
    plt.xlabel('$n$')
    plt.ylabel('$x(n)$')
    plt.grid()
    plt.savefig('../figs/x_n.pdf')
    plt.show()

if __name__ == '__main__':
    main()
