
import os
import pandas as pd

# project path
project_path = os.path.dirname(os.path.dirname(__file__))

# raw data path
raw_path = os.path.join(project_path, "data", "raw")

# collect dataset details
data = []

for root, dirs, files in os.walk(raw_path):
    for file in files:
        if file.endswith(".csv"):

            path = os.path.join(root, file)
            df = pd.read_csv(path)

            data.append({
                "dataset": file,
                "rows": len(df),
                "columns": len(df.columns),
                "missing_values": df.isnull().sum().sum(),
                "duplicates": df.duplicated().sum()
            })

            print("Checked:", file)

# create report
report = pd.DataFrame(data)

# save report
output_path = os.path.join(
    project_path, "reports", "data_quality_report"
)

os.makedirs(output_path, exist_ok=True)

report.to_csv(
    os.path.join(output_path, "dataset_inventory.csv"),
    index=False
)

print("\nDataset Inventory:")
print(report)

print("\nTotal datasets:", len(report))
print("\nReport saved successfully!")
