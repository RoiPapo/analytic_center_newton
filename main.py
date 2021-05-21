import numpy as np



def back(alpha, beta, s):
    """
    finds best back step
    :param alpha: Armajio parameter
    :param beta: Armajio parameter
    :param s: step size
    :return:
    """
    def lsearch(f, xk, gk):
        t = s
        while f(xk) - f(xk - t * gk) < alpha * t * np.linalg.norm(gk) ** 2:
            t = t * beta
        return t
    return lsearch

def analytic_center(A,b,x0):
    pass


def main():
    pass



if __name__ == "__main__":
    main()
