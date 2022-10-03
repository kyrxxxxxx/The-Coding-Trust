import tkinter as tk
window = tk.Tk()

def getname():
    name = entry.get()
    labelName = tk.Label(text=name).pack()

def delete1st():
    entry.delete(0)

def delete04():
    entry.delete(0,4)

def deleteall():
    entry.delete(0, tk.END)

def insertreal():
    entry.insert(0,'real ')


label = tk.Label(text='Name').pack()
entry = tk.Entry()
entry.pack()

btngetname = tk.Button(text='Get Name', command=getname).pack()
btndelete1 = tk.Button(text='delete 1st', command=delete1st).pack()
btndelete4 = tk.Button(text='Delete 0-4', command=delete04).pack()
btndeleteall = tk.Button(text='delete all', command=deleeall).pack()

btninsertreal = tk.Button(text="insert 'real'", command=insertreal).pack()
