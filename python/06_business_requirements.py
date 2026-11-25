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


# 3 How will you standardize technical skills such as Python, SQL, AWS, Azure, and Java?
# locate dataset
file_path = os.path.join(
    project_path,
    "data", "silver", "jobs",
    "job_skills_synthetic.csv"
)

# load dataset
df = pd.read_csv(file_path)

print("Original skills:")
print(df["skill"].unique())

# skill normalization mapping
skill_mapping = {
    "python programming": "Python",
    "python": "Python",
    "py": "Python",
    "sql": "SQL",
    "structured query language": "SQL",
    "mysql": "MySQL",
    "sql server": "SQL Server",
    "aws": "AWS",
    "amazon web services": "AWS",
    "azure": "Azure",
    "microsoft azure": "Azure",
    "java": "Java",
    "core java": "Java",
    "pyspark": "PySpark"
}

# standardize skills
df["skill"] = df["skill"].str.strip().str.lower()

df["standardized_skill"] = df["skill"].map(skill_mapping).fillna(
    df["skill"].str.title()
)

# check results
print("\nStandardized skills:")
print(df[["skill", "standardized_skill"]].drop_duplicates())

# save output
output_path = os.path.join(
    project_path, "data", "silver", "jobs"
)

df.to_csv(
    os.path.join(output_path, "job_skills_standardized.csv"),
    index=False
)

print("\nSkill standardization completed!")


# 4. How will you extract skills from job descriptions?
import re
# load job descriptions
file_path = os.path.join(
    project_path,
    "data",
    "silver",
    "jobs",
    "job_descriptions_synthetic.csv"
)

df = pd.read_csv(file_path)

# define technical skills
skill_list = [
    "python",
    "sql",
    "mysql",
    "sql server",
    "pandas",
    "numpy",
    "pyspark",
    "power bi",
    "tableau",
    "excel",
    "aws",
    "azure",
    "java",
    "machine learning",
    "git",
    "databricks"
]

# function to extract skills
def extract_skills(text):

    if pd.isna(text):
        return []

    text = text.lower()

    extracted_skills = []

    for skill in skill_list:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            extracted_skills.append(skill.title())

    return extracted_skills


# extract skills from job description
df["extracted_skills"] = df["description"].apply(
    extract_skills
)

# calculate skill count
df["skill_count"] = df["extracted_skills"].apply(len)

# display results
print(df[[
    "job_id",
    "job_title",
    "extracted_skills",
    "skill_count"
]].head(10))

# save extracted skills
output_path = os.path.join(
    project_path,
    "data",
    "silver",
    "jobs"
)

df.to_csv(
    os.path.join(
        output_path,
        "job_descriptions_skills_extracted.csv"
    ),
    index=False
)

print("\nSkill extraction completed successfully!")


# 5 How will you identify students with incomplete training records?

# load training dataset
training_file_path = os.path.join(
    project_path,
    "data",
    "silver",
    "training",
    "attendance_training_synthetic.csv"
)

training = pd.read_csv(training_file_path)

print("\nTraining dataset loaded successfully!")

# filter incomplete training records
incomplete_training = training[
    (training["modules_completed"] < training["modules_total"]) |
    (training["attendance_pct"] < 75) |
    (training["training_completion_pct"] < 100)
].copy()

# function to identify reasons
def identify_reason(row):

    reasons = []

    if row["modules_completed"] < row["modules_total"]:
        reasons.append("Incomplete modules")

    if row["attendance_pct"] < 75:
        reasons.append("Low attendance")

    if row["training_completion_pct"] < 100:
        reasons.append("Incomplete training")

    return ", ".join(reasons)


# apply the function
incomplete_training["incomplete_reason"] = incomplete_training.apply(
    identify_reason,
    axis=1
)

# display report
print("\nStudents with incomplete training records:")

print(incomplete_training[[
    "student_id",
    "attendance_pct",
    "modules_completed",
    "modules_total",
    "training_completion_pct",
    "incomplete_reason"
]].head(10))


# save report
report_path = os.path.join(
    project_path,
    "reports",
    "data_quality_report"
)

os.makedirs(report_path, exist_ok=True)

incomplete_training.to_csv(
    os.path.join(
        report_path,
        "incomplete_training_records.csv"
    ),
    index=False
)

print("\nIncomplete training report saved successfully!")

# 6 How will you automate student performance data collection?


# ==========================================
# Q6 - AUTOMATE STUDENT PERFORMANCE DATA COLLECTION
# ==========================================

from datetime import datetime

print("\n========== Q6: AUTOMATED STUDENT PERFORMANCE DATA COLLECTION ==========")

# define source datasets
dataset_paths = {
    "students": os.path.join(
        project_path,
        "data", "silver", "students",
        "students_master_synthetic.csv"
    ),

    "technical": os.path.join(
        project_path,
        "data", "silver", "assessments",
        "technical_assessments_synthetic.csv"
    ),

    "programming": os.path.join(
        project_path,
        "data", "silver", "assessments",
        "programming_assessments_synthetic.csv"
    ),

    "communication": os.path.join(
        project_path,
        "data", "silver", "assessments",
        "communication_assessments_synthetic.csv"
    ),

    "training": os.path.join(
        project_path,
        "data", "silver", "training",
        "attendance_training_synthetic.csv"
    ),

    "interviews": os.path.join(
        project_path,
        "data", "silver", "interviews",
        "mock_interviews_synthetic.csv"
    )
}


# initialize collection log
collection_log = []

# load student master dataset
if not os.path.exists(dataset_paths["students"]):
    raise FileNotFoundError(
        "Student master dataset is missing!"
    )

student_data = pd.read_csv(dataset_paths["students"])

if "student_id" not in student_data.columns:
    raise KeyError(
        "student_id is missing from student master dataset!"
    )

print("Student master dataset loaded successfully.")

# initialize consolidated dataset
performance_data = student_data.copy()

# process remaining datasets
for dataset_name, file_path in dataset_paths.items():

    if dataset_name == "students":
        collection_log.append({
            "dataset_name": dataset_name,
            "status": "success",
            "records_collected": len(student_data),
            "collection_time": datetime.now()
        })
        continue

    try:

        # check whether file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"{dataset_name} file not found"
            )

        # load dataset
        dataset = pd.read_csv(file_path)

        # validate student_id
        if "student_id" not in dataset.columns:
            raise KeyError(
                f"student_id missing in {dataset_name} dataset"
            )

        # check duplicate student IDs
        duplicate_count = dataset["student_id"].duplicated().sum()

        if duplicate_count > 0:
            raise ValueError(
                f"{dataset_name} contains {duplicate_count} "
                "duplicate student_id records"
            )

        # rename columns to avoid column name conflicts
        dataset = dataset.rename(
            columns={
                column: f"{dataset_name}_{column}"
                for column in dataset.columns
                if column != "student_id"
            }
        )

        # merge dataset with consolidated data
        performance_data = performance_data.merge(
            dataset,
            on="student_id",
            how="left",
            validate="one_to_one"
        )

        # record successful collection
        collection_log.append({
            "dataset_name": dataset_name,
            "status": "success",
            "records_collected": len(dataset),
            "collection_time": datetime.now()
        })

        print(
            f"{dataset_name} dataset collected successfully."
        )

    except Exception as e:

        # record failure
        collection_log.append({
            "dataset_name": dataset_name,
            "status": "failed",
            "records_collected": 0,
            "collection_time": datetime.now(),
            "error_message": str(e)
        })

        print(
            f"Error collecting {dataset_name} dataset: {e}"
        )


# create integrated data folder
integrated_folder = os.path.join(
    project_path,
    "data", "silver", "integrated"
)

os.makedirs(integrated_folder, exist_ok=True)


# save consolidated performance dataset
performance_output_path = os.path.join(
    integrated_folder,
    "student_performance_master.csv"
)

performance_data.to_csv(
    performance_output_path,
    index=False
)

print("\nConsolidated student performance dataset saved!")
print("Total consolidated records:", len(performance_data))
print("Total consolidated columns:", len(performance_data.columns))


# create report folder
report_folder = os.path.join(
    project_path,
    "reports", "data_quality_report"
)

os.makedirs(report_folder, exist_ok=True)


# save collection log
collection_log_df = pd.DataFrame(collection_log)

log_output_path = os.path.join(
    report_folder,
    "student_performance_collection_log.csv"
)

collection_log_df.to_csv(
    log_output_path,
    index=False
)


# display collection summary
print("\n========== COLLECTION SUMMARY ==========")

print(collection_log_df)

print("\n========== FINAL DATASET PREVIEW ==========")

print(performance_data.head(10))


print("\nStudent performance data collection completed!")
print("Performance dataset:", performance_output_path)
print("Collection log:", log_output_path)

