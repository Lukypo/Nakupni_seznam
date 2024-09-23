def add_item(item_list: list) -> None:
    item: str = input("Zadejte název položky k přidání: ")
    item_list.append(item)
    print(f"Položka {item} byla přidána.")

def remove_item(item_list: list) -> None:
    item: str = input("Zadejte název položky k odebrání: ")
    if item in item_list:
        item_list.remove(item)
        print(f"Položka {item} byla odebrána.")
    else:
        print(f"Položka není v seznamu")


items: list = []
add_item(items)
add_item(items)
remove_item(items)