from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TenderCreate(BaseModel):
    company_id: int
    title: str
    description: str | None = None


class TenderResponse(BaseModel):
    id: int
    company_id: int
    title: str
    description: str | None
    status: str
    created_at: datetime

    nit_number: str | None = None
    tender_date: str | None = None
    project_location: str | None = None
    project_length_km: float | None = None
    project_cost_cr: float | None = None
    bid_start_date: str | None = None
    bid_end_date: str | None = None
    bid_opening_date: str | None = None

    model_config = ConfigDict(from_attributes=True)


class TenderUpdate(BaseModel):
    company_id: int | None = None
    title: str | None = None
    description: str | None = None
    status: str | None = None