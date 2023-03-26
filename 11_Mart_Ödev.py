#1-Aldığı isim soy isim ile listeye öğrenci ekleyen
print("**************************************************")
ögrenci = ["Enes Polat","Adil Polat"]
isimsoyisim = input("İsim ve soyisim giriniz: ")
ögrenci.append(isimsoyisim)
print(ögrenci)
#2-Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
print("**************************************************")
isimsoyisim = input("İsim ve soyisim giriniz: ")
if isimsoyisim and ögrenci:
    ögrenci.remove(isimsoyisim)
    print(ögrenci)
else:
    print("Listede yok")
print("**************************************************")
#3-Listeye birden fazla öğrenci eklemeyi mümkün kılan
ögrenci = ["Enes Polat","Adil Polat"]

sayiGir = int(input("Sayi Giriniz: "))

for i in range(sayiGir):
    isimsoyisim = str(input("İsim ve soyisim giriniz: "))
    ögrenci.append(isimsoyisim)
    print(ögrenci)
#4-Listedeki tüm öğrencileri tek tek ekrana yazdıran
print("**************************************************")
for i in ögrenci:
   print(i)
#5-Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan python kodu
print("**************************************************")



print("**************************************************")
#6-Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
sayi = int(input("Sayi gir: "))

isimsoyisim = str(input("İsim giriniz: "))

for i in range(sayi):
    ögrenci.remove(isimsoyisim)

print(ögrenci)

print("**************************************************")

