import argparse
import json
from pathlib import Path

from converters.csv_converter import convert_csv
from converters.xlsx_converter import convert_xlsx
from converters.pdf_converter import convert_pdf


def detect_converter(file_path):
    ext = Path(file_path).suffix.lower()

    if ext == ".csv":
        return convert_csv
    elif ext in [".xlsx", ".xls"]:
        return convert_xlsx
    elif ext == ".pdf":
        return convert_pdf
    else:
        raise ValueError(f"Formato não suportado: {ext}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert CSV, XLSX or PDF files to JSON"
    )

    parser.add_argument(
        "input",
        help="Input file path"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output JSON file name",
        default="output.json"
    )

    args = parser.parse_args()

    input_file = Path(args.input)

    if not input_file.exists():
        print("❌ Arquivo não encontrado.")
        return

    try:
        converter = detect_converter(input_file)
        data = converter(input_file)

        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"✅ Conversão concluída: {args.output}")

    except Exception as e:
        print(f"❌ Erro: {e}")


if __name__ == "__main__":
    main()