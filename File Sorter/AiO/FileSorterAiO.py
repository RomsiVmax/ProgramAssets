import shutil
import time
import os
import tkinter as tk
from tkinter import ttk

global fns
global username
global onedrivechecker
username = os.getlogin()
onedrivechecker=os.path.isdir(f"C:\\Users\\{username}\\OneDrive\\Desktop")
fns = [] #fns stands for file names

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






def gfn():  #gfn stands for get file names
    global fns
    global onedrivechecker
    if onedrivechecker==True:
        fns = [f for f in os.listdir(f"C:/Users/{username}/OneDrive/Desktop/sort")]

    else:
        fns = [f for f in os.listdir(f"C:/Users/{username}/Desktop/sort")]
    print(fns)




def gfe():  #gfe stands for get file extension

    global fn
    global fe
    fnep = fn.rfind('.') #fnep stands for file name extension point


    if fnep != -1:
        fe=fn[fnep+1:] #fe stands for file extension








def checkifsorteddirexists():
    global sorteddirexists
    sorteddirexists=os.path.isdir(f"C:\\Users\\{username}\\OneDrive\\Desktop\\sorted")
    if sorteddirexists==False:
        sorteddirexists=os.path.isdir(f"C:\\Users\\{username}\\Desktop\\sorted")
        
    print(f"Ordner existiert:{sorteddirexists}")
checkifsorteddirexists()


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
        print("OneDrive -- Yes")
        os.mkdir(f"C:\\Users\\{username}\\OneDrive\\Desktop\\sorted")
    else:
        os.mkdir(f"C:\\Users\\{username}\\Desktop\\sorted")
    checkifsorteddirexists()
    upd(updateablemessage2,f"Ordner existent:{sorteddirexists}")








def payload3():
    checkifsortdirexists()
    upd(updateablemessage1,f"Ordner existent:{sortdirexists}")
    checkifsorteddirexists()
    upd(updateablemessage2,f"Ordner existent:{sorteddirexists}")
    
    if onedrivechecker==True:
        payload3unlocked1=os.path.isdir(f"C:\\Users\\{username}\\OneDrive\\Desktop\\sort")
    else:
        payload3unlocked1=os.path.isdir(f"C:\\Users\\{username}\\Desktop\\sort")

    if onedrivechecker==True:
        payload3unlocked2=os.path.isdir(f"C:\\Users\\{username}\\OneDrive\\Desktop\\sorted")
    else:
        payload3unlocked2=os.path.isdir(f"C:\\Users\\{username}\\Desktop\\sorted")



    if payload3unlocked1==True:
        if payload3unlocked2==True:
            gfn()
            
            
            for item in fns:
                global fn #fn stands for file name
                fn=item
                print(fn)
                gfe()
                global fe

                ae=os.path.isdir(f"C:\\Users\\{username}\\OneDrive\\Desktop\\sorted\\{fe}") #ae stands for already exists
                if ae==False:
                    os.mkdir(f"C:\\Users\\{username}\\OneDrive\\Desktop\\sorted\\{fe}")
                
                shutil.copy2(f"C:\\Users\\{username}\\OneDrive\\Desktop\\sort\\{item}", f"C:\\Users\\{username}\\OneDrive\\Desktop\\sorted\\{fe}")
            if onedrivechecker==True:
                shutil.rmtree(f"C:\\Users\\{username}\\OneDrive\\Desktop\\sort", ignore_errors=True)
                
            else:
                shutil.rmtree(f"C:\\Users\\{username}\\Desktop\\sort", ignore_errors=True)


            

        else:

            for i in range(0,3):
                updateablemessage2.config(bg="red")
                root.update_idletasks()
                time.sleep(.5)
                updateablemessage2.config(bg=root.cget("bg"))
                root.update_idletasks()
                time.sleep(.5)
        
        
        
        
        
        
        
        
        
    else:
        for i in range(0,3):
            updateablemessage1.config(bg="red")
            root.update_idletasks()
            time.sleep(.5)
            updateablemessage1.config(bg=root.cget("bg"))
            root.update_idletasks()
            time.sleep(.5)




def payload4():
    print("a")




root = tk.Tk()


root.title("VmaxStudios File Sorter")
root.geometry("700x700+80+300")
root.resizable(False, False)
root.grid_columnconfigure(0, weight=1)







message = tk.Label(root, text="Schritt 1:")
message.grid(row=1, column=0, padx=5, pady=5)

payload1b = tk.Button(
    root, text="Erstelle sort-Ordner",
    command=payload1,
    fg="black",
    font=("Arial", 12)
)
payload1b.grid(row=1, column=1, padx=5, pady=5)

updateablemessage1 = tk.Label(root, text=f"Ordner existent:{sortdirexists}")
updateablemessage1.grid(row=1, column=2, padx=5, pady=5)



tk.Label(root).grid(row=2, column=0)




message = tk.Label(root, text="Schritt 2:")
message.grid(row=3, column=0, padx=5, pady=5)

payload2b = tk.Button(
    root, text="Erstelle sorted-Ordner",
    command=payload2,
    fg="black",
    font=("Arial", 12)
)
payload2b.grid(row=3, column=1, padx=5, pady=5)

updateablemessage2 = tk.Label(root, text=f"Ordner existent:{sorteddirexists}")
updateablemessage2.grid(row=3, column=2, padx=5, pady=5)




tk.Label(root).grid(row=4, column=0)





message = tk.Label(root, text="Schritt 3:")
message.grid(row=5, column=0, padx=5, pady=5)

message = tk.Label(root, text="Lege die zu sortierenden Dateien in den sort-Ordner")
message.grid(row=5, column=1, padx=5, pady=5)




tk.Label(root).grid(row=6, column=0)





message = tk.Label(root, text="Schritt 4:")
message.grid(row=7, column=0, padx=5, pady=5)

payload3b = tk.Button(
    root, text="Sortiere!",
    command=payload3,
    fg="black",
    font=("Arial", 12)
)
payload3b.grid(row=7, column=1, padx=5, pady=5)





tk.Label(root).grid(row=8, column=0)
tk.Label(root).grid(row=9, column=0)
tk.Label(root).grid(row=10, column=0)






payload4b = tk.Button(
    root, text="Zum professionellen Modus wechseln",
    command=payload4,
    fg="black",
    font=("Arial", 8)
)
payload4b.grid(row=11, column=2, padx=5, pady=5)




root.mainloop()
