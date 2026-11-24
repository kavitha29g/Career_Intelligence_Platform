import os
import pandas as pd

# locate project
project_path = os.path.dirname(os.path.dirname(__file__))

# locate student dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "students",
    "students_master_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("Original shape:", df.shape)

# --------------------------------
# 1. Remove exact duplicates
# --------------------------------

df_cleaned = df.drop_duplicates().copy()

print("Duplicates removed:", len(df) - len(df_cleaned))

# --------------------------------
# 2. Check missing values
# --------------------------------

print("\nMissing values:")
print(df_cleaned.isnull().sum())

# --------------------------------
# 3. Check invalid CGPA
# --------------------------------

if "cgpa" in df_cleaned.columns:

    print("\nInvalid CGPA:")
    print(df_cleaned[
        (df_cleaned["cgpa"] < 0) |
        (df_cleaned["cgpa"] > 10)
    ])

# --------------------------------
# 4. Check negative backlogs
# --------------------------------

if "backlogs" in df_cleaned.columns:

    print("\nInvalid backlogs:")
    print(df_cleaned[df_cleaned["backlogs"] < 0])

# --------------------------------
# 5. Check negative internships
# --------------------------------

if "internships" in df_cleaned.columns:

    print("\nInvalid internships:")
    print(df_cleaned[df_cleaned["internships"] < 0])

# --------------------------------
# 6. Check negative projects
# --------------------------------

if "projects_completed" in df_cleaned.columns:

    print("\nInvalid projects:")
    print(df_cleaned[df_cleaned["projects_completed"] < 0])

# --------------------------------
# 7. Check duplicate student IDs
# --------------------------------

if "student_id" in df_cleaned.columns:

    print("\nDuplicate student IDs:")
    print(df_cleaned[
        df_cleaned["student_id"].duplicated(keep=False)
    ])

# --------------------------------
# 8. Check missing student IDs
# --------------------------------

if "student_id" in df_cleaned.columns:

    print("\nMissing student IDs:")
    print(df_cleaned[df_cleaned["student_id"].isnull()])

# --------------------------------
# 9. Standardize text columns
# --------------------------------

text_columns = df_cleaned.select_dtypes(
    include="object"
).columns

for column in text_columns:

    df_cleaned[column] = (
        df_cleaned[column]
        .str.strip()
    )

# --------------------------------
# 10. Final summary
# --------------------------------

print("\nFinal dataset shape:", df_cleaned.shape)

print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nStudent dataset cleaning inspection completed!")


# locate institution dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "students",
    "institutions_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("\nInstitution dataset shape:", df.shape)

# --------------------------------
# 1. Remove exact duplicates
# --------------------------------

df_cleaned = df.drop_duplicates().copy()

print("Duplicates removed:", len(df) - len(df_cleaned))

# --------------------------------
# 2. Check missing values
# --------------------------------

print("\nMissing values:")
print(df_cleaned.isnull().sum())

# --------------------------------
# 3. Check data types
# --------------------------------

print("\nData types:")
print(df_cleaned.dtypes)

# --------------------------------
# 4. Check duplicate institution IDs
# --------------------------------

if "institution_id" in df_cleaned.columns:

    print("\nDuplicate institution IDs:")
    print(df_cleaned[
        df_cleaned["institution_id"].duplicated(keep=False)
    ])

# --------------------------------
# 5. Standardize text columns
# --------------------------------

text_columns = df_cleaned.select_dtypes(
    include="object"
).columns

for column in text_columns:

    df_cleaned[column] = df_cleaned[column].str.strip()

# --------------------------------
# 6. Final summary
# --------------------------------

print("\nFinal dataset shape:", df_cleaned.shape)

print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nInstitution dataset cleaning inspection completed!")

# locate technical skill assessment dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "assessments",
    "technical_assessments_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("\nTechnical Skill Assessment shape:", df.shape)

# 1. Remove exact duplicates
df_cleaned = df.drop_duplicates().copy()

print("Duplicates removed:", len(df) - len(df_cleaned))

# 2. Check missing values
print("\nMissing values:")
print(df_cleaned.isnull().sum())

# 3. Check data types
print("\nData types:")
print(df_cleaned.dtypes)

# 4. Check duplicate assessment IDs
if "assessment_id" in df_cleaned.columns:

    print("\nDuplicate assessment IDs:")
    print(df_cleaned[
        df_cleaned["assessment_id"].duplicated(keep=False)
    ])

# 5. Check assessment scores
score_columns = [
    col for col in df_cleaned.columns
    if "score" in col.lower()
]

for column in score_columns:

    print(f"\nInvalid values in {column}:")

    print(df_cleaned[
        (df_cleaned[column] < 0) |
        (df_cleaned[column] > 100)
    ])

# 6. Standardize text columns
text_columns = df_cleaned.select_dtypes(
    include="object"
).columns

for column in text_columns:

    df_cleaned[column] = df_cleaned[column].str.strip()

# 7. Final summary
print("\nFinal dataset shape:", df_cleaned.shape)

print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nTechnical Skill Assessment cleaning inspection completed!")


# locate programming assessment dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "assessments",
    "programming_assessments_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("\nProgramming Assessment shape:", df.shape)

# 1. Remove exact duplicates
df_cleaned = df.drop_duplicates().copy()

print("Duplicates removed:", len(df) - len(df_cleaned))

# 2. Check missing values
print("\nMissing values:")
print(df_cleaned.isnull().sum())

# 3. Check data types
print("\nData types:")
print(df_cleaned.dtypes)

# 4. Check duplicate assessment IDs
if "assessment_id" in df_cleaned.columns:

    print("\nDuplicate assessment IDs:")
    print(df_cleaned[
        df_cleaned["assessment_id"].duplicated(keep=False)
    ])

# 5. Check invalid scores
score_columns = [
    col for col in df_cleaned.columns
    if "score" in col.lower()
]

for column in score_columns:

    print(f"\nInvalid values in {column}:")

    print(df_cleaned[
        (df_cleaned[column] < 0) |
        (df_cleaned[column] > 100)
    ])

# 6. Standardize text columns
text_columns = df_cleaned.select_dtypes(
    include="object"
).columns

for column in text_columns:

    df_cleaned[column] = df_cleaned[column].str.strip()

# 7. Final summary
print("\nFinal dataset shape:", df_cleaned.shape)

print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nProgramming Assessment cleaning inspection completed!")


# locate communication assessment dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "assessments",
    "communication_assessments_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("\nCommunication Assessment shape:", df.shape)

# 1. Remove exact duplicates
df_cleaned = df.drop_duplicates().copy()

print("Duplicates removed:", len(df) - len(df_cleaned))

# 2. Check missing values
print("\nMissing values:")
print(df_cleaned.isnull().sum())

# 3. Check data types
print("\nData types:")
print(df_cleaned.dtypes)

# 4. Check duplicate assessment IDs
if "assessment_id" in df_cleaned.columns:

    print("\nDuplicate assessment IDs:")
    print(df_cleaned[
        df_cleaned["assessment_id"].duplicated(keep=False)
    ])

# 5. Check invalid scores
score_columns = [
    col for col in df_cleaned.columns
    if "score" in col.lower()
]

for column in score_columns:

    print(f"\nInvalid values in {column}:")

    print(df_cleaned[
        (df_cleaned[column] < 0) |
        (df_cleaned[column] > 100)
    ])

# 6. Standardize text columns
text_columns = df_cleaned.select_dtypes(
    include="object"
).columns

for column in text_columns:

    df_cleaned[column] = df_cleaned[column].str.strip()

# 7. Final summary
print("\nFinal dataset shape:", df_cleaned.shape)

print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nCommunication Assessment cleaning inspection completed!")

# locate training dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "training",
    "attendance_training_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("\nTraining dataset shape:", df.shape)

# 1. Remove exact duplicates
df_cleaned = df.drop_duplicates().copy()

print("Duplicates removed:", len(df) - len(df_cleaned))

# 2. Check missing values
print("\nMissing values:")
print(df_cleaned.isnull().sum())

# 3. Check data types
print("\nData types:")
print(df_cleaned.dtypes)

# 4. Check duplicate training IDs
if "training_id" in df_cleaned.columns:

    print("\nDuplicate training IDs:")
    print(df_cleaned[
        df_cleaned["training_id"].duplicated(keep=False)
    ])

# 5. Check attendance percentage
if "attendance_percentage" in df_cleaned.columns:

    print("\nInvalid attendance percentage:")
    print(df_cleaned[
        (df_cleaned["attendance_percentage"] < 0) |
        (df_cleaned["attendance_percentage"] > 100)
    ])

# 6. Standardize text columns
text_columns = df_cleaned.select_dtypes(
    include="object"
).columns

for column in text_columns:

    df_cleaned[column] = df_cleaned[column].str.strip()

# 7. Final summary
print("\nFinal dataset shape:", df_cleaned.shape)

print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nTraining dataset cleaning inspection completed!")

# locate mock interview dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "interviews",
    "mock_interviews_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("\nMock Interview dataset shape:", df.shape)

# 1. Remove exact duplicates
df_cleaned = df.drop_duplicates().copy()

print("Duplicates removed:", len(df) - len(df_cleaned))

# 2. Check missing values
print("\nMissing values:")
print(df_cleaned.isnull().sum())

# 3. Check data types
print("\nData types:")
print(df_cleaned.dtypes)

# 4. Check duplicate student IDs
if "student_id" in df_cleaned.columns:

    print("\nDuplicate student IDs:")
    print(df_cleaned[
        df_cleaned["student_id"].duplicated(keep=False)
    ])

# 5. Check invalid interview scores
score_columns = [
    "technical_interview_score",
    "hr_interview_score",
    "confidence_score"
]

for column in score_columns:

    if column in df_cleaned.columns:

        print(f"\nInvalid values in {column}:")

        print(df_cleaned[
            (df_cleaned[column] < 0) |
            (df_cleaned[column] > 100)
        ])

# 6. Check interview date
if "mock_interview_date" in df_cleaned.columns:

    print("\nInvalid interview dates:")

    df_cleaned["mock_interview_date"] = pd.to_datetime(
        df_cleaned["mock_interview_date"],
        errors="coerce"
    )

    print(
        df_cleaned[
            df_cleaned["mock_interview_date"].isnull()
        ]
    )

# 7. Standardize text columns
text_columns = df_cleaned.select_dtypes(
    include="object"
).columns

for column in text_columns:

    df_cleaned[column] = df_cleaned[column].str.strip()

# 8. Final summary
print("\nFinal dataset shape:", df_cleaned.shape)

print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nMock Interview dataset cleaning inspection completed!")


# locate job description dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "jobs",
    "job_descriptions_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("Original shape:", df.shape)

# remove exact duplicates
df_cleaned = df.drop_duplicates().copy()

# check missing values
print("\nMissing values:")
print(df_cleaned.isnull().sum())

# check data types
print("\nData types:")
print(df_cleaned.dtypes)

# check duplicate job IDs
print("\nDuplicate job IDs:")
print(df_cleaned[df_cleaned["job_id"].duplicated(keep=False)])

# check invalid salary
print("\nInvalid salary records:")
print(df_cleaned[
    (df_cleaned["salary_min_lpa"] < 0) |
    (df_cleaned["salary_max_lpa"] < 0) |
    (df_cleaned["salary_min_lpa"] > df_cleaned["salary_max_lpa"])
])

# convert posted date
df_cleaned["posted_date"] = pd.to_datetime(
    df_cleaned["posted_date"],
    errors="coerce"
)

# standardize text columns
text_columns = df_cleaned.select_dtypes(include="object").columns

for column in text_columns:
    df_cleaned[column] = df_cleaned[column].str.strip()

# final summary
print("\nFinal dataset shape:", df_cleaned.shape)
print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nData types of all columns:")
for column in df_cleaned.columns:
    print(f"{column} : {df_cleaned[column].dtype}")

print("\nJob Description cleaning inspection completed!")


# locate job skills dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "jobs",
    "job_skills_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("Original shape:", df.shape)

# remove exact duplicates
df_cleaned = df.drop_duplicates().copy()

# check missing values
print("\nMissing values:")
print(df_cleaned.isnull().sum())

# check data types
print("\nData types:")
print(df_cleaned.dtypes)

# check missing job IDs and skills
print("\nMissing job IDs:")
print(df_cleaned[df_cleaned["job_id"].isnull()])

print("\nMissing skills:")
print(df_cleaned[df_cleaned["skill"].isnull()])

# standardize skill names
df_cleaned["skill"] = df_cleaned["skill"].str.strip()

# final summary
print("\nFinal dataset shape:", df_cleaned.shape)

print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nData types of all columns:")
for column in df_cleaned.columns:
    print(f"{column} : {df_cleaned[column].dtype}")

print("\nJob Skills cleaning inspection completed!")


# locate company dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "companies",
    "companies_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("Original shape:", df.shape)

# remove exact duplicates
df_cleaned = df.drop_duplicates().copy()

# check missing values
print("\nMissing values:")
print(df_cleaned.isnull().sum())

# check data types
print("\nData types:")
print(df_cleaned.dtypes)

# check duplicate company IDs
print("\nDuplicate company IDs:")
print(df_cleaned[df_cleaned["company_id"].duplicated(keep=False)])

# standardize text columns
text_columns = df_cleaned.select_dtypes(include="object").columns

for column in text_columns:
    df_cleaned[column] = df_cleaned[column].str.strip()

# final summary
print("\nFinal dataset shape:", df_cleaned.shape)

print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nData types of all columns:")
for column in df_cleaned.columns:
    print(f"{column} : {df_cleaned[column].dtype}")

print("\nCompany dataset cleaning inspection completed!")

# locate company requirements dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "companies",
    "company_requirements_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("Original shape:", df.shape)

# remove exact duplicates
df_cleaned = df.drop_duplicates().copy()

# check missing values
print("\nMissing values:")
print(df_cleaned.isnull().sum())

# check data types
print("\nData types:")
print(df_cleaned.dtypes)

# check duplicate company IDs
print("\nDuplicate company IDs:")
print(df_cleaned[df_cleaned["company_id"].duplicated(keep=False)])

# check invalid openings
print("\nInvalid openings:")
print(df_cleaned[df_cleaned["openings"] < 0])

# check invalid CGPA
print("\nInvalid minimum CGPA:")
print(df_cleaned[
    (df_cleaned["minimum_cgpa"] < 0) |
    (df_cleaned["minimum_cgpa"] > 10)
])

# check invalid salary
print("\nInvalid salary:")
print(df_cleaned[df_cleaned["salary_lpa"] < 0])

# standardize text columns
text_columns = df_cleaned.select_dtypes(include="object").columns

for column in text_columns:
    df_cleaned[column] = df_cleaned[column].str.strip()

# final summary
print("\nFinal dataset shape:", df_cleaned.shape)

print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nData types of all columns:")
for column in df_cleaned.columns:
    print(f"{column} : {df_cleaned[column].dtype}")

print("\nCompany Requirements cleaning inspection completed!")

# locate student applications dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "placements",
    "student_job_applications_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("Original shape:", df.shape)

# remove exact duplicates
df_cleaned = df.drop_duplicates().copy()

# check missing values
print("\nMissing values:")
print(df_cleaned.isnull().sum())

# check data types
print("\nData types:")
print(df_cleaned.dtypes)

# check duplicate application IDs
print("\nDuplicate application IDs:")
print(df_cleaned[
    df_cleaned["application_id"].duplicated(keep=False)
])

# convert application date
df_cleaned["application_date"] = pd.to_datetime(
    df_cleaned["application_date"],
    errors="coerce"
)

# standardize text columns
text_columns = df_cleaned.select_dtypes(include="object").columns

for column in text_columns:
    df_cleaned[column] = df_cleaned[column].str.strip()

# final summary
print("\nFinal dataset shape:", df_cleaned.shape)

print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nData types of all columns:")
for column in df_cleaned.columns:
    print(f"{column} : {df_cleaned[column].dtype}")

print("\nStudent Applications cleaning inspection completed!")

# locate historical placements dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "placements",
    "historical_placements_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("Original shape:", df.shape)

# remove exact duplicates
df_cleaned = df.drop_duplicates().copy()

# check missing values
print("\nMissing values:")
print(df_cleaned.isnull().sum())

# check data types
print("\nData types:")
print(df_cleaned.dtypes)

# check duplicate placement IDs
print("\nDuplicate placement IDs:")
print(df_cleaned[
    df_cleaned["placement_id"].duplicated(keep=False)
])

# check invalid salary
print("\nInvalid salary records:")
print(df_cleaned[df_cleaned["offered_salary_lpa"] < 0])

# convert placement date
df_cleaned["placement_date"] = pd.to_datetime(
    df_cleaned["placement_date"],
    errors="coerce"
)

# standardize text columns
text_columns = df_cleaned.select_dtypes(include="object").columns

for column in text_columns:
    df_cleaned[column] = df_cleaned[column].str.strip()

# final summary
print("\nFinal dataset shape:", df_cleaned.shape)

print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nData types of all columns:")
for column in df_cleaned.columns:
    print(f"{column} : {df_cleaned[column].dtype}")

print("\nHistorical Placements cleaning inspection completed!")


# locate job salary roles dataset
file_path = os.path.join(
    project_path,
    "data",
    "bronze",
    "jobs",
    "job_salary_roles_synthetic.csv"
)

# read dataset
df = pd.read_csv(file_path)

print("Original shape:", df.shape)

# remove exact duplicates
df_cleaned = df.drop_duplicates().copy()

# check missing values
print("\nMissing values:")
print(df_cleaned.isnull().sum())

# check data types
print("\nData types:")
print(df_cleaned.dtypes)

# check invalid salary values
print("\nInvalid salary records:")
print(df_cleaned[
    (df_cleaned["salary_min_lpa"] < 0) |
    (df_cleaned["salary_max_lpa"] < 0) |
    (df_cleaned["salary_min_lpa"] > df_cleaned["salary_max_lpa"])
])

# standardize text columns
text_columns = df_cleaned.select_dtypes(include="object").columns

for column in text_columns:
    df_cleaned[column] = df_cleaned[column].str.strip()

# final summary
print("\nFinal dataset shape:", df_cleaned.shape)

print("\nFinal missing values:")
print(df_cleaned.isnull().sum())

print("\nData types of all columns:")
for column in df_cleaned.columns:
    print(f"{column} : {df_cleaned[column].dtype}")

print("\nJob Salary Roles cleaning inspection completed!")


# consolidated data cleaning verification

bronze_path = os.path.join(project_path, "data", "bronze")

summary = []
column_details = []

for root, dirs, files in os.walk(bronze_path):

    for file in files:

        if file.endswith(".csv"):

            file_path = os.path.join(root, file)
            data = pd.read_csv(file_path)

            # dataset summary
            summary.append({
                "dataset": file,
                "rows": len(data),
                "columns": len(data.columns),
                "missing_values": data.isnull().sum().sum(),
                "duplicate_rows": data.duplicated().sum()
            })

            # column-level details
            for column in data.columns:

                column_details.append({
                    "dataset": file,
                    "column": column,
                    "data_type": str(data[column].dtype),
                    "missing_values": data[column].isnull().sum()
                })

# create reports folder
report_path = os.path.join(
    project_path,
    "reports",
    "data_quality_report"
)

os.makedirs(report_path, exist_ok=True)

# save summary report
summary_df = pd.DataFrame(summary)

summary_df.to_csv(
    os.path.join(report_path, "cleaning_verification_report.csv"),
    index=False
)

# save column report
details_df = pd.DataFrame(column_details)

details_df.to_csv(
    os.path.join(report_path, "column_verification_report.csv"),
    index=False
)

print("\nCleaning verification reports generated successfully!")
print("\nDataset summary:")
print(summary_df)


