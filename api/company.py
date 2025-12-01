from fastapi import APIRouter
from database import Session
from database.models import Company
from database.schems import CompanyData as cd

company_router=APIRouter()

@company_router.get("/companies")
def get_all_companies():
    with Session() as db:
        data=db.query(Company).all()

    message={
        "status":"OK",
        "message":"All companies are fetched successfuly",
        "companies":data
    }

    return message

@company_router.post("/companies")
def create_company(data:cd):
    with Session() as db:
        company=Company(
            name=data.name,
            industry=data.industry,
            location=data.location,
            description=data.description
        )

        db.add(company)
        db.commit()
        db.refresh(company)
    message={
        "status":"OK",
        "message":"Company created successfuly",
        "company":company
    }
    return message