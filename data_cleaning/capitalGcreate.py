import json
import csv

# Load the cleaned JSON file
with open("cleaned_god_output.json", "r", encoding="utf-8") as file:
    cleaned_data = json.load(file)

# Function to load CSV data into a dictionary
def load_csv_to_dict(file_path):
    csv_data = {}
    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Check if "Medicine" or "Drug" exists in the CSV
            medicine = row.get("Medicine") or row.get("Drug")
            if medicine:
                medicine = medicine.strip().lower()  # Normalize medicine name
                comment = row.get("Comment") or row.get("Comments")
                comment = comment.strip() if comment else None
           
                csv_data[medicine] = comment
    return csv_data

# Load data from the CSV files
breastfeed_data = load_csv_to_dict("breast_output.csv")
pregnancy_data = load_csv_to_dict("preg_output.csv")
hepatic_data = load_csv_to_dict("hepatic_output.csv")
renal_data = load_csv_to_dict("renal_output.csv")

# Add the Severe Warnings attribute to each medicine in the cleaned data
for entry in cleaned_data:
    medicine_name = entry["Medicine"].strip().lower()  # Normalize medicine name
    entry["Severe Warnings"] = {
        "breastfeed": breastfeed_data.get(medicine_name, "No data available"),
        "pregnancy": pregnancy_data.get(medicine_name, "No data available"),
        "hepatic": hepatic_data.get(medicine_name, "No data available"),
        "renal": renal_data.get(medicine_name, "No data available"),
    }

# Save the updated data back to a JSON file
with open("capitalG.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_data, file, indent=4, ensure_ascii=False)

print("Updated cleaned_god_output.json with Severe Warnings attribute.")