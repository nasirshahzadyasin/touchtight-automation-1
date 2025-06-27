import json

with open("behave_raw.json") as f:
    behave_data = json.load(f)

ctrf_result = {
    "tool": "behave",
    "version": "1.2.6",
    "tests": []
}

for feature in behave_data:
    for scenario in feature.get("elements", []):
        test_case = {
            "feature": feature["name"],
            "name": scenario["name"],
            "tags": scenario.get("tags", []),
            "status": scenario["steps"][-1]["result"]["status"],
            "steps": [
                {
                    "name": step["name"],
                    "keyword": step["keyword"],
                    "status": step["result"]["status"]
                } for step in scenario["steps"]
            ]
        }
        ctrf_result["tests"].append(test_case)

with open("Touchtight_Automation_Test_Report.json", "w") as out:
    json.dump(ctrf_result, out, indent=2)
