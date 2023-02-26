# Headless CRM API
This is a sample project for creating a headless CRM API using the Python FastAPI framework. It includes a SQLite database and features such as user authentication with JWT, CRUD operations for Contacts, Leads, and Events, and unit tests using the Pytest framework.

## Installation
To install this project, first clone the repository:

```
git clone https://github.com/yourusername/headless_crm_api.git
```

Then, create a virtual environment and install the required packages:

```
cd headless_crm_api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration
This project uses a .env file to store configuration variables. You can copy the included .env.sample file to create your own .env file:
Edit the .env file to set your own values for the configuration variables.

## Database
This project uses a SQLite database. You can create the database by running the init_db.py script:

```
python init_db.py
```
This will create a new headless_crm.db file in the instance directory.

## Running the API
To run the API, use the following command:

```
uvicorn app:app --reload
```

This will start the API on http://localhost:8000.

## API Endpoints
The following endpoints are available in the Headless CRM API:

### Contact Endpoints
- GET /contacts: List all contacts.
- GET /contacts/{contact_id}: Get a specific contact.
- POST /contacts: Create a new contact.
- PUT /contacts/{contact_id}: Update an existing contact.
- DELETE /contacts/{contact_id}: Delete an existing contact.

### Lead Endpoints
- GET /leads: List all leads.
- GET /leads/{lead_id}: Get a specific lead.
- POST /leads: Create a new lead.
- PUT /leads/{lead_id}: Update an existing lead.
- DELETE /leads/{lead_id}: Delete an existing lead.

### Event Endpoints
- GET /events: List all events.
- GET /events/{event_id}: Get a specific event.
- POST /events: Create a new event.
- PUT /events/{event_id}: Update an existing event.
- DELETE /events/{event_id}: Delete an existing event.

### Authentication Endpoints
POST /token: Generate an access token for authentication.

## Authentication
The Headless CRM API uses JWT (JSON Web Tokens) for authentication. To access protected endpoints, you must include an access token in the Authorization header of your requests.

To generate an access token, send a POST request to the /token endpoint with your email and password in the request body.

```
{
  "email": "user@example.com",
  "password": "password"
}
```
If your email and password are valid, the API will respond with an access token in the following format:

```
{
  "access_token": "xxxxxxx",
  "token_type": "bearer"
}
```
Include the access_token value in the Authorization header of your requests to protected endpoints.

```
Authorization: Bearer xxxxxxxx
```

## API Documentation
The API documentation is available at http://localhost:8000/docs when the API is running.

## Testing
To run the unit tests, use the following command:

```
pytest --html=report.html
```