import time #讀取程式使用時間
timestart = time.time()
answer = 0 #答案初始
a = 0
b = 0
c = 0
d = 0
e = 0 
#設置五個變數的初始
#各個變數從0取到最大值
for a_temp in range (0,51):
    for b_temp in range (0,31):
        for c_temp in range (0,71):
            for d_temp in range (0,27):
                for e_temp in range (0,43):
                        if(5*a_temp + 7*b_temp + 9*c_temp + 2*d_temp + e_temp <=250):
                            if(18*a_temp + 4*b_temp - 9*c_temp + 10*d_temp + 12*e_temp <= 285):
                                if(4*a_temp + 7*b_temp + 3*c_temp + 8*d_temp + 5*e_temp <= 211):
                                    if(5*a_temp + 13*b_temp + 16*c_temp + 3*d_temp - 7*e_temp<=315):
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
