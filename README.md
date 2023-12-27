# fastapi_poc

## Conda

I'm having problems running this app using a conda environment.  For now, use venv instead.

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
python3 -m uvicorn main:app --reload
```

## API Docs

[Swagger UI](http://127.0.0.1:8000/docs)
[Redoc](http://127.0.0.1:8000/redoc)
