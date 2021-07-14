class restaurant:
    setmenu=["Chines","American", "Italian" , "Indain", "Thai"]
def welcome():
    print("WELCOME TO THE 5 STAR international RESTAURANT!!")
    print("here you can reseve your table to have a wonderful meal")
welcome()
              
def __init__(self):
    self.output=""
    
def place(where):  
    if where == "city" or "sea":
        print("great choice")
    else:
        print("please try again")
where=input("please choose your table for tonight (city / sea) view")
place(where)

def time(when):
    if  12>when>1:
        print("good timming")
    else:
        print("Unforunately we are closed")

when= int(input("When you are planning to visit our restaurant?(1pm to 12am)"))
time(when)


def cuisine(fav):
    if fav == "y":
        type=input("choose your wishing for cuisine for tonight from the list")
        print("Get ready to have an unforgettable meals")
    else:
        setmenu=["Chines","American", "Italian" , "Indain", "Thai"]
        xxx=input("Please write your fav cuisine and we will do our best to prepare it for you if possible")
        setmenu.append(xxx)
        print(setmenu)
        print("Get ready to have an unforgettable meals")

        
print("setmenu=[Chines,American, Italian , Indain, Thai]")
fav=input("Is your fav cuisine on the list? Yes= y No=n")

cuisine(fav)

def end():
    print("This is the end of the reserving systme. I wish you a great experience")
end()
