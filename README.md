# PI Film Industrialization Toolkit

**PI Film Industrialization Toolkit** is an open-source engineering toolkit for organizing production data, quality records, process trial information, and technical reports in specialized polyimide (PI) film manufacturing workflows.

This project is built for practical industrial engineering work, especially where manufacturing knowledge is often scattered across spreadsheets, screenshots, trial notes, shift records, and one-time reports.

The goal is to provide reusable, transparent, and maintainable workflows for engineers who need to convert complex production information into structured engineering outputs.

## What this project does

This toolkit currently focuses on:

- daily production output summaries;
- product-level production statistics;
- A/B/C grade weight ratio calculation;
- A1 + A2 grouping for A-grade yield analysis;
- synthetic sample data for non-confidential demonstrations;
- Markdown and LaTeX report templates;
- reusable documentation patterns for process trial reports;
- weekly engineering report templates;
- basic Python utilities for manufacturing data analysis.

## Why this project matters

Specialized industrial manufacturing domains often have practical engineering needs that are not well represented in mainstream open-source software.

In PI film industrialization and polymer film manufacturing, engineers repeatedly need to:

1. normalize production data;
2. summarize product-level output;
3. calculate grade distribution;
4. compare process trials;
5. prepare technical reports;
6. preserve engineering know-how in a structured and reusable form.

This project attempts to bridge real manufacturing practice and modern AI-assisted engineering documentation.

## Non-confidential principle

This repository **does not include**:

- proprietary production recipes;
- customer data;
- company-specific production parameters;
- confidential process windows;
- private equipment settings;
- internal commercial information.

All examples are anonymized, generalized, or fully synthetic. The repository is intended to provide reusable workflow structures rather than disclose any proprietary manufacturing know-how.

## Repository structure

```text
docs/       General engineering workflow documentation
templates/  Markdown and LaTeX report templates
scripts/    Python utilities for production and quality data analysis
examples/   Synthetic datasets and generated sample outputs
reports/    Example report output folder
.github/    Issue templates for open-source collaboration
```

## Quick start

Install dependencies:

```bash
pip install -r requirements.txt
```

Run sample production summary:

```bash
python scripts/production_summary.py
```

Run product grade statistics:

```bash
python scripts/product_grade_statistics.py
```

Run A-grade yield analysis:

```bash
python scripts/yield_analysis.py
```

Generate a Markdown report:

```bash
python scripts/report_table_generator.py
```

## Example data format

```csv
date,product,thickness_um,grade,weight_kg,remarks
2026-06-01,GC100,100,A1,125.5,synthetic sample
2026-06-01,GC100,100,B,18.2,synthetic sample
```

## Intended users

This project may be useful for:

- PI film process engineers;
- polymer film manufacturing teams;
- industrial engineering managers;
- quality engineers;
- technical documentation maintainers;
- manufacturing teams adopting AI-assisted reporting workflows.

## Roadmap

- Add Excel-ready export utilities.
- Add automated chart generation.
- Add more synthetic process trial examples.
- Add bilingual Chinese/English engineering templates.
- Add validation utilities for production data quality.
- Add optional LaTeX PDF report generation workflow.

## License

This project is released under the MIT License.
