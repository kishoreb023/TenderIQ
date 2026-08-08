from sqlalchemy.orm import Session

from app.models.company import Company
from app.models.tender import Tender
from app.schemas.company import CompanyCreate, CompanyUpdate


class CompanyRepository:

    @staticmethod
    def create(
        db: Session,
        company_data: CompanyCreate
    ) -> Company:

        company = Company(
            name=company_data.name,
            industry=company_data.industry
        )

        db.add(company)
        db.commit()
        db.refresh(company)

        return company

    @staticmethod
    def get_all(db: Session) -> list[Company]:
        return db.query(Company).all()

    @staticmethod
    def get_by_id(
        db: Session,
        company_id: int
    ) -> Company | None:

        return db.query(Company).filter(
            Company.id == company_id
        ).first()

    @staticmethod
    def update(
        db: Session,
        company: Company,
        company_data: CompanyUpdate
    ) -> Company:

        if company_data.name is not None:
            company.name = company_data.name

        if company_data.industry is not None:
            company.industry = company_data.industry

        db.commit()
        db.refresh(company)

        return company

    @staticmethod
    def has_tenders(
        db: Session,
        company_id: int
    ) -> bool:

        return db.query(Tender).filter(
            Tender.company_id == company_id
        ).first() is not None

    @staticmethod
    def delete(
        db: Session,
        company: Company
    ):
        db.delete(company)
        db.commit()