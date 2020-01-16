# Fraas Marcel
import numpy as np
import matplotlib.pyplot as plt


def f(w, b):
    return ((1-w)**2) + (100*((b - w**2)**2))

def propagate(w, b):

    cost = f(w, b)

    # Calculate dw, db
    dw = 2*(-1+w-(200*b*w)+(200*(w**3)))
    db = 200*(b-(w**2))

    cost = np.squeeze(cost)

    grads = {'dw': dw,
             'db': db}

    return grads, cost


def optimize(w, b, num_iter, learning_rate):
    costs = []

    for i in range(num_iter):
        grads, cost = propagate(w, b)

        w = w - learning_rate * grads['dw']
        b = b - learning_rate * grads['db']

        costs.append(cost)

    params = {'w': w,
              'b': b}

    return params, grads, costs

for i in range(1,9,1) :

    # Do not change the following 5 lines - they are needed for the contour plot.
    N = 250
    lin = np.linspace(-0.2, 1.2, N)
    wlin, blin = np.meshgrid(lin, lin)
    f_values = f(wlin, blin)
    plt.contour(wlin, blin, f_values.reshape(N, N), levels=np.logspace(-1,3,8))

    # Find the parameters w and b that minimize f(w,b) and print these parameters as well as the corresponding function value.
    params, grads, costs = optimize(0, 0, 7500, 0.001*i)
    print(params)

    # Plot (w,b) as a single red point (or red star 'r*').
    plt.plot(params['w'],params['b'],'r*')
    plt.show()


    # Plot the costs
    plt.plot(costs)
    plt.show()