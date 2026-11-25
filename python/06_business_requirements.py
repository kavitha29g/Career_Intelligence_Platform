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



# 2 How will you identify students with missing academic or skill information?


# dataset paths
students_path = os.path.join(
    project_path, "data", "silver",
    "students", "students_master_synthetic.csv"
)

technical_path = os.path.join(
    project_path, "data", "silver",
    "assessments", "technical_assessments_synthetic.csv"
)

programming_path = os.path.join(
    project_path, "data", "silver",
    "assessments", "programming_assessments_synthetic.csv"
)

communication_path = os.path.join(
    project_path, "data", "silver",
    "assessments", "communication_assessments_synthetic.csv"
)

# load datasets
students = pd.read_csv(students_path)
technical = pd.read_csv(technical_path)
programming = pd.read_csv(programming_path)
communication = pd.read_csv(communication_path)

# combine student and assessment data
data = students.merge(technical, on="student_id", how="left")
data = data.merge(programming, on="student_id", how="left")
data = data.merge(communication, on="student_id", how="left")

# identify missing information
missing_data = data[data.isnull().any(axis=1)].copy()

# identify missing columns for each student
missing_data["missing_fields"] = missing_data.apply(
    lambda row: ", ".join(row.index[row.isnull()]),
    axis=1
)

# select report columns
missing_report = missing_data[
    ["student_id", "institution_id", "missing_fields"]
]

# save report
report_path = os.path.join(
    project_path, "reports", "data_quality_report"
)

os.makedirs(report_path, exist_ok=True)

missing_report.to_csv(
    os.path.join(report_path, "missing_student_information.csv"),
    index=False
)

# display results
print("Total students:", len(students))
print("Students with missing information:", len(missing_report))

print("\nMissing information report:")
print(missing_report.head(20))

print("\nMissing student information analysis completed!")