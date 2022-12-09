for year in [2019, 2020, 2021]:
    numeric = 0
    alphanumeric = 0
    full = 0

    file = open(f"{year}.txt", "r")
    list_of_password = file.readlines()
    list_of_proc_password = []
    for password in list_of_password:
        proper_password = password.rstrip("\n")
        if (len(proper_password) != 0):
            list_of_proc_password.append(proper_password)

    for password in list_of_proc_password:
        if password.isdigit():
            numeric += 1
        elif password.isalnum():
            alphanumeric += 1
        else:
            full += 1

    print(f"Year {year}")
    print(f"Numeric : {numeric}")
    print(f"Alphanumeric : {alphanumeric}")
    print(f"Full ASCII : {full}")
    print("\n")

    file.close()
