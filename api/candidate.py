from fastapi import APIRouter
from database import Session
from database.models import Candidate
from database.schems import CandidateData as cd

candidate_router=APIRouter()


@candidate_router.post("/candidates")
def add_candidate(data:cd):
    with Session() as db:
        candidate=Candidate(
            full_name=data.full_name,
            email=data.email,
            phone=data.phone,
            resume_text=data.resume_text
        )

        db.add(candidate)
        db.commit()
        db.refresh(candidate)

    message={
        "status":"OK",
        "message":"Candidate is created",
        "candidate":candidate
    }

    return message


    
