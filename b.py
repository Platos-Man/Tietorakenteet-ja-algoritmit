# tee ratkaisu tänne
def eka_sana(lause):
    sana1 = ""
    i = 0
    while i < len(lause):
        if lause[i] == " ":
            return sana1
        sana1 += lause[i]
        i += 1


def toka_sana(lause):
    sana = ""
    i = 0
    toka = False
    while i < len(lause):
        if toka and lause[i] == " ":
            break
        elif toka:
            sana += lause[i]
        elif lause[i] == " ":
            toka = True
        i += 1
    return sana


def vika_sana(lause):
    vika = ""
    i = -1
    while i > -len(lause):
        if lause[i] == " ":
            lause = lause[i + 1 :]
            return lause
        vika += lause[i]
        i -= 1


def eka_sana2(lause):
    return lause.split(" ")[0]


def toka_sana2(lause):
    return lause.split(" ")[1]


def vika_sana2(lause):
    return lause.split(" ")[-1]


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    list = [
        "olipa kerran ohjelmointi",
        "sen pituinen se",
        "Lorem ipsum dolor sit amet consectetur adipiscing elit",
        "eka toka",
        "Tee ohjelma joka kysyy käyttäjältä merkkijonoa ja yksittäistä merkkia",
    ]
    for lause in list:
        print(eka_sana(lause), end=" ")
        print(toka_sana(lause), end=" ")
        print(vika_sana(lause))
        print(eka_sana2(lause), end=" ")
        print(toka_sana2(lause), end=" ")
        print(vika_sana2(lause))
    # lause = "ensimmäinen toka vika"
    # print(eka_sana(lause))
    # print(toka_sana(lause))
    # print(vika_sana(lause))
