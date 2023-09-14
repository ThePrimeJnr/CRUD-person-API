# 🚀 CRUD Person API - HNGx Backend SE Intern 🚀

### Project Description

This CRUD Person API is a part of our HNGx backend SE internship project. It allows you to perform Create, Read, Update, and Delete operations on person records.

### Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)

### Installation

To set up this project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/DestinedCodes/CRUD-person-API

# Change into the project directory
cd CRUD-person-API

# Install dependencies
pip install -r requirements.txt

# Run the Api locally
gunicorn run:app
```

### Usage

To use the CRUD Person API, follow these guidelines:

- **Create a Person**
  - URL: `/api`
  - Method: POST
  - Request Body: `{ "name": "John Doe" }`
  - Response: `<name> created successfully` or `400 Bad Request`

- **Get a Person by ID**
  - URL: `/api/<int:user_id>`
  - Method: GET
  - Response: `200 OK` with person details or `404 Not Found`

- **Update a Person by ID**
  - URL: `/api/<int:user_id>`
  - Method: PUT or PATCH
  - Request Body: `{ "name": "Updated Name" }`
  - Response: `<name> updated successfully` or `404 Not Found`

- **Delete a Person by ID**
  - URL: `/api/<int:user_id>`
  - Method: DELETE
  - Response: `<name> deleted successfully` or `404 Not Found`

### Testing

To run tests for the API, use the following command:

```bash
python -m unittest tests/<specific test file>
```

### Deployment

For production deployment, follow these steps:

1. Configure your production environment variables.
2. Set up a production-ready database.
3. Deploy your API using a hosting service or server.

### Contributing

I am open to contributions on related projects from FrontEnd to Backend even Systems Engineering project, you can reachout to me via socials.
