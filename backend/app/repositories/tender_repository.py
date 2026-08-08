from sqlalchemy.orm import Session

from app.models.tender import Tender
from app.schemas.tender import TenderCreate, TenderUpdate


class TenderRepository:

    @staticmethod
    def create(
        db: Session,
        tender_data: TenderCreate
    ) -> Tender:

        tender = Tender(
            company_id=tender_data.company_id,
            title=tender_data.title,
            description=tender_data.description
        )

        db.add(tender)
        db.commit()
        db.refresh(tender)

        return tender

    @staticmethod
    def get_all(
        db: Session,
        company_id: int | None = None,
        status: str | None = None,
        search: str | None = None
    ) -> list[Tender]:

        query = db.query(Tender)

        if company_id is not None:
            query = query.filter(
                Tender.company_id == company_id
            )

        if status is not None:
            query = query.filter(
                Tender.status == status
            )

        if search is not None:
            query = query.filter(
                Tender.title.ilike(f"%{search}%")
            )

        return query.all()

    @staticmethod
    def get_by_id(
        db: Session,
        tender_id: int
    ) -> Tender | None:

        return db.query(Tender).filter(
            Tender.id == tender_id
        ).first()

    @staticmethod
    def update(
        db: Session,
        tender: Tender,
        tender_data: TenderUpdate
    ) -> Tender:

        if tender_data.company_id is not None:
            tender.company_id = tender_data.company_id

        if tender_data.title is not None:
            tender.title = tender_data.title

        if tender_data.description is not None:
            tender.description = tender_data.description

        if tender_data.status is not None:
            tender.status = tender_data.status

        db.commit()
        db.refresh(tender)

        return tender

    @staticmethod
    def update_extracted_information(
        db: Session,
        tender: Tender,
        information: dict
    ) -> Tender:

        if information.get("nit_number") is not None:
            tender.nit_number = information["nit_number"]

        if information.get("tender_date") is not None:
            tender.tender_date = information["tender_date"]

        if information.get("title") is not None:
            tender.title = information["title"]

        if information.get("project_location") is not None:
            tender.project_location = information["project_location"]

        if information.get("project_length_km") is not None:
            tender.project_length_km = information["project_length_km"]

        if information.get("project_cost_cr") is not None:
            tender.project_cost_cr = information["project_cost_cr"]

        if information.get("bid_start_date") is not None:
            tender.bid_start_date = information["bid_start_date"]

        if information.get("bid_end_date") is not None:
            tender.bid_end_date = information["bid_end_date"]

        if information.get("bid_opening_date") is not None:
            tender.bid_opening_date = information["bid_opening_date"]

        db.commit()
        db.refresh(tender)

        return tender

    @staticmethod
    def delete(
        db: Session,
        tender: Tender
    ):
        db.delete(tender)
        db.commit()