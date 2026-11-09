# Automação para Mesclar PDFs

Script em Python que junta vários arquivos PDF em um único documento, na ordem dos nomes dos arquivos. Resolve uma tarefa repetitiva do dia a dia: consolidar relatórios, contratos ou comprovantes antes de enviar ou arquivar.

---

## Como funciona

1. Lê todos os arquivos `.pdf` da pasta `arquivos/` (se ela não existir, usa a pasta do próprio script).
2. Ordena pelo nome, então basta numerar os arquivos para definir a ordem (`01. ...`, `02. ...`).
3. Mescla tudo com o `PdfMerger` e salva o resultado em `PDFfinal.pdf`.

O próprio `PDFfinal.pdf` é ignorado na leitura, para o script poder ser executado várias vezes sem duplicar páginas.

## Exemplo

Os arquivos `01. PDF.pdf`, `02. Arquivo.pdf` e `03. Ultimo Arquivo.pdf` deste repositório são a entrada de exemplo, e `PDFfinal.pdf` é o resultado.

## Como executar

```bash
pip install PyPDF2
python autoresumo.py
```

## Tecnologias

`Python` `PyPDF2` `os`

## Próximos passos

- Interface gráfica para escolher os arquivos e a ordem
- Opção de selecionar páginas específicas de cada PDF

---

**Luana Godoy** · Estudante de Análise e Desenvolvimento de Sistemas
[LinkedIn](https://www.linkedin.com/in/luana-chiebao) · [GitHub](https://github.com/Chiebao)
