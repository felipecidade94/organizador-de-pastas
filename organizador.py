import os
import shutil
from pathlib import Path
def criar_pastas(caminho):
   try:
      arquivos = os.listdir(caminho)
   except FileNotFoundError:
      print(f"Pasta '{caminho}' não encontrada.")
      return

   for arquivo in arquivos:
      caminho_arquivo = os.path.join(caminho, arquivo)
      if os.path.isfile(caminho_arquivo):
         extensao = Path(caminho_arquivo).suffix
         print(f"Arquivo: {arquivo} | Extensão: {extensao}")
         pasta = f'{caminho}/{extensao[1:]}'
         os.makedirs(pasta, exist_ok=True)

def mover(caminho):
   try:
      arquivos = os.listdir(caminho)
   except FileNotFoundError:
      print(f"Pasta '{caminho}' não encontrada.")
      return

   for arquivo in arquivos:
      caminho_arquivo = os.path.join(caminho, arquivo)
      if os.path.isfile(caminho_arquivo):
         extensao = Path(caminho_arquivo).suffix
         print(f"Arquivo: {arquivo} | Extensão: {extensao}")
         pasta = f'{caminho}/{extensao[1:]}'
         shutil.move(caminho_arquivo, f'{pasta}/{arquivo}')
         
if __name__ == "__main__":
   pasta_alvo = "./testes"  # Crie essa pasta e coloque arquivos lá para testar
   criar_pastas(pasta_alvo)
   mover(pasta_alvo)