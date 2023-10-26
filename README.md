There's two basic ways you can install airflow:
1. locally (where you have to download all the functionalities individually)
2. using Docker (Docker containers provide an isolated environment for running Airflow and its dependencies)

**This will take you through the steps to install Airflow using Docker.**

### STEP 1
The first step is to install Docker, if you don't already have it on your system. You can go to the link below and install Docker for your specific system by following the instructions available there.
 ```bash
    https://docs.docker.com/desktop/
 ```
If you wish to check the successful installation of Docker and Docker-compose (will be done along with Docker) on your system, you can use the following commands:
 ```bash
    docker --version
 ```
 ```bash
    docker-compose --version
 ```

### STEP 2
After this, it is recommended that you make a new folder in your system for airflow-docker, wherein you can download the docker-compose file describing all the services needed by airflow. 
 ```bash
    mkdir airflow-docker
 ```
 ```bash
    cd airflow-docker
 ```

### STEP 3
Here, you need to upload the docker-compose file, which has been made for us by the Airflow community. You can access the .yaml file from here:
 ```bash
    https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
 ```
To deploy Airflow on Docker Compose, you should fetch docker-compose.yaml:
 ```bash
    curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.2/docker-compose.yaml'
 ```

### STEP 4
Run the following command to start and run a set of Docker containers defined in a docker-compose.yml file in Docker Compose:
 ```bash
    docker-compose up
 ```

### STEP 5
You are now ready to access Airflow on one of your browsers:
```bash
   http://localhost:8080/login/
```
The default username and password, both are set as "airflow". 
