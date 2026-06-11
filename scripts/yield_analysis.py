"""Simple yield analysis utility for synthetic manufacturing data."""

from pathlib import Path
import pandas as pd


def calculate_a_grade_yield(file_path: str | Path) -> pd.DataFrame:
    """Calculate A-grade yield by date and product."""
    df = pd.read_csv(file_path)
    df = df.copy()
    df["grade_group"] = df["grade"].replace({"A1": "A", "A2": "A"})

    grouped = (
        df.groupby(["date", "product", "grade_group"], as_index=False)["weight_kg"]
        .sum()
    )

    total = (
        grouped.groupby(["date", "product"], as_index=False)["weight_kg"]
        .sum()
        .rename(columns={"weight_kg": "total_weight_kg"})
    )

    a_grade = (
        grouped[grouped["grade_group"] == "A"]
        .groupby(["date", "product"], as_index=False)["weight_kg"]
        .sum()
        .rename(columns={"weight_kg": "a_grade_weight_kg"})
    )

    result = total.merge(a_grade, on=["date", "product"], how="left")
    result["a_grade_weight_kg"] = result["a_grade_weight_kg"].fillna(0)
    result["a_grade_yield_pct"] = (
        result["a_grade_weight_kg"] / result["total_weight_kg"] * 100
    ).round(2)

    return result


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    input_file = root / "examples" / "sample_production_data.csv"
    output_file = root / "examples" / "sample_output_yield_analysis.csv"

    result = calculate_a_grade_yield(input_file)
    result.to_csv(output_file, index=False)
    print(result)
    print(f"\nSaved yield analysis to: {output_file}")
