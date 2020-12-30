# Docker-Postgres-Demo

Demo Application that shows Flask interacting with PostgreSQL within Docker Containers


## Setup

Start the demo application by running the following commands:

``` bash
## Create Docker Images
docker-compose build

## Start Containers
docker-compose up -d

## Watch STDOUT Logs
docker-compose logs -f 
```

## Usage

Navigate to the following endpoints to accomplish the desired tasks:

### Visit Homepage

`http://localhost:8081/`


### Add 'Default' Users

`http://localhost:8081/add_default`

### List All Users

`http://localhost:8081/search`

### List Single User

`http://localhost:8081/search/admin`

### Display Search Error

`http://localhost:8081/search/fake`

### Delete User Account

`http://localhost:8081/delete/admin`