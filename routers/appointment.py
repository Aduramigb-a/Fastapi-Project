from fastapi import APIRouter
from schemas.appointment import CreateAppointment, appointments
from services.appointment import AppointmentService


appointment_router = APIRouter()

# create appointment
@appointment_router.post('/', status_code=201)
def create_appointment(data_in: CreateAppointment):
  response = AppointmentService.create_appointment(data_in)
  return response

# complete appointment
@appointment_router.put('/{appointment_id}', status_code=200)
def complete_appointment(appointment_id: int):
  response = AppointmentService.complete_appointment(appointment_id)
  return response


# cancel appointment
@appointment_router.delete('/{appointment_id}', status_code=200)
def cancel_appointment(appointment_id: int):
  response = AppointmentService.cancel_appointment(appointment_id)
  return response


# all appointments
@appointment_router.get('/', status_code=200)
def get_all_appointment():
  return appointments