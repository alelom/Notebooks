n = float(input())
if int(n) != 0:
    fractional = n % int(n)
else: 
    fractional = n
rounded_fractional = round(fractional, 3)
print (rounded_fractional)