from sqlalchemy.orm import Session

from app.repositories.tender_repository import TenderRepository
from app.repositories.company_repository import CompanyRepository
from app.schemas.tender import TenderCreate, TenderUpdate


class TenderService:

    @staticmethod
    def create_tender(
        db: Session,
        tender_data: TenderCreate
    ):
        company = CompanyRepository.get_by_id(
            db,
            tender_data.company_id
        )

        if company is None:
            raise ValueError("Company not found")

        return TenderRepository.create(
            db,
            tender_data
        )

    @staticmethod
    def get_tenders(
        db: Session,
        company_id: int | None = None,
        status: str | None = None,
        search: str | None = None
    ):
        return TenderRepository.get_all(
            db,
            company_id,
            status,
            search
        )

    @staticmethod
    def get_tender(
        db: Session,
        tender_id: int
    ):
        return TenderRepository.get_by_id(
            db,
            tender_id
        )

    @staticmethod
    def update_tender(
        db: Session,
        tender_id: int,
        tender_data: TenderUpdate
    ):
        tender = TenderRepository.get_by_id(
            db,
            tender_id
        )

        if tender is None:
            raise ValueError("Tender not found")

        if tender_data.company_id is not None:
            company = CompanyRepository.get_by_id(
                db,
                tender_data.company_id
            )

            if company is None:
                raise ValueError("Company not found")

        return TenderRepository.update(
            db,
            tender,
            tender_data
        )

    @staticmethod
    def delete_tender(
        db: Session,
        tender_id: int
    ):
        tender = TenderRepository.get_by_id(
            db,
            tender_id
        )

        if tender is None:
            raise ValueError("Tender not found")

        TenderRepository.delete(
            db,
            tender
        )

        return {
            "message": "Tender deleted successfully"
        }

