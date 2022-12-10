import json
import requests
from tkinter import*
def buttonAction():
    with open("vivod.txt","w") as file:
        user = txtField.get()
        url = f"https://api.github.com/users/{user}"
        userInfo = requests.get(url).json()
        enum = ['company', 'created_at', 'email', 'id', 'name', 'url']
        data = userInfo.keys()
        for i in data:
            if i in enum:
                file.write(f"{i}:{userInfo[i]}" + '\n')
    head.configure(text = "Успех")


root = Tk()
root.title('GIT request')
root.geometry('500x250')
root["bg"] = "#008080"

head = Label(root, bg = "#008080", fg = "#00FF00", text = 'Введите имя репозитория', font = ('Courier New', 20))
head.pack(expand=True)
txtField = Entry(root,width=40,font=('Courier New', 12))
txtField.pack(expand=True)
button = Button(root, bg = "#20B2AA", fg = "#DC143C", text = 'Нажми на меня',command = buttonAction)
button.pack(expand=True)

root.mainloop()
