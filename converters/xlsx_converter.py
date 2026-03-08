import pandas as pd


def convert_xlsx(file_path):
    df = pd.read_excel(file_path)

    return {
        "type": "xlsx",
        "rows": len(df),
        "columns": list(df.columns),
        "data": df.to_dict(orient="records")
    }