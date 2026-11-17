from databases import db, cursor

def kitoblarni_korish():
    cursor.execute("SELECT * FROM kitoblar")
    kitoblar = cursor.fetchall()

    if len(kitoblar) == 0:
        print("Kitoblar mavjud emas!")
    else:
        for kitob in kitoblar:
            print(kitob)


def kitob_qoshish():
    nomi = input("Kitob nomi: ")
    muallif = input("Muallif: ")
    kategoriya = input("Kategoriya: ")
    narx = int(input("Narx: "))
    sana = input("Sana: ")

    cursor.execute("""
        INSERT INTO kitoblar (nomi, muallif, kategoriya, narx, sana)
        VALUES (?, ?, ?, ?, ?)
    """, (nomi, muallif, kategoriya, narx, sana))

    db.commit()
    print("Kitob qo'shildi!")

def kitob_malumotini_yangilash():
    id = int(input("Kitob ID sini kiriting: "))

    cursor.execute("SELECT * FROM kitoblar WHERE id = ?", (id,))
    kitob = cursor.fetchone()

    if kitob:
        print("Kitob topildi!")

        nomi = input("Yangi nom: ")
        muallif = input("Yangi muallif: ")
        kategoriya = input("Yangi kategoriya: ")
        narx = int(input("Yangi narx: "))
        sana = input("Yangi sana: ")

        cursor.execute("""
            UPDATE kitoblar
            SET nomi=?, muallif=?, kategoriya=?, narx=?, sana=?
            WHERE id=?
        """, (nomi, muallif, kategoriya, narx, sana, id))

        db.commit()
        print("Ma'lumot yangilandi!")

    else:
        print("Bunday ID li kitob topilmadi!")


def kitob_ochirish():
    id = int(input("O'chiriladigan kitob ID sini kiriting: "))

    cursor.execute("SELECT * FROM kitoblar WHERE id = ?", (id,))
    kitob = cursor.fetchone()

    if kitob:
        cursor.execute("DELETE FROM kitoblar WHERE id = ?", (id,))
        db.commit()
        print("Kitob muvaffaqiyatli o'chirildi!")
    else:
        print("Bunday ID li kitob topilmadi!")