# Latihan Konversi Satuan Temperature

#  Program Konversi Celcius Ke Satuan Lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('masukan suhu dalam celcius: '))
print("Suhu yang kamu masukan adalah",celcius ,"°C")

# Reamur
# 4/5 * C

reamur =  (4/5) * celcius
print("Suhu dalam Reamur adalah: ",reamur,"°R")

# Fahrenheit
# 9/5 * C + 32

fahrenheit = (9/5) * celcius + 32
print("Suhu dalam Fahrenheit adalah: ",fahrenheit,"°F")

# Kelvin
# C + 273

kelvin = celcius + 273 
print("Suhu dalam Kelvin adalah: ",kelvin,"°K")
