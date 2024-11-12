from pydantic import BaseModel
from schemas.doctors import Doctor

class Appointment(BaseModel):
  appointment_id: int
  patient: int
  doctor: Doctor
  date: str

class CreateAppointment(BaseModel):
  patient: int
  date: str




appointments: list[Appointment] = []



