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
Returns:
```
{
  "data": {
    "email": "your_badass_email",
    "password": "hashed_password",
    "role": 1,
    "username": "your_username"
  },
  "message": "User created",
  "resource": "Users",
  "status": 200
}
```

### Deleting data from db 
Pass to the API the ID of the item you want to delete
```python3
>>> delete("project_url/admin/api/users/id").json()
```
Returns:
```json
{
  "data": {
    "active": true,
    "cpf": "11111111111",
    "date_created": "2020-06-10T00:02:39.039469",
    "email": "your_badass_email",
    "full_name": "your_beautiful_name",
    "id": 48,
    "password": "hashed_password",
    "role": 1,
    "username": "your_username"
  },
  "message": "User deleted",
  "resource": "Users",
  "status": 200
}
```
### Update data from db
Query the json with the updates passing the id of the item you want to update. If you are updating a password you need to confirm it
```python3
>>> payload = {"name":"your_new_beautiful_name","password": "super_secret_password", "confirm_password": "super_secret_password"}
>>> put("project_url/admin/api/users/id",json=payload).json()
```
returns:
```json
{
  "full_name": "your_new_beautiful_name",
  "password": "super_secret_password",
  "confirm_password": "super_secret_password"
}
```
### Listing users
You can list the users in pages, the default page size is 10, bu you can change it passing via GET

Using default page size:
```python3
>>> get("project_url/admin/api/users/page/1").json()
```
Returns:
```
{
  "data": [
    {user01_data},
    {user02_data},
    {user03_data},
    {user04_data},
    ...  
  ],
  "message": "List paginated users",
  "page": 1,
  "pages": 1,
  "params": {
    "page_id": 1,
    "page_size": 10
  },
  "resource": "User",
  "status": 200,
  "total": 3
}
```
Using custom page size:
If you have more users than the page size you can change the number of the page (e.g) If you have 7 users and set gaze_size=1 you can chose the page number up to 7.
```python3
>>> get("project_url/admin/api/users/page/page_number?page_size=2").json()
```
Returns:
```
{
  "data": [
    {user01_data},
    {user02_data}
  ],
  "message": "List paginated users",
  "page": 1,
  "pages": 2,
  "params": {
    "page_id": 1,
    "page_size": 2
  },
  "resource": "User",
  "status": 200,
  "total": 3
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
  * flask_restful
* SQLAlchemy
* Marshmallow
* Postgres
* Docker
* Docker-Compose
