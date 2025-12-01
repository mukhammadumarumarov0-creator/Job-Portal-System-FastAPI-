from fastapi import APIRouter
from database import Session
from database.models import Application,Candidate,Job
from database.schems import ApplicationData as ad

application_router=APIRouter()

@application_router.get("/application")
def get_all_application():
    with Session() as db:
        data=db.query(Application).all()


    message={
        "status":"OK",
        "message":"All application are fetched successfuly",
        "companies":data
    }

    return message


@application_router.post("/application")
def create_application(data:ad):
    with Session() as db:
        application=Application(
            candidate_id=data.candidate_id,
            job_id=data.job_id
        )
        
        db.add(application)
        db.commit()
        db.refresh(application)

    message={
        "status":"OK",
        "message":"Application is created",
        "application":application
    }
    return message


@application_router.get("/get_candidate_by_id/{candidate_id}")
def get_candidate(candidate_id:int):

    with Session() as db:
        stmt=db.query(Candidate).where(Candidate.id==candidate_id)
        candidate=db.scalars(stmt).first()

    message={
        "status":"OK",
        "message":"Candidate is fetched successfuly",
        "candidate":candidate
    }
    return message


@application_router.get("/get_job_by_id/{job_id}")
def get_job(job_id:int):

    with Session() as db:
        stmt=db.query(Job).where(Job.id==job_id)
        job=db.scalars(stmt).first()

    message={
        "status":"OK",
        "message":"Job is fetched successfuly",
        "candidate":job
    }
    return message


@application_router.put("/application_status/{application_id}_{new_status}")
def update_status(application_id:int,new_status:str):
    with Session() as db:
     try:
        application=db.get(Application,application_id)
        if application:
            application.status=new_status

            db.commit()
            db.refresh(application)

            message={
                        "status":"OK",
                        "message":"Application status is updated",
                        "application":application
                    }

            return message
        else:
            return {"message":"There is no such application"}
        
     except Exception as err:
         print("update_status funksiaysida xatolik",err)