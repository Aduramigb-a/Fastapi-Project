from schemas.appointment import appointments
from fastapi import HTTPException
from schemas.appointment import CreateAppointment, appointments, Appointment
from schemas.doctors import doctors

class AppointmentService():
  @staticmethod
  
  def create_appointment(data_in: CreateAppointment):
    appointment_id = len(appointments) + 1

    for doctor_id, doctor in doctors.items():
        if doctor.is_available:
          new_appointment = Appointment(appointment_id=appointment_id, patient=data_in.patient, doctor=doctor, date=data_in.date)
          doctor.is_available = False
          appointments.append(new_appointment)
          return {'message': 'success', 'data': new_appointment}
    raise HTTPException(status_code=404, detail="No Doctors Available")
  

  def complete_appointment(appointment_id):
     for appointment in appointments:
        if appointment.appointment_id == appointment_id:
          appointment.doctor.is_available = True
          return {'message': 'Appointment Completed'}
        raise HTTPException(status_code=404, detail="Appointment Does Not Booked")
     
  def cancel_appointment(appointment_id):
    for appointment in appointments:
        if appointment.appointment_id == appointment_id:
          appointment.doctor.is_available = True
          appointments.remove(appointment)
          return {'message': 'Appointment Cancelled Successfully'}
    raise HTTPException(status_code=404, detail='Appointment Not Found')


