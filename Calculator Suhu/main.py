# Suhu Celcius

C = float(input('\nMasukan suhu yang ingin kamu ubah dalam Celcius : '))
print ('Suhu yang telah kamu masukan adalah ', C ,'°C')

R = ( 4 / 5 ) * C 
print ('Suhu yang diubah menjadi R menjadi ',R,'°R')

F = ( 9 / 5 ) * C + 32 
print ('Suhu yang diubah menjadi F menjadi ',F,'°F')

K = ( C + 273 ) 
print( 'Suhu yang diubah menjadi K menjadi ',K,'°K')

print('')
print('==============================================================')

# Suhu Reamur

Re = float(input('\nMasuka Suhu yang ingin kamu ubah dalam Reamur :\n'))
print ('Suhu yang Telah kamu masukan adalah ', Re,'°R')

Ce = ( 5 / 4 ) * Re 
print ('Suhu yang diubah menjadi C menjadi ',Ce,'°R') 

Fa = ( 9 / 4 ) * Re + 32 
print ('Suhu yang diubah menjadi F menjadi ',Fa,'°F')

Ke = ( 5 / 4 ) * Re + 273 
print ('Suhu yang diubah menjadi K menjadi ',Ke,'°K') 


print('')
print('==============================================================')

# Suhu Fahrenhait 

fah = float(input('\nMasuka Suhu yang ingin kamu ubah dalam Fahrenhait :\n'))

Cel = (5 / 9) * fah - 32 
print ('Suhu yang diubah menjadi C menjadi ',Cel,'°C') 

Rea = (4 / 9) * fah - 32 
print ('Suhu yang diubah menjadi R menjadi ',Ke,'°R')

Kel = 5 / 9 * (fah - 32) + 273 
print ('Suhu yang diubah menjadi K menjadi ',Kel,'°K') 


print('')
print('==============================================================')

# Suhu Kelvin 

Kelv = float(input('\nMasuka Suhu yang ingin kamu ubah dalam Kelvin :\n'))

Cels = Kelv - 273 
print ('Suhu yang diubah menjadi C menjadi ',Cels,'°C') 

Ream =  4 / 5 * ( Kelv - 32 )
print ('Suhu yang diubah menjadi R menjadi ',Ream,'°R') 

Fahr = (Kelv - 273.15 ) * 9/5 + 32
print ('Suhu yang diubah menjadi F menjadi ',Fahr,'°F') 


