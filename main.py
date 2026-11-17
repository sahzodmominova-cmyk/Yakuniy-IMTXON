from funksiyalar import *

while True:
    print("===== KITOBLAR BAZASI =====")
    print("1. Kitoblarni ko'rish")
    print("2. Kitob qo'shish")
    print("3. Kitob ma'lumotini yangilash")
    print("4. Kitob o'chirish")
    print("0. Dasturdan chiqish")

    tanlov = input("Tanlovni kiriting: ")

    if tanlov == "1":
        kitoblarni_korish()

    elif tanlov == "2":
        kitob_qoshish()

    elif tanlov == "3":
        kitob_malumotini_yangilash()

    elif tanlov == "4":
        kitob_ochirish()

    elif tanlov == "0":
        print("Dastur tugadi!")
        break

    else:
        print("Noto'g'ri tanlov!")