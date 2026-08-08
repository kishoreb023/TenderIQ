from sqlalchemy.orm import Session

from app.repositories.company_repository import CompanyRepository
from app.schemas.company import CompanyCreate, CompanyUpdate


class CompanyService:

    @staticmethod
    def create_company(
        db: Session,
        company_data: CompanyCreate
    ):
        return CompanyRepository.create(db, company_data)

    @staticmethod
    def get_companies(db: Session):
        return CompanyRepository.get_all(db)

    @staticmethod
    def get_company(
        db: Session,
        company_id: int
    ):
        return CompanyRepository.get_by_id(db, company_id)

    @staticmethod
    def update_company(
        db: Session,
        company_id: int,
        company_data: CompanyUpdate
    ):
        company = CompanyRepository.get_by_id(
            db,
            company_id
        )

        if company is None:
            raise ValueError("Company not found")

        return CompanyRepository.update(
            db,
            company,
            company_data
        )

    @staticmethod
    def delete_company(
        db: Session,
        company_id: int
    ):
        company = CompanyRepository.get_by_id(
            db,
            company_id
        )

        if company is None:
            raise ValueError("Company not found")

        if CompanyRepository.has_tenders(
            db,
            company_id
        ):
            raise ValueError(
                "Company cannot be deleted because it has associated tenders"
            )

        CompanyRepository.delete(
            db,
            company
        )

        return {
            "message": "Company deleted successfully"
        }