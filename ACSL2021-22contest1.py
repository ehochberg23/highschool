'''
Created on Jan 14, 2022

@author: EHochberg23
'''


def findTime(cstr):
    H = 0
    M = 0
    S = 0

    L = list(cstr)

    if L[0] == "R":
        H += 1
    elif L[0] == "G":
        M += 5
    elif L[0] == "B":
        S += 5
    elif L[0] == "Y":
        H += 1
        M += 5
    elif L[0] == "C":
        M += 5
        S += 5
    elif L[0] == "M":
        S += 5
        H += 1
    elif L[0] == "W":
        H += 0
        M += 0
        S += 0

    if L[1] == "R":
        H += 1
    elif L[1] == "G":
        M += 5
    elif L[1] == "B":
        S += 5
    elif L[1] == "Y":
        H += 1
        M += 5
    elif L[1] == "C":
        M += 5
        S += 5
    elif L[1] == "M":
        S += 5
        H += 1
    elif L[1] == "W":
        H += 0
        M += 0
        S += 0

    if L[2] == "R":
        H += 2
    elif L[2] == "G":
        M += 10
    elif L[2] == "B":
        S += 10
    elif L[2] == "Y":
        H += 2
        M += 10
    elif L[2] == "C":
        M += 10
        S += 10
    elif L[2] == "M":
        S += 10
        H += 2
    elif L[2] == "W":
        H += 0
        M += 0
        S += 0

    if L[3] == "R":
        H += 3
    elif L[3] == "G":
        M += 15
    elif L[3] == "B":
        S += 15
    elif L[3] == "Y":
        H += 3
        M += 15
    elif L[3] == "C":
        M += 15
        S += 15
    elif L[3] == "M":
        S += 15
        H += 3
    elif L[3] == "W":
        H += 0
        M += 0
        S += 0

    if L[4] == "R":
        H += 5
    elif L[4] == "G":
        M += 25
    elif L[4] == "B":
        S += 25
    elif L[4] == "Y":
        H += 5
        M += 25
    elif L[4] == "C":
        M += 25
        S += 25
    elif L[4] == "M":
        S += 25
        H += 5
    elif L[4] == "W":
        H += 0
        M += 0
        S += 0

    if H >= 12:
        H = H - 12
    if M >= 60:
        M = M - 60
        H += 1
    if S >= 60:
        S = S - 60
        M = M + 1
    if H < 10:
        H = "0" + str(H)
    if M < 10:
        M = "0" + str(M)
    if S < 10:
        S = "0" + str(S)

    final = (str(H) + ":" + str(M) + ":" + str(S))

    return (final)