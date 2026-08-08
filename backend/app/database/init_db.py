from app.database.base import Base
from app.database.session import engine

from app.models.company import Company
from app.models.tender import Tender
from app.models.tender_document import TenderDocument


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database tables created successfully!")