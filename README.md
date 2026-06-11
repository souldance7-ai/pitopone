# PI Film Industrialization Toolkit

> 面向 PI 膜、聚合物薄膜与制造业工程场景的开源工程工具包。  
> 用于生产数据统计、产品别分析、A/B/C 等级占比、质量跟踪、制程验证报告、周报模板、技术文章沉淀与 AI 辅助工程文档化。

**PI Film Industrialization Toolkit** 是一个把制造现场零散资料转成结构化工程输出的开源项目。  
它不公开任何公司机密、客户资料、真实配方、专有参数或内部工艺窗口，只提供通用化、脱敏化、模板化、可复用的方法。

---

## 项目定位

在 PI 膜产业化、聚合物薄膜制造、石墨导热膜基材、电子级薄膜、TPI/MPI/复合膜等专业领域，很多工程知识并不天然存在于开源世界中。

实际现场资料通常分散在：

- Excel 生产记录；
- 截图与聊天记录；
- 试验记录；
- 质量异常表；
- 周报与会议纪要；
- 技术报告；
- 个人经验判断。

本项目希望把这些内容整理成可复用的开源结构，包括：

- 数据字段标准；
- 统计脚本；
- 报告模板；
- 质量分析方法；
- 制程验证记录格式；
- 技术文章框架；
- AI 辅助工程文档化流程。

---

## 当前内容模块

| 模块 | 内容 |
|---|---|
| `docs/zh_CN/` | 中文项目说明、开源边界、路线图 |
| `docs/articles/` | PI 膜产业化、质量统计、制程验证、石墨导热膜、TPI/MPI 应用等技术文章 |
| `docs/applications/` | 应用场景拆解，如 FPC/FCCL、先进封装、石墨导热膜等 |
| `templates/zh_CN/` | 中文周报、制程验证报告、质量统计报告模板 |
| `examples/zh_CN/` | 中文合成样例数据 |
| `scripts/` | 数据检查、统计与报告生成脚本 |

---

## 适用对象

- PI 膜制程工程师；
- 聚合物薄膜制造工程师；
- 品质工程师；
- 技术管理人员；
- 工艺试验与产业化导入人员；
- 需要把工程经验转成结构化报告的制造业团队；
- 需要用 AI 辅助整理工程资料的开源使用者。

---

## 非机密原则

本项目不包含：

- 公司真实配方；
- 客户资料；
- 内部生产数据；
- 专有设备参数；
- 真实制程窗口；
- 商业合同信息；
- 未公开技术文件。

所有样例均为合成数据或通用化表达，仅用于开源方法展示。

---

## 快速开始

安装依赖：

```bash
pip install -r requirements.txt
```

运行生产统计：

```bash
python scripts/production_summary.py
```

运行等级占比统计：

```bash
python scripts/product_grade_statistics.py
```

检查 CSV 数据字段完整性：

```bash
python scripts/csv_schema_checker.py
```

---

## 推荐阅读顺序

1. [`docs/zh_CN/project_positioning_zh.md`](docs/zh_CN/project_positioning_zh.md)
2. [`docs/zh_CN/open_source_boundary_zh.md`](docs/zh_CN/open_source_boundary_zh.md)
3. [`docs/articles/01_pi_film_industrialization_overview_zh.md`](docs/articles/01_pi_film_industrialization_overview_zh.md)
4. [`docs/articles/02_from_production_data_to_engineering_report_zh.md`](docs/articles/02_from_production_data_to_engineering_report_zh.md)
5. [`docs/articles/03_quality_grade_statistics_method_zh.md`](docs/articles/03_quality_grade_statistics_method_zh.md)
6. [`docs/articles/04_process_trial_documentation_zh.md`](docs/articles/04_process_trial_documentation_zh.md)
7. [`docs/applications/application_map_zh.md`](docs/applications/application_map_zh.md)

---

## Roadmap

- 增加 Excel 美化输出；
- 增加自动图表生成；
- 增加中英文双语技术报告模板；
- 增加更多合成制程验证案例；
- 增加面向质量异常的分析模板；
- 增加 LaTeX PDF 自动生成流程；
- 增加 AI 辅助技术文章整理工作流。

---

## License

MIT License
