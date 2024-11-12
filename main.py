from fastapi import FastAPI

app = FastAPI()

#import routers
from routers.patient import patient_router
from routers.doctor import doctor_router
from routers.appointment import appointment_router

# include router
app.include_router(router=patient_router, prefix="/patients", tags=["Patients"])
app.include_router(router=doctor_router, prefix='/doctors', tags=['Doctors'])
app.include_router(router=appointment_router, prefix="/appointments", tags=['Appointments'])

@app.get('/', status_code=200)
def home():
  return "Welcome To My Medical Appointment API"