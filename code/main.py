from tkinter import *


root = Tk()
root.title("ДС")
root.geometry("200x100+100+100")
root.resizable(False, False)

l1 = Label(root, text="ВЫБЕРЕТЕ ВИД ВЫЧИСЛЕНИЙ:")
l1.pack(side=TOP)

buttonBalka = Button(root, text="Прогибы балки", width=20)
buttonBalka.pack(side=TOP)
buttonSterg = Button(root, text="Стержень", width=20)
buttonSterg.pack(side=TOP)
l = []
lx = []
ly = []
mi = 0

root.mainloop()
