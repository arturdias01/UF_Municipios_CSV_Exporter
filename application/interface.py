from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from uf_requests import Uf_requests


def get_entry():  #  add dados na Treeview
    for item in tv.get_children():
        tv.delete(item)
    global new_uf
    new_uf = Uf_requests(entrada.get())
    municipios = new_uf.get_municipios()
    for municipio in municipios:
        tv.insert('', 'end', values=(municipio[0], municipio[1]))


def esc_csv():
    new_uf.escrever_csv()
    popup_csv()


def popup_csv():  # Mensagem que aparece ao criar o arquivo csv
    message = messagebox.showinfo(title='CSV_files', message='Arquivo CSV criado.\n')
    print(message)
    entrada.delete(0, 'end')

    
# Parte Visual:

app = Tk() 
app.title('Trabalho Marcio')
app.geometry('640x360')
app.resizable(width=0, height=0)

lb = Label(app, text='UF:')
lb.place(x=60, y=20)

entrada = Entry(app, width=5, bd=3)
entrada.place(x=90, y=18)

btn_obter_lista = Button(app, text='Obter municípios', command=get_entry)
btn_obter_lista.place(x=140, y=16)

btn_criar_csv = Button(app, text='Criar arquivo CSV', command=esc_csv)
btn_criar_csv.place(x=250, y=16)

tv = ttk.Treeview(app, columns=('id', 'nome'), show='headings')
tv.column('id', minwidth=0, width=80)
tv.column('nome', minwidth=0, width=250)
tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.pack(fill='both', expand=True, padx=50, pady=50)


app.mainloop()


