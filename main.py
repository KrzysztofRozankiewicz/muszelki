import sys

def print_menu():
    print(5 * "\n")
    print(25 * "-", "ANALIZATOR TEKSTÓW", 25 * "-")
    print("1. Pobierz plik z internetu ")
    print("2. Zlicz liczbę liter w pobranym pliku ")
    print("3. Zlicz liczbę wyrazów w pliku ")
    print("4. Zlicz liczbę znaków interpunkcyjnych w pliku ")        
    print("5. Zlicz liczbę zdań w pliku ")
    print("6. Wygeneruj raport o użyciu liter (A-Z) ")
    print("7. Zapisz statystyki z punktów 2-5 do pliku statystyki.txt ")
    print("8. Wyjście z programu ")
    print(70 * "-")


while True:
	print_menu()
	
	
	#get user input and convert to int
	while True:
		user_input = input ("Dokonaj wyboru [1-8]: ")
		try:
			choice = int(user_input)
			if choice>=1 and choice <=8:
				break
		except ValueError:
			choice = -1

		print("!! DOKONANO NIEPRAWIDŁOWEGO WYBORU !!\n")

	#print(choice)

	if choice == 1:
		print(" Pobieranie plik z internetu...")
	elif choice == 2:
		print(" Zliczanie liczby liter w pobranym pliku...")
	elif choice == 3:
		print(" Zliczanie liczby wyrazów w pliku...")
	elif choice == 4:
		print("	Zliczanie znaków interpunkcyjnych w pliku...")
	elif choice == 5:
		print(" Zliczanie liczby zdań w pliku...")
	elif choice == 6:
		print(" Generowanie raportu użycia liter (A-Z)")
	elif choice == 7:
		print(" Zapisywanie statystyki z punktów 2-5 do pliku statystyki.txt...")
	elif choice == 8:
		sys.exit()
	else:
		print("!! DOKONANO NIEPRAWIDŁOWEGO WYBORU !!\n")
