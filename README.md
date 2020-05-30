# KanbanDashboard
A Kanban Dashboard using Javascript and Python as a first project to learn new technologies and as a portfolio
## Using the API
### Insert a user 
Pass a json object as bellow (Method=POST):
```json
{
  "name": "your_beautiful_name",
  "email": "your_badass_email"
}
```
### Returning data from db (METHOD=GET)
```json
{
  "id": "int",
  "name": "your_beautiful_name",
  "email": "your_badass_email"
}
```

### Initializing the API:
```shell script
python3 -m venv venv
. venv/bin/activate
pip3 install -r API/requiriments/dev.txt
cd API
flask run
```

#### Things used
* Flask (Micro Framework)
  * flask_marshmallow
  * flask_sqlalchemy
* SQLAlchemy
* Marshmallow
* Postgres
* Docker
* Docker-Compose
