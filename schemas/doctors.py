from pydantic import BaseModel
from enum import Enum

class Doctor(BaseModel):
  doctor_id: int
  name: str
  specialization: str
  phone: "str"
  is_available: bool = True




class CreateEditDoctor(BaseModel):
  name: str
  specialization: str
  phone: "str"
  is_available: bool = True


doctors: dict[int, Doctor] = {1: Doctor(doctor_id=1, name='Dave', specialization='Optician', phone="0500", is_available=True), 2: Doctor(
    doctor_id=2, name='Edward', specialization='Dermatologist', phone="0100", is_available=True)}
