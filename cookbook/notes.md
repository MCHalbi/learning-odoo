# Odoo Cookbook - Notes
# Section 1: Introduction to Odoo Development
## Chapter 1: Quick Start Using the Developer Mode
## Chapter 2: Preparing the Development Environment
## Chapter 3: Your First Odoo Application
- **addon module** – a directory containing an Odoo manifest file
- **addons directory** – a directory containing several addon modules
- **addons path** – an Odoo configuration, containing a list of directories where
the Odoo-Server looks for addons

By default, there are two directories in the addons path:
- `odoo/addons` – containing the base apps bundled with Odoo
- `odoo/odoo/addons` – containing the Odoo core features

Flags for the `odoo` command:
- `--addons-path` – A list of all directories to use as addon directories
- `-d`/`--database` – The database to use. If it does not exist, it will be created
- `-c`/`--config` – The config file to use


## Chapter 4: Extending Modules
# Section 2: Models
## Chapter 5: Importing, Exporting, and Module Data
## Chapter 6: Models – Structuring the Application Data
# Section 3: Business Logic 
## Chapter 7: Recordsets – Working with Model Data
## Chapter 8: Business Logic – Supporting Business Logic
## Chapter 9: External API – Integrating with Other Systems
# Section 4: Views
## Chapter 10: Backend Views – Designing the User Interface
## Chapter 11: Kanban Views and Client-Side QWeb
## Chapter 12: Creating Printable PDF Reports with Server-Side QWeb
## Chapter 13: Creating Web and Portal Frontend Features
# Section 5: Deployment and Maintenance
## Chapter 14: Understanding Odoo Built-In Models
## Chapter 15: Deploying and Maintaining Production Instances
