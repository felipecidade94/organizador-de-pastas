import os
from pathlib import Path

def criar_pastas(caminho):
   try:
      arquivos = os.listdir(caminho)
   except FileNotFoundError:
      print(f"Pasta '{caminho}' não encontrada.")
      return
   os.makedirs(f'{caminho}/src', exist_ok=True)
   for arquivo in arquivos:
      caminho_arquivo = os.path.join(caminho, arquivo)
      if os.path.isfile(caminho_arquivo):
         extensao = Path(caminho_arquivo).suffix
         print(f"Arquivo: {arquivo} | Extensão: {extensao}")
         os.makedirs(f'{caminho}/src/{extensao[1:]}', exist_ok=True)

