def U_P_Splitter(data: str):
    data = data.strip()
    tmp = data.split()

    if len(tmp) >= 2:
        # Fájlba írás
        with open("szétszedett.txt", "a", encoding="utf-8") as f:  # "a" = append (hozzáfűzés)
            f.write(f"user: {tmp[0]}, password: {tmp[1]}\n")
    else:
        print(f"Hiba: nem megfelelő formátum: {data}")


# Használat:
U_P_Splitter("kis fasz")
U_P_Splitter("alma körte")
U_P_Splitter("hello világ")

# A "szétszedett.txt" fájl tartalma:
# user: kis, password: fasz
# user: alma, password: körte
# user: hello, password: világ

#ellentét, baolvasás

def U_P_SplitterReverse():
    with open("beolvasni.txt", "r", encoding="utf-8") as f:
        data = f.read()

    data = data.strip()
    splitted_to_u_p = {}

    for sor in data.splitlines():
        if sor.strip():
            tmp = sor.split()
            if len(tmp) >= 2:
                splitted_to_u_p[tmp[0]] = tmp[1]

    # Kiírás sorokra bontva
    for user, password in splitted_to_u_p.items():
        print(f"user: {user}, password: {password}")

    return splitted_to_u_p

U_P_SplitterReverse()