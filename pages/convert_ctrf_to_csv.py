import json
import csv

with open("ctrf_result.json", "r") as f:
    data = json.load(f)

with open("ctrf_result.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Feature", "Test Case", "Status", "Step Count", "Tags"])

    for test in data["tests"]:
        feature = test.get("feature", "N/A")
        name = test.get("name")
        status = test.get("status")
        step_count = len(test.get("steps", []))
        tags = ", ".join(test.get("tags", [])) if test.get("tags") else ""
        writer.writerow([feature, name, status, step_count, tags])
