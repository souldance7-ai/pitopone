# 第 3 天：新增制程验证 CSV 范例

本次新增文件：

```text
examples/process_trial_sample_data.csv
```

## 文件用途

这个 CSV 是一个通用化、合成化、非机密的 PI 膜产业化制程验证样例数据。  
它用于展示如何把现场试验记录拆成可统计、可比较、可生成报告的数据字段。

## 重点字段说明

| 字段 | 说明 |
|---|---|
| trial_id | 制程验证编号 |
| date | 日期 |
| product | 产品代号，使用合成名称 |
| thickness_um | 厚度，单位 um |
| trial_stage | 验证阶段，例如 pilot / early-trial / production-intro |
| condition_group | 条件组，例如 C1 / C2 / C3 |
| condition_description | 条件说明，已通用化处理 |
| output_weight_kg | 产出重量 |
| grade_a1_kg | A1 等级重量 |
| grade_a2_kg | A2 等级重量 |
| grade_b_kg | B 等级重量 |
| grade_c_kg | C 等级重量 |
| a_total_kg | A1 + A2 合计 |
| a_ratio_pct | A 等级占比 |
| b_ratio_pct | B 等级占比 |
| c_ratio_pct | C 等级占比 |
| main_observation | 主要观察 |
| risk_level | 风险等级 |
| next_action | 下一步建议 |
| remarks | 备注 |

## 开源边界

本文件不包含真实生产数据、真实配方、客户信息、设备参数或公司内部工艺窗口。  
所有数据均为 synthetic sample，仅用于开源项目的数据结构展示。

## 建议 Commit message

```text
Add synthetic process trial CSV example
```
