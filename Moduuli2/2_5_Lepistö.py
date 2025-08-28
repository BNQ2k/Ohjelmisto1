leiviskä = float(input("Syötä leiviskät: "))
naulat = float(input("Syötä naulat: "))
luodit = float(input("Syötä luodit: "))
leiviskäg = leiviskä * 20
naulatg = naulat * 32
luoditg = luodit * 13.3

massag = leiviskä * leiviskäg + naulat * naulatg + luodit * luoditg

kg = int(massag // 1000)
g = massag % 1000

print("Massa nykymittojen mukaan:")
print(f"{kg} kilogrammaa ja {g:.2f} grammaa.")