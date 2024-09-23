def pridat_polozku(seznam):
    polozka = input("Zadejte název položky k přidání: ")
    seznam.append(polozka)
    print(f"Položka {polozka} byla přidána.")