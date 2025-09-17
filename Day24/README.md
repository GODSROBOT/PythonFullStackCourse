# Day 24: SQL — Normalization

## 📘 Topics Covered

- Why normalize: reduce redundancy, avoid update anomalies
- Normal forms and criteria:
  - 1NF: atomic values, no repeating groups
  - 2NF: remove partial dependencies (on part of a composite key)
  - 3NF: remove transitive dependencies (non-key → non-key)
  - BCNF: every determinant must be a candidate key

## 📄 Scripts

- Normalization examples: [`SQL/normalistaion.sql`](./SQL/normalistaion.sql)

## 🔗 References
- Normalization Intro: https://www.sqltutorial.org/sql-normalization/
- 1NF/2NF/3NF: https://www.guru99.com/database-normalization.html
- BCNF: https://www.geeksforgeeks.org/boyce-codd-normal-form-bcnf/