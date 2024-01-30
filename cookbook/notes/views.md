# Views
*Odoo Documentation:
  [[14.0](https://www.odoo.com/documentation/14.0/developer/reference/addons/views.html)]
  [[16.0](https://www.odoo.com/documentation/16.0/developer/reference/backend/views.html)]*

- Stored in the database table `ir.ui.view`:
- Backend:
    - **Einstellungen > Technisch > Benutzer-Interface > Ansichten**
    - **Settings > Technical > User Interface > Views**

## Basic Structure
```xml
<record id="MODEL_view_TYPE" model="ir.ui.view">
    <field name="name">NAME</field>
    <field name="model">MODEL</field>
    <field name="arch" type="xml">
        <view>
    </field>
</record>
```

## List View
*Odoo Documentation:
  [[14.0](https://www.odoo.com/documentation/14.0/developer/reference/addons/views.html#list)]
  [[16.0](https://www.odoo.com/documentation/16.0/developer/reference/backend/views.html#list)]*

## Form View
*Odoo Documentation:
  [[14.0](https://www.odoo.com/documentation/14.0/developer/reference/addons/views.html)]
  [[16.0](https://www.odoo.com/documentation/16.0/developer/reference/backend/views.html)]*

## Search View
*Odoo Documentation:
  [[14.0](https://www.odoo.com/documentation/14.0/developer/reference/addons/views.html)]
  [[16.0](https://www.odoo.com/documentation/16.0/developer/reference/backend/views.html)]*

