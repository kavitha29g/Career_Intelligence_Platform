# 1 How will you combine student information from multiple institutions?

import os
import pandas as pd

# locate project
project_path = os.path.dirname(os.path.dirname(__file__))

# locate silver datasets
students_path = os.path.join(
    project_path,
    "data", "silver", "students",
    "students_master_synthetic.csv"
)

institutions_path = os.path.join(
    project_path,
    "data", "silver", "students",
    "institutions_synthetic.csv"
)

# load datasets
students = pd.read_csv(students_path)
institutions = pd.read_csv(institutions_path)

print("Students:", students.shape)
print("Institutions:", institutions.shape)

# combine datasets
integrated_data = students.merge(
    institutions,
    on="institution_id",
    how="left",
    indicator=True
)

# check unmatched institution records
print("\nUnmatched institution records:")
print(integrated_data[integrated_data["_merge"] == "left_only"])

# remove merge indicator
integrated_data.drop(columns="_merge", inplace=True)

# save integrated dataset
output_path = os.path.join(
    project_path,
    "data", "silver", "integrated"
)

os.makedirs(output_path, exist_ok=True)

integrated_data.to_csv(
    os.path.join(output_path, "student_institution_data.csv"),
    index=False
)

print("\nIntegrated dataset shape:", integrated_data.shape)
print("\nStudent and institution data integration completed!")