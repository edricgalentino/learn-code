# # # konsep input dan memasukkannya kedalam variabel

# # name = input('what is your name?')
# # color = input('what color do you like?')
# # print(name + ' likes' + color)

# # ask_weight_pound = input('what is your weight? (in pound)')
# # weight_in_kilograms = int(ask_weight_pound)/ 2.2
# # print(weight_in_kilograms)
# # weight_in_kilograms

# # # konsep for in range(angka pertama = angka dimulainya hitungan pada pengulangan. angka kedua adalah angka berakhirnya looping - 1. angka ketiga adalah rasio penjumlahan nilai dari looping tersebut, biasanya jika tidak ditulis maka nilai defaultnya = 1.)

# # for i in range(1,5):
# #     print(i)

# # for i in range(8,56,2):
# #     i+=2
# #     if i % 7 == 1:
# #         print(i-1)

# # for i in range(6,23,3):
# #     print(i,end=' ')

# # n=10
# # output=''
# # for i in range(5,n):
# #     output += str(n)
# #     n += 1
# #     print(n) 
# # print(output)

# # siji = [[1,2,3]]
# # loro = [[5,2,2]]
# # telu = [[3,3,3]]
# # res = []
# # for i in range(3):
# #     res.append(siji[0][i] + loro[0][i] + telu[0][i])
# # print(res)



# # ===================================================================
# #                        Recursion

# # def f(n):
# #     if n==0: # base case (untuk mengakhiri fungsi rekursif itu sendiri)
# #         return
# #     print(n)
# #     f(n-1) # recursive case
# # f(5)

# # def mystery(num):
# #     if num == 1:
# #         return 1
# #     return num + mystery(num-1)
# # print(mystery(11))

# # def power(num, n):
# # # base case: num powered by 0 = 1
# #     if n == 0:
# #         return 1
# # # recursion case
# #     return num * power(num, n-1)
# # print(power(5,3))

# # reverse string
# # def reverse(s):
# #     if len(s) == 0:
# #         return s
# #     else:
# #         return reverse(s[1:]) + s[0]
# # print(reverse('perihalmakanlontongdoang'))

# # Faktorial
# # def factorial(e):
# #     if e == 1:  # base case
# #         return e
# #     return e * factorial(e-1) # recursive case
# #     # 7(factorial(6 * factorial (5 * factorial (4 ... ))))
# # print(factorial(7))

# # Fibonacci
# # def fibonacci(n): 
# #     if n == 0 or n == 1:  # base cases 
# #         return 1 
# #     else: 
# #         return fibonacci(n-1) + fibonacci(n-2) # recursive case
# # print(fibonacci(7))


# # def f(n):
# #     if n != 0 :
# #         return 3 * f(n-1)
# #     else:
# #         return 1

# # f(3)

# # x={}
# # x["a"]=[1,2,3]
# # x["b"]=[4,5,6]
# # x["c"]=[7,8,9]

# # y= ["a", "c"]

# # for i in range(len(y)):
# #     print(x[y[i]][1], end="")



# # ===================================================================

# # def fun(x):
# #     x.append(3)

# # y = [1,2]
# # z = fun(y)
# # print(y,z)

# # def m(x):
# #     z = []
# #     for y in x:
# #         if (y and True) or False:
# #             z.append(y)
# #     return len(z)





# # a= 6
# # b= 12

# # while b:
# #     a, b = b, a%b
# # print(a)

# # result = 1
# # lst= [1,3,5,7]
# # # for element in lst:
# # #     result *= element
# # i=0
# # while i < len(lst):
# #     result *= lst[i]
# #     i+=1
# # print(result)

# # def cpe(lst):
# #     result=[]
# #     for i in lst:
# #         count=0
# #         for j in  :
# #             if lst[j] > 0 and i % 2 == 0:
# #                 count += 1
# #         result.append(count)
# #     return result
# # print(cpe([[2,1,0], [4,3,4]]))

# # def total_penjualan(b,d,s):
# #     tb = 3000000*b
# #     td = 10000000*d
# #     ts = 2000000*s
# #     total=tb+ts+td
# #     return total
# # print(total_penjualan(2,2,0))

# # x = [3,2,1]
# # y = x
# # z = y
# # y.append(7)
# # z.remove(1)
# # print(x)

# # def fun(x):
# #     x.append(3)
# # y = [1,2]
# # z = fun(y)
# # print(z)




# # mylist = ['you', 'i', 'we']
# # for word in mylist:
# #     print('...'+'.'*(3-len(word))+word.format(word))

# # word = "pemrograman"
# # word.replace("r", "")
# # print(word)
# # returnnya word awal yaitu 'pemrograman' karena fungsi replace tidak di definisikan dan tidak dijalankan hanya di deklarasikan

# # kata = "terang"
# # kata[0] = "k"
# # if kata[0] == "k":
# #     print("kerang")
# # else:
# #     print("terang")

# # kal ='muhammad atallah azzam taqi'
# # print((kal.split()))

# # def has_duplicate(lst):
# #     new_lst = {}
# #     for elem in lst:
# #         if elem not in new_lst:
# #             new_lst[elem] = 1
# #         else:
# #             return True
# #     return False

# # print(has_duplicate([1,2,4,4,5,5]))

# # hasil = ''
# # for i in range(0,20):
# #     for j in range(i):
# #         hasil += '*'
# #     hasil += '\n'
# # print(hasil)

# # def printSomeWord():
# #     print('Yeay, i\'ve been printed')

# # class runMeToPrint:
# #     printMe = printSomeWord() 

# # i = [1,2,3,4,5]
# # a = min(i)
# # print(a)

# # def cari_fpb(a,b):
# #     if b == 0:
# #         return a;  
# #     else: 
# #         return cari_fpb(b,a%b)
# # print(cari_fpb(12,18))

# # data types

# # qi= '2707070'
# # qs='2'
# # print(str(qi)+qs)


# # q = [1, 'string', 1.2]

# # print('FPB dari 27 dan 54 adalah:',cari_fpb(27,54))
# # print('FPB dari 27 dan 54 adalah:',cari_fpb(54,27))
# # print('FPB dari 7 dan 5 adalah:',cari_fpb(7,5))

# # def most_frequent(string):
# #     char_freq = {}
# #     for char in string:
# #         char = char.strip()
# #         if char == " ":
# #             continue
# #         if char not in char_freq:
# #             char_freq[char] = 1
# #         else:
# #             char_freq[char] += 1

# #     char_freq = sorted(char_freq.items(), key=lambda value:value[1], reverse = True)

# #     string_char = ''
# #     for key, value in char_freq:
# #         string_char += f"{key}:{value}\n"

# #     return string_char

# # with open("words.txt") as file:
# #     string_words = file.read().lower()
# #     print(most_frequent(string_words))


# # file_name = input("Masukkan nama file input : ")
# # print() 

# # # handling when file not found or empty
# # try : 
# #     file = open(file_name, "r")
# #     lines = file.readlines()
# #     if len(lines) == 0:
# #         raise Exception
# # except FileNotFoundError :
# #     print("File input tidak ada :(")
# #     exit()
# # except : 
# #     print("File input ada tapi kosong :(")
# #     exit()

# # full_name = input('masukan nama: ')
# # first_name = full_name.split()[-1]
# # last_name = full_name.split()[0]
# # print(first_name + ' ' + last_name + ' bagus')

# # l = [1,2]
# # l+= [3]
# # print(l)
# # l = l.append(4)
# # print(l)

# # def berstemmer(kalimat):
# #     stem_kal = ''
# #     for word in kalimat.split():
# #         if word[0:3] == "ber":
# #             word = word[3:]
# #         elif word[0:2] == "be":
# #             word = word[2:]
# #         stem_kal += word + ' '
# #     return stem_kal
# # print(berstemmer("bersimpati bersama beruang beringas"))

# # def max_cap(s):
# #     ucode = ''
# #     for i in s:
# #         if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
# #             if i > ucode:
# #                 ucode = i
# #     if ucode != '':
# #         return ucode
# #     return None
# # print(max_cap('mengembaliKkan Nilai V'))


# # for i in range(10,42,3):
# #     i+=3
# #     if i%7==1:
# #         print(i-1)

# # def is_factor(x,y):
# #     if y % x == 0 or x % y == 0:
# #         return True
# #     return False

# # 13,1,6,0,3,1,1,1,0
# # 1000,1000,100,1100,10,1100,1,1101



# # a,b=31,7
# # print(a%b)
# # print(b%a)
# # print((a<b) and (a!=b))
# # print(-15//b)
# # print(-15%b)
# # print(a/4)

# # def replace_with_1(s, c):
# #     result = ''
# #     for x in s:
# #         if x == c:
# #             s[x] += '1'
# #     return result
# # print(replace_with_1('apasaja', 'a'))


# # d1= {'o':1,'tw':2, 'th':3}
# # d2= {'z':4,'y':5, 't':6}
# # dict3 = d1.copy()
# # dict3.update(d2)
# # for k, el in dict3.items():
# #     print(el, end=' ')
# class Book(object): 
#     def __init__(self, title, price):
#         self.__title = title
#         self.__price = price
        
#     def get_title(self):
#         return self.__title # 1 point
        
#     def get_price(self):
#         return self.__price # 1 point


# class Cart(object):
#     def __init__(self):
#         self.__shopping_cart = []
        
#     def add_item(self, item):
#         """ menambahkan sebuah item di posisi akhir list shopping cart """
#         self.__shopping_cart.append(item) # 3 point

#     def total_price(self):
#         """ melakukan loop terhadap shopping cart, dan menghitung total harga """
#         totalPrice = 0
#         for p in range(len(self.__shopping_cart)):
#             totalPrice += p
#         return totalPrice        # 5 point

# if __name__ == '__main__':
        
#     my_cart = Cart()
    
#     my_cart.add_item(Book("Python", 50000))
#     my_cart.add_item(Book("Java", 30000))
#     my_cart.add_item(Book("Data Mining", 45000))
#     my_cart.add_item(Book("Clean Code", 70000))
#     my_cart.add_item(Book("Effective Programming", 70000))
        
#     print("total price = {}".format(my_cart.total_price()))
    





# # def largest(s):
# #     x=s[0]
# #     for c in s:
# #         if x>c:
# #             pass
# #         else:
# #             x=c
# #     return x
# # print(largest('rasazkan'))



# # x,y=-1,1
# # con = 4
# # for i in range(con):
# #     print(x,y)
# #     if x>y:
# #         x,y=y,x
# #     elif x<y:
# #         x+=1
# #         continue
# #     else:
# #         break

# # def mystery(param):
# #     i,j=0,len(param) - 1
# #     while (i != j) and (param[i] == param[j]):
# #         i+=1
# #         j-=1
# #     return i == j
# # print(mystery('kasurnababanrusak'))

















# # file = open('input.txt', 'r')
# # for line in file.readlines()[::-1]:
# #     print(line.strip(r))
# # file.close()

# # alis = [1,2,3]

# # blis = alis
# # clis = [4,5,6]
# # alis = [4,5,6]
# # print(alis,blis,clis)



# # ka = 'phyton'
# # k = ka[3:]
# # print(k)

# # # processing happiness, sadness, and anger
# # happiness = 50
# # sadness = 50
# # anger = 50

# # def smile() :
# #     global happiness
# #     happiness += 9
# #     global sadness
# #     sadness -= 6
# #     validation()

# # def sad() :
# #     global anger
# #     anger -= 8
# #     global sadness
# #     sadness += 10
# #     validation()
   
# # def angry() :
# #     global anger
# #     anger += 13
# #     global happiness
# #     happiness -= 5
# #     validation()
   
# # # validate wether its excessive or too little or not
# # def validation() : 
# #     global anger, happiness, sadness
# #     if anger > 100 : 
# #         anger = 100
# #     elif anger < 0 : 
# #         anger = 0
# #     if happiness > 100 : 
# #         happiness = 100
# #     elif happiness < 0 : 
# #         happiness = 0
# #     if sadness > 100 :
# #         sadness = 100
# #     elif sadness < 0 : 
# #         sadness = 0

# # # processing per line
# # for line in lines : 
# #     words = line.split()

# #     # processing per word
# #     for word in words : 
# #         if (word == "(smile)") :
# #             print("\U0001f603", end=" ")
# #             if line.startswith("Pak Chanek") :
# #                 smile()
# #         elif (word == "(sad)") :
# #             print("\U0001f622", end=" ")
# #             if line.startswith("Pak Chanek") :
# #                 sad()
# #         elif (word == "(angry)") :
# #             print("\U0001f621", end=" ")
# #             if line.startswith("Pak Chanek") :
# #                 angry()
# #         else : 
# #             print(word, end=" ")
# #     print()


# # # printing the result
# # print ("\nMengukur suasana hati....")
# # print ("\n##### Hasil Pengukuran #####")
# # print (f"Happiness = {happiness} | Sadness = {sadness} | Anger = {anger}")
# # print ("##### Kesimpulan #####")

# # # making conslusion
# # if happiness > sadness and happiness > anger : 
# #     kesimpulan = "bahagia"
# # elif sadness > happiness and sadness > anger : 
# #     kesimpulan = "sedih"
# # elif anger > happiness and anger > sadness : 
# #     kesimpulan = "marah"
# # elif happiness == sadness and happiness > anger : 
# #     kesimpulan = "bahagia atau sedih"
# # elif happiness == anger and happiness > sadness :
# #     kesimpulan = "bahagia atau marah" 
# # elif sadness == anger and sadness > happiness : 
# #     kesimpulan = "sedih atau marah" 
# # elif sadness == happiness and sadness == anger : 
# #     print ("Kesimpulan tidak ditemukan.")
# #     exit()

# # print (f"Pak Chanek sedang {kesimpulan}.")



# # ---------------------------------------FILE BARU----------------------------------------


# # for i in range(0,4):
# #     print(i)
# # n=5
# # output=''

# # for i in range(0,n):
# #     output += str(n)
# #     n += 1
# #     print(n)    
# # print(output)

# # a= 6
# # b= 12

# # while b:
# #     a, b = b, a%b
    
# # print(a)

# # result = 1
# # lst= [1,3,5,7]
# # # for element in lst:
# # #     result *= element
# # i=0
# # while i < len(lst):
# #     result *= lst[i]
# #     i+=1
# # print(result)

# # def cpe(lst):
# #     result=[]
# #     for i in lst:
# #         count=0
# #         for j in  :
# #             if lst[j] > 0 and i % 2 == 0:
# #                 count += 1
# #         result.append(count)
# #     return result
# # print(cpe([[2,1,0], [4,3,4]]))

# # def total_penjualan(b,d,s):
# #     tb = 3000000*b
# #     td = 10000000*d
# #     ts = 2000000*s
# #     total=tb+ts+td
# #     return total
# # print(total_penjualan(2,2,0))

# # x = [3,2,1]
# # y = x
# # z = y
# # y.append(7)
# # z.remove(1)
# # print(x)

# # def fun(x):
# #     x.append(3)
# # y = [1,2]
# # z = fun(y)
# # print(z)


# # siji = [[1,2,3]]
# # loro = [[5,2,2]]
# # telu = [[3,3,3]]
# # res = []
# # for i in range(3):
# #     res.append(siji[0][i] + loro[0][i] + telu[0][i])
# # print(res)

# # mylist = ['you', 'i', 'we']
# # for word in mylist:
# #     print('...'+'.'*(3-len(word))+word.format(word))

# # word = "pemrograman"
# # word.replace("r", "")
# # print(word)
# # returnnya word awal yaitu 'pemrograman' karena fungsi replace tidak di definisikan dan tidak dijalankan hanya di deklarasikan

# # kata = "terang"
# # kata[0] = "k"
# # if kata[0] == "k":
# #     print("kerang")
# # else:
# #     print("terang")

# # kal ='muhammad atallah azzam taqi'
# # print((kal.split()))





# # file_name = input("Masukkan nama file input : ")
# # print() 

# # # handling when file not found or empty
# # try : 
# #     file = open(file_name, "r")
# #     lines = file.readlines()
# #     if len(lines) == 0:
# #         raise Exception
# # except FileNotFoundError :
# #     print("File input tidak ada :(")
# #     exit()
# # except : 
# #     print("File input ada tapi kosong :(")
# #     exit()

# # full_name = input('masukan nama: ')
# # first_name = full_name.split()[-1]
# # last_name = full_name.split()[0]
# # print(first_name + ' ' + last_name + ' bagus')

# # l = [1,2]
# # l+= [3]
# # print(l)
# # l = l.append(4)
# # print(l)

# # def berstemmer(kalimat):
# #     stem_kal = ''
# #     for word in kalimat.split():
# #         if word[0:3] == "ber":
# #             word = word[3:]
# #         elif word[0:2] == "be":
# #             word = word[2:]
# #         stem_kal += word + ' '
# #     return stem_kal
# # print(berstemmer("bersimpati bersama beruang beringas"))

# # def max_cap(s):
# #     ucode = ''
# #     for i in s:
# #         if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
# #             if i > ucode:
# #                 ucode = i
# #     if ucode != '':
# #         return ucode
# #     return None
# # print(max_cap('mengembaliKkan Nilai V'))



# # def is_factor(x,y):
# #     if y % x == 0 or x % y == 0:
# #         return True
# #     return False

# # 13,1,6,0,3,1,1,1,0
# # 1000,1000,100,1100,10,1100,1,1101






# # ka = 'phyton'
# # k = ka[3:]
# # print(k)

# # # processing happiness, sadness, and anger
# # happiness = 50
# # sadness = 50
# # anger = 50

# # def smile() :
# #     global happiness
# #     happiness += 9
# #     global sadness
# #     sadness -= 6
# #     validation()

# # def sad() :
# #     global anger
# #     anger -= 8
# #     global sadness
# #     sadness += 10
# #     validation()
   
# # def angry() :
# #     global anger
# #     anger += 13
# #     global happiness
# #     happiness -= 5
# #     validation()
   
# # # validate wether its excessive or too little or not
# # def validation() : 
# #     global anger, happiness, sadness
# #     if anger > 100 : 
# #         anger = 100
# #     elif anger < 0 : 
# #         anger = 0
# #     if happiness > 100 : 
# #         happiness = 100
# #     elif happiness < 0 : 
# #         happiness = 0
# #     if sadness > 100 :
# #         sadness = 100
# #     elif sadness < 0 : 
# #         sadness = 0

# # # processing per line
# # for line in lines : 
# #     words = line.split()

# #     # processing per word
# #     for word in words : 
# #         if (word == "(smile)") :
# #             print("\U0001f603", end=" ")
# #             if line.startswith("Pak Chanek") :
# #                 smile()
# #         elif (word == "(sad)") :
# #             print("\U0001f622", end=" ")
# #             if line.startswith("Pak Chanek") :
# #                 sad()
# #         elif (word == "(angry)") :
# #             print("\U0001f621", end=" ")
# #             if line.startswith("Pak Chanek") :
# #                 angry()
# #         else : 
# #             print(word, end=" ")
# #     print()


# # # printing the result
# # print ("\nMengukur suasana hati....")
# # print ("\n##### Hasil Pengukuran #####")
# # print (f"Happiness = {happiness} | Sadness = {sadness} | Anger = {anger}")
# # print ("##### Kesimpulan #####")

# # # making conslusion
# # if happiness > sadness and happiness > anger : 
# #     kesimpulan = "bahagia"
# # elif sadness > happiness and sadness > anger : 
# #     kesimpulan = "sedih"
# # elif anger > happiness and anger > sadness : 
# #     kesimpulan = "marah"
# # elif happiness == sadness and happiness > anger : 
# #     kesimpulan = "bahagia atau sedih"
# # elif happiness == anger and happiness > sadness :
# #     kesimpulan = "bahagia atau marah" 
# # elif sadness == anger and sadness > happiness : 
# #     kesimpulan = "sedih atau marah" 
# # elif sadness == happiness and sadness == anger : 
# #     print ("Kesimpulan tidak ditemukan.")
# #     exit()

# # print (f"Pak Chanek sedang {kesimpulan}.")


n = int(input('angka'))
d= {}

for i in range(n):
    first,second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])
# class User:
#     def __init__(self, username, password):
#         self.__username = username
#         self.__password = password
#         self.__list_of_product = [] # 1 poin

#     def get_username(self):
#         return self.__username

#     def get_password(self):
#         return self.__password

#     def get_list_of_product(self):
#         return self.__list_of_product
    
#     def beli_product(self, product):
#         self.__list_of_product -= product# 1 poin

#     def print_list_of_product(self):
#         for i in self.__list_of_product : # 1 poin
#             print(i) # 1 poin
# class Product:
#     def __init__(self, name, amount, price):
#         self.__name = name
#         self.__amount = amount
#         self.__price = price

#     def get_name(self):
#         return self.__name

#     def get_amount(self):
#         return self.__amount

#     def get_price(self):
#         return self.__price

#     def __str__(self):
#         return self.__name + " dengan jumlah " + self.__amount + " mempunyai total harga " + (self.__amount * self.__price)
# class Admin(__5__): # 1 poin
#     def __init__(self, username, password):
#         (__6__) # 1 poin

#     def hapus_barang_user(self, user, nama_barang):
#         list_of_product = user.get_list_of_product()
#         (__7__) # implementasi semua algoritma di sini. (4 poin)