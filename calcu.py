
import matplotlib.pyplot as plt
import numpy as np
import xlwt
A = np.zeros ((300,784),dtype=float)
A1 = np.zeros ((300,784),dtype=float)

f = open('C:\\Users\孙世奇\Desktop\稀疏矩阵数据\layer1.txt')
lines = f.readlines()
A_row = 0
k=0

# 矩阵存储到矩阵
for line in lines:
    list = line.strip('\n').split(' ')
    #print(list)
    A[A_row:] = list[0:784]
    A_row += 1







#矩阵二值化

for i in range(0,A.shape[0]):
    for j in range(0,A.shape[1]):
     if  A[i][j] != 0:
          A[i][j] = 255
        #  k=k+1


#矩阵进行

k2=0
for i in range (0,18):
    for j in range (0,49):
        k=0
        heart=i*16+j*16
        for i1 in range(0,16):
            for  j1 in range(0,16):
                if A[i*16+i1][j*16+j1] != 0:
                    k=k+1
        if k/(16*16)>0.2:
            k2=k2+1
            for i1 in range(0, 16):
                for j1 in range(0, 16):
                    A1[i * 16 + i1][j * 16 + j1]=A[i*16+i1][j*16+j1]
                    A[i * 16 + i1][j * 16 + j1]=0

k=0
for i in range(0,A.shape[0]):
    for j in range(0,A.shape[1]):
     if  A[i][j] != 0:
         # A1[i][j] = 255
          k=k+1




# 打印灰度图
fig =plt.figure()
plt.imshow(A, cmap=plt.cm.gray)

plt.show()
print(k/(300*784))


#print(k/(300*100) )

#print(A)

#plt.matshow(A)

#plt.show()