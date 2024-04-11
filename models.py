from pydantic import BaseModel


class Patient(BaseModel):
    first_name: str
    last_name: str
    address: str
    age: int

class CreatePatientRequest(BaseModel):
    last_name: str
    address: str
    age: int

class PatientResponse(BaseModel):
    first_name: str