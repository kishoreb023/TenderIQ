
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.tender_document import TenderDocumentResponse
from app.services.tender_document_service import TenderDocumentService
from app.utils.pdf_extractor import extract_text_from_pdf


router = APIRouter(
    prefix="/tenders",
    tags=["Tender Documents"]
)


@router.get(
    "/{tender_id}/documents",
    response_model=list[TenderDocumentResponse]
)
def get_documents(
    tender_id: int,
    db: Session = Depends(get_db)
):
    try:
        return TenderDocumentService.get_documents(
            db,
            tender_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get(
    "/documents/{document_id}",
    response_model=TenderDocumentResponse
)
def get_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    try:
        return TenderDocumentService.get_document(
            db,
            document_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.delete(
    "/documents/{document_id}"
)
def delete_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    try:
        return TenderDocumentService.delete_document(
            db,
            document_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.post(
    "/{tender_id}/documents",
    response_model=TenderDocumentResponse
)
def upload_document(
    tender_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Only PDF files are allowed
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    try:
        # Save uploaded file
        file_path = f"uploads/{file.filename}"

        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        # Extract text from PDF
        extracted_text = extract_text_from_pdf(
            file_path
        )

        # Store document and extracted text
        return TenderDocumentService.create_document(
            db,
            tender_id,
            file.filename,
            file_path,
            file.content_type,
            extracted_text
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process document: {str(e)}"
        )

