from numpy import *

m1 = matrix(' 1,2,3; 4,5,6; 7,8,9 ')
m2 = matrix(' 0,0,0; 0,0,0; 0,0,0 ')
for i in range(len(3)):
    for j in range(len(3)):
        for k in range(len(3)):
            sum[i][j] = sum + sum[i][j]*sum[j][k]
        sum = 0
    

