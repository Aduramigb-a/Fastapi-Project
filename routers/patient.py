from fastapi import APIRouter
from schemas.patient import CreateEditPatient
from services.patient import PatientServices 

patient_router = APIRouter()

# get patients
@patient_router.get('/', status_code=200)
def get_patients():
  response = PatientServices.get_patients()
  return response

# create patient
@patient_router.post('/', status_code=201)
def create_patient(data_in: CreateEditPatient):
  response = PatientServices.create_patient(data_in)
  return response

# edit patient
@patient_router.put('/{patient_id}', status_code=204)
def edit_patient(patient_id: int, data_in: CreateEditPatient):
  response = PatientServices.edit_patient(patient_id, data_in)
  return response

# delete patient
@patient_router.delete('/{patient_id}', status_code=200)
def delete_patient(patient_id: int):
  response = PatientServices.delete_patient(patient_id=patient_id)
  return response