import sys

from urllib.request import urlopen
from string import ascii_lowercase
import os


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
		
		global letters
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

		global words
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

                global punctation        
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

                global sentences 
                sentences = 0
                sentences = data.count(".") + data.count("!") + data.count("?")
                print("Ilość zdań w pliku " ,filename, " to ", str(sentences))
        except FileNotFoundError:
                print(" ** Nie mogę znaleść pliku ", filename)
        except Exception:
                print(" ** Nie mogę otworzyć pliku ",filename) 


def generate_report():
	try:
		with open(filename, 'r') as myfile:
			data = myfile.read()
		
		for char in ascii_lowercase:
			x = data.count(char) + data.count(char.upper())
			print( char.upper(),": ",x)
	except FileNotFoundError:
		print(" ** Brak pliku ",filename, " **")
	except Exception:
		print(" ** Nie mogę otworzyć pliku ",filename)

def save_stats():

    path="statystyki.txt"
    if os.path.isfile(path):
        os.unlink(path)

    myfile = open('statystyki.txt','a')
    myfile.write("Ilość liter: ")
    myfile.write(str(letters))
    myfile.write("\n")
    myfile.write("Ilość słów: ")
    myfile.write(str(words))
    myfile.write("\n")
    myfile.write("Ilość znaków interpunkcyjnych: ")
    myfile.write(str(punctation))
    myfile.write("\n")
    myfile.write("Ilość zdań: ")
    myfile.write(str(sentences))
    myfile.write("\n")
    myfile.close()


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
		count_words()
	elif choice == 4:
		count_punctation()
	elif choice == 5:
		count_sentences()
	elif choice == 6:
		generate_report()
	elif choice == 7:
		print(" Zapisywanie statystyki z punktów 2-5 do pliku statystyki.txt...")
		save_stats()
	elif choice == 8:
		sys.exit()
	else:
		print("!! DOKONANO NIEPRAWIDŁOWEGO WYBORU !!\n")
