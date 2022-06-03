from tkinter import *
import random

root = Tk()
root.title("Bag list")
root.geometry("500x600")

items_label = Label(root)
items_random = Label(root)
ListItems=['Bottle','Tiffin','ID Card','Chocolates','Chips','Tickets','Hanky']

items_label["text"]="Listed Items: "+str(ListItems)
items_label.place(relx=0.5,rely=0.4,anchor=CENTER)

def pickitems():
    random_item = random.randint(0,6)

    if random_item == 0:
        items_random["text"]="Put Bottle in Bag"
        
    if random_item == 1:
        items_random["text"]="Put Tiffin in Bag"
    
    if random_item == 2:
        items_random["text"]="Put Id Card in Bag"
        
    if random_item == 3:
        items_random["text"]="Put Chocolates in Bag"
        
    if random_item == 4:
        items_random["text"]="Put Chips in Bag"
        
    if random_item == 5:
        items_random["text"]="Put Tickets in Bag"
        
    if random_item == 6:
        items_random["text"]="Put Hanky in Bag"
        
        

button1 = Button(root,text="Which item do i put in bag?",command=pickitems)
button1.place(relx=0.5,rely=0.5,anchor=CENTER)
items_random.place(relx=0.5,rely=0.6,anchor=CENTER)


root.mainloop()