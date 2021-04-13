from aplikacja import Application

if __name__ == '__main__':
    aplikacja = Application()
    aplikacja.wypisz()

    while True:
        print('---' * 30)
        print('co chrzesz zrobić? [w-wypisz, d-dodaj, q-wyjdz, u-remove, z-oznacz jako zrobione]: ')
        polecenie = input('Napisz "w", "d" "z" "u" lub "q": ')
        if polecenie == 'w':
            aplikacja.wypisz()
        elif polecenie == 'd':
            aplikacja.dodaj()
        elif polecenie == 'z':
            aplikacja.oznacz_jako_zrobione()
        elif polecenie == 'u':
            aplikacja.usun()
        elif polecenie == 'q':
            quit()
        else:
            print('nie rozumiem')