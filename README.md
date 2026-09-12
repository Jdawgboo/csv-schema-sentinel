# CSV Schema Sentinel

A dependency-free Python utility that infers simple CSV column types and validates required typed fields.

```bash
python tool.py sample.csv
python -m unittest -v
```

The inferred types are `bool`, `int`, `float`, and `str`. Empty cells are ignored during inference. This is a lightweight data-contract helper, not a replacement for database or full schema-validation systems.
