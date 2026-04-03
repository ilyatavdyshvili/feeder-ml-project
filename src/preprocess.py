import pandas as pd

def load_data(path):
    df = pd.read_excel(path)

    # обработка чисел
    for col in df.columns[1:]:
        df[col] = df[col].astype(str).str.replace(",", ".")
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.dropna()
    return df
