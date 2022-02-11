# A Prime Example

<!-- <p><br></br></p> -->

Get started by following the guide below to build this project

## Prerequisites

The project requirements:
 
* Python 3 (3.9)

`Note`: tested using the highlighted versions of the tools

## Build

To build the project to run in as a container, run the below from the project root:

    docker build -t prime-example -f Dockerfile .

    docker docker tag prime-example:latest <owner>/prime-example:latest

    docker push <owner>/prime-example:latest

`Note`: replace the owner of the image repository

## Test

To run and test the app:

Container:
```bash

docker run -it -d --name prime-example prime-example:latest

docker exec -it prime-example python -m main --number 10
['2', '3', '5', '7']

docker exec -it prime-example python -m main --number 20
['2*', '3*', '5*', '7*', '11', '13', '17', '19']

```

Locally:
```bash
python -m virtualenv -p `which python3` .venv

source .venv/bin/activate

python -m main --number 10
['2', '3', '5', '7']

python -m main --number 20
['2*', '3*', '5*', '7*', '11', '13', '17', '19']
```
