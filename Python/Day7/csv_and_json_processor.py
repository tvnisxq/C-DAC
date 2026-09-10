import csv
import json


def process_student_records(input_csv_path, output_json_path):
  total_students = 0
  total_score = 0.0
  top_scorer = {"name": "", "score": float("-inf")}
  course_counts = {}

  # Open and read the CSV file using DictReader
  with open(input_csv_path, mode="r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
      total_students += 1
      score = float(row["score"])
      total_score += score
      name = row["name"]
      course = row["course"]

      # Update top scorer if the current student has a strictly higher score
      if score > top_scorer["score"]:
        top_scorer = {"name": name, "score": score}

      # Track the frequency of each course enrollment
      course_counts[course] = course_counts.get(course, 0) + 1

  # Compute the arithmetic mean, handling cases with 0 students to prevent ZeroDivisionError
  average_score = (
      round(total_score / total_students, 2) if total_students > 0 else 0.0
  )

  # Structure the aggregated data into a dictionary
  summary_data = {
      "total_students": total_students,
      "average_score": average_score,
      "top_scorer": top_scorer,
      "course_counts": course_counts,
  }

  # Export the summary dictionary to a JSON file formatted with 4 spaces of indentation
  with open(output_json_path, mode="w", encoding="utf-8") as json_file:
    json.dump(summary_data, json_file, indent=4)