#-----------VERİ TİPLERİ-------------#
#--String (metin)
str = 'Enes',"Enes" #Str veri tipi metinsel vb. ifadeler için kullanırız

#--Numarik (sayısal)
x = 20 
y = 21,2 #x = int, y = float, z = double ve w = coplex sayısal ifadeler için kullanırız
z = 22,3
w = 57j

#--Dizi Sequence (sıralama)  
#*list
dersler = ["Matematik","Fen","Sosyal"] #listeler yapmamıza listeler halinde işlemler yapmamıza olanak sağlar

#*Tuple
dersler = ("Matematik","Fen","Kimya") #listeler yapmamıza olanak sağlar ama parantez içindeki değerleri değiştiremeyiz

#*Range
i = 1
for i in range(10): 
    print(i) # Girilen değerler arasında sayısal bir dizin oluşturur ve çıktı verir

#--Mapping (haritalama)
dictname = {}
dictname ['isim'] = "Enes" #veriyi anahtarlayarak tutar anahtarladığı verinin karşısına gelen veriyi tutar

#--Set veri
#*Set 
ornekSet = {"elma", "muz", "kiraz"}
print(ornekSet)# #rasgele sıralanmış diziler oluşturmamızı sağlar

#*Frozenset(Kısıtlanmış Küme)
kisitli_kume = frozenset(["Python",3.14,5,'A'])
print(kisitli_kume)
frozenset({5, 3.14, 'Python', 'A'})#Değişmez bir set oluşturmak için kullanılır sadece okuma amaçlı

#--Bool
print(3>2) #Doğru yanlış koşul ifadeleri için kullanırız

#----------------------------------------------------------------#

#2 - Kodlama.io sitesinde değişken olarak düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

str = "Kodlama.io daki tüm metinler str"
bool = "butonlara basıldığında dönen değer"
int = "dersi tamamlama yüzdesindeki sayısal değerler"

#----------------------------------------------------------------#

#3 - Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

username = "Enes"
password = "asd123"

if username == "Enes" and password == "asd123":
    print("Kullanıcı adı ve şifre doğru")
else:
    print("Girdiğiniz bilgiler yanlış")