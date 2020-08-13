# INVENTORY MODULE
Item module for microservices.


# FEATURES:
1. Get items - Users with login credentials
2. Post/Put/Update - Admin with login credentials (Restaurants, Ecommerce, etc.)


# SETUP
1. Install requirements:
    `pip install -r requirements.txt`
2. Create .env file with the following variables:
    `
    FLASK_APP="app.py"
    APP_SETTINGS="<testing/development/staging/production>"
    SECRET="<create_your_own>"
    DATABASE_URL="mysql://<username>:<password>@<host>:<port>/<database_name>"
    TEST_DATABASE_URL="mysql://<username>:<password>@<host>:<port>/<database_name>"
    `
3. Build docker container:
