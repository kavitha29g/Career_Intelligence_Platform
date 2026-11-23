
import os
import shutil
import pandas as pd
from datetime import datetime

# project path
project_path = os.path.dirname(os.path.dirname(__file__))

# raw and bronze paths
raw_path = os.path.join(project_path, "data", "raw")
bronze_path = os.path.join(project_path, "data", "bronze")

# create bronze folder
os.makedirs(bronze_path, exist_ok=True)

# store ingestion details
ingestion_report = []

# scan raw folder
for root, dirs, files in os.walk(raw_path):

    for file in files:

        if file.endswith(".csv"):

            source_file = os.path.join(root, file)

            # preserve folder structure
            relative_folder = os.path.relpath(root, raw_path)

            destination_folder = os.path.join(
                bronze_path, relative_folder
            )

            os.makedirs(destination_folder, exist_ok=True)

            destination_file = os.path.join(
                destination_folder, file
            )

            # copy file into bronze
            shutil.copy2(source_file, destination_file)

            # inspect ingested file
            df = pd.read_csv(destination_file)

            ingestion_report.append({
                "dataset": file,
                "source_folder": relative_folder,
                "rows_ingested": len(df),
                "columns_ingested": len(df.columns),
                "ingestion_time": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "status": "success"
            })

            print("Ingested:", file)

# create ingestion report
report = pd.DataFrame(ingestion_report)

# save report
report_path = os.path.join(
    project_path, "reports", "data_quality_report"
)

os.makedirs(report_path, exist_ok=True)

report.to_csv(
    os.path.join(report_path, "bronze_ingestion_report.csv"),
    index=False
)

print("\nBronze ingestion completed!")
print("Total datasets ingested:", len(report))
