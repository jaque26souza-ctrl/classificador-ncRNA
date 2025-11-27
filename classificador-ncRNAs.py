# Classificador de ncRNAs
# Projeto PyLadies - Jaqueline Alves de Souza 

# Função para ler um arquivo fasta
def ler_fasta(caminho_fasta):
    sequencias = {}
    nome = None 
    seq = []

    