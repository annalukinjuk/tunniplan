from tkinter import*
root=Tk()

Label(text="Имя:").grid(row=0,column=0)
table_name=Entry(width=30)
table_name.grid(row=0,column=1,columnspan=3)

Label(text="столбцов: ").grid(row=1,column=0)
table_column=Spinbox(width=7,from_=1,to=50)
table_column.grid(row=1,column=1)
Label(text="столбцов:").grid(row=1,column=2)
table_row=Spinbox(width=7,from_=1,to=100)
table_row.grid(row=1,column=3)

Button(text="справка").grid(row=2,column=0)
Button(text="вставить").grid(row=2,column=2)
Button(text="отменить").grid(row=2,column=3)

root.mainloop()