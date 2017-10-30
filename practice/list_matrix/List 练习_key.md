# List 练习

```python
# 需要用到的python模块
import numpy
# 定义两个List,分别作为矩阵A和B
# 带入自己的abcd值
A = [[a,b],
     [c,d]]

B = [[m],
     [n]]

# List类型不能直接进行矩阵运算, 需要转为numpy规定的矩阵类型
A = numpy.mat(A)
B = numpy.mat(B)
# 生成A矩阵的逆
A = numpy.invert(A)
# 左乘,得到答案
X = A*B
# 输出答案
print('X='X[0,0],',Y=',X[1,0])
# 如果版本是Python2.X
# print('X='X[0,0],',Y=',X[1,0])

```

