# routes/root_routes.py

from fastapi import APIRouter, Depends

from dependencies.api_key_dependency import check_custom_api_key

router = APIRouter()


@router.get("/", dependencies=[Depends(check_custom_api_key)])
def read_root():
    return {"Hello": "World"}
