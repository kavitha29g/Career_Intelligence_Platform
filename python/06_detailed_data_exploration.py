
import os
import pandas as pd

# locate project
project_path = os.path.dirname(os.path.dirname(__file__))
raw_path = os.path.join(project_path, "data", "raw")

# store column level details
details = []

# scan all csv files
for root, dirs, files in os.walk(raw_path):

    for file in files:

        if file.endswith(".csv"):

            path = os.path.join(root, file)
            df = pd.read_csv(path)

            for column in df.columns:

                details.append({
                    "dataset": file,
                    "column": column,
                    "data_type": str(df[column].dtype),
                    "missing_values": df[column].isnull().sum(),
                    "missing_percentage": round(
                        df[column].isnull().mean() * 100, 2
                    ),
                    "unique_values": df[column].nunique(),
                })

            print("Explored:", file)

# create report
report = pd.DataFrame(details)

# save report
output_path = os.path.join(
    project_path, "reports", "data_quality_report"
)

os.makedirs(output_path, exist_ok=True)

report.to_csv(
    os.path.join(output_path, "detailed_data_exploration.csv"),
    index=False
)

print("\nDetailed exploration completed!")
print("Total columns analyzed:", len(report))
