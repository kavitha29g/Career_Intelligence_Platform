import os
import pandas as pd

# locate project
project_path = os.path.dirname(os.path.dirname(__file__))

bronze_path = os.path.join(project_path, "data", "bronze")
silver_path = os.path.join(project_path, "data", "silver")

validation_report = []

# scan silver datasets
for root, dirs, files in os.walk(silver_path):

    for file in files:

        if file.endswith(".csv"):

            silver_file = os.path.join(root, file)
            df = pd.read_csv(silver_file)

            # locate corresponding bronze file
            relative_path = os.path.relpath(root, silver_path)
            bronze_file = os.path.join(bronze_path, relative_path, file)

            bronze_df = pd.read_csv(bronze_file)

            validation_report.append({
                "dataset": file,
                "bronze_rows": len(bronze_df),
                "silver_rows": len(df),
                "silver_columns": len(df.columns),
                "missing_values": df.isnull().sum().sum(),
                "duplicate_rows": df.duplicated().sum(),
                "validation_status": "passed" if df.duplicated().sum() == 0 else "check"
            })

# create report
validation_df = pd.DataFrame(validation_report)

# save report
report_path = os.path.join(
    project_path,
    "reports",
    "data_quality_report"
)

os.makedirs(report_path, exist_ok=True)

validation_df.to_csv(
    os.path.join(report_path, "silver_validation_report.csv"),
    index=False
)

print("\nSilver validation report:")
print(validation_df)

print("\nSilver validation completed!")