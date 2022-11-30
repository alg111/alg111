# 題目條件
"""
5ₓ₁ +7ₓ₂ +9ₓ₃ +2ₓ₄ +1ₓ₅ ≤ 250
18ₓ₁ +4ₓ₂ -9ₓ₃ +10ₓ₄ +12ₓ₅ ≤ 285
4ₓ₁ +7ₓ₂ +3ₓ₃ +8ₓ₄ +5ₓ₅ ≤ 211
5ₓ₁ +13ₓ₂ +16ₓ₃ +3ₓ₄ -7ₓ₅ ≤ 315

最大值

7ₓ₁ +8ₓ₂ +2ₓ₃ +6ₓ₄ +9ₓ₅

以4ₓ₁ +7ₓ₂ +3ₓ₃ +8ₓ₄ +5ₓ₅ ≤ 211得知
x1最大為50 x2最大為30 x3最大為70 x4最大為26 x5最大為42
"""
<a href="https://gitlab.com/cccnqu111/alg/-/blob/master/A2-QA/integerProgramming/README.md" title="Title">題目敘述</a> 

# 暴力法
'''
import time #讀取程式使用時間
timestart = time.time()
answer = 0 #答案初始
a = 0,b = 0,c = 0,d = 0,e = 0 #設置五個變數的初始
#各個變數從0取到最大值
for a_temp in range (0,51):
    for b_temp in range (0,31):
        for c_temp in range (0,71):
            for d_temp in range (0,27):
                for e_temp in range (0,43):
                        if(5*a_temp+7*b_temp+9*c_temp+2*d_temp+e_temp<=250):
                            if(18*a_temp+4*b_temp-9*c_temp+10*d_temp+12*e_temp <= 285):
                                if(4*a_temp+7*b_temp+3*c_temp+8*d_temp+5*e_temp <= 211):
                                    if(5*a_temp+13*b_temp+16*c_temp+3*d_temp-7*e_temp<=315):
                                        tanswer = 7*a_temp + 8*b_temp + 2*c_temp + 6*d_temp + 9*e_temp #最大值預設答案
                                        if(tanswer > answer):
                                            a = a_temp
                                            b = b_temp
                                            c = c_temp
                                            d = d_temp
                                            e = e_temp
                                            answer = tanswer

timeend =  time.time()             #結束時間                             
print(answer,a,b,c,d,e,"花費了:",timeend-timestart,"秒")

'''
* 實作
改變次數答案相同
'''
(base) jiangyushangdeMacBook-Air:QA1 jiangyushang$ python BruteForce.py
331 0 1 13 0 33 花費了: 29.79974603652954 秒
(base) jiangyushangdeMacBook-Air:QA1 jiangyushang$ python BruteForce.py
331 0 1 13 0 33 花費了: 11.972163200378418 秒
'''
# 爬山演算法
參考同學部分程式碼並做上自己的註解與修改
'''
import random
import time #讀取程式使用時間
timestart = time.time()
max_num = 5
h = 1 #移動距離
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
＃最終答案
answer = [0, 0, 0, 0, 0]

#主程式
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
            
#移動
def Move():
    for i in range(max_num):
        answer[i] = current_answer[i]
        current_temp1[i] = current_answer[i]
        current_temp2[i] = current_answer[i]

#計算求最大值
def Count(a):
    temp = 0
    for i in range(max_num):
        temp = temp + a[i]*num[i]
    return temp

#限制條件
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

'''
* 實作
更改移動距離發現答案有所不同
'''
(base) jiangyushangdeMacBook-Air:QA1 jiangyushang$ python HillClimbing.py
[8, 8, 8, 8, 7] 250
移動 101 次
花費了: 0.0016522407531738281 秒
(base) jiangyushangdeMacBook-Air:QA1 jiangyushang$ python HillClimbing.py
[8, 8, 8, 8, 7] 250
移動 101 次
花費了: 0.001399993896484375 秒
(base) jiangyushangdeMacBook-Air:QA1 jiangyushang$ python HillClimbing.py
[9, 7, 7, 7, 7] 238
移動 104 次
花費了: 0.0008471012115478516 秒
'''