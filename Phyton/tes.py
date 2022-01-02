# def f(n):
#     if n != 0 :
#         return 3 * f(n-1)
#     else:
#         return 1

# print(f(3))

# x={}
# x["a"]=[1,2,3]
# x["b"]=[4,5,6]
# x["c"]=[7,8,9]

# y= ["a", "c"]

# for i in range(len(y)):
#     print(x[y[i]][1], end="")


# yori = {1:2, 1.0:3, True:4}
# hana = set("Tralalalili") | {'parapap'} ^ {True,False,False,0.0}
# dango = 2*yori[1]
# yori[True]=len(hana)/2
# dango-= yori[True] + yori[1]
# print(dango)

# def f(n):
#     if _jawab_ >=4 :
#         return 0 
#     else:
#         return n + f(n-2)

# print(f(5))

# class A:
#     def __init__(self):
#         print ("A")
# class B:
#     def __init__(self):
#         print ("B")
# class C(A):
#     def __init__(self):
#         super().__init__()
#         print ("C")
# class D(C,B):
#     def __init__(self):
#         super().__init__()
#         print ("D")

# obj_d =D()

# def f(a,b):
#     if a.split()[0][0] == a.split()[0][1] and b.split()[0][0] == b.split()[0][1]:
#         if a.split()[0][1] != a.split()[0][2] and b.split()[0][1] != b.split()[0][2]:
#             print("False")
#     elif a.split()[0][1] == a.split()[0][2] and b.split()[0][1] == b.split()[0][2]:
#             print("False")
#     else:    
#         print("True")

# f("abe","bed")

                    # 8
# 286
# x = 8
# def A(x, y):
#     return x + y
# def B(x):
#     return x * 2

# def C(y):
#     global x
#     x += 5
#     return x * y
# a = A(x, 3)
# b = B(a)
# x = C(b)
# print(x)


                    # 9
# MENJUMLAHKAN HASIL BAGI TERDEKAT DAN SISA BAGI
# def abc(num):
#   if num < 10:
#     return num
#   else:
#     return abc(num%10 + abc(num//10)) 

# def main():
#   n = 799682
#   print(abc(n))

# if __name__ == ‘__main__’:
#   main()



                    # 11
# MENGEPRINT NILAI A SEBANYAK B KALI
# def f(a,b):
#     if a-1 ==  0:
#         print(b)
#     else:
#         print(b)
#         return f(a-1,b)
# f(1,1)




                    #14
# ERROR KETIKA N BILANGAN >998 DAN N < 0
# def mystery(N):
#     if N == 0:
#         return 0;
#     else:
#         return N + mystery(N-1);
# mystery(998)




# lst_barang = [['sukri', 1000], ['migemes', 2500], ['bistrong', 8000]]

# harga = lst_barang.__dict__

# for i in lst_barang:
#     harga[i[0]] = i[1]

# nama_barang = input()
# if nama_barang in harga:
#     print(...) # 2, cetak harga sesuai nama_barang


                    # 16
# MENGURUTKAN ANGKA TERKECIL KE TERBESAR SEBANYAK N KALI (TIDAK HAURS SEMUA TERURUT)
# def mystery(n, A):
#     if n == 1:
#         return A
#     for i in range(n - 1):
#         if A[i] > A[i + 1]:
#             A[i], A[i + 1] = A[i + 1], A[i]
#         print(A)
#     return mystery(n - 1, A)
# mystery(7, [16,62,100,31,1,34,77,54,29])


                    # 19
# MENGEPRINT NILAI 2 NILAI TERBESAR KE LAYAR
# def mystery(a):
#     if (len(a) < 2):
#         return "-_-"
#     if(len(a) == 2):
#         return a
#     else:
#         if(a[0] + a[1] > a[1] + a[2]):
#             temp = a[0]
#             a[0] = a[2]
#             a[2] = temp
#         if(a[1] > a[2]):
#             a[1], a[2] = a[2], a[1]
#         return mystery(a[1:])
# print(mystery([24,5,10,11,19,6,7,1,10]))


                    #18 
# MENGEPRINT NILAI a GLOBAL KARNA FUNCTION TDK MERETURN NILAI APAPUN
# a = [1,2]
# def h(b):
#     b = [3,4]
# h(a)
# print(a)


                # 3
# class A:
#   a = 0
# a1 = A()
# a2 = A()
# a3 = A()

# a = 0 DIUBAH DIBAWAH INI JADI a = 1 (KHUSUS a1)
# a1.a = 1

# a = 0 DIUBAH DIBAWAH INI JADI a = 2 (UNTUK SEMUA A SELAIN a1)
# A.a = 2

# a1.a = a1.a + a2.a
# print(a1.a)
# print(a2.a)
# print(a3.a)
# 3,2,2


                    # 2
# MENJUMLAHKAN KATA DALAM Y YANG SAMA PERSIS DENGAN x
# def f(x,y):
#   counter = 0
#   for a in y:
#     if a == x:
#       counter += 1
#   return counter
# print(f("makan",["menggunakan", "makan", 'makan']))


                    # 1
# y = 2
# def a(x):
#   global y
#   y = y ** x
# def b(lst):
#   for i in range (len(lst)):
#     lst[i] = y ** lst[i]
# def c(lst):
#   for val in lst:
#     val *= y
# x1 = 2
# a(x1)
# print(y)     # output?
# lst1 = [1,2,0]
# b(lst1)
# print(lst1)  # output?
# lst2 = [1,2,0]
# c(lst2)
# print(lst2)  # output?


                    # 10
# MENGEMBALIKAN y SBG DICT r DGN KEY SBG BILANGAN ASLI y DAN VALUE SEBAGAI BILANGAN YANG TELAH DIPANGKATKAN OLEH x. DAN MENJUMLAHKAN VALUENYA DI KEY "SUM"
def dctSumPower(x,*y):
    r = dict([])
    for i in range(len(y)):
        r[y[i]] = y[i] ** x
    r['sum'] = 0
    for s in range(1,len(r)):
        r['sum'] += r[s]
    return r
print(dctSumPower(3,1,2,3,4)) 

# class Gadget ( object ):
#     def __init__ ( self , merek , tipe ):
#         self . merek = merek
#         self . tipe = tipe
#     def __str__ ( self ):
#         return 'Gadget {} dengan tipe {} '. format ( self . merek , self . tipe )
# class Handphone ( Gadget ):
#     def __init__ ( self , merek , tipe , os ):
#         super (). __init__ ( merek , tipe )
#         self . os = os
#     def __str__ ( self ):
#         return super (). __str__ () + \
#         ': Handphone {} dengan os {} '. format ( self . merek , self . os )
# class Tablet ( Gadget ):
#     def __init__ ( self , merek , tipe , ukuran ):
#         super (). __init__ ( merek , tipe )
#         self . ukuran = ukuran
#     def __str__ ( self ):
#         return 'Tablet berukuran {} inch '. format ( self . ukuran )
# tb = Tablet ( " Super " , " 3 " , " 12 " )
# print ( tb )
# hp = Handphone ( " Space " , " 2 " , " Door " )
# print ( hp )

# class Hero:

#     jml_hero = 0

#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#     def siapa(self):
#         print("namaku adalah " + self.name)

# hero1 = Hero(input("nama", "darah"))
# print(hero1.di)

# import tkinter

# main_window = tkinter.Tk()

# print(main_window)

# a = {}
# print(type(a))
# mhs = {"nama":'a'}
# print(mhs["nama"])
# print(mhs.get('nama'))

# from tkinter import*

# root = Tk()

# class GUI(Canvas):
#     '''inherits Canvas class (all Canvas methodes, attributes will be accessible)
#        You can add your customized methods here.
#     '''
#     def __init__(self,master,*args,**kwargs):
#         Canvas.__init__(self, master=master, *args, **kwargs)

# polygon = GUI(root)
# polygon.create_polygon([150,75,225,0,300,7],     outline='gray', 
#             fill='gray', width=2)

# polygon.pack()
# root.mainloop()

a = {}
print(type(a))