from fastapi import HTTPException
from schemas.doctors import CreateEditDoctor, doctors, Doctor

class DoctorService():
  @staticmethod

  def create_doctor(data_in:CreateEditDoctor):
    doctor_id = len(doctors) + 1
    doctors[doctor_id] = Doctor(doctor_id=doctor_id, name=data_in.name, specialization=data_in.specialization, phone=data_in.phone, is_available=True)
    return {'message': "Successful", "data": doctors[doctor_id]}
  
  def edit_doctor(doctor_id: int, data_in: CreateEditDoctor):
    doctor = doctors.get(doctor_id)
    if doctor:
      doctor.name = data_in.name
      doctor.specialization = data_in.specialization
      doctor.phone = data_in.phone
      doctor.is_available = data_in.is_available
      return {'message': 'Successful', 'data': doctor}
    else:
      raise HTTPException(status_code=404, detail='Doctor Not Found')
    
  def delete_doctor(doctor_id: int):
    doctor = doctors.get(doctor_id)
    if doctor:
      del doctors[doctor_id]
      return {'message': 'Successful'}
    else: 
      raise HTTPException(status_code=404, detail='Doctor Not Available')
    
  def set_availability(doctor_id: int, is_available: bool):
    doctor = doctors.get(doctor_id)
    if not doctor:
      raise HTTPException(status_code=404, detail="Doctor Not Found")
    doctor.is_available = is_available
    return {'message': 'success',}
