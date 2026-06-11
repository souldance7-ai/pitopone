"""Production summary utility.

This script summarizes synthetic production output by date, product, and grade.
It is designed for non-confidential engineering workflow demonstration.
"""

from pathlib import Path
import pandas as pd


def summarize_production(file_path: str | Path) -> pd.DataFrame:
    """Summarize production data by date, product, and grade."""
    df = pd.read_csv(file_path)
    required_columns = {"date", "product", "grade", "weight_kg"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    summary = (
        df.groupby(["date", "product", "grade"], as_index=False)["weight_kg"]
        .sum()
        .sort_values(["date", "product", "grade"])
    )

    return summary


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    input_file = root / "examples" / "sample_production_data.csv"
    output_file = root / "examples" / "sample_output_production_summary.csv"

    result = summarize_production(input_file)
    result.to_csv(output_file, index=False)
    print(result)
    print(f"\nSaved summary to: {output_file}")
