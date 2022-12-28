本作業參考網路資料並加以統整而得，參考資料在此文最後
# 題目介紹
```
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
```
# Example
```
CASE1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

CASE2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

CASE3:
Input: nums = [3,3], target = 6
Output: [0,1]
```
# 限制
* Constraints:
```
陣列長度為介於2到10⁴ 之間 ->不需考慮特殊情況(陣列無值或僅有一值的情況)

陣列內元素的值介於-10⁹ 到 10⁹ 之間

整數目標值 亦介於-10⁹ 到 10⁹ 之間

只有一種有效的答案存在
```

# 題目解析
從 nums 中找出兩數相加等於 target 的兩數索引值，回傳兩數索引值組成的容器（List 或 Object）。從題目給的限制及敘述中，可以得知必然只會有一組要求符合的結果，沒有規定回傳資料的順序。
## 解題思路:
* 先找第一個數字，再從剩下的數字找到能不能加總到整數目標值(target)
要是第一個數字搭配剩下的都沒找到，那就換第二個數字開始，一路找到結束為止
* 一開始想透過排序的方式來解題，以最小值為基礎來與其他數相加求解，後來發現與實際想法有出入
# 方法一：暴力法
透過雙層迴圈的方式找到（1)num(2)target 
```
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):               ＃取得陣列長度並取得第一個數值  
            for j in range(i+1, len(nums)):      ＃取得地藝術值以後的數來做相加組合
                if nums[i] + nums[j] == target:  #如果nums陣列裡的i,j兩數相加=target就回傳
                    return [i, j]
```
* 缺點
速度慢，且如果陣列過大可能會逾時
# 方法二：雜湊表
* 雜湊表

雜湊表(Hash Table)又稱哈希表，是透過雜湊函式(Hash Function)來計算出一個鍵(key)與值(value)所對應的位置，進而建立雜湊表格，而後也能夠過雜湊函式來搜尋找出鍵值存放在表格的位置。由於動作都需要先經由雜湊函式來執行，若不被知道雜湊函式情況下，保密性就極高，因此很常被應用在加密、解密、壓縮、驗證等領域

概念圖：
![GITHUB]( https://ithelp.ithome.com.tw/upload/images/20210917/20121027auspOHzYk5.jpg "雜湊表")

改變思路：
將結果：
```
num1 + num2 == target
```
換成：
```
target - num1 = num2
```
將 num1 暫存並檢查已存過的 num1 是否等於現在所需要的 num2，如果索引值相等答案不成立，依序尋找．

* 需要一個可以自定義 key 的資料結構來暫存 num1，這裡可以使用 Python 中的 dictionary，這種類似雜湊表（Hash Table）的資料結構
* 實作：
```
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - num1
            if num2 in d:
                return [d[num2], i]   ＃需要 num1、num2 的索引值，要把索引值記錄下來
            d[num1] = i
```
由此不僅減少迴圈使用外，更能加快程式運行速度，解決逾時問題

# 參考資料
<a href="https://ithelp.ithome.com.tw/articles/10268077" title="Title">雜湊法</a>

<a href="https://leetcode.com/problems/two-sum/" title="Title">題目來源</a>

模仿部分程式碼，並加上自身註解
<a href="https://zyrastory.com/coding/leetcode/leetcode-1-two-sum-解題思路及翻譯/" title="Title">程式參考來源</a>
