
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.company import (
    CompanyCreate,
    CompanyResponse,
    CompanyUpdate
)
from app.services.company_service import CompanyService


router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)


@router.post("/", response_model=CompanyResponse)
def create_company(
    company_data: CompanyCreate,
    db: Session = Depends(get_db)
):
    return CompanyService.create_company(
        db,
        company_data
    )


@router.get("/", response_model=list[CompanyResponse])
def get_companies(
    db: Session = Depends(get_db)
):
    return CompanyService.get_companies(db)


@router.get("/{company_id}", response_model=CompanyResponse)
def get_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    company = CompanyService.get_company(
        db,
        company_id
    )

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    return company


@router.put("/{company_id}", response_model=CompanyResponse)
def update_company(
    company_id: int,
    company_data: CompanyUpdate,
    db: Session = Depends(get_db)
):
    try:
        return CompanyService.update_company(
            db,
            company_id,
            company_data
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
@router.delete("/{company_id}")
def delete_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    try:
        return CompanyService.delete_company(
            db,
            company_id
        )

    except ValueError as e:
        message = str(e)

        if message == "Company not found":
            raise HTTPException(
                status_code=404,
                detail=message
            )

        if message == "Company cannot be deleted because it has associated tenders":
            raise HTTPException(
                status_code=409,
                detail=message
            )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )