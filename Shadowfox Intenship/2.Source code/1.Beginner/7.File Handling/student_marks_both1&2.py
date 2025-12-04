import csv

# Read the original CSV file
with open("C:\\Users\\krish\\OneDrive\\Desktop\\Shadowfox Intenship\\2.Source code\\1.Beginner\\7.File Handling\\student_marks.csv", "r") as file:

    reader = csv.DictReader(file)
    students = []

    for row in reader:
        # Convert marks to integer
        row["Math"] = int(row["Math"])
        row["English"] = int(row["English"])
        row["Science"] = int(row["Science"])

        # Calculate total and average
        row["Total_Marks"] = row["Math"] + row["English"] + row["Science"]
        row["Average_Marks"] = row["Total_Marks"] / 3

        students.append(row)

# Write to a new CSV file
with open("C:\\Users\\krish\\OneDrive\\Desktop\\Shadowfox Intenship\\2.Source code\\1.Beginner\\7.File Handling\\student_marks.csv","w",newline="") as new_file:
    fieldnames = ["Name","Math","English","Science","Total_Marks","Average_Marks"]
    writer = csv.DictWriter(new_file,fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

print("New file student_marks_updated.csv created successfully!")
