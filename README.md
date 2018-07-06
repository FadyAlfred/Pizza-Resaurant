# Restaurant
### External Documentation:

1. [Django](https://docs.djangoproject.com/en/2.0/releases/2.0/)
2. [Markdown](https://bitbucket.org/tutorials/markdowndemo), used for the formatting of this README file.

### Installation:
##### System Dependencies:

1. Install git:  
`sudo apt-get install -y git`
2. Clone or download this repo.
3. Install pip and vitualenv:  
`sudo apt-get install -y virtualenv`  
`sudo apt-get install -y python3-pip`
4. Create a virtual environment:  
`virtualenv -p python3 ~/.virtualenvs/restaurant`
5. Activate the virtual environment:  
`source ~/.virtualenvs/restaurant/bin/activate`
6. Install requirements in the virtualenv:  
`pip3 install -r requirements.txt`

##### Relational database dependencies (PostgreSQL):
1. Install components for Ubuntu:  
`sudo apt-get update`  
`sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib`
2. Switch to **postgres** (PostgreSQL administrative user):  
`sudo su postgres`
3. Log into a Postgres session:  
`psql`
4. Create database with name **restaurant**:  
`CREATE DATABASE restaurant;`
5. Create a database user which we will use to connect to the database:  
`CREATE USER restaurant_user WITH PASSWORD 'restaurant_pass';`
6. Modify a few of the connection parameters for the user we just created:  
`ALTER ROLE restaurant_user SET client_encoding TO 'utf8';`  
`ALTER ROLE restaurant_user SET default_transaction_isolation TO 'read committed';`  
`ALTER ROLE restaurant_user SET timezone TO 'UTC';` 
`ALTER USER restaurant_user CREATEDB;`
7. Give our database user access rights to the database we created:  
`GRANT ALL PRIVILEGES ON DATABASE restaurant TO restaurant_user;`
8. Exit the SQL prompt and the postgres user's shell session:  
`\q` then `exit`
9. Activate the virtual environment:  
`source ~/.virtualenvs/restaurant/bin/activate`
10. Make Django database migrations: 
`python manage.py migrate`

##### Use admin interface:
1. Create an admin user:  
`python manage.py createsuperuser`
2. Run the project locally:  
`python manage.py runserver`
3. Navigate to: `http://localhost:8000/admin/`
 

### API Endpoints
##### Pizza
Method: `GET`  
Endpoint: `/pizza/`  
Description: `List all pizzas from the database`

Method: `POST`  
Endpoint: `/pizza/`  
Payload:  
`{  
    "name": "pizza name",  
    "description": "pizza description"   
}`
Description: `Create new pizza in the database`

Method: `PUT`  
Endpoint: `/pizza/"pizza-id"/`  
Payload:  
`{  
    "name": "new name or old name",  
    "description": "new description or old description"   
}`
Description: `Update existing pizza in the database`

Method: `DELETE`  
Endpoint: `/pizza/"pizza-id"/`  
Description: `Delete existing pizza in the database`

##### Order
Method: `GET`  
Endpoint: `/order/`  
Description: `List all orders from the database`

Method: `POST`  
Endpoint: `/order/`  
Payload:  
`{  
    "pizza_id": "pizza id",  
    "pizza_size":"30 or 50 only",
	"customer_name":"customer name",
	"customer_address":"customer address"  
}`
Description: `Create new order in the database`

Method: `PUT`  
Endpoint: `/order/"order-id"/`  
Payload:  
`{  
    "pizza_id": "old record or updated",  
    "pizza_size":"old record or updated",
	"customer_name":"old record or updated",
	"customer_address":"old record or updated"  
}`
Description: `Update existing order in the database`

Method: `DELETE`  
Endpoint: `/order/"order-id"/`  
Description: `Delete existing order in the database`

##### Customer Orders
Method: `GET`  
Endpoint: `customer/"customer-name"/orders/` 
Description: `List all customer orders from the database`

