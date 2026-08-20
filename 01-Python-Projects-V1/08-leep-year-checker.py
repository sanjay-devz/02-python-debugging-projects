def is_leepyear(year):
    return (year % 400 == 0 ) or (year % 4 == 0 and year % 100 != 0)


A = is_leepyear(2024)
B = is_leepyear(2026)
C = is_leepyear(1999)
print(A)
print(B)
print(C)

#simple leep year finding program