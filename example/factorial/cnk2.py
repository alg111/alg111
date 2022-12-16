def Clist(n, k):
    global goallist
    goallist = [0] * k                  #設置目標陣列的個數，將數值初始化為0
    combinations(0, 1, n, k)            #列舉數列


	
def combinations(i, start, n, k):
  if i == k:                            #當i超過目標陣列個數，印出目標陣列
    print(goallist)
  else:
    for j in range(start, n+1):         #列舉出目標陣列
      goallist[i] = j               
      combinations(i + 1, j + 1, n, k)  #透過遞迴的方式填滿目標陣列

Clist(4, 2)