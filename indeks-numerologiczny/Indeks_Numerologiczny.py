


def print_hi(name):
    liczba = int(input("Podaj liczbę większą od 0: "))
    if liczba <= 0:
        raise ValueError("Liczba musi być większa od 0!!")
    else:
        bez_zer = 0
        odwrocona = 0
        iloczyn = 10
        krok = 0
        while liczba > 0:

            if liczba % 10 == 0:
                liczba = liczba // 10
                continue
            else:
                odwrocona = odwrocona * 10 + liczba % 10
                liczba = liczba // 10
        while odwrocona > 0:
            bez_zer = bez_zer * 10 + odwrocona % 10
            odwrocona = odwrocona // 10
        print("Po pominięciu zer otrzymaliśmy liczbę:", bez_zer, )
        while iloczyn >= 10:
            krok += 1
            while liczba > 0:

                if liczba % 10 == 0:
                    liczba = liczba //10
                    continue
                else:
                    odwrocona = odwrocona*10 + liczba % 10
                    liczba = liczba // 10

            while odwrocona > 0:
                bez_zer = bez_zer*10 + odwrocona % 10
                odwrocona = odwrocona // 10
            iloczyn = 1


            while bez_zer > 0:
                iloczyn = iloczyn * (bez_zer % 10)
                bez_zer = bez_zer // 10
            liczba = iloczyn



    print("Indeks numerologiczny wynosi: ",iloczyn,)
    print("Liczba kroków, które musieliśmy zrobić wynosi:",krok,)











if __name__ == '__main__':
    print_hi('PyCharm')


