from pydantic import BaseModel


class Patient(BaseModel):
  patient_id: int
  name: str
  age: int
  sex: str
  weight: str
  height: str
  phone: str

class CreateEditPatient(BaseModel):
  name: str
  age: int
  sex: str
  weight: str
  height: str
  phone: str



patients: dict[int, Patient] = {1: Patient(patient_id=1, name='Olu', age=24, sex='M', weight='75kg', height='175cm', phone='0901')}