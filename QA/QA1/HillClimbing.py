import random
import time #讀取程式使用時間
timestart = time.time()
max_num = 5
h = 2 #移動距離
#變數條件
coefs = [[5, 7, 9, 2, 1],
        [18, 4, -9, 10, 12],
        [4, 7, 3, 8, 5],
        [5, 13, 15, 3, -7]]

maxs = [250,  285, 211, 315]
#最大答案
num = [7, 8, 2, 9, 6]
#答案暫存
current_answer = [0, 0, 0, 0, 0]
current_temp1 = [0, 0, 0, 0, 0]
current_temp2 = [0, 0, 0, 0, 0]

answer = [0, 0, 0, 0, 0]

# 主程式
def Climbing():
    failCount = 0
    while failCount < 100:
        dh = random.randint(0,h) #移動距離變數
        for i in range(max_num):
            current_temp1[i] += dh
            current_temp2[i] -= dh
            a = Count(current_temp1)
            b = Count(current_temp2)
            if a >= b:
                for j in range(max_num):
                    current_answer[j] = current_temp1[j]
            else:
                for j in range(max_num):
                    current_answer[j] = current_temp2[j]

            if limit(current_answer) == False:
                failCount += 1
            elif limit(current_answer) == True:
                Move()
                
    print(answer, Count(answer))
    print("移動",failCount,"次")
            
# 移動
def Move():
    for i in range(max_num):
        answer[i] = current_answer[i]
        current_temp1[i] = current_answer[i]
        current_temp2[i] = current_answer[i]

# 計算求最大值
def Count(a):
    temp = 0
    for i in range(max_num):
        temp = temp + a[i]*num[i]
    return temp

# 限制條件
def limit(t):
    temp = 0
    for i in coefs:
        a = 0
        for j in range(max_num):
            a = a + i[j]*t[j]
        if a > maxs[temp]:
            return False
        temp += 1
    return True




Climbing()
timeend =  time.time()             #結束時間                             
print("花費了:",timeend-timestart,"秒")
