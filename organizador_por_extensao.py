import os
import shutil
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

def mover_src(caminho):
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
         destino = Path(f'{caminho}/src/{extensao[1:]}/{arquivo}')
         if not os.path.exists(destino):
            shutil.move(caminho_arquivo, destino)
         else:
            nome, extensao = os.path.splitext(destino)
            contador = 1
            novo_destino = f'{nome}_{contador}{extensao}'
            while os.path.exists(novo_destino):
               contador += 1
               novo_destino = f'{nome}_{contador}{extensao}'
            shutil.move(caminho_arquivo, novo_destino)

if __name__ == "__main__":
   pasta_alvo = "./testes"  # Crie essa pasta e coloque arquivos lá para testar
   criar_pastas(pasta_alvo)
   mover_src(pasta_alvo)