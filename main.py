import sys

from urllib.request import urlopen


url = urlopen("https://s3.zylowski.net/public/input/3.txt")

filename = "3.txt"

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


def count_letters():
	try:
		with open(filename, 'r') as myfile:
			data = myfile.read()
		
		letters = 0
		for x in data:
			if x.isalpha():
				letters+=1

		print(" Ilość liter w pliku ",filename," to ", str(letters))
	except FileNotFoundError:
		print(" ** Brak pliku ",filename, " **")
	except Exception:
		print(" ** Nie mogę otworzyć pliku ",filename)
		
def count_words():
	try:
		with open(filename, 'r') as myfile:
			data = myfile.read()
		
		words = 0
		words = len(data.split())
		print("Ilość wyrazów w pliku " ,filename, " to ", str(words))
	except FileNotFoundError:
		print(" ** Nie mogę znaleść pliku ", filename)
	except Exception:
		print(" ** Nie mogę otworzyć pliku ",filename)

def count_punctation():
        try:
                with open(filename, 'r') as myfile:
                        data = myfile.read()
                        
                punctation = 0
                punctation = data.count(".") + data.count("!") + data.count("?") + data.count(",") + data.count("'")
                print("Ilość znaków interpunkcyjnych w pliku " ,filename, " to ", str(punctation))
        except FileNotFoundError:
                print(" ** Nie mogę znaleść pliku ", filename)
        except Exception:
                print(" ** Nie mogę otworzyć pliku ",filename)

def count_sentences():
        try:
                with open(filename, 'r') as myfile:
                        data = myfile.read()
                        
                sentences = 0
                sentences = data.count(".") + data.count("!") + data.count("?")
                print("Ilość zdań w pliku " ,filename, " to ", str(sentences))
        except FileNotFoundError:
                print(" ** Nie mogę znaleść pliku ", filename)
        except Exception:
                print(" ** Nie mogę otworzyć pliku ",filename) 


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
		count_letters()
	elif choice == 3:
		print(" Zliczanie liczby wyrazów w pliku...")
		count_words()
	elif choice == 4:
		print("	Zliczanie znaków interpunkcyjnych w pliku...")
		count_punctation()
	elif choice == 5:
		print(" Zliczanie liczby zdań w pliku...")
		count_sentences()
	elif choice == 6:
		print(" Generowanie raportu użycia liter (A-Z)")
	elif choice == 7:
		print(" Zapisywanie statystyki z punktów 2-5 do pliku statystyki.txt...")
	elif choice == 8:
		sys.exit()
	else:
		print("!! DOKONANO NIEPRAWIDŁOWEGO WYBORU !!\n")
