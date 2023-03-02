# vigilant-journey

This a blank canvas! Ready for development, testing, automation, etc!

## Flask-PyMongo Dockerized Application

This is a simple Flask-PyMongo application that connects to a MongoDB database using Docker Compose.

### Prerequisites
- Docker installed on your machine.


### Installation

1. Clone this repository.

2. Navigate to the root directory of the project.

3. Run the following command to build the Docker containers:

`docker-compose build`

Start the Docker containers using the following command:


`docker-compose up`


5. Open a web browser and navigate to http://localhost:8000/ to see the application running.


### Code Structure
The code is structured in the following way:

-  **app.py**: This file contains the Flask-PyMongo application code that connects to the MongoDB database.

-  **Dockerfile**: This file contains the Docker instructions to build the Python container. 

-  **docker-compose.yml**: This file contains the Docker Compose instructions to start the MongoDB and Python containers.

### Configuration
The application is configured using environment variables. The MONGO_URI environment variable is used to connect to the MongoDB database. It is set in the docker-compose.yml file.

### Docker Compose Configuration
The Docker Compose file docker-compose.yml defines two services: mongo and python.

### mongo
This service uses the official MongoDB Docker image. It exposes port 27017 and maps the ./mongo-data directory on the host to /data/db inside the container.

### python
This service builds a Docker image using the Dockerfile in the root directory of the project. It depends on the mongo service and exposes port 8000. It sets the MONGO_URI environment variable to mongodb://my-mongo-container:27017/mydatabase.

### networks
This section defines a bridge network called my-network that both services use to communicate with each other.

### Conclusion
This is a simple Flask-PyMongo application that connects to a MongoDB database using Docker Compose. The application can be easily deployed on any machine that has Docker installed.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/pydev2007)
