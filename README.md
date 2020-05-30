# KanbanDashboard
A Kanban Dashboard using Javascript and Python as a first project to learn new technologies and as a portfolio
## Using the API
### Insert a user 
Pass a json object as bellow (Method=POST)
```json
{
  "name": "your_beautiful_name",
  "email": "your_badass_email"
}
```

### Deleting data from db (METHOD=GET)
Pass to the API the ID of the item you want to delete (i.e.) "http://project_url:5000/api/delete/<id>", returns:
```shell script
{
  "deleted_id": "Deleted"
}
```
### Update data from db (METHOD=POST)
Query the json with the updates passing the id of the item you want to update (i.e.) "http://project_url:5000/api/update/<id>" with this json {"name":"your_new_beautiful_name"}, returns 
```json
{
  "id": "int",
  "name": "your_new_beautiful_name"
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
flask run
```

### 

#### Things used
* Flask (Micro Framework)
  * flask_marshmallow
  * flask_sqlalchemy
* SQLAlchemy
* Marshmallow
* Postgres
* Docker
* Docker-Compose
