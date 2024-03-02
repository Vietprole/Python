# multiline string
print("""Tháp mười đẹp nhất bông sen
Việt Nam đẹp nhất có tên Bác Hồ""")

# string concatenation
print("Hello" + "Mary")

# string repetition
print("Hello Peter " * 5)

numbers = "0123456789"
print(numbers[6:10])
print(numbers[-12:-7])
print(numbers[:3])
print(numbers[-5:])

x = 1.2243243223
print('%.2f' % x)

str1 = "Python"
# str1[0] = "Q" # no item assignment

str1 = "Python"
str1 = "Q" + str1[1:]
print(str1)

# using concatenation
name = "Trà"
age = str(18)
print(name + " năm nay " + age + " tuổi. Hỏi bạn trai của " 
+ name + " bao nhiêu tuổi?")

# using f-string
name = "Trà"
age = 18
print(f"{name} năm nay {age} tuổi. Hỏi bạn trai của {name} bao nhiêu tuổi?")

# using format
name = "Trà"
age = 18
print("{0} năm nay {1} tuổi. Hỏi bạn trai của {0} bao nhiêu tuổi?".format(name, age))

len("Python")
