# Quality Analysis Method

This document describes a general method for summarizing quality grade distribution in manufacturing output.

## Key indicators

- total output weight;
- product-level output weight;
- A-grade weight;
- B-grade weight;
- C-grade weight;
- A-grade ratio;
- downgrade ratio;
- daily and product-level trend.

## Grade grouping

For many manufacturing reports, A1 and A2 are grouped as total A-grade:

```text
A_total = A1 + A2
```

The ratio can be calculated as:

```text
grade_ratio = grade_weight / product_total_weight
```

## Example interpretation

If a product has a high B/C ratio, the engineering team may review upstream production conditions, handling records, process trial notes, or quality observation logs.

This project does not define proprietary control limits. Users should define their own limits according to their internal standards.
