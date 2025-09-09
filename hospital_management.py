def search_by_disease(patients, disease):
    result = [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]
    return result


# Input
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = "Flu"

# Process
matching_patients = search_by_disease(patients, search_disease)

# Output
print(f"Patients with {search_disease}:", matching_patients)
