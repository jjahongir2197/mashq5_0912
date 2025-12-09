Tuple Comprehension

1 - misol

result = tuple(x for x in range(1, 31) if x % 3 == 0)
print(result)

2 - misol

numbers = [-1, 4, -5, -11, -33, 31, 67, 91]
result = tuple(x for x in numbers if x > 0)
print(result)

3 - misol

result = tuple((x,x ** 2) for x in range(1, 16))
print(result)

4 - misol

words = ["hello", "world", "python"]
result = tuple(w[-1] for w in words)
print(result)

5 - misol

numbers = list(range(1, 21))
result = tuple(numbers[i]**2 for i in range(len(numbers)) if i % 2 == 1)
print(result)
