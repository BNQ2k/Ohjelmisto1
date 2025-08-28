yritykset = 0
maksimi_yrit = 5


while yritykset < maksimi_yrit:
    tunnus = input("Anna tunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    else:
        yritykset += 1
        print("Pääsy evätty")
if yritykset == maksimi_yrit:
    print("Liian monta virheellistä yritystä.")