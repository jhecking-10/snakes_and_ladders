def tutorial_check():
    while True:
        try:
            tutorial = input("Tutorial?\nType y/n:\n")
            tutorial = tutorial.lower()
            if tutorial == "y" or tutorial == "yes":
                print("Tutorial loading...\nPlease wait...")
                break
            elif tutorial == "n" or tutorial == "no":
                print("Game loading...\nPlease wait...")
                break
            else:
                raise ValueError
        except ValueError:
            print('Please type either "y" or "n"')

def main():
    print("~~~~~~~~~~Shoots and Ladders~~~~~~~~~~")
    tutorial_check()

if __name__ == "__main__":
    main()
