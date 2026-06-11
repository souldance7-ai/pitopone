"""Product grade statistics utility.

This script calculates A/B/C grade weight ratios by product using synthetic data.
A1 and A2 are grouped as A-grade.
"""

from pathlib import Path
import pandas as pd


def calculate_grade_ratio(file_path: str | Path) -> pd.DataFrame:
    """Calculate grade weight percentage by product."""
    df = pd.read_csv(file_path)
    required_columns = {"product", "grade", "weight_kg"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df = df.copy()
    df["grade_group"] = df["grade"].replace({"A1": "A", "A2": "A"})

    pivot = (
        df.pivot_table(
            index="product",
            columns="grade_group",
            values="weight_kg",
            aggfunc="sum",
            fill_value=0,
        )
        .reset_index()
    )

    for col in ["A", "B", "C"]:
        if col not in pivot.columns:
            pivot[col] = 0.0

    pivot["total_weight_kg"] = pivot[["A", "B", "C"]].sum(axis=1)

    for col in ["A", "B", "C"]:
        pivot[f"{col}_ratio_pct"] = (
            pivot[col] / pivot["total_weight_kg"] * 100
        ).round(2)

    return pivot[
        [
            "product",
            "total_weight_kg",
            "A",
            "B",
            "C",
            "A_ratio_pct",
            "B_ratio_pct",
            "C_ratio_pct",
        ]
    ]


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    input_file = root / "examples" / "sample_production_data.csv"
    output_file = root / "examples" / "sample_output_grade_statistics.csv"

    result = calculate_grade_ratio(input_file)
    result.to_csv(output_file, index=False)
    print(result)
    print(f"\nSaved grade statistics to: {output_file}")
