# Bölüm 1: Kullanıcının girdiği metni dosyaya yazma ve okuma
print("Bölüm 1: Tek metin yazma ve okuma")
metin = input("Bir metin girin: ")

# Dosyaya yazma
with open("metin.txt", "w", encoding="utf-8") as dosya:
    dosya.write(metin)

# Dosyayı okuma ve ekrana yazdırma
with open("metin.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print("Dosyadan okunan içerik:", icerik)

print("\n" + "-"*50 + "\n")

# Bölüm 2 ve 3: 5 satır veri alma, kaydetme ve satır satır okuma
print("Bölüm 2: 5 satır veri kaydetme ve okuma")
# Kullanıcıdan 5 satır veri al
satirlar = []
for i in range(5):
    satir = input(f"{i+1}. satırı girin: ")
    satirlar.append(satir + "\n")

# Dosyaya yazma (append yerine "w" kullanıyoruz çünkü yeni bir dosya olacak)
with open("bes_satir.txt", "w", encoding="utf-8") as dosya:
    dosya.writelines(satirlar)

# Dosyayı satır satır okuma ve ekrana yazdırma
print("\nDosyadan satır satır okunan içerik:")
with open("bes_satir.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        print(satir.strip())