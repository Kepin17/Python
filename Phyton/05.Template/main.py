# Operasi Aritmatika

a = 11
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi kurang -
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi kali *
hasil = a * b
print(a,'.',b,'=',hasil)

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# operasi eksponen (Pangkat) **
hasil = a ** b
print(a,'pangkat',b,'=',hasil)


# operasi mpdulus (sisa pembagian) %
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

# prioritas operasi, operational precendence 

'''
Prioritas list : 
1) () 
2) eksponen 
3) perkalian
4) tambah kurang
'''
x = 3
y = 2 
z = 4

hasil = x ** y * z + x / y - y % z // x 
print(x ,'**', y ,'*', z ,'+' ,x, '/' ,y ,'-' ,y, '%' , z ,'//', x,'=',hasil )


hasil = x + y * z

print(x, '+' , y , '*' , z, '=', hasil)

# Kurung Menyerobot antrian

hasil =( x + y ) * z

print('(',x, '+' , y,')' , '*' , z, '=', hasil)