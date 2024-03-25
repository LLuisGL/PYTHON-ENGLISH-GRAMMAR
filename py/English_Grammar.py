import random
import time
import ast

#VARIABLES GENERALES
lifes = 3

#LEER DICCIONARIO
def dictionary_lecture():
    f = open("dictionary_words.py")
    read = f.readlines()
    line1 = read[1]
    dictionary = ""
    count = 0
    for element in line1:
        if(element == "}"):
            dictionary += element
            break
        elif(count >21):
            dictionary += element
        else:
            count += 1
    dictionary_ast = ast.literal_eval(dictionary)
    return dictionary_ast

#ESPACIO DE LINEAS

def space():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

#MENU PRINCIPAL

def menu():

    print("=========================== \n1. New Game \n2. Search Any Words \n3. Create A Word \n4. Exit \n===========================")
    n = int(input(""))
    return n

#VALIDACION VIDAS
def validation_lifes(lifes):
    if(lifes == 0):
        return True
    else:
        return False

#VALIDACION PALABRA
def validation_answer(word_user, word_validation):
    first_letter = word_validation
    try:
        letter = dictionary_lecture().get(first_letter)
        for element in letter:
            if(element == word_user.upper()):
                return True
                break
        else:
            return False

    except:
        print("Word Not Found")
        return False
#LOADING
def loading():
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(3)

#NUEVO JUEGO

def newGame(lifes):
    #CAPTURA LA LETRA CON LA QUE SE VA A JUGAR 
    choosen_letter_len = random.randint(0, len(dictionary_lecture()) - 1)
    choosen_letter_key = list(dictionary_lecture())[choosen_letter_len]

    print(f"===============||    {choosen_letter_key}    ||==================")
    time.sleep(1)
    while(True):
        if(validation_lifes(lifes) == True):
            print("Nice try, you lose:( ")
            break
        answer = input("--->")
        if(validation_answer(answer, choosen_letter_key) == True):
            print("Congratulation, you win! ^^ ")
            break
        else:
            lifes -= 1
            print(f"Word not found, try again. Lifes = {lifes}")
    time.sleep(5)    
    return

#BUSCADOR DE PALARAS
def searchWord():
    while(True):    
        answer = input("Type any letter that you want to know the list of words with it \n")
        space()
        try:
            word_list = dictionary_lecture().get(answer.lower())
            print(f"|| words with the letter {answer.upper()}: {word_list} ||")
            print("\n\n")
        except:
            print("We don't find any word with the letter that you've wroten")
        answer = input("Do you want continue searching words? (YES) (NO) \n")
        if(answer.upper() != "YES"):
            break
    return

#CREAR PALABRAS
def creationWord():
    dictionary = dictionary_lecture()
    answer = input("Write any word that you'd like to add \n")
    flag = False
    for letter in answer:
        for letter_dictionary in dictionary:
            if(letter.lower() == letter_dictionary and answer.upper() not in dictionary.get(letter_dictionary)):
                dictionary.get(letter_dictionary).append(answer.upper())
                flag = True
    print("Creating word, give a while")
    loading()
    if(flag == True):
        print("Word Create Succesfully!")
    else:
        print("ERROR: Your word was already created!")
    time.sleep(2)
    f = open("dictionary_words.py", "w")
    f.write(f"def words():\n    word_dictionary = {dictionary}\n    return word_dictionary")
    f.close()

#CODIGO BASE

while(True):
    space()
    player = menu()
    if(player == 1):
        space()
        newGame(lifes)
    elif(player == 2):
        space()
        searchWord()
    elif(player == 3):
        space()
        creationWord()
    else:
        print("Exiting")
        loading()
        break