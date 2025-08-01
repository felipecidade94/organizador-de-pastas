from criar_pastas import criar_pastas
from mover import mover

if __name__ == '__main__':
   pasta_alvo = './testes'
   criar_pastas(pasta_alvo)
   mover(pasta_alvo)