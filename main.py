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


def main() -> None:
    items: list = []
    while True:
        print(f"Přidat položku - 1 | Odebrat položku - 2 | Konec - 3")
        command: int = int(input("Zadejte číslo příkazu: "))
        if command == 1:
            add_item(items)
        elif command == 2:
            remove_item(items)
        elif command == 3:
            print("Program byl ukončen.")
            break
        else:
            print("Neplatný příkaz.")


if __name__ == "__main__":
    main()
