##    for i in [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
##        print("%2d, %6.4f" % (i, gumbelCDF(i)))

##    i = 0.5; delta = 0.5; n = 0
##    cdf = gumbelCDF(i)
##    err = abs(cdf - 0.5)
##    while err > 1e-16:
##        i += (delta / 2) if cdf < 0.5 else -(delta / 2)
##        cdf = gumbelCDF(i)
##        err = abs(cdf - 0.5)
##        delta /= 2
##        n += 1
##    print("%2d %18.15f %18.15f %18.15f" % (n, delta, i, cdf))
        
##    for i in range(len(oneMinusAlphaOneSided)):
##        print("%d, %5.3f, %5.3f" % (i,                        \
##                                    oneMinusAlphaOneSided[i], \
##                                    ksTestGoodnessOfFit[i] ),
##              criticalValue(i))
##
##    for i in range(len(oneMinusAlphaTwoSided)):
##        print("%d, %5.3f, %5.3f" % (i,                        \
##                                    oneMinusAlphaTwoSided[i], \
##                                    ksTestGoodnessOfFit[i] ),
##              criticalValue(i, True, False))
##
##    for i in range(len(oneMinusAlphaOneSided)):
##        print("%d, %5.3f, %5.3f" % (i,                        \
##                                    oneMinusAlphaOneSided[i], \
##                                    ksTestTwoSample[i] ),
##              criticalValue(i, False))
##
##    for i in range(len(oneMinusAlphaTwoSided)):
##        print("%d, %5.3f, %5.3f" % (i,                        \
##                                    oneMinusAlphaTwoSided[i], \
##                                    ksTestTwoSample[i] ),
##              criticalValue(i, False, False))
