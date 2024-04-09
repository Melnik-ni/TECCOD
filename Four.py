def sort_strings(strings):
    strings.sort(key=len)  # Сортировка по возрастанию
    print("Сортировка по возрастанию: ", strings)
    strings.sort(key=len, reverse=True)  # Сортировка по убыванию
    print("Сортировка по убыванию: ", strings)

strings = ["апельсин", "лимон", "ананас", "гранат", "персик", "22"]
sort_strings(strings)