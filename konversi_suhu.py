print("\n PROGRAM KONVERSI SUHU\n")

#fahrenheit to kelvin
F = float(input("Masukkan Suhu Dalam F: "))
print("Suhu Dalam F adalah : ", F)

Kelvin = (F-32)*5/9+273.15
print("Suhu Dalam Kelvin adalah : ", Kelvin)

#Kelvin to F
print("==== K TO F ====")
K = float(input("Masukkan Suhu dalam Kelvin : "))
print("Suhu Dalam K adalah : ", K)

F = (K-273.15)*9/5+32
print("Suhu Dalam F adalah : ", F)

