from .config import Base
from sqlalchemy.orm import mapped_column,Mapped,relationship
from sqlalchemy import String,Text,Integer,DateTime,func,ForeignKey,Enum
from typing import Optional
from datetime import datetime
import enum

class Company(Base):
    __tablename__="companies"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    industry:Mapped[str]=mapped_column(String(150))
    location:Mapped[str]=mapped_column(String(150))
    description:Mapped[Optional[str]]=mapped_column(nullable=True)

    job:Mapped[list["Job"]]=relationship(back_populates="company")


class Job(Base):
    __tablename__="jobs"

    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(100))
    description:Mapped[str]=mapped_column(Text)
    salary:Mapped[int]=mapped_column(Integer())
    posted_at:Mapped[datetime]=mapped_column(DateTime,default=func.now())
    company_id:Mapped[int]=mapped_column(ForeignKey("companies.id"))

    company:Mapped["Company"]=relationship(back_populates="job")
    application:Mapped[list["Application"]]=relationship(back_populates="job")


class Candidate(Base):
    __tablename__="candidates"

    id:Mapped[int]=mapped_column(primary_key=True)
    full_name:Mapped[str]=mapped_column(String(100))
    email:Mapped[str]=mapped_column(String(200))
    phone:Mapped[str]=mapped_column(String(13))
    resume_text:Mapped[Optional[str]]=mapped_column(Text)

    application:Mapped[list["Application"]]=relationship(back_populates="candidate")


class StatusChoice(str,enum.Enum):
    PENDING="Pending"
    ACCEPTED="Accepted"
    REJECTED="Rejected"
 

class Application(Base):
    __tablename__="applications"

    id:Mapped[int]=mapped_column(primary_key=True)
    candidate_id:Mapped[int]=mapped_column(ForeignKey("candidates.id"))
    job_id:Mapped[int]=mapped_column(ForeignKey("jobs.id"))
    applied_at:Mapped[datetime]=mapped_column(DateTime,default=func.now())
    status:Mapped[str]=mapped_column(Enum(StatusChoice),default=StatusChoice.PENDING)

    candidate:Mapped["Candidate"]=relationship(back_populates="application")
    job:Mapped["Job"]=relationship(back_populates="application")





