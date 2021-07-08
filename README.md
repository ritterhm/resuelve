# Evaluación Backend Resuelve tu Deuda


## Requirements

To run this project you only need python 3.8 or higher installed. This project
don't use any external libraries.

Optionally you can install [gunicorn3](https://gunicorn.org/) for performance
reasons due to default command can only process a petition by time. If you
still need better performance you can easily append
[Nginx](https://docs.gunicorn.org/en/stable/deploy.html) to stack.


## API

The project only counts with an API mapped to root path `/`.


## Return HTTP Status Codes

| Code | Returned when... |
| ------------- |:-------------:|
| 200 | All it's ok. You should expect calculated data. |
| 400 | Bad formed or incorrect data in request json. |
| 404 | Any path other than `/`. |
| 405 | For all HTTP request methods except `POST`. |
| 500 | Programing error in service code. Error can be shown in terminal or log in case of using Nginx |


## Configuration

By default service run in port 8080 in localhost `http://localhost:8080/` if
you want to change the port you can edit `PORT` in line 36 inside `wsgi.py`
file.

For the gunicorn wraper `ghttpd.sh` you can change `port` variable in line 17.


## Runing the Service

1. Download code in a local machine.
2. Enter `src/` directory in project path.
3. Run the following command as suitable for your operating system.
	a. For windows: `python wsgi.py`.
	b. For Linux and Mac: `python3 wsgi.py`.
	c. If you have gunicorn3 installed optionally you can run (only for linux) `bash ghttpd.sh`.


## Test Example (Linux)

You can use any tool you want for but a simple test example can be done in CLI.
To enable this a file test.json file is included in project.

To do a test a terminal and type the next commands:

```
	$ cd $project_path/data
	$ curl -d @test.json -H "Content-Type: application/json" -v -X POST http://localhost:8080
```
