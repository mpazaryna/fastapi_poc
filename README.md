# fastapi_poc

## Conda

```sh
# create and activate a new enviroment
conda create --name fastapi_poc python=3.12 
conda activate fastapi_poc
```

## Create Python environment

```sh
python3 -m venv venv
source venv/bin/activate
deactivate
```

```sh
# when running locally, otherwise I get a error
python3 -m uvicorn server:app --reload
```

## API Docs

[Swagger UI](http://127.0.0.1:8000/docs)
[Redoc](http://127.0.0.1:8000/redoc)

## Refactor main.py to server.py

To refactor your server.py for better code separation and maintainability, you can extract the route handlers and configurations into separate modules. The goal is to have serve.py primarily serve as a router and entry point to your application, while the business logic and configurations are managed in their respective modules.
