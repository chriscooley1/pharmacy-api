import json

from fastapi import FastAPI

from models import Patient


app = FastAPI()


with open("patients.json", "r") as f:
    patient_list = json.load(f)

# Use the first name as the unique identifier. For example, in the PUT route, you'd have something like this: "/patients/{first_name}"
patients: list[Patient] = []

for patient in patient_list:
    patients.append(Patient(**patient))


@app.get("/patients")
async def get_patients() -> list[Patient]:
    return patients

@app.post("/patients")
async def create_patients(patient: Patient) -> None:
    patients.append(patient)

@app.put("/patients/{first_name}")
async def update_patients(first_name: str, updated_patient: Patient) -> None:
    for i, patient in enumerate(patients):
        if patient.first_name == first_name:
            patients[i] = updated_patient
            return
    patients.append(updated_patient)
    return

@app.delete("/patients/{first_name}")
async def delete_patients(first_name: str) -> None:
    for i, patient in enumerate(patients):
        if patient.first_name == first_name:
            patients.pop(i)
            return