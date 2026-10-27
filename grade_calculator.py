
def get_grade(marks):
    """Return the grade and an encouraging message."""
    if marks >= 90:
        return "A", "Excellent work! Keep shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do even better! 😊"
    elif marks >= 60:
        return "D", "Keep practicing! Improvement is possible! 💪"
    else:
        return "F", "Don't give up! Learn from mistakes and try again! ❤️"


def get_valid_marks():
    """Keep asking until valid marks between 0 and 100 are entered."""
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Please enter a value from 0 to 100.")

        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def calculate_grade():
    """Get student details and display the final result."""
    name = input("Enter student name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    marks = get_valid_marks()
    grade, message = get_grade(marks)

    print("\n" + "=" * 35)
    print(f"📊 RESULT FOR {name.upper()}:")
    print(f"Marks: {marks:g}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")
    print("=" * 35)


def main():
    """Run the grade calculator."""
    print("WELCOME TO STUDENT GRADE CALCULATOR")
    calculate_grade()


if __name__ == "__main__":
    main()
