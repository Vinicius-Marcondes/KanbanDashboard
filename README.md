# KanbanDashboard
A Kanban Dashboard using Javascript and Python as a first project to learn new technologies and as a portfolio
![Python application](https://github.com/Vinicius-Marcondes/KanbanDashboard/workflows/Python%20application/badge.svg)
## Using the API
### Insert a user 
Pass a json object as bellow
```json
{
  "username": "your_username",
  "full_name": "your_beautiful_name",
  "email": "your_badass_email",
  "password": "super_secret_password",
  "cpf": "11111111111",
  "role": 1
}
```

### Deleting data from db 
Pass to the API the ID of the item you want to delete
```python3
>>> get("project_url/api/delete/1").json()
```
returns:
```json
{
  "1": "Deleted"
}
```
### Update data from db
Query the json with the updates passing the id of the item you want to update
```python3
>>> post("project_url/api/update/1",json{"name":"your_new_beautiful_name"}).json()
```
returns:
```json
{
  "id": "1",
  "name": "your_new_beautiful_name"
}
```
### Returning data from db
```python3
>>> get("project_url/api/show").json()
```
returns:
```json
{
  "username": "your_username",
  "full_name": "your_beautiful_name",
  "email": "your_badass_email",
  "password": "super_secret_password",
  "cpf": "11111111111",
  "role": 1
}
...
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
