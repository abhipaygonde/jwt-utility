# jwt-utility

## Background

This utility is used to generate a JSON Web Token using Python language and some opensource libraries. 

JWT contains the below claims:

#### 1. iat - Timestamp of the request as specified by the specification
#### 2. jti - A cryptographic nonce which is unique
#### 3. payload - A json payload of the structure: {"data": "input data", "date": "today's date"} where data is a parameter that the utility accepts as it's input

## Prerequisites

1.  Docker and Docker compose installed on the machine

## Quick Start Guide

### Using Docker Compose

```sh

# Start the services using docker compose
docker-compose -p jwt-utility -f docker-compose.yaml up -d

# Shutdown the services
docker-compose -p jwt-utility -f docker-compose.yaml down

```
### Using Makefile
> The ```make``` utility defines set of tasks to be executed. Here we are using make file to build and run the jwt-utility.

```sh
#build the docker image
make build

#run the docker container with the image created
make run
```

### Stopping the Docker container

```sh
docker stop jwt-utility
```

### Fully containerized implementation

#### 1. Build the docker image

```sh
make build
```

#### 2. Start the utility

Start the service and check if whole containers are working well.

```sh
make run
```

#### 3. Finally, Done!

Open in your browser the (http://localhost/docs) service (A FastAPI swagger UI)

> Click on “/get-token” and then click on “Try it Out” and enter the input data in the "Query" text field and then “Execute”. You will the response from the server below that tab. If everything works well you can have the token generated like this :

![Screenshot 2022-11-18 at 1 58 44 PM](https://user-images.githubusercontent.com/18436924/202656351-8a966d6a-c9b2-4632-ae3d-de3690db927f.png)

> Copy this token and go to the second endpoint “/verify-token”, click on “Try it out”, paste the token and execute it in the same way as you executed the previous endpoint. You will see the following screen : 

![Screenshot 2022-11-18 at 2 00 14 PM](https://user-images.githubusercontent.com/18436924/202656675-81769948-465a-4bfc-9be3-5253edbf80fd.png)

This response is for a valid token, now change the token and execute it again. You will now see the exception saying that “JWT Token Validation Failed”.

![Screenshot 2022-11-18 at 2 05 24 PM](https://user-images.githubusercontent.com/18436924/202657627-0fee8108-bba0-4df0-a275-93e7fe42208a.png)

or open terminal and paste the below curl requests:

```sh
# get token curl request
curl -X 'GET' \
  'http://localhost/get-token?q=demo_token' \
  -H 'accept: application/json'
  
#verify token curl request
curl -X 'GET' \
  'http://localhost/verify-token?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJwYXlsb2FkIjp7ImRhdGEiOiJkZW1vX3Rva2VuIiwiZGF0ZSI6IjIwMjItMTEtMTgifSwiaWF0IjoxNjY4NzYwMDQ2LCJqdGkiOiJ2eFlSN3llb25hd1V1OXZCaEZlWlpYL3Z0a1RVWW9qZ05CdHE2cWpjN2lKVW1zM2JRRDdjajNjZ2RrcjVEbHl5WkxjWE03bmFPanNia25xTUl6WVJDUT09In0.27ASahwIR0A4g5MFRWFP15Wdz3rqaWjLsCjFnn22r5rTqvLS5ssdDh837F4gevjIKYoDnoWM3jYuF_sxInO1XA' \
  -H 'accept: application/json'

 ```
