from  tkinter import *
from tkinter import ttk

janela = Tk()
janela.title ('flores da favela')



ree = ttk.Treeview(janela, selectmode="browse", column= ("column1","column2","column3","column4"), show='headings')

tree.column("column", width=200, minwidth=50, stretch=NO)
tree.heading("#1",text='nome')

tree.column("column", width=100, minwidth=50, stretch=NO)
tree.heading("#2",text='idade')

tree.column("column", width=300, minwidth=50, stretch=NO)
tree.heading("#3",text='Endereço')

tree.column("column", width=200, minwidth=50, stretch=NO)
tree.heading("#4",text='Id')

tree.grid(row=0, column=0)






janela.mainloop()