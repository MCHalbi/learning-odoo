# Odoo Cheatsheet
1. [Models](#models)
1. [Security groups](#security-groups)
1. [Access rules](#access-rules)

## Models
- Database table: `ir.model`
- Backend: **Einstellungen > Technisch > Datenbankstruktur > Modell-Abhängigkeiten**

#### Example
*models/library_book.py*
```python
from odoo import model, fields

class Book(models.Model):
    _name = "library.book"
    _description = "Book"

    name =  fields.Char("Title", required=True)
```

## Security groups
- Database table: `res.groups`.
- Backend: **Einstellungen > Benutzer und Unternehmen > Gruppen**

#### Example
*security/library_security.xml:*
```xml
<odoo>
  <data>
    <record id="library_group_user" model="res.group">
      <field name="name">User</field>
      <filed name="implied_ids"
        eval="[(4, ref('base.group_user'))]" />
  </data>
</odoo>
```

| Field | Example | Explanation |
| --- | --- | --- |
| `record.id` | `library_group_user` | XML ID of the security group |
| `record.model` | `res.group` | model name of the security group model |
| field `name` | User | Name of the group |
| field `implied_ids` |  | List of groups to which a user of this group is also added |

## Access rules
- Database table: `ir.model.access`.
- Backend: **Einstellungen > Technisch > Sicherheit > Zugriffsrechte**

#### Example
*security/ir.model.access.csv:*
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_book_user,BookUser,model_library_book,library_group_user,1,1,1,0
```

| Field | Example | Explanation |
| --- | --- | --- |
| `id` | `access_book_user` | XML ID of access rule |
| `name` | `BookUser` | access rule display name |
| `model_id` | `model_library_book` | model XML ID |
| `group_id` | `library_group_user` | group XML ID |
| `perm_read` | `1` | Boolean flag for read permissions |
| `perm_write` | `1` | Boolean flag for write permissions |
| `perm_create` | `1` | Boolean flag for create permissions |
| `perm_unlink` | `0` | Boolean flag for delete permissions |
