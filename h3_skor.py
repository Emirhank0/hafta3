import random
gs=random.randint((0,10))
print(gs)
fb=random.randint((0,10))
print(fb)

if gs>fb:
    print("GS FB'den dahaçok gol atmıştır.")

elif fb>gs:
    print("FB GS'den daha fazla gol atmıştır.")

else:
    print("İkisinin golü eşit")
