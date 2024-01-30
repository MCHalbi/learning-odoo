# External identifiers / XML IDs
- Identifies a particular record in Odoo
- Human readable (instead of database id)
- Database ids of records are not persistent through Odoo startups. XML IDs allow us to reference a particular record
  without knowing the actual numerical id of the record.
- Stored in table `ir.model.data`
    - `complete_id`: Composed of module name and XML ID
    - `name`: XML ID
    - `model`: model name of the referenced record
    - `module`: module name in which the XML ID is defined
    - `res_id`: database id of the referenced record
- Data of `ir.model.data` can be viewed in Odoo via
    - **Settings > Technical > Sequences & Identifiers > External Identifiers**
    - **Einstellungen > Technisch > Sequenzen- und Identifizierungsmerkmale > Externe Identifikatoren**

- Example:
  ```
   library_app.menu_library
  |           |            |
  +-----------+------------+
   module name    XML ID
  |                        |
  +------------------------+
         complete ID
  ```
