from tkinter import *
from tkinter.messagebox import showwarning

janela = Tk()
janela.geometry('500x500')
janela.title('To-do List made in Python')


def adicionar():
    tarefa = entrada.get()
    if tarefa:
        listbox.insert(END, tarefa)
        entrada.delete(0, END)
    else:
        showwarning("Atenção", "O campo está vazio!")


def deletar():
    tarefa = listbox.curselection()
    if tarefa:
        listbox.delete(tarefa)
    else:
        showwarning("Atenção", "Você não selecionou nenhuma tarefa!")

def concluir():
    indice = listbox.curselection()
    if indice:
        tarefa = listbox.get(indice)
        listbox.delete(indice)
        listbox.insert(indice, f'{tarefa}: finalizada')
        listbox.itemconfig(indice, fg="gray", selectbackground="lightgray")
    else:
        showwarning("Atenção", "Você não selecionou nenhuma tarefa!")



entrada = Entry(janela, width=20)
entrada.pack(pady=10)

botao_entrada = Button(janela, text='Adicionar Tarefa', command=adicionar)
botao_entrada.pack(pady=5)

listbox = Listbox(janela, height=15, width=30)
listbox.pack(pady=5)

botao_concluir = Button(janela, text='Marcar como Concluída', command=concluir)
botao_concluir.pack(pady=5)


botao_deletar = Button(janela, text='Excluir Tarefa', command=deletar)
botao_deletar.pack(pady=5)


janela.mainloop()