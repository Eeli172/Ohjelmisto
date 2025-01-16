leiviska_float = float(input("Anna leiviskät: "))
naula_float = float(input("Anna naulat: "))
luoti_float = float(input("Anna luodit: "))

gramma_float = ((((leiviska_float*20) + naula_float) * 32) + luoti_float) * 13.3

kg = gramma_float // 1000
g = round(gramma_float - (kg * 1000), 2)


print(f"Massa nykymittojen mukaan on {kg} kg ja {g} g")
