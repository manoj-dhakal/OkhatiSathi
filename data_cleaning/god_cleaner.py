import json

# Load the JSON file
with open("god_output.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Dictionary to store the best entry for each medicine
medicine_dict = {}

# Iterate through the list of dictionaries
for entry in data:
    medicine_name = entry["Medicine"]
    # Count the number of non-empty attributes
    filled_attributes_count = sum(
        1 for key, value in entry.items() if key != "Medicine" and value and isinstance(value, str) and value.strip()
    )

    # If the medicine is not in the dictionary or the current entry has more filled attributes, update it
    if medicine_name not in medicine_dict or filled_attributes_count > medicine_dict[medicine_name]["filled_count"]:
        medicine_dict[medicine_name] = {"entry": entry, "filled_count": filled_attributes_count}

# Extract the cleaned list of dictionaries
cleaned_data = [value["entry"] for value in medicine_dict.values()]

# Print the number of dictionaries before and after cleaning
print(f"Number of dictionaries before cleaning: {len(data)}")
print(f"Number of dictionaries after cleaning: {len(cleaned_data)}")

# Save the cleaned data back to a JSON file
with open("cleaned_god_output.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_data, file, indent=4, ensure_ascii=False)