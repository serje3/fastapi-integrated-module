from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException

from dependencies import get_ml_service
from schema.dataset import Dataset
from services.ml import MachineLearningService

router = APIRouter(
    prefix="/models",
    tags=["Models"]
)


@router.post("/analyze")
def model_analyze(input_dataset: Dataset,
                  ml_service: Annotated[MachineLearningService, Depends(get_ml_service)]) -> List:
    match input_dataset.name:
        case "model1":
            return ml_service.predict_model_1(input_dataset.content)
    raise HTTPException(404, "No machine learning model found")
