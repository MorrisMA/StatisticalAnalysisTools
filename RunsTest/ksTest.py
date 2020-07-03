'''
    Kolomogorov-Smirnov Goodness-of-Fit Test (KS-Test)
'''


import math
import random
import statistics

oneMinusAlphaOneSided  = [0.900, 0.950, 0.975, 0.990, 0.995]
oneMinusAlphaTwoSided  = [0.800, 0.900, 0.950, 0.980, 0.990]

# used these D statistic values for n > 40 samples

ksTestGoodnessOfFit = [1.52, 1.73, 1.92, 2.15, 2.30]
ksTestTwoSample     = [1.07, 1.22, 1.36, 1.52, 1.63]

# Euler's Constant

eulerConstant = 0.57721566490153286060

def gumbelCDF(x, mu=0.0, beta=1.0, maximum=True):
    z = (x - mu) / beta
    if maximum:
        return math.exp(-math.exp(-z))
    else:
        return 1 - math.exp(-math.exp(z))

def criticalValue(index, gof=True, oneSided=True):
    if gof:
        if oneSided:
            return oneMinusAlphaOneSided[index], ksTestGoodnessOfFit[index]
        else:
            return oneMinusAlphaTwoSided[index], ksTestGoodnessOfFit[index]
    else:
        if oneSided:
            return oneMinusAlphaOneSided[index], ksTestTwoSample[index]
        else:
            return oneMinusAlphaTwoSided[index], ksTestTwoSample[index]


if __name__ == '__main__':

    fileName = input("Enter filename: ")
    
    with open(fileName, mode='r') as fin:
        inputData = fin.readlines()
    data = list(float(datIn) for datIn in inputData)

    segmentLen = int(input("Enter segment length: "))
    sampleSize = int(input("Enter sample size:    "))

    samples = list()

    for i in range(int(len(data) / segmentLen)):
        start = i * segmentLen; stop = (i + 1) * segmentLen
        
        mean = statistics.harmonic_mean(random.sample(data[start:stop], sampleSize))
        samples.append(mean)
    mean = statistics.harmonic_mean(samples)

    print("%.2f" % mean, statistics.multimode(samples), statistics.multimode(data))

    quant = [round(q, 3) for q in statistics.quantiles(data, n=100)]
    print(quant)


    pass
