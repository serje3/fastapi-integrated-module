from fastapi import APIRouter, HTTPException
from fastapi.openapi.models import Response, Header

router = APIRouter(
    prefix="/datasets",
    tags=["Datasets"]
)


@router.get("/{dataset_name}")
def get_dataset(dataset_name):
    try:
        with open("datasets/" + dataset_name + ".csv", "r") as f:
            response_body = f.read()
    except FileNotFoundError as e:
        return HTTPException(404, "File not found exception")
    return response_body
