
from sqlalchemy.orm import Session

from app.repositories.tender_document_repository import (
    TenderDocumentRepository
)
from app.repositories.tender_repository import TenderRepository

from app.utils.pdf_extractor import extract_text_from_pdf
from app.utils.tender.information_extractor import (
    extract_tender_information
)


class TenderDocumentService:

    @staticmethod
    def create_document(
        db: Session,
        tender_id: int,
        file_name: str,
        file_path: str,
        file_type: str,
        extracted_text: str | None = None
    ):
        # Check whether tender exists
        tender = TenderRepository.get_by_id(
            db,
            tender_id
        )

        if tender is None:
            raise ValueError("Tender not found")

        # Extract text from PDF
        if extracted_text is None:
            extracted_text = extract_text_from_pdf(
                file_path
            )

        # Extract structured tender information
        information = extract_tender_information(
            extracted_text
        )

        # Update tender with extracted information
        TenderRepository.update_extracted_information(
            db,
            tender,
            information
        )

        # Save document and extracted text
        return TenderDocumentRepository.create(
            db,
            tender_id,
            file_name,
            file_path,
            file_type,
            extracted_text
        )

    @staticmethod
    def get_documents(
        db: Session,
        tender_id: int
    ):
        tender = TenderRepository.get_by_id(
            db,
            tender_id
        )

        if tender is None:
            raise ValueError("Tender not found")

        return TenderDocumentRepository.get_all(
            db,
            tender_id
        )

    @staticmethod
    def get_document(
        db: Session,
        document_id: int
    ):
        document = TenderDocumentRepository.get_by_id(
            db,
            document_id
        )

        if document is None:
            raise ValueError("Document not found")

        return document

    @staticmethod
    def delete_document(
        db: Session,
        document_id: int
    ):
        document = TenderDocumentRepository.get_by_id(
            db,
            document_id
        )

        if document is None:
            raise ValueError("Document not found")

        TenderDocumentRepository.delete(
            db,
            document
        )

        return {
            "message": "Document deleted successfully"
        }

