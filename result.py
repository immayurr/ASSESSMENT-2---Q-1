students = {
    "Alice": {"Python": 85, "Mathematics": 92, "AI": 88},
    "Bob": {"Python": 45, "Mathematics": 38, "AI": 55}, 
    "Charlie": {"Python": 95, "Mathematics": 98, "AI": 96},
    "David": {"Python": 70, "Mathematics": 65, "AI": 42},
    "Emma": {"Python": 88, "Mathematics": 79, "AI": 85},
}

def assign_grade(percentage):

    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


processed_students = {}

for name, marks in students.items():
    total = sum(marks.values())
    percentage = total / 3 
    grade = assign_grade(percentage)

    processed_students[name] = {
        "marks": marks,
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade,
    }

topper_name = max(
    processed_students, key=lambda k: processed_students[k]["percentage"]
)

failed_students = []
for name, data in processed_students.items():
    for subject, score in data["marks"].items():
        if score < 50:
            failed_students.append((name, subject, score))
            break  

sorted_students = sorted(
    processed_students.items(), key=lambda x: x[1]["percentage"], reverse=True
)


print("=== STUDENT SEMESTER RESULTS ===")
for name, data in processed_students.items():
    print(
        f"Student: {name} | Total: {data['total']} | Percentage: {data['percentage']}% | Grade: {data['grade']}"
    )

print("\n=== CLASS TOPPER ===")
print(
    f"Topper: {topper_name} with {processed_students[topper_name]['percentage']}%"
)

print("\n=== STUDENTS WHO FAILED IN ANY SUBJECT ===")
if failed_students:
    for name, subject, score in failed_students:
        print(f"{name} failed in {subject} (Score: {score})")
else:
    print("No students failed any subject.")

print("\n=== STUDENTS SORTED BY PERCENTAGE (HIGHEST TO LOWEST) ===")
for name, data in sorted_students:
    print(f"{name}: {data['percentage']}%")
