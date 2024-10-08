first = input('Enter your first name ')
if len(first) < 5:
    surname = input('Enter your surname ')
    full = first.upper() + surname.upper()
    print(full)
else:
    surname = input('Enter your surname ')
    full = first.lower() + surname.upper()
    print(full)