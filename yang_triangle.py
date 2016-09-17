def triangles(n):
    L1 = [1]
    L2 = [1,1]
    i, j = 0, 0
    while i<n:
        yield L1
        L1 = L2
        L = tuple(L1)
        i = i +1
        if i > 1: 
            while j<=i:
                if j==0 :
                    L2[j] = 1
                elif j ==i:
                    L2.append(1)
                else:
                    L2[j] =L[j]+L[j-1]
                j = j+1
            j = 0
    return 