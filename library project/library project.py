
class Library ():
    def __init__(self ,name ="library",books = ["game","olivar","thron"] ,lendbox =[] ) -> None:
        self.name = name + " library"
        self.__books = books
        self.__lendbox = lendbox
        pass

    def Displaybook(self):
        print("\nbooks are avilable in library. \n")
        return print(self.__books)

    def Addbook (self):
        while 1 :
            print("to end process press 0.")
            inp =input("enter book name you want to add to library: ")
            if inp in self.__books or inp in self.__lendbox :
                print(f"{inp} is already in library.")
                break
            else:
                newbook=inp
                self.__books.append(newbook)
            if inp == "0":
                break
    def Lendbook (self):
        while True:
            print("to end process press 0.")
            inp = input("enter name book you want to lend: ")
            inp_lower =inp.lower()

            if inp_lower in self.__books :
                self.__books.remove(inp_lower) #lentbook
                self.__lendbox.append(inp_lower)
            elif inp_lower in self.__lendbox:
                print(f"{inp} is already lended.")
            else : print(f"{inp} inp not in library.")

            if inp == "0":
                break

    def Returnbook(self):
        inp = input("enter name book you want to return: ")
        inp_lower =inp.lower()

        if inp_lower in self.__lendbox :
            self.__lendbox.remove(inp_lower) #lentbook
            self.__books.append(inp_lower)

        elif inp_lower in self.__books :
            print(f"{inp} is already in library :)")

        else : print("error")

list = ["seven deadly sins", "black clover","tales"]
harry =Library("harry",list)

print(f"\nwelcome to {harry.name}. \n")

def One_more():

    print("1- display avilable books.")
    print("2- lend book from library.")
    print("3- add books to library.")
    print("4- return lended book from library.")
    print("5- exit library.")
    press = input("\nenter please number of process you want :")
    if press == "1" :
        harry.Displaybook()
    elif press == "2" :
        harry.Lendbook()
    elif press == "3" :
        harry.Addbook()
    elif press == "4" :
        harry.Returnbook()
    elif press == "5" :
        print(f"thank you from comeing {harry.name}.")
        return 0
    else : One_more()
    rst = input("do you want to process again ?\n yes/no\n")

    if rst == "yes":
        One_more()
    elif rst == "no":
        print(f"\nthank you from comeing {harry.name}.")
        return 0
    else:
        One_more()
while True :

    x=One_more()
    if x ==0:
        break
    