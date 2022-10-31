def votosComputado(arr):
    arrAscend = sorted(arr)
    result = []
    
    if max(arr) < len(arrAscend):
        for x in range(1, len(arrAscend)):
            if (x + 1) not in arrAscend:
                result.append(x+1)
        
    else:
        for x in range(1, max(arr)):
            if (x + 1) not in arrAscend:
                result.append(x+1)
                
    return result
    
print(votosComputado([4,3,2,3,1]))
print(votosComputado([5,66,99,76,97,67,22,72,37,33]))
