# File to JSON Converter

Ferramenta CLI em Python para converter arquivos **CSV, XLSX e PDF** em **JSON**.

## 🚀 Funcionalidades

* Converter arquivos CSV para JSON
* Converter planilhas XLSX para JSON
* Extrair texto de PDFs para JSON
* CLI simples de usar

## 📦 Instalação

```bash
git clone https://github.com/luanamcrs/file-to-json.git
cd file-to-json

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## ▶️ Uso

```bash
python convert.py arquivo.csv
```

Definir saída:

```bash
python convert.py arquivo.csv -o resultado_csv.json
```

## 📁 Estrutura do projeto

```
file-to-json
│
├── converters
│   ├── csv_converter.py
│   ├── xlsx_converter.py
│   └── pdf_converter.py
│
├── convert.py
├── requirements.txt
└── README.md
```
