from fastapi import HTTPException
from schemas.patient import patients, CreateEditPatient, Patient

class PatientServices():
  @staticmethod

  def get_patients():
    return {'message': 'success', 'data': patients}
  

  def create_patient(data_in: CreateEditPatient):
    new_id = len(patients) + 1
    patients[new_id] = Patient(patient_id=new_id, name=data_in.name, age=data_in.age, sex=data_in.sex, weight=data_in.weight, height=data_in.height, phone=data_in.phone)
    return {'message': 'User Created Successfully', 'data': patients.get(new_id)}
  

  def edit_patient(patient_id: int, data_in: CreateEditPatient):
    patient = patients.get(patient_id)
    if patient:
      patient.name = data_in.name
      patient.age = data_in.age
      patient.weight = data_in.weight
      patient.height = data_in.height
      patient.phone = data_in.phone
      patient.sex = data_in.sex
      return {'message': 'Successful', 'data': patient}
    else:
      raise HTTPException(status_code=404, detail="Patient Not Available")


  def delete_patient(patient_id: int):
    patient = patients.get(patient_id)
    if patient:
      del patients[patient_id]
      return {'message': 'Successful'}
    else:
      raise HTTPException(status_code=404, detail='Patient Not Found')
