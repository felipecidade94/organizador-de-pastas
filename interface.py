import tkinter as tk
from tkinter import filedialog
from criar_pastas import criar_pastas
from mover_src import mover_src

def escolher_pasta():
   pasta = filedialog.askdirectory()
   if pasta:
      print(f'Pasta selecionada: {pasta}')
      label_resultado.config(text=f'Pasta: {pasta}')
      criar_pastas(pasta)
      mover_src(pasta)

# Criar a janela
janela = tk.Tk()
janela.title('Selecionar Pasta')

# Botão
botao = tk.Button(janela, text='Escolher Pasta', command=escolher_pasta)
botao.pack(pady=10)

# Label pra mostrar a pasta escolhida
label_resultado = tk.Label(janela, text='Nenhuma pasta selecionada.')
label_resultado.pack()

# Iniciar loop da interface
janela.mainloop()
