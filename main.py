from criar_pastas import criar_pastas
from mover_src import mover_src

if __name__ == '__main__':
   pasta_alvo = './testes'
   criar_pastas(pasta_alvo)
   mover_src(pasta_alvo)