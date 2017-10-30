# List 练习

## List 方法与使用总结

如果忘了List的操作, 请阅读并执行这个程序:

```python
# 声明编码
coding='utf-8'
# 这个程序在Python2.X下写成. 
# 如在Python3.X中执行请注意添加print()函数的括号对.
print 'this is about list test'

a =[1,2,3,4]
a.append(5)
print a

b =[5,6]

a.extend(b)
print a

a.insert(0,0)
print a
a.insert(len(a),10)
print a

a.pop()
print a

a.reverse()
print a

print 'use list as stack'
stack = [1,2]
stack.append(3)
stack.append(4)
print stack

stack.pop()
stack.pop()
print stack

print 'use list as sequence'

from collections import deque
queue = deque(['aa','bb','cc'])
queue.append('dd')
queue.append('ee')
print queue.popleft()
print queue

print 'functional programming tools three important function use'

print 'filter use'
def f(x): return x%3==0 or x%5==0
ll = filter(f,range(2,25))
print ll

print  'map use'
def cube(x): return x*x*x
cc = map(cube,range(1,10))
print cc

print 'reduce use '
def  add(a,b): return a+b
i = reduce(add,range(1,11))
print i

print 'list  comprehension'

squares = [x**2 for x in range(10)]
print squares

mm = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print mm


print 'nested list comprehension'

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]]

print matrix

print 'The following list comprehension will transpose rows and columns:'

new_matrix = [[row[i] for row in matrix] for i in range(4)]

print new_matrix
```

## 挑战: 矩阵求解二元一次方程组

上文里出现的Matrix矩阵也就是我们常说的二维数组/列表.

如果我们把一维的列表作为元素, 放在在另一个列表里, 这时候就形成了二维数组. 如果列表的长度宽度都一致, 形如

```python
[[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9,10,11,12]]
```

则称其为矩阵. 矩阵的相关知识在IGCSE数学里有涉及.

矩阵有一些应用, 我们这里用来编写一个二元一次方程组的求解程序.

对于一个二元一次方程组我们可以写成如下形式:


$$
\begin{equation}
\begin{cases}
ax+by=m\\
cx+dy=n
\end{cases}
\end{equation}
$$
如果我们其中的系数提取出来,写成$\left[\begin{matrix}a & b\\c & d \\\end{matrix}\right]$的形式, 我们就得到了一个系数矩阵.

现给出计算公式: 系数矩阵*未知数矩阵=常数矩阵, 记为$AX=B$

$$
\left[
\begin{matrix}
  a&b \\
   c&d \\
    \end{matrix}
  \right]
  \left[
  \begin{matrix}
  x \\
  y
  \end{matrix}
  \right]
  =
    \left[
  \begin{matrix}
  m \\
  n
  \end{matrix}
  \right]
$$

两边同时左乘系数矩阵的逆, 可得$X=A^{-1}B$. 注意, 矩阵左乘和右乘会得到不一样的结果. 

### 挑战

完成这个程序.

一些提示: 

```python
# 声明编码
coding='utf-8'
# 需要用到的python模块
import numpy
# 定义两个List,分别作为矩阵A和B
# 带入自己的abcd值到下面的List里
A = [[a,b],
     [c,d]]

B = [[m],
     [n]]

# List类型不能直接进行矩阵运算, 需要转为numpy规定的矩阵类型
A = numpy.mat(A)
B = numpy.mat(B)
# 生成A矩阵的逆
A = numpy.invert(A)
# 请完成中间的部分,得到矩阵未知数X

# 输出答案
print('X='X[0,0],',Y=',X[1,0])
# X[0,1]表示第0行第1列,是矩阵的下标表示法
# 如果版本是Python2.X
# print('X='X[0,0],',Y=',X[1,0])
```



