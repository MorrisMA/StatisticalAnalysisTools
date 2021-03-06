'''
    https://www.itl.nist.gov/div898/handbook/eda/section3/eda35d.htm

    Runs Test constructed in accordance with the description provided at the
    link above. The code was tested using the example and associated provided.
'''

import math

def calcStatistic(data, avg):
    inp = str()
    cur = str()     # current type of run
    n1 = int(0)     # number of runs of positive values
    n2 = int(0)     # number of runs of negative values
    p = int(0)      # number positive values
    n = int(0)      # number negative values
    N = int(0)      # total number of samples

    cur = '-' if data[0] < avg else '+'

    for i in data:
        inp = '-' if i < avg else '+'

        if inp == '+':
            p += 1
            if cur != inp:
                cur = inp
                n2 += 1
        else:
            n += 1
            if cur != inp:
                cur = inp
                n1 += 1

    N = p + n
    R = n1 + n2
    Rbar = ((2 * p * n) / N) + 1
    sr = math.sqrt((2 * p * n * (2 * p * n - N)) / (N * N *(N - 1)))

    Z = (R - Rbar) / sr

    return Z, R, Rbar, sr, p, n, n1, n2

if __name__ == '__main__':

    fileName  = str()
    
    medStr = str()
    strStr = str()
    stpStr = str()
    
    median = int()
    start  = int()
    end    = int()

    fileName  = input("Enter file name of data file (text) to test: ")
    if fileName != '':
        try:
            with open(fileName, mode='r') as fin:
                inputData = fin.readlines()

            print("len(%s) = %d" % (fileName, len(inputData)))
            print()
            
            strStr = input("Enter start line (Null == first line)  : ")
            start  = 0 if strStr == '' else int(strStr)
            
            stpStr = input("Enter stop line  (Null == all lines)   : ")
            end    = len(inputData) if stpStr == '' else int(stpStr)

            print()

##            # trim the input data to the desired section
##            inputData = inputData[start:end]
            # convert the input data to a numeric representation
            intStr = input("Is data integer (Y/y) or floating point (other): ")
            if intStr in ['Y', 'y']:
                data = list(int(line) for line in inputData)
            else: data = list(float(line) for line in inputData)

            print()

            medStr = input("Enter data partition value (Null == 0) : ")
            if intStr in ['Y', 'y']:
                median = 0   if medStr == '' else int(medStr)
            else:
                median = 0.0 if medStr == '' else float(medStr)

            sum = float(0)
            avg = float(0)
            
            if medStr == '':
                for i in data: sum += i
                avg = sum / len(data)
            else: avg = median

            Z, R, Rbar, sr, p, n, n1, n2 = calcStatistic(data[start:end], avg)

            print()
            print("%5d, %8.3f, %8.3f, %8.3f, %8.3f" % \
                  (len(data), Z, R, Rbar, sr) )
            print("%8.1f, %5d, %5d, %5d, %5d" % (avg, p, n, n1, n2) )
            print()

            segStr = input("Enter segment size (500 default): ")
            segLen = 500 if segStr == '' else int(segStr)

            numSeg = int(len(data) / segLen)
            p1 = math.log(math.log(1/0.99))
            p5 = math.log(math.log(1/0.95))

            runStatistics = list(calcStatistic(data[i * segLen: \
                                                    i * segLen + segLen], \
                                               avg) for i in range(numSeg)  )

            for i in range(numSeg):
                start = i * segLen; end = start + segLen
                Z, R, Rbar, sr, p, n, n1, n2 = calcStatistic(data[start:end],
                                                             avg)
                passP1 = True if Z >= p1 else False
                passP5 = True if Z >= p5 else False

                runsTestPass = passP1 or passP5

                print("%5d, %5s, %8.3f, %5d, %8.3f, %8.3f, %5d, %5d, %5d, %5d" % \
                      (i, runsTestPass, Z, R, Rbar, sr, p, n, n1, n2) )

            Zbar = float(0.0)

            for run in runStatistics:
                Z, R, Rbar, sr, p, n, n1, n2 = run
                Zbar += Z
            Zbar /= len(runStatistics)

            sZ = float(0.0)

            for run in runStatistics:
                Z, R, Rbar, sr, p, n, n1, n2 = run
                sZ += (Z - Zbar) * (Z - Zbar)
            sZ = math.sqrt(sZ / len(runStatistics))
            print(len(runStatistics), Zbar, sZ)
                
        except IOError as error:
            print("Error - file not found")
    else:
        print("Data File required.")
