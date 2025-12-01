from pydantic import BaseModel


class ApplicationData(BaseModel):

    candidate_id:int
    job_id:int


class CandidateData(BaseModel):

    full_name:str
    email:str
    phone:str
    resume_text:str


class JobData(BaseModel):

    title:str
    description:str
    salary:int
    company_id:int


class CompanyData(BaseModel):

    name:str
    industry:str
    location:str
    description:str
    