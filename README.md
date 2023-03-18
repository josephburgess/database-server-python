# Python Database Server

This is a simple key-value store application built using Python, Flask, and MongoDB. The application provides two endpoints to set and get key-value pairs and add them to a MongoDB database.

## Requirements

  - Python 3.7 or higher
  - Flask
  - Flask-PyMongo
  - MongoDB

## Installation

  1. Clone this repository:

```bash
git clone https://github.com/yourusername/simple-key-value-store.git
cd simple-key-value-store
```

  2. Create a virtual environment and install the required packages:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

  3. Update the MONGO_URI in app.py to match your MongoDB configuration:

```python
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
```

## Running the application

  1. Start the application by running:
  
```bash
python app.py
```

  The application will be accessible at `http://localhost:5000`.

## API Endpoints

### Set Key-Value

  - Endpoint: /set
  - Method: PUT
  - Query Parameters:
    - key: The key to set the value for
    - value: The value to store for the key
  - Returns:
    - 201 Created: Key-value pair created successfully
    - 400 Bad Request: Missing or invalid input

### Get Key-Value

  - Endpoint: /get
  - Method: GET
  - Query Parameters:
    - key: The key to retrieve the value for
  - Returns:
    - 200 OK: Key-value pair found and returned
    - 400 Bad Request: Missing or invalid input
    - 404 Not Found: Key not found

## Examples

### Set a key-value pair:

```bash
curl -X PUT "http://localhost:5000/set?key=my_key&value=my_value"
```

Response:
```bash
{
  "message": "Created"
}
```

### Get a key-value pair:

```bash
curl "http://localhost:5000/get?key=my_key"
```

Response:
```bash
{
  "message": "OK",
  "value": "my_value"
}
```

## Testing
I used Pytest for testing this project and achieved 100% test coverage. 

To run the test suite for this project, navigate to the project directory in your terminal and run the command:

```bash
pytest
```

This will run all of the test cases in the tests directory.