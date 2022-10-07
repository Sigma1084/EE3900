from matplotlib import pyplot as plt

def main():
    N = 25
    X = [1, 1]
    for n in range(2, N+3):
        X.append(X[-1] + X[-2])
    Y = [1]
    for n in range(1, N+1):
        Y.append(X[n-1] + X[n+1])
    plt.stem(range(N+1), Y)
    plt.xlabel('$n$')
    plt.ylabel('$y(n)$')
    plt.grid()
    plt.savefig('../figs/y_n.pdf')
    plt.show()

if __name__ == '__main__':
    main()

