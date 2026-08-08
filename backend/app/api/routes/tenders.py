from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.tender import (
    TenderCreate,
    TenderResponse,
    TenderUpdate
)
from app.services.tender_service import TenderService


router = APIRouter(
    prefix="/tenders",
    tags=["Tenders"]
)


@router.post("/", response_model=TenderResponse)
def create_tender(
    tender_data: TenderCreate,
    db: Session = Depends(get_db)
):
    try:
        return TenderService.create_tender(
            db,
            tender_data
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )



@router.get("/", response_model=list[TenderResponse])
def get_tenders(
    company_id: int | None = None,
    status: str | None = None,
    search: str | None = None,
    db: Session = Depends(get_db)
):
    return TenderService.get_tenders(
        db,
        company_id,
        status,
        search
    )




@router.get("/{tender_id}", response_model=TenderResponse)
def get_tender(
    tender_id: int,
    db: Session = Depends(get_db)
):
    tender = TenderService.get_tender(
        db,
        tender_id
    )

    if tender is None:
        raise HTTPException(
            status_code=404,
            detail="Tender not found"
        )

    return tender


@router.put("/{tender_id}", response_model=TenderResponse)
def update_tender(
    tender_id: int,
    tender_data: TenderUpdate,
    db: Session = Depends(get_db)
):
    try:
        return TenderService.update_tender(
            db,
            tender_id,
            tender_data
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
@router.delete("/{tender_id}")
def delete_tender(
    tender_id: int,
    db: Session = Depends(get_db)
):
    try:
        return TenderService.delete_tender(
            db,
            tender_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )