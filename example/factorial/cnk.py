# 修改老師部分程式碼
import random

def randomCombination(A, k): 
	global chooses 
	chooses = []							#定義全域函數
	for j in range(k):
		i = random.randrange(0, 5)			#取隨機數 0 - 4
		while A[i] in chooses:				#當取道相同值就在取一次，直到數字不同
			 i = random.randrange(0, 5)
		if not A[i] in chooses:
			chooses.append(A[i])			#取道不同值就加到新陣列
	chooses.sort()
	if len(chooses)==k:						#當長度滿足k就印出來
		print(chooses)
	return 

arr = [1,2,3,4,5]
for j in range(10):
	randomCombination(arr, 3)

