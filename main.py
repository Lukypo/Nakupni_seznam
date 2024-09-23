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
        print(f"Položka {item} není v seznamu")


def view_items(item_list: list) -> None:
    print("Seznam položek:")
    for item in item_list:
        print(item)


def sort_items_alphabetically(item_list: list) -> None:
    item_list.sort()
    print("Seznam byl seřazen abecedně.")
    view_items(item_list)


def get_item_count(item_list: list) -> None:
    print(f"Počet položek v seznamu: {len(item_list)}")


def main() -> None:
    items: list = []
    while True:
        print(f"Přidat položku - 1 | Odebrat položku - 2 | Zobrazit položky - 3 | Seřadit položky - 4 | Počet položek - 5 | Konec - 6")
        user_input: str = input("Zadejte číslo příkazu: ")
        if not user_input.isdigit():
            print("Neplatný příkaz")
            continue

        command: int = int(user_input)
        if command == 1:
            add_item(items)
        elif command == 2:
            remove_item(items)
        elif command == 3:
            view_items(items)
        elif command == 4:
            sort_items_alphabetically(items)
        elif command == 5:
            get_item_count(items)
        elif command == 6:
            break
        else:
            print("Neplatný příkaz")


if __name__ == "__main__":
    main()
