本作業參考網路資料並加以統整而得，參考資料在此文最後
# 題目介紹
```
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
```
# Example
```
CASE1:
Input: s = "()"
Output: true

CASE2:
Input: s = "()[]{}"
Output: true

CASE3:
Input: s = "(]"
Output: false
```
# 限制
* Constraints:
```
1 <= s.length <= 104
s consists of parentheses only '()[]{}'
```

# 題目解析
這一題顧名思義就是要我們檢查一串括號是否為合法括號，就好比程式碼編譯器的判定，括號要兩兩成對，且相同類型的括號要配相同類型的括號（譬如大括號要配大括號）。如果是合法括號就回傳true，否則回傳false。
## 解題思路:
* 這題是使用 stack 解題的經典範例。我們只要碰到 (、{、[ 就將其放入 stack 中，如果遇到 )、}、] 則匹配 stack 的最頂部（stack 是後進先出的資料結構），如果是合法的匹配，則將其 stack 頂部的字符彈出。
* 如果 stack 為空，而又碰到了需要匹配 )、}、] 的情況，則意味著這是個不合法的字串，直接回傳 false。如果匹配到最後 stack 為空，回傳 true、反之則 false。
# 方法一：堆疊解法

* 堆疊

是電腦科學中的一種抽象資料型別，只允許在有序的線性資料集合的一端（稱為堆疊頂端，top）進行加入資料（push）和移除資料（pop）的運算。因而按照後進先出（LIFO, Last In First Out）的原理運作，堆疊常用一維陣列或連結串列來實現。常與另一種有序的線性資料集合佇列相提並論

基本操作：

推入：將資料放入堆疊頂端，堆疊頂端移到新放入的資料。

彈出：將堆疊頂端資料移除，堆疊頂端移到移除後的下一筆資料。

概念圖：
![GITHUB]( https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Data_stack.svg/400px-Data_stack.svg.png"堆疊概念圖")

* 解題思路：

先建立一個堆疊，假如括號為左括號就先加入堆疊，如果是右括號則比對與堆疊最上層的括號是否成對，如果是的話就把最上層的括號丟掉（用pop），最後再檢查堆疊中是否還有括號，如果沒有就表示這是一個合法的括號，如果有則非合法括號。

```
class Solution:
    def isValid(self, s: str) -> bool:
        # Init
        st = []
        
        # Matching
        for c in s:
            if c in ['(', '{', '[']:
                st.append(c)
            elif len(st) == 0: return False
            elif st[-1] == '(' and c != ')': return False
            elif st[-1] == '{' and c != '}': return False
            elif st[-1] == '[' and c != ']': return False
            else: st.pop()
        
        return len(st) == 0
```

* 透過對list的操作，包括list[-1]、list.append()與list.pop()的方式模擬一個堆疊的資料型態，因為這些操作的時間複雜度都是big O(1)的，因此不會過於浪費時間。

# 參考資料
<a href="https://zh.wikipedia.org/zh-tw/堆栈" title="Title">堆疊</a>

<a href="https://leetcode.com/problems/valid-parentheses/" title="Title">題目來源</a>

模仿部分程式碼，並加上自身註解
<a href="https://ithelp.ithome.com.tw/articles/10260607" title="Title">程式參考來源</a>
