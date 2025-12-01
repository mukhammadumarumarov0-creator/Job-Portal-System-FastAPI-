from fastapi import FastAPI
from database import Base,engine
from api import application_router,job_router,candidate_router,company_router
 

app=FastAPI(title="JobPortalSystem - Backend")

Base.metadata.create_all(bind=engine)

app.include_router(application_router,prefix="/applications")
app.include_router(job_router,prefix="/jobs")
app.include_router(candidate_router,prefix="/candidates")
app.include_router(company_router,prefix="/companies")






