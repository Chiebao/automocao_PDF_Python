from PyPDF2 import PdfMerger
import os

ARQUIVO_FINAL = "PDFfinal.pdf"

# Usa a pasta "arquivos" se ela existir; senão, a pasta do próprio script
pasta = "arquivos" if os.path.isdir("arquivos") else "."

# Lista os PDFs em ordem alfabética, ignorando o arquivo final gerado antes
lista_arquivos = sorted(
    arquivo for arquivo in os.listdir(pasta)
    if arquivo.lower().endswith(".pdf") and arquivo != ARQUIVO_FINAL
)
print("Arquivos que serão mesclados:", lista_arquivos)

merger = PdfMerger()
for arquivo in lista_arquivos:
    merger.append(os.path.join(pasta, arquivo))

merger.write(ARQUIVO_FINAL)
merger.close()
print(f"Pronto! {len(lista_arquivos)} arquivos mesclados em {ARQUIVO_FINAL}")
