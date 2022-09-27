from email.policy import default
from sqlalchemy import Column,Integer,String,ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship,backref

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key = True)
    name = Column (String(50))
    email = Column(String(120),unique = True)
    password = Column(String(100),nullable=False)
    balance = Column(Integer,default = 0,nullable = False)
    scooters = relationship("Scooter",secondary="hire",back_populates="users")

class Scooter(Base):
    __tablename__ = "scooter"
    id = Column(Integer,primary_key = True)
    users = relationship("User",secondary="hire",back_populates="scooters",lazy="joined")

class Hire(Base):
    __tablename__ = "hire"
    id =  Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id',ondelete="CASCADE"),primary_key = True)
    scooter_id = Column(Integer,ForeignKey('scooter.id',ondelete="CASCADE"),primary_key = True)

