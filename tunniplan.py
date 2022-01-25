from tkinter import*
root=Tk()
root.configure(bg="#c2abff")

Tunniplan={}
#with open("TextFile1.txt","r") as f:
#	for i in f: # создаем цикл по кол-ву строк
#		k,v=i.strip().split(" -") # отделяем слова на строчке в строчке по знаку " - "
#		Lessons[k.strip()]=v.strip() # добавляем в словарь
with open("TextFile1.txt","r", encoding="utf-8-sig") as o:
    for i in o:
        t,p=i.strip().split("-")
        Tunniplan[t.strip()]=p.strip()

def newwind(a):
	a1=a.replace(" \n", "")
	#showinfo("tunni informatsioon",f"{a}")
	newwd=Toplevel() #tk()
	abc=Label(newwd,text=Lessons.get(a1),font="Calibri 23",fg="black",justify=CENTER)
	newwd.geometry("500x90")
	abc.pack()


def info(a):
    a_=a.replace(" \n","")
    infokno=Toplevel()
    okowko=Label(infokno,text=uroki.get(a_),font="Arial 26",fg="black",justify=CENTER)
    infokno.geometry("500x150")
    ak.pack()

def svoboda():
	showinfo(title="окно",message="отдыхать и кушать!!!") 
def dopest():
	showinfo(title="доп.эстонский",message="эстонский для двоечников\n Учитель - Olesja Ojamäe\n Кабинет - B234")
def dopest():
	showinfo(title="доп.эстонский",message="эстонский для двоечников\n Учитель - Alina Laanevali-Toots\n Кабинет - B236")
def log():
	showinfo(title="логистика",message="логистика\n Учитель - Инесса Климанская\n Кабинет - B002")
def mat():
	showinfo(title="математика",message="математика\n Учитель - Nadewda Voronova\n Кабинет - B133")
def matt():
	showinfo(title="доп.математика",message="математитка для двоечников\n Учитель - Nadezda Voronova\n Кабинет - B133")
def rus():
	showinfo(title="русский",message="письмо и речь\n Учитель - Ljudmila Mihhajlova\n Кабинет - B221")
def kemt():
	showinfo(title="доп.химия",message="химия для двоечников\n Учитель - Svetlana Pisestkaja\n Кабинет - B144")
def progr():
	showinfo(title="програмирование",message="пайтон и гитхаб\n Учитель - Marina Oleinik\n Кабинет - E007")
def füsik():
	showinfo(title="физика",message="физика\n Учитель - Nadewda Voronova\n Кабинет - B133")
def kunst():
	showinfo(title="ИЗО",message="рисуем \n Учитель - Aleksandrova\n Кабинет - B232")
def fizra():
	showinfo(title="физра",message="физра\n Учитель - Maksim\n Кабинет - спортзал Акорпус")
def rak():
	showinfo(title="офисные программы",message="офисные программы \n Учитель - Merkulova\n Кабинет - E010")
def est():
	showinfo(title="эстонский",message="эстонский\n Учитель - Olesja Ojamäe\n Кабинет - B234")

def angl():
	showinfo(title="английский",message="английский\n Учитель - Olga Borodina\n Кабинет - B227")


Label(text="0\n7.40-8.25", font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=2,sticky=W+E+N+S)
Label(text="1\n8.30-9.15",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=3,sticky=W+E+N+S)
Label(text="2\n9.20-10.05",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=4,sticky=W+E+N+S)
Label(text="3\n10.10-10.55",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=5,sticky=W+E+N+S)
Label(text="4\n11.00-11.45",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=6,sticky=W+E+N+S)
Label(text="5\n11.50-12.35",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=7,sticky=W+E+N+S)
Label(text="6\n12.40-13.25",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=8,sticky=W+E+N+S)
Label(text="7\n13.30-14.15",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=9,sticky=W+E+N+S)
Label(text="8\n14.20-15.05",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=10,sticky=W+E+N+S)
Label(text="9\n15.10-15.55",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=11,sticky=W+E+N+S)
Label(text="10\n16.00-16.45",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=12,sticky=W+E+N+S)

Label(text="ПН",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=1,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)
Label(text="ВТ",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=3,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)
Label(text="СР",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=5,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)
Label(text="ЧТ",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=7,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)
Label(text="ПТ",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=9,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)

Label(text=" ",height=2,bg="#c2abff",borderwidth=1,relief="groove").grid(row=1,column=3,sticky=W+E+N+S)
dope2=Button(text="доп.эстонский \n 2 группа",bg="#ff0086",borderwidth=1,relief="flat",command=dopest).grid(row=2,column=3,sticky=W+E+N+S)
log=Button(text="логистика",bg="#ffb1da",borderwidth=1,relief="flat").grid(row=1,rowspan=2,column=4,columnspan=2,sticky=W+E+N+S)
mat=Button(text="математика",bg="#fd41bd",borderwidth=1,relief="flat").grid(row=1,rowspan=2,column=6,columnspan=2,sticky=W+E+N+S)
Label(text="окно",bg="#730086",borderwidth=1,relief="flat",command=svoboda).grid(row=1,rowspan=2,column=8,sticky=W+E+N+S)
ru=Button(text="русский язык",bg="#FF35A0",borderwidth=1,relief="flat").grid(row=1,rowspan=2,column=9,columnspan=2,sticky=W+E+N+S)
dopm=Button(text="доп.математика",bg="#fd41bd",borderwidth=1,relief="flat").grid(row=1,rowspan=2,column=11,sticky=W+E+N+S)

Label(text=" \n",bg="#c2abff",borderwidth=1,relief="groove").grid(row=6,column=3,sticky=W+E+N+S)
doph=Button(text="доп.химия",borderwidth=1, height=4, relief="flat",bg="#C929CB").grid(row=3,rowspan=2,column=3,sticky=W+E+N+S)
py1=Button(text="программирование",bg="#c57eff",borderwidth=1,relief="flat").grid(row=3,rowspan=2,column=4,columnspan=3,sticky=W+E+N+S)
Label(text="окно",bg="#730086",borderwidth=1,relief="flat",command=svoboda).grid(row=3,rowspan=2,column=7,sticky=W+E+N+S)
sc=Button(text="физика",bg="#9a76fa",borderwidth=1,relief="flat").grid(row=3,rowspan=2,column=8,columnspan=2,sticky=W+E+N+S)

dope=Button(text="доп.эстонский \n 1 группа",borderwidth=1,relief="flat",bg="#ff0086").grid(row=5,column=3,sticky=W+E+N+S)
izo=Button(text="искусство",borderwidth=1,relief="flat",bg="#C929CB").grid(row=5,rowspan=2,column=4,columnspan=2,sticky=W+E+N+S)
Label(text="окно",bg="#730086",borderwidth=1,relief="flat",command=svoboda).grid(row=5,rowspan=2,column=6,sticky=W+E+N+S)
pe=Button(text="физкультура",borderwidth=1,relief="flat",bg="#C929CB").grid(row=5,rowspan=2,column=7,columnspan=2,sticky=W+E+N+S)

log2=Button(text="логистика",borderwidth=1,relief="flat",bg="#ffb1da").grid(row=7,rowspan=2,column=3,columnspan=2,sticky=W+E+N+S)
Label(text="окно",bg="#730086",borderwidth=1,relief="flat",command=svoboda).grid(row=7,rowspan=2,column=5,sticky=W+E+N+S)
py2=Button(text="программирование",bg="#c57eff",borderwidth=1,relief="flat").grid(row=7,rowspan=2,column=6,columnspan=2,sticky=W+E+N+S)
en1=Button(text="английский \n 1 группа",bg="#c7b5f7",borderwidth=1,relief="flat").grid(row=7,column=8,columnspan=2,sticky=W+E+N+S)
exl2=Button(text="офисные программы \n 2 группа",borderwidth=1,relief="flat",bg="#FF71BC").grid(row=8,column=8,columnspan=2,sticky=W+E+N+S)
exl1=Button(text="офисные программы \n 1 группа",borderwidth=1,relief="flat",bg="#FF71BC").grid(row=7,column=10,columnspan=2,sticky=W+E+N+S)
est2=Button(text="эстонский \n 2 группа",bg="#ff0086",borderwidth=1,relief="flat").grid(row=8,column=10,columnspan=2,sticky=W+E+N+S)

et1=Button(text="эстонский \n 1 группа",bg="#ff0086",borderwidth=1,relief="flat").grid(row=9,column=3,columnspan=2,sticky=W+E+N+S)
exl22=Button(text="офисные программы \n 2 группа",borderwidth=1,bg="#FF71BC",relief="flat").grid(row=10,column=3,columnspan=2,sticky=W+E+N+S)
py3=Button(text="программирование",bg="#c57eff",borderwidth=1,relief="flat").grid(row=9,rowspan=2,column=5,columnspan=5,sticky=W+E+N+S)
exl11=Button(text="офисные программы \n 1 группа",borderwidth=1,bg="#FF71BC",relief="flat").grid(row=9,column=10,columnspan=2,sticky=W+E+N+S)
eng2=Button(text="английский \n 2 группа",borderwidth=1,bg="#c7b5f7",relief="flat").grid(row=10,column=10,columnspan=2,sticky=W+E+N+S)


root.mainloop()