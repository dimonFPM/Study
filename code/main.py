from tkinter import *


root = Tk()
root.title("ДС")
root.geometry("200x100+100+100")
root.resizable(False, False)


#region балка
def balka():
    root1 = Toplevel()
    root1.title("Моделирование фундамента")
    root1.geometry("730x560+310+20")
    root1.resizable(False, False)

    # Canvas
    q1 = Canvas(root1, width=495, height=400, bg="white")
    q1.grid(row=0, column=0, rowspan=8, columnspan=10)
    q1.create_rectangle(2, 2, 496, 401)
    q1.create_rectangle(10, 30, 489, 391)
    q1.create_text(239, 15, text="Зависимость собственных частот от полуширины балки", )
    q1.create_text(40, 45, text="K,a", font="Arial 15")
    q1.create_text(455, 45, text="a", font="Arial 15")
    x = 78.42
    for i in range(7):
        q1.create_line(x, 30, x, 391)
        x += 68.42
    x = 62.81
    for i in range(10):
        q1.create_line(10, x, 489, x)
        x += 32.81
    x = 110
    for i in range(5):
        a = str(i + 1)
        q1.create_text(x, 45, text=a, font="Arial 15")
        x += 70
    x = 80
    for i in range(10):
        a = str(i + 1)
        q1.create_text(40, x, text=a, font="Arial 15")
        x += 33

    # Label
    l1 = Label(root1, text="Входные данные:", font="Arial 15")
    l1.grid(row=8, column=0, columnspan=8, sticky=W)
    l2 = Label(root1, text="Граничные условия:", font="Arial 15")
    l2.grid(row=0, column=10, columnspan=3, sticky=W)
    l3 = Label(root1, text="Вид нагрузки:", font="Arial 15")
    l3.grid(row=4, column=10, columnspan=3, sticky=W)
    e_l = Label(root1, text="E=")
    j_l = Label(root1, text="J=")
    m_l = Label(root1, text="m=")
    w_l = Label(root1, text="w=")
    t_l = Label(root1, text="точность=")
    k_l = Label(root1, text="k=")
    a_l = Label(root1, text="a=")
    time_l = Label(root1, text="время=")
    e_l.grid(row=9, column=0, sticky=W)
    j_l.grid(row=10, column=0, sticky=W)
    m_l.grid(row=11, column=0, sticky=W)
    w_l.grid(row=12, column=0, sticky=W)
    t_l.grid(row=13, column=0, sticky=W)
    k_l.grid(row=9, column=4, sticky=W)
    a_l.grid(row=10, column=4, sticky=W)
    time_l.grid(row=11, column=4, sticky=W)

    # Entry
    e_e = Entry(root1, )
    j_e = Entry(root1, )
    m_e = Entry(root1, )
    w_e = Entry(root1, )
    t_e = Entry(root1, )
    k_e = Entry(root1, )
    a_e = Entry(root1, )
    time_e = Entry(root1, )
    e_e.grid(row=9, column=1, columnspan=2)
    j_e.grid(row=10, column=1, columnspan=2)
    m_e.grid(row=11, column=1, columnspan=2)
    w_e.grid(row=12, column=1, columnspan=2)
    t_e.grid(row=13, column=1, columnspan=2)
    k_e.grid(row=9, column=5, columnspan=2)
    a_e.grid(row=10, column=5, columnspan=2)
    time_e.grid(row=11, column=5, columnspan=2)

    ######################################## ввод данных для теста/потом удалить
    e_e.insert(0, 6)
    j_e.insert(0, 3)
    m_e.insert(0, 7)
    w_e.insert(0, 1)
    t_e.insert(0, format(0.0000001, '.7f'))
    k_e.insert(0, 3)
    a_e.insert(0, 1)
    time_e.insert(0, 0)
    ########################################

    # Button
    # b1 = Button(root1, text="Рассчитать", bg="orange", command=tableBalka)
    b1 = Button(root1, text="Рассчитать", bg="orange")

    b1.grid(row=13, column=11)
    # b2 = Button(root1, text="Очистить", command=clean, bd=0)
    b2 = Button(root1, text="Очистить", bd=0)
    b2.grid(row=13, column=10)

    # Radiobutton
    r_var = IntVar()
    r_var1 = IntVar()
    r_var1.set(0)
    r_var.set(0)
    r_1 = Radiobutton(root1, text="Жёсткая заделка краёв балки", variable=r_var, value=0)
    r_2 = Radiobutton(root1, text="Шарнирное опирание краёв балки", variable=r_var, value=1)
    r_3 = Radiobutton(root1, text="Свобоное операние балки", variable=r_var, value=2)
    r_4 = Radiobutton(root1, text="Равномерно распределённая\nнагрузка", variable=r_var1, value=0)
    r_5 = Radiobutton(root1, text="Параболически распределённая\nнагрузка", variable=r_var1, value=1)
    r_1.grid(row=1, column=10, columnspan=3, sticky=W)
    r_2.grid(row=2, column=10, columnspan=3, sticky=W)
    r_3.grid(row=3, column=10, columnspan=3, sticky=W)
    r_4.grid(row=5, column=10, columnspan=3, sticky=W)
    r_5.grid(row=6, column=10, columnspan=3, sticky=W)

    # checkbutton
    r_var2 = IntVar()
    r_var2.set(0)
    ch1 = Checkbutton(root1, text="Анимация", variable=r_var2, onvalue=1, offvalue=0)
    ch1.grid(row=9, column=10, sticky=W)

    # l = []
    # lx = []
    # ly = []

    root1.mainloop()
#endregion

#region стержень
def sterg():
    root2 = Toplevel()
    root2.title("Моделирование стержня")
    root2.geometry("700x560+310+20")
    root2.resizable(False, False)

    #отрисовка интерфеса данного окна
    q1 = Canvas(root2, width=430, height=400, bg="white")
    q1.grid(row=0, column=0, rowspan=8, columnspan=10)
    q1.create_rectangle(2, 2, 431, 401)
    q1.create_rectangle(10, 30, 420.58, 391)
    q1.create_text(239, 15, text="Зависимость собственных частот от массы тела")
    q1.create_text(40, 45, text="m,w", font="Arial 15")
    x = 78.42
    for i in range(6):
        q1.create_line(x, 30, x, 391)
        x += 68.42
    x = 62.81
    for i in range(10):
        q1.create_line(10, x, 420.58, x)
        x += 32.81
    x = 110
    for i in range(5):
        a = str(i + 1)
        q1.create_text(x, 45, text=a, font="Arial 15")
        x += 70
    x = 80
    for i in range(10):
        a = str(i + 1)
        q1.create_text(40, x, text=a, font="Arial 15")
        x += 33

    # Label
    l1 = Label(root2, text="Входные данные:", font="Arial 15")
    l1.grid(row=8, column=0, columnspan=8, sticky=W)
    l2 = Label(root2, text="Граничные условия:", font="Arial 15")
    l2.grid(row=0, column=10, columnspan=3, sticky=W)
    l3 = Label(root2, text="Дополнительные данные:", font="Arial 15")
    l3.grid(row=4, column=10, columnspan=3, sticky=SW)

    e_l = Label(root2, text="E=")
    f_l = Label(root2, text="F=")
    m_l = Label(root2, text="m=")
    w_l = Label(root2, text="w=")
    t_l = Label(root2, text="точность=")
    p_l = Label(root2, text="p=")
    s_l = Label(root2, text="s=")
    l_l = Label(root2, text="l=")
    time_l = Label(root2, text="время=")
    ny_l = Label(root2, text="Коэф. Пуассона=")
    h_l = Label(root2, text="Ширина упругой полосы=")
    a_l = Label(root2, text="Ширина стержня=")

    e_l.grid(row=9, column=0, sticky=W)
    f_l.grid(row=10, column=0, sticky=W)
    m_l.grid(row=11, column=0, sticky=W)
    w_l.grid(row=12, column=0, sticky=W)
    # t_l.grid(row=13, column=0, sticky=W)
    p_l.grid(row=9, column=4, sticky=W)
    s_l.grid(row=10, column=4, sticky=W)
    l_l.grid(row=11, column=4, sticky=W)
    time_l.grid(row=12, column=4, sticky=W)
    ny_l.grid(row=5, column=10, sticky=NW)
    h_l.grid(row=6, column=10, sticky=NW)
    a_l.grid(row=7, column=10, sticky=NW)

    # Entry
    e_e = Entry(root2)
    f_e = Entry(root2)
    m_e = Entry(root2)
    w_e = Entry(root2)
    # t_e = Entry(root2)
    p_e = Entry(root2)
    s_e = Entry(root2)
    l_e = Entry(root2)
    time_e = Entry(root2)
    ny_e = Entry(root2, width=15)
    h_e = Entry(root2, width=15)
    a_e = Entry(root2, width=15)

    e_e.grid(row=9, column=1, columnspan=2)
    f_e.grid(row=10, column=1, columnspan=2)
    m_e.grid(row=11, column=1, columnspan=2)
    w_e.grid(row=12, column=1, columnspan=2)
    # t_e.grid(row=13, column=1, columnspan=2)
    p_e.grid(row=9, column=5, columnspan=2)
    s_e.grid(row=10, column=5, columnspan=2)
    l_e.grid(row=11, column=5, columnspan=2)
    time_e.grid(row=12, column=5, columnspan=2)
    ny_e.grid(row=5, column=11, sticky=NW)
    h_e.grid(row=6, column=11, sticky=NW)
    a_e.grid(row=7, column=11, sticky=NW)

    ######################################## ввод данных для теста/потом удалить
    e_e.insert(0, 1)
    f_e.insert(0, 1)
    m_e.insert(0, 1)
    w_e.insert(0, 1)
    # t_e.insert(0, 1)
    p_e.insert(0, 1)
    s_e.insert(0, 1)
    l_e.insert(0, 1)
    time_e.insert(0, 0)
    ny_e.insert(0, 0.3)
    h_e.insert(0, 1)
    a_e.insert(0, 2)
    ########################################

    # Button
    # b1 = Button(root2, text="Рассчитать", bg="orange", command=tableSterg)
    b1 = Button(root2, text="Рассчитать", bg="orange")

    b1.grid(row=13, column=11)
    # b2 = Button(root2, text="Очистить", bd=0, command=clean)
    b2 = Button(root2, text="Очистить", bd=0)

    b2.grid(row=13, column=10)

    # Radiobutton
    r_var = IntVar()
    r_var.set(0)
    r_1 = Radiobutton(root2, text="Стержень закреплён жёстко", variable=r_var, value=0)
    r_2 = Radiobutton(root2,
                      text="Стержень без трения контактирует с\nполуограниченным деформируемым\nоснованием средой"
                           "\n(Необходимы дополнительные данные)",
                      variable=r_var, value=1)
    r_1.grid(row=1, column=10, columnspan=3, sticky=W)
    r_2.grid(row=2, column=10, columnspan=3, sticky=W)

    # checkbutton
    r_var1 = IntVar()
    r_var1.set(0)
    ch1 = Checkbutton(root2, text="Анимация", variable=r_var1, onvalue=1, offvalue=0)
    ch1.grid(row=9, column=10, sticky=W)
    root2.mainloop()
#endregion

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
