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

    random.seed()

    with open('bootstrap.dat', 'r') as fin:
        runs = fin.readlines()

    inputFile = input("Enter input filename:  ")
    outptFile = input("Enter output filename: ")
    sampleTyp = bool(input("Enter type of sampling " \
                           + "(0: without replacement; 1: w/ replacement): "))
    
    with open(inputFile, mode='r') as fin:
        inputData = fin.readlines()
    data = list(float(datIn) for datIn in inputData)

    with open(outptFile, mode='w') as fout:
        for run in runs:
            tmp = run.split(',')
            segmentLen = int(tmp[0])
            sampleSize = int(tmp[1])

            sample = list()
            means = list(); stdevs = list()
            runMeans = list(); runStDev = list()
            for k in range(10):
                for j in range(100):
                    for i in range(int(len(data) / segmentLen)):
                        start = i * segmentLen; stop = (i + 1) * segmentLen
                        if sampleTyp:
                            sample = random.choices(data[start:stop],
                                                    k=sampleSize)
                        else:
                            sample = random.samples(data[start:stop],
                                                    k=sampleSize)
                        fmean = statistics.fmean(sample)
                        stdev = statistics.stdev(sample)
                        means.append(fmean)
                        stdevs.append(stdev)
                    
                    fmean = statistics.fmean(means)
                    runMeans.append(fmean)
                    stdev = statistics.stdev(stdevs)
                    runStDev.append(stdev)

                print("%4d, %4d," % (segmentLen, sampleSize),
                      "%10.3f,"   % (statistics.fmean(runMeans)),
                      "%10.3f,"   % (statistics.median(runMeans)),
                      "%8.3f,"    % (statistics.fmean(runStDev)),
                      "%8.3f"     % (statistics.median(runStDev)) )

                print("%4d, %4d," % (segmentLen, sampleSize),
                      "%10.3f,"   % (statistics.fmean(runMeans)),
                      "%10.3f,"   % (statistics.median(runMeans)),
                      "%8.3f,"    % (statistics.fmean(runStDev)),
                      "%8.3f"     % (statistics.median(runStDev)), file=fout)

    pass
