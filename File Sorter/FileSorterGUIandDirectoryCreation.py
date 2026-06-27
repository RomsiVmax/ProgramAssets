import time
import os
import tkinter as tk
from tkinter import ttk

global username
global onedrivechecker
username = os.getlogin()
onedrivechecker=os.path.isdir(f"C:\\Users\\{username}\\OneDrive\\Desktop")

def checkifsortdirexists():
    global sortdirexists
    sortdirexists=os.path.isdir(f"C:\\Users\\{username}\\OneDrive\\Desktop\\sort")
    if sortdirexists==False:
        sortdirexists=os.path.isdir(f"C:\\Users\\{username}\\Desktop\\sort")
        
    print(f"Ordner existiert:{sortdirexists}")
checkifsortdirexists()


def upd(labelname,updatedmessage):
    labelname.config(text=f"{updatedmessage}")
    root.update_idletasks()

    




def payload1():
    if onedrivechecker==True:
        print("OneDrive -- Yes")
        os.mkdir(f"C:\\Users\\{username}\\OneDrive\\Desktop\\sort")
    else:
        os.mkdir(f"C:\\Users\\{username}\\Desktop\\sort")
    checkifsortdirexists()
    upd(updateablemessage1,f"Ordner existent:{sortdirexists}")





def payload2():
    if onedrivechecker==True:
        payload2unlocked=os.path.isdir(f"C:\\Users\\{username}\\OneDrive\\Desktop\\sort")
    else:
        payload2unlocked=os.path.isdir(f"C:\\Users\\{username}\\Desktop\\sort")

    if payload2unlocked==True:
        print("Payload unlocked")
        os.startfile("C:\\Program Files\\File Sorter\\Backend\\File Sorter.bat")
    else:
        for i in range(0,3):
            updateablemessage1.config(bg="red")
            root.update_idletasks()
            time.sleep(.5)
            updateablemessage1.config(bg=root.cget("bg"))
            root.update_idletasks()
            time.sleep(.5)

    checkifsortdirexists()
    upd(updateablemessage1,f"Ordner existent:{sortdirexists}")







root = tk.Tk()


root.title("VmaxStudios File Sorter")
root.geometry("500x500+80+300")
root.resizable(False, False)




message = tk.Label(root, text="Schritt 1:")
message.pack()

payload1b = tk.Button(
    root, text="Erstelle sort-Ordner",
    command=payload1,
    fg="black",
    font=("Arial", 12)
)
payload1b.pack()

updateablemessage1 = tk.Label(root, text=f"Ordner existent:{sortdirexists}")
updateablemessage1.pack()





message = tk.Label(root, text="Schritt 2:")
message.pack()

message = tk.Label(root, text="Lege die zu sortierenden Dateien in den sort-Ordner!")
message.pack()

message = tk.Label(root, text="Schritt 3:")
message.pack()
payload2b = tk.Button(
    root, text="Sortiere!",
    command=payload2,
    fg="black",
    font=("Arial", 12)
)
payload2b.pack()



root.mainloop()
