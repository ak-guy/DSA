"""
Coding Problem Tracker CLI with Dynamic Grid Layout

This script provides a Command Line Interface (CLI) tool to track coding interview
problems in an organized, human-readable, plain-text grid format (`problem_tracker.txt`).
It mimics an Excel spreadsheet inside a text file by dynamically calculating column
widths based on the maximum string length of each data entry.

Schema Layout:
-------------
1. problem_id      : Unique Integer identifier for the problem (Primary Key).
2. problem_name    : String name of the problem (e.g., "Two Sum").
3. could_solve     : String enum value indicating success status ['Yes', 'No', 'Partial'].
4. difficulty      : String enum value indicating problem difficulty ['Easy', 'Medium', 'Hard'].
5. revision_date   : Target completion/revision date in 'YYYY-MM-DD' format.
                     Defaults to exactly 1 week (7 days) from the current system date.
6. remaining_date  : Automatically generated live status/countdown tracker.
                     Computes the delta between the system date and the `revision_date`.
7. similar_problem : Optional comma-separated IDs or names of related problems. Defaults to 'None'.

Core Operations:
----------------
- Initialization : Creates the text file with a stylized layout if it does not exist.
- Upsert Logic   : Reads the existing document. If an entered `problem_id` already exists,
                   the script updates that exact record. Otherwise, it appends a new record.
- Live Refresh   : Every single execution triggers a full recalculation of the `remaining_date`
                   countdown timer for EVERY row in the document relative to the current day.
- Dynamic Layout : Dynamically calculates maximum width required per column across the dataset
                   and formats the final output text cleanly using custom spacing matrix buffers.

Usage Examples:
---------------
1. Adding a new problem using default target date (1 week from today):
   $ python3 tracker.py 1 "Two Sum" Yes Easy

2. Overwriting or adding a hard problem with a custom past or future date:
   $ python3 tracker.py 23 "Merge k Sorted Lists" No Hard --revision_date "2026-05-20" --similar_problem "21, 88"
"""

import argparse
import os
import re
from datetime import datetime, timedelta

# Define the filename
FILE_NAME = "problem_tracker.txt"

# Define the schema/headers
SCHEMA = [
    "problem_id",
    "problem_name",
    "could_solve",
    "difficulty",
    "revision_date",
    "remaining_date",
    "similar_problem",
]

# Set minimum widths for each column to ensure headers fit comfortably
MIN_WIDTHS = {
    "problem_id": 12,
    "problem_name": 25,
    "could_solve": 13,
    "difficulty": 12,
    "revision_date": 15,
    "remaining_date": 22,
    "similar_problem": 17,
}


def calculate_days_elapsed(revision_date_str):
    """Calculates the days between revision_date and the current date."""
    try:
        rev_date = datetime.strptime(revision_date_str, "%Y-%m-%d").date()
        current_date = datetime.now().date()
        delta = current_date - rev_date

        if delta.days == 0:
            return "0 days (Today)"
        elif delta.days == 1:
            return "1 day ago"
        elif delta.days == -1:
            return "In 1 day (Tomorrow)"
        elif delta.days < -1:
            return f"In {abs(delta.days)} days (Future)"
        else:
            return f"{delta.days} days ago"
    except ValueError:
        return revision_date_str


def parse_existing_file():
    """Parses the padded text file back into a list of dictionaries."""
    data_rows = []
    if not os.path.exists(FILE_NAME):
        return data_rows

    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        lines = file.readlines()
        if not lines:
            return data_rows

        # Skip header line (index 0) and divider line (index 1)
        for line in lines[2:]:
            if not line.strip():
                continue

            # Split by 2 or more spaces to separate columns cleanly
            parts = [p.strip() for p in re.split(r"\s{2,}", line.strip())]

            # Pad parts with empty strings if any trailing optional data was short
            while len(parts) < len(SCHEMA):
                parts.append("")

            row_dict = dict(zip(SCHEMA, parts))
            data_rows.append(row_dict)

    return data_rows


def rewrite_file_with_dynamic_padding(all_data):
    """Calculates maximum column widths dynamically and writes perfectly padded grid."""
    # Step 1: Calculate the maximum width needed for each column
    column_widths = MIN_WIDTHS.copy()

    for row in all_data:
        for field in SCHEMA:
            val_len = len(str(row[field]))
            if val_len > column_widths[field]:
                column_widths[field] = val_len

    # Add a buffer of 3 spaces between columns
    padding_buffer = 3

    # Step 2: Build the string format template (e.g., "{:<12}   {:<25}   ...")
    format_template = "".join([
        f"{{:<{column_widths[field]}}}{' ' * padding_buffer}" for field in SCHEMA
    ]).rstrip()

    # Step 3: Write out to the file
    with open(FILE_NAME, mode="w", encoding="utf-8") as file:
        # Write Headers
        file.write(format_template.format(*SCHEMA) + "\n")

        # Write a clean separator line underneath headers
        separator = format_template.format(*[
            "-" * column_widths[field] for field in SCHEMA
        ])
        file.write(separator + "\n")

        # Write Data Rows
        for row in all_data:
            row_values = [str(row[field]) for field in SCHEMA]
            file.write(format_template.format(*row_values) + "\n")


def add_or_update_problem(new_data):
    """Adds a new problem or updates an existing one, recalculating all rows."""
    existing_rows = parse_existing_file()
    updated = False

    # Process and recalculate existing records
    for row in existing_rows:
        if row["problem_id"] == str(new_data["problem_id"]):
            # Update matching row with incoming info
            new_data["remaining_date"] = calculate_days_elapsed(
                new_data["revision_date"]
            )
            row.update(new_data)
            updated = True
        else:
            # Refresh live countdown for all other rows
            row["remaining_date"] = calculate_days_elapsed(row["revision_date"])

    # If it's a completely new row, append it to the dataset
    if not updated:
        new_data["remaining_date"] = calculate_days_elapsed(new_data["revision_date"])
        existing_rows.append(new_data)

    # Re-render everything with new dynamic layouts
    rewrite_file_with_dynamic_padding(existing_rows)

    if updated:
        print(f"Successfully updated Problem ID {new_data['problem_id']}.")
    else:
        print(
            f"Successfully added new Problem ID {new_data['new_id'] if 'new_id' in new_data else new_data['problem_id']}."
        )


def main():
    parser = argparse.ArgumentParser(
        description="Track coding problems with beautiful dynamic column layouts."
    )

    parser.add_argument("problem_id", type=int, help="Unique ID of the problem")
    parser.add_argument("problem_name", type=str, help="Name of the problem")
    parser.add_argument(
        "could_solve", type=str, choices=["Yes", "No", "Partial"], help="Can solve?"
    )
    parser.add_argument(
        "difficulty", type=str, choices=["Easy", "Medium", "Hard"], help="Difficulty"
    )

    one_week_from_now = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

    parser.add_argument(
        "--revision_date", type=str, default=one_week_from_now, help="YYYY-MM-DD"
    )
    parser.add_argument(
        "--similar_problem", type=str, default="None", help="Similar problems"
    )

    args = parser.parse_args()

    problem_data = vars(args)
    problem_data["remaining_date"] = ""

    add_or_update_problem(problem_data)


if __name__ == "__main__":
    main()
