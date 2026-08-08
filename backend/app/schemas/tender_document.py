
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TenderDocumentResponse(BaseModel):
    id: int
    tender_id: int
    file_name: str
    file_path: str
    file_type: str
    uploaded_at: datetime
    extracted_text: str | None = None

    model_config = ConfigDict(from_attributes=True)
