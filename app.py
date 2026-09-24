import sys

def generate_report(course_name, student_count):
    with open("build_report.txt", "w") as f:
        f.write(f"Course Name: {course_name}\n")
        f.write(f"Students Enrolled: {student_count}\n")
    print("Report build_report.txt generated successfully.")

if __name__ == "__main__":
    # Read arguments passed from Jenkins script step
    if len(sys.argv) > 2:
        generate_report(sys.argv[1], sys.argv[2])
    else:
        generate_report("DevOps Engineering", "45")
