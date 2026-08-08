from sqlalchemy.orm import Session

from app.models.tender_document import TenderDocument


class TenderDocumentRepository:

    @staticmethod
    def create(
        db: Session,
        tender_id: int,
        file_name: str,
        file_path: str,
        file_type: str,
        extracted_text: str | None = None
    ) -> TenderDocument:

        document = TenderDocument(
            tender_id=tender_id,
            file_name=file_name,
            file_path=file_path,
            file_type=file_type,
            extracted_text=extracted_text
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def get_all(
        db: Session,
        tender_id: int
    ) -> list[TenderDocument]:

        return db.query(TenderDocument).filter(
            TenderDocument.tender_id == tender_id
        ).all()

    @staticmethod
    def get_by_id(
        db: Session,
        document_id: int
    ) -> TenderDocument | None:

        return db.query(TenderDocument).filter(
            TenderDocument.id == document_id
        ).first()

    @staticmethod
    def delete(
        db: Session,
        document: TenderDocument
    ):
        db.delete(document)
        db.commit()