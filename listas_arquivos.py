import os

def listar_arquivos_e_extensoes(caminho):
   try:
      arquivos = os.listdir(caminho)
   except FileNotFoundError:
      print(f"Pasta '{caminho}' não encontrada.")
      return

   for arquivo in arquivos:
      caminho_arquivo = os.path.join(caminho, arquivo)
      if os.path.isfile(caminho_arquivo):
         _, extensao = os.path.splitext(arquivo)
         print(f"Arquivo: {arquivo} | Extensão: {extensao}")
         os.makedirs(extensao[1:], exist_ok=True)


if __name__ == "__main__":
   pasta_alvo = "./teste"  # Crie essa pasta e coloque arquivos lá para testar
   listar_arquivos_e_extensoes(pasta_alvo)