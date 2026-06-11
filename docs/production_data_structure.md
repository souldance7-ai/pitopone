# Production Data Structure

This project uses simple CSV files so that engineers can start from Excel-like data and gradually move toward automated analysis.

## Recommended columns

| Column | Description |
|---|---|
| date | Production date |
| product | Product name or product code |
| thickness_um | Film thickness in micrometers |
| grade | Quality grade, such as A1, A2, B, or C |
| weight_kg | Output weight in kilograms |
| remarks | Optional observation |

## Example

```csv
date,product,thickness_um,grade,weight_kg,remarks
2026-06-01,GC100,100,A1,125.5,synthetic sample
2026-06-01,GC100,100,A2,42.8,synthetic sample
2026-06-01,GC100,100,B,18.2,synthetic sample
```

## Notes

A1 and A2 can be grouped into A-grade when calculating product-level quality yield.
