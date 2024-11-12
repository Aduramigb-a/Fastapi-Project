from fastapi import APIRouter
from schemas.doctors import doctors, CreateEditDoctor
from services.doctor import DoctorService

doctor_router = APIRouter()


# get 
@doctor_router.get('/', status_code=200)
def get_all_doctors():
  return doctors

# create a doctor
@doctor_router.post('/', status_code=201)
def create_doctor(data_in: CreateEditDoctor):
  response = DoctorService.create_doctor(data_in)
  return response

# edit doctor
@doctor_router.put('/{doctor_id}', status_code=200)
def edit_doctor(doctor_id: int, data_in: CreateEditDoctor):
  response = DoctorService.edit_doctor(doctor_id, data_in)
  return response


# delete a doctor
@doctor_router.delete('/{doctor_id}', status_code=200)
def delete_doctor(doctor_id: int):
  response = DoctorService.delete_doctor(doctor_id)
  return response


# set availability
@doctor_router.put('/{doctor_id}/availability', status_code=200)
def set_availability(doctor_id: int, is_available: bool):
  response = DoctorService.set_availability(doctor_id, is_available)
  return response