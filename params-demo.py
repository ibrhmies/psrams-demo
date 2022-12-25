#kendisine gönderilen iki sayıdan hangisi büyük bunu yazdıran fonksiyonu bulunuz

def karsilastirma(a,b):
    if a>b:
        print(f"{a} büyüktür {b} sayısından")
    elif b>a:
        print(f"{b} büyüktür {a} sayısından")
    else :
        print("iki sayı eşittir.")

karsilastirma(45,67)

#2->kendisine gönderilen bir string bilgi içinde her karakter kaçar kez tekrarlanmış bulun.

def bilgi(isim):
    return {harf : isim.count(harf) for harf in isim }

sonuc = bilgi("merhaba")

print(sonuc)

#3->kendisine gönderilen renk isimlerinden içinde blue varsa true döndüren fonksiyonu yazınız

def kontrolBlue(*args):
    if "blue" in args:
        return "true"
    return "False"    

sonuc = kontrolBlue("mavi","red")
print(sonuc)