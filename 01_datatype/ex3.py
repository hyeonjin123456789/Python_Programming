# 불리언(bool)

print(2 < 3)
print(2 > 3)
print(2 == 3)
print(2 != 3)

print("뽀로로!" > "크롱")

# bool()
print(bool(3))
print(bool(0))
print(bool("hello"))
print(bool(""))
print(bool([10]))
print(bool([]))

# None 자료형
a = None
print(a, type(a))
print(bool(a))

if a is None:
    print("값이 없습니다.")