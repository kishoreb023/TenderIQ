from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Tender(Base):
    __tablename__ = "tenders"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="new",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    nit_number: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    tender_date: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    project_location: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    project_length_km: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    project_cost_cr: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    bid_start_date: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    bid_end_date: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    bid_opening_date: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    company: Mapped["Company"] = relationship(
        "Company",
        back_populates="tenders"
    )

    documents: Mapped[list["TenderDocument"]] = relationship(
        "TenderDocument",
        back_populates="tender",
        cascade="all, delete-orphan"
    )