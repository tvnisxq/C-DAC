import csv
import json


def convert_log_file(input_log_path, output_csv_path, output_json_path):
  records = []

  with open(input_log_path, mode="r", encoding="utf-8") as log_file:
    for line in log_file:

      line = line.strip()
      if not line:
        continue

      # Split the line using '|' as the delimiter and remove extra whitespace
      parts = [p.strip() for p in line.split("|")]

      if len(parts) == 4:
        timestamp, user_id, endpoint, status_code_str = parts

        record = {
            "timestamp": timestamp,
            "user_id": user_id,
            "endpoint": endpoint,
            "status_code": int(status_code_str),
        }
        records.append(record)

  fieldnames = ["timestamp", "user_id", "endpoint", "status_code"]

  with open(output_csv_path, mode="w", encoding="utf-8", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)


  with open(output_json_path, mode="w", encoding="utf-8") as json_file:
    json.dump(records, json_file, indent=2)