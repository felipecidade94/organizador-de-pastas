import tkinter as tk
from tkinter import filedialog
from criar_pastas import criar_pastas
from mover import mover

def escolher_pasta():
   pasta = filedialog.askdirectory()
   if pasta:
      print(f'Pasta selecionada: {pasta}')
      label_resultado.config(text=f'Pasta: {pasta}')
      criar_pastas(pasta)
      mover(pasta)

janela = tk.Tk()
janela.title('Selecionar Pasta')

botao = tk.Button(janela, text='Escolher Pasta', command=escolher_pasta)
botao.pack(pady=10)

label_resultado = tk.Label(janela, text='Nenhuma pasta selecionada.')
label_resultado.pack()


janela.mainloop()
