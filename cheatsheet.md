# Chapter 1
- Business objects (= Python class)
- Objects view
- Data files
- Web controllers (handles requests)

# Odoo Addon structure
```
<module root>
├─ __init__.py
├─ __manifest__.py
├─ data
│  └─ ...
├─ models
│  ├─ __init__.py
│  └─ ...
├─ tests
│  ├─ __init__.py
│  └─ ...
├─ views
│  └─ ...
└─ security
   └─ ir.model.access.csv
```
