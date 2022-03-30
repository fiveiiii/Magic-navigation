from fastapi import APIRouter
from server.models.response_data_model import ResponseModel
router = APIRouter()


@router.get("navigations/all_list", response_model=ResponseModel)
def queryAllNavigations():
    return {"data": "all_list"}
