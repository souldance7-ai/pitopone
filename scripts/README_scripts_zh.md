# scripts 说明

## production_summary.py

按日期、产品、等级统计重量。

## product_grade_statistics.py

按产品统计 A/B/C 等级重量与比例，其中 A1 + A2 合并为 A。

## yield_analysis.py

计算产品别 A 等级良率。

## report_table_generator.py

把 CSV 转成 Markdown 报告表格。

## csv_schema_checker.py

检查 CSV 是否包含必要字段：

- date
- product
- thickness_um
- grade
- weight_kg
