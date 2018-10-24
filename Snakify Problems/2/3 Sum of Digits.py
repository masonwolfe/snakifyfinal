num = int(input())
hundreds = num // 100
tens = (num - hundreds * 100) // 10
ones = (num - ((hundreds * 100) + (tens * 10)) )
print(hundreds + tens + ones)
