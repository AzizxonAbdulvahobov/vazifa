"""1) shunday funksiya yozingki, u ikkita parametreni qabul qilsin. birinchi parametredagi 
barcha sozlar ikkinchi parametrda bolishi kerak. 2) shunday funksiya yozingki u bittra parametrani str 
typda qabul qilsin va osha sozni ichidagi unli harflar sonini qaytarsin 3) shunday funksiya yozingki u raqamlarni
qabul qilsin va 0llar sonini qaytarsin 4) shunday funksiya yozingki u ikkita parametr qabul qilsin va birinchi
parametralarni ichidagi barcha unli harflar ikkinchisida mavjudligini tekshiring 5) strni ichidagi barcha 
sozlarni sonini qaytaring (split methhodidan foydalanmang) barcha natijalar githubga yuklanib reponi linkini
yuboring"""
# 1
# parametr1 = "Assalomu alaykum"
# parametr2 = "Assalomu alaykum"
# def chek(parametr1,parametr2):
#     parametr1 = parametr1.split()
#     parametr2 = parametr2.split()
#     return parametr1==parametr2
# print(chek(parametr1,parametr2))

# 2

# def check_unli(parametr):
#     count = 0
#     unli_harflar = 'aeiouAEIOU'
    
#     for tekshir in parametr:
#         if tekshir in unli_harflar:
#             count += 1
#     return count

# print(check_unli('Salom dunyo'))

# 3
# def count_zero(number):
#     return number.count('0')
# number = str(20080829)
# print(f"Nollar soni:{count_zero(number)}")

# 4
# def tekshir_mavjudligi(matn1, matn2):
#     unli_harflar = "aeiouAEIOU"
#     unli_harf1 = ''
#     unli_harf2 = ''
    
#     for matn in matn1:
#         if matn in unli_harflar:
#             unli_harf1 += matn
    
#     for matn in matn2:
#         if matn in unli_harflar:
#             unli_harf2 += matn

#     return unli_harf1 == unli_harf2

# print(tekshir_mavjudligi('Azizxon', 'Azizxon'))

# 5
def soz_soni(matn):
    count = 1 
    for soz in matn:
        if soz.isspace():
            count += 1
    return count
matn = "I am Azizxon Abdulvahobov"
print(soz_soni(matn))