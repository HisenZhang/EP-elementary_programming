#Python 循环&判断 练习
## Fibonacci
这道题利用递归求解编写程序比较简单
```python
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print fib(36)
```



##  Narcissistic Number

水仙花数问题

```python
for n in range(100,1000):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if n == i ** 3 + j ** 3 + k ** 3:
        print n
```



