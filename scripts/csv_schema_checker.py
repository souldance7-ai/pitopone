"""CSV schema checker for manufacturing data.

This tool checks whether a CSV file contains required columns.
It is designed for simple engineering data validation.
"""

from pathlib import Path
import pandas as pd


REQUIRED_COLUMNS = {"date", "product", "thickness_um", "grade", "weight_kg"}


def check_schema(file_path: str | Path) -> None:
    df = pd.read_csv(file_path)
    columns = set(df.columns)
    missing = REQUIRED_COLUMNS - columns

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    print("CSV schema check passed.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    sample_file = root / "examples" / "sample_production_data.csv"
    check_schema(sample_file)
