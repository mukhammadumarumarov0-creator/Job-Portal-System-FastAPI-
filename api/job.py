from fastapi import APIRouter
from sqlalchemy.orm import joinedload
from database import Session
from database.models import Job,Company
from database.schems import JobData 


job_router=APIRouter()



@job_router.get("/jobs")
def get_all_jobs():
    with Session() as db:
        stmt=db.query(Job).options(joinedload(Job.company))
        jobs=db.scalars(stmt).unique().all()

    message={
        "status":"OK",
        "message":"All jobs are fetched successfuly",
        "jobs":jobs
    }

    return message


@job_router.post("/jobs")
def create_job(data:JobData):
    with Session() as db:
        job=Job(
          title=data.title,
          description=data.description,
          salary=data.salary,
          company_id=data.company_id
        )

        db.add(job)
        db.commit()
        db.refresh(job)

    message={
        "status":"OK",
        "message":"Job created successfuly",
        "job":job
    }
    return message


@job_router.get("/get_company_by_id/{company_id}")
def get_company(company_id:int):

    with Session() as db:
        stmt=db.query(Company).where(Company.id==company_id)
        company=db.scalars(stmt).first()

    message={
        "status":"OK",
        "message":"Company is fetched successfuly",
        "candidate":company
    }
    return message
