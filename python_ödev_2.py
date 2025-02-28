## 1. Asal sayı kontrolü
def asal_mi(değer):
    if değer <=1:
        return print({değer},"asal sayı değildir.")
    elif değer == 2:
        return print({değer},"asal sayıdır.")
    elif değer > 2:
        for i in range(2,değer):
            if değer % i == 0:
                return print({değer},"asal sayı değildir.")
    else:
        return print({değer},"asal sayıdır.")
            
asal_mi(7)
asal_mi(10)
asal_mi(2)
asal_mi(1)
asal_mi(-3)

## 2. Basit Hesap Makinesi
def hesap_makinesi(sayi1, sayi2, işlem):
    if işlem == "+":
        print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}") 
    elif işlem == "-":
        print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
    elif işlem == "*":
        print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
    elif işlem == "/":
        if sayi2 == 0:
            print("Bölme işlemi için ikinci sayı 0 olamaz!")
        else:
            print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")
    else:
        print("Geçersiz işlem türü!")
    
hesap_makinesi(5, 3, '+')  
hesap_makinesi(10, 2, '/') 
hesap_makinesi(4, 0, '/')  
hesap_makinesi(6, 2, '%')   



