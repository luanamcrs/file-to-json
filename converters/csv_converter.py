import pandas as pd


def convert_csv(file_path):
    df = pd.read_csv(file_path)

    return {
        "type": "csv",
        "rows": len(df),
        "columns": list(df.columns),
        "data": df.to_dict(orient="records")
    }