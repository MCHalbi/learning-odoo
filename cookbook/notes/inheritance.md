# Inheritance mechanisms
1. [classical inheritance / in-place extension](#classical-inheritance-%2F-in-place-extension)
2. [prototype inheritance](#prototype-inheritance)
3. [mixins](#mixins)
4. [delegation inheritance](#delegation-inheritance)

## classical inheritance / in-place extension
### Effect on Database
Adds the new model fields to the database table of the existing parent model.

### Effects on ORM API
New / modified fields and methods are accessible from the new model.
Records of the parent model do not know about these fields and methods.

### Syntax
- Set the field `_inherit` to a model name but do not define `_name`.
- Fields and methods can be added by defining athem in the child model.
- Fields from the parent model can be modified by defining a field with the same name as in the parent model in the
  child model and setting the desired attributes. Attributes omitted in the child model fields are left as in the parent
  model.
- Methods from the parent model can be extended by calling `super()`

### Example
*library_app/models/library_book.py:*
```python
import odoo import fields, models

class Book(models.Model):
    _name = "library.book"
    _description = "Book"
    ...
    isbn = fields.Char("ISBN")
    ...
    def _check_isbn(self):
        ...
```

*library_member/models/library_book.py:*
```python
import odoo import fields, models

class Book(models.Model):
    _inherit = "library.book"  # make "library.book" the parent model
    ...
    isbn = fields.Char(help="Use a valid ISBN-13 or ISBN-10.")  # extend isbn field by help attribute
    ...
    def _check_isbn(self):
        ...
        if len(isbn) == 10:
            ...  # adding check logic for ISBN-10
        else:
            return super()._check_isbn()  # call ISBN-13 check of parent model
```

## prototype inheritance
### Effect on Database
Copies the parent model table and adds the new fields to the child model table.

### Effects on ORM API
New / modified fields and methods are accessible from the new model.
Records of the parent model do not know about these fields and methods.

### Syntax
- Set `_inherit` to a model name and set `_name` to a name different to the name of the parent model
- Fields and methods can be added by defining them in the child model.
- Fields from the parent model can be modified by defining a field with the same name as in the parent model in the
  child model and setting the desired attributes. Attributes omitted in the child model fields are left as in the parent
  model.
- Methods from the parent model can be extended by calling `super()`

## mixins
Creates model which is composed from the fields and methods from the mixin models.
Mixin models are usually not meant to be used standalone and inherit from `models.AbstactModel`.

### Effect on Database
Creates a new model table in the database which contains all fields from the mixin models.

### Effects on ORM API
All methods and fields of the used mixin classes are available from records of the new model.

### Syntax
- Set `_inherit` to a list of model names and set `_name` to a name different to the name of the parent model.

### Example
```python
class Member(models.Model):
    _name = "library.member"
    _description = "Library Member"
    _inherit = ["mail.thread", "mail.activity.mixin"]
```

## delegation inheritance
Creates a model which has all fields of a given parent model without duplicating database tables.

### Effect on Database
Creates a parent model record for every child model record. The child model has a foreign key to the parent model.

### Effects on ORM API
- Fields of the parent model(s) are directly available from the child model:
  `child_model.parent_field`
- Methods from the parent model must be called by using dot notation:
  `child_model.parent_model_id.parent_method()`

### Syntax
- Option 1: Set `detegate=True` in a Many2one field.
- Option 2: User `_inherits` field

### Example
With `delegate` attribute:
```python
from odoo import fields, models

class Member(models.Model):
    _name = "library.member"
    _description = "Library Member"
    ...
    partner_id = fields.Many2one(
        "res.partner",
        delegate=True,  # user delegation inheritance
        ondelete="cascade",  # delete Partner record if Library Member record is deleted
        required=True  # create Partner record on Library Member record creation
    )
```

With `_inherits`:
```python
from odoo import fields, models

class Member(models.Model):
    _name = "library.member"
    _description = "Library Member"
    _inherits = {"res.partner": partner_id}
    ...
    partner_id = fields.Many2one(
        "res.partner",
        ondelete="cascade",  # delete Partner record if Library Member record is deleted
        required=True  # create Partner record on Library Member record creation
    )
```
