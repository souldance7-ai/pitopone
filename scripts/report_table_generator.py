"""Generate markdown tables from synthetic production summary data."""

from pathlib import Path
import pandas as pd


def to_markdown_table(file_path: str | Path) -> str:
    """Convert a CSV file into a Markdown table."""
    df = pd.read_csv(file_path)
    return df.to_markdown(index=False)


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    input_file = root / "examples" / "sample_production_data.csv"
    output_file = root / "reports" / "sample_output_report.md"

    markdown_table = to_markdown_table(input_file)
    output_file.write_text(
        "# Sample Production Data Report\n\n" + markdown_table + "\n",
        encoding="utf-8",
    )
    print(f"Saved markdown report to: {output_file}")
