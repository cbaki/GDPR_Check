import re
import math
import requests

with open("D:\\test\\metin.txt", "r") as metin:
    metin = metin.read()

metin=metin.split(" ")
for i in metin:
    print(i)

def epostakontrol(metin):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, metin):
        return True
    else:
        return False

for metin in metin:
    if epostakontrol(metin):
        print("{} E-posta adresi doğru.".format(metin))
    else:
        pass

with open("D:\\test\\metin.txt", "r") as metin:
    telreg = metin.read()

def telefon_no_sorgu(telno):
    pattern = r"(\d{3})-(\d{7})"
    telreg = re.search(pattern, telno)


    if telreg:
        gsm_tel = telreg.groups()[0]
        if gsm_tel.startswith("53"):
            print(telreg.group(),"Turkcell")
        elif gsm_tel.startswith("50") or gsm_tel.startswith("55"):
            print(telreg.group(),"Türk Telekom")
        elif gsm_tel.startswith("54"):
            print(telreg.group(),"Vodafone")
    else:
        pass

baslangic = 0

while baslangic <= len(telreg)-10:
    sayac = 0
    telno = ""
    for idx, x in enumerate(telreg):
        if idx >= baslangic:
            sayac = sayac + 1
            telno = telno + x
        if sayac == 11:
            break
    if telefon_no_sorgu(telno):
        pass
    baslangic = baslangic + 1

with open("D:\\test\\metin.txt", "r") as metin:
    metin = metin.read()

pattern = r"\d"
tcreg = re.findall(pattern, metin)

def tckimlikdogrula(tc):
    x=0
    y=0
    tc_no=str(tc)

    yeni_tc = tc_no[:9]

    tekler = int(tc_no[0]) + int(tc_no[2]) + int(tc_no[4]) + int(tc_no[6]) + int(tc_no[8])
    x = x + (tekler * 7)

    ciftler = int(tc_no[1]) + int(tc_no[3]) + int(tc_no[5]) + int(tc_no[7])
    y = y + ciftler

    toplam3 = int(tc_no[0]) + int(tc_no[1]) + int(tc_no[2]) + int(tc_no[3]) + int(tc_no[4]) + int(tc_no[5]) + int(
        tc_no[6]) + int(tc_no[7]) + int(tc_no[8]) + int(tc_no[9])

    z = x - y
    onuncu = z % 10
    yeni_tc += str(onuncu)

    toplam=0
    for i in yeni_tc:

        toplam += int(i)
    onbir = toplam % 10

    yeni_tc += str(onbir)
    return yeni_tc == tc_no

baslangic = 0

while baslangic <= len(tcreg)-11:
    sayac = 0
    kimlik = ""
    for idx, x in enumerate(tcreg):
        if idx >= baslangic:
            sayac = sayac + 1
            kimlik = kimlik + x
        if sayac == 11:
            break
    if tckimlikdogrula(kimlik):
        print(kimlik,"TC Numarası doğru.")
    baslangic = baslangic + 1

vk_pattern = r"\d"
vkreg = re.findall(vk_pattern, metin)

def mod(sayi, m):
    return sayi % m

def IsTax(metin):
    v1 = mod((int(metin[0]) + 9), 10)
    v2 = mod((int(metin[1]) + 8), 10)
    v3 = mod((int(metin[2]) + 7), 10)
    v4 = mod((int(metin[3]) + 6), 10)
    v5 = mod((int(metin[4]) + 5), 10)
    v6 = mod((int(metin[5]) + 4), 10)
    v7 = mod((int(metin[6]) + 3), 10)
    v8 = mod((int(metin[7]) + 2), 10)
    v9 = mod((int(metin[8]) + 1), 10)
    vLast = int(metin[9])

    v11 = mod((v1 * 512), 9)
    v21 = mod((v2 * 256), 9)
    v31 = mod((v3 * 128), 9)
    v41 = mod((v4 * 64), 9)
    v51 = mod((v5 * 32), 9)
    v61 = mod((v6 * 16), 9)
    v71 = mod((v7 * 8), 9)
    v81 = mod((v8 * 4), 9)
    v91 = mod((v9 * 2), 9)

    if v1 != 0 and v11 == 0: v11 = 9
    if v2 != 0 and v21 == 0: v21 = 9
    if v3 != 0 and v31 == 0: v31 = 9
    if v4 != 0 and v41 == 0: v41 = 9
    if v5 != 0 and v51 == 0: v51 = 9
    if v6 != 0 and v61 == 0: v61 = 9
    if v7 != 0 and v71 == 0: v71 = 9
    if v8 != 0 and v81 == 0: v81 = 9
    if v9 != 0 and v91 == 0: v91 = 9

    toplam = v11 + v21 + v31 + v41 + v51 + v61 + v71 + v81 + v91

    if mod(toplam, 10) == 0:
        toplam = 0
    else:
        toplam = (10 - mod(toplam, 10))

    if toplam == vLast:
        return True
    else:
        return False

baslangic = 0

while baslangic <= len(vkreg)-10:
    sayac = 0
    vkno = ""
    for idx, x in enumerate(vkreg):
        if idx >= baslangic:
            sayac = sayac + 1
            vkno = vkno + x
        if sayac == 11:
            break
    if IsTax(vkno):
        print(vkno,"Vergi Numarası Doğru.")
    else:
        pass
    baslangic = baslangic + 1

kk_reg = re.findall('\d', metin)

for i in range(len(kk_reg)-15):
    rakam = ''.join(kk_reg[i:i+16])
    kontrol_toplami = 0
    for j in range(16):
        if j % 2 == 0:
            carpim = int(rakam[j]) * 2
            if carpim > 9:
                carpim = carpim - 9
            kontrol_toplami += carpim
        else:
            kontrol_toplami += int(rakam[j])
    if kontrol_toplami % 10 == 0:
        print("Geçerli kart numarası: ", rakam)
        bin_numarasi = rakam[:6]
        response = requests.get(f"https://lookup.binlist.net/{bin_numarasi}")
        if response.ok:
            response_json = response.json()
            if 'bank' in response_json:
                print("Kart ait olduğu banka: ", response_json['bank']['name'])
                print("Kart tipi: ", response_json['brand'])
                print("Para Birimi: ", response_json['country']['currency'])
            else:
                print("Kart tipi: ", response_json['scheme'])
    else:
        pass