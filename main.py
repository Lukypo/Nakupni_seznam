def add_item(item_list):
    item = input("Zadejte název položky k přidání: ")
    item_list.append(item)
    print(f"Položka {item} byla přidána.")