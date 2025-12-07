# -----------------------------------------------------------
# Classificador de ncRNAs
# Projeto PyLadies - Jaqueline Alves de Souza
# -----------------------------------------------------------

from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Função para ler um arquivo FASTA simples
def ler_fasta(caminho_arquivo):
    sequencias = {}
    nome = None
    seq = []

    with open(caminho_arquivo, "r") as f:
        for linha in f:
            linha = linha.strip()

            if linha.startswith(">"):
                if nome:
                    sequencias[nome] = "".join(seq)
                nome = linha[1:]
                seq = []
            else:
                seq.append(linha)

        if nome:
            sequencias[nome] = "".join(seq)

    return sequencias


# -----------------------------------------------------------
def classificar_tamanho(seq):
    tamanho = len(seq)

    if tamanho < 18:
        return "Fragmento muito curto"

    if 18 <= tamanho <= 24:
        return "miRNA"
    if 26 <= tamanho <= 31:
        return "piRNA"
    if 60 <= tamanho <= 300:
        return "snoRNA"
    if 100 <= tamanho <= 300:
        return "snRNA"
    if tamanho > 350:
        return "lncRNA"

    return "ncRNA não identificado pelo tamanho"


# -----------------------------------------------------------
def calcular_gc(seq):
    g = seq.count("G")
    c = seq.count("C")
    total = len(seq)

    if total == 0:
        return 0

    gc_percent = (g + c) / total * 100
    return round(gc_percent, 2)


# -----------------------------------------------------------
def interpretar_gc(gc):
    if 40 <= gc <= 60:
        return "GC moderado, comum em miRNAs"
    if gc < 30:
        return "GC baixo, possível lncRNA"
    if gc > 60:
        return "GC alto, menos comum em ncRNAs"
    return "GC dentro do esperado"


# -----------------------------------------------------------
def main():
    print("\n=== Escolha o arquivo FASTA ===\n")

    # Abre janela para escolher arquivo
    Tk().withdraw()
    arquivo = askopenfilename(
        title="Selecione o arquivo FASTA",
        filetypes=[("Arquivos FASTA", "*.fasta *.fa *.txt"), ("Todos os arquivos", "*.*")]
    )

    if not arquivo:
        print("Nenhum arquivo selecionado. Encerrando.")
        return

    sequencias = ler_fasta(arquivo)

    print("\n=== Classificação de ncRNAs ===\n")

    for id_seq, seq in sequencias.items():
        tamanho = len(seq)
        tipo = classificar_tamanho(seq)
        gc = calcular_gc(seq)
        interpretacao = interpretar_gc(gc)

        print(f"ID: {id_seq}")
        print(f"Tamanho: {tamanho} bases")
        print(f"Classificação: {tipo}")
        print(f"GC%: {gc}")
        print(f"Interpretação GC: {interpretacao}")
        print("-" * 40)


# Executa o programa
if __name__ == "__main__":
    main()


    