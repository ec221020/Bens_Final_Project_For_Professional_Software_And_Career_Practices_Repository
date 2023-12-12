import numpy as np

def PmCc(x, y):
    meanx = np.mean(x)
    meany = np.mean(y)


    numerator = np.sum((x - meanx) * (y - meany))
    denominator_x = np.sqrt(np.sum((x - meanx)**2))
    denominator_y = np.sqrt(np.sum((y - meany)**2))


    p = numerator / (denominator_x * denominator_y)


    return p


def linear_regression(x, y):
    meanx   = np.mean(x)
    meany   = np.mean(y)
    sigmax  = np.std(x)
    sigmay  = np.std(y)
    sigmaxy = np.sum(np.multiply(x-meanx,y-meany))/(len(x)-1)
    m = sigmaxy/(sigmax*sigmax) 
    q = meany-m*meanx
    return m,q

