import numpy as np


def calculate_attendance_marks(attendance_percentage):
    if attendance_percentage >= 75:
        return 5
    else:
        return "Debarred"


def calculate_result(cat1_marks, cat2_marks, final_marks,
                     internal_marks, attendance_percentage):

    # Attendance check
    attendance_result = calculate_attendance_marks(attendance_percentage)

    if attendance_result == "Debarred":
        return "Debarred from Subject"

    attendance_marks = attendance_result

    # CAT1: 50 marks converted to 15
    cat1_contribution = (cat1_marks / 50) * 15

    # CAT2: 50 marks converted to 15
    cat2_contribution = (cat2_marks / 50) * 15

    # Final Exam: 100 marks converted to 30
    final_contribution = (final_marks / 100) * 30

    # Internal Assessment: already out of 35
    internal_contribution = internal_marks

    # Final Exam minimum requirement
    if final_marks < 40:
        return "F"

    # Total marks
    total_marks = (
        cat1_contribution
        + cat2_contribution
        + final_contribution
        + internal_contribution
        + attendance_marks
    )

    return total_marks


def assign_grade_and_analysis(total_marks, mean, std_dev):

    threshold_S = mean + 1.5 * std_dev
    threshold_A = mean + 0.5 * std_dev
    threshold_B = mean - 0.5 * std_dev
    threshold_C = mean - 1.0 * std_dev
    threshold_D = mean - 1.5 * std_dev
    threshold_E = mean - 2.0 * std_dev

    if total_marks >= threshold_S:
        grade = "S"
        analysis = " - Exceptional Performance!"

    elif total_marks >= threshold_A:
        grade = "A"
        analysis = " - Excellent Performance!"

    elif total_marks >= threshold_B:
        grade = "B"
        analysis = " - Good Performance"

    elif total_marks >= threshold_C:
        grade = "C"
        analysis = " - Satisfactory Performance"

    elif total_marks >= threshold_D:
        grade = "D"
        analysis = " - Marginal Pass"

    elif total_marks >= threshold_E:
        grade = "E"
        analysis = " - Requires significant effort"

    else:
        grade = "F"
        analysis = " - Needs Improvement"

    return f"{grade}{analysis}"


def get_student_input(student_number):

    print(f"\n--- Entering Data for Student {student_number} ---")

    # CAT1
    while True:
        try:
            cat1 = float(input("Enter CAT1 Marks (out of 50): "))

            if 0 <= cat1 <= 50:
                break
            else:
                print("Error: CAT1 marks must be between 0 and 50.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    # CAT2
    while True:
        try:
            cat2 = float(input("Enter CAT2 Marks (out of 50): "))

            if 0 <= cat2 <= 50:
                break
            else:
                print("Error: CAT2 marks must be between 0 and 50.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Final Exam
    while True:
        try:
            final = float(input("Enter Final Exam Marks (out of 100): "))

            if 0 <= final <= 100:
                break
            else:
                print("Error: Final marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Internal Assessment
    while True:
        try:
            internal = float(input("Enter Internal Assessment Marks (out of 35): "))

            if 0 <= internal <= 35:
                break
            else:
                print("Error: Internal marks must be between 0 and 35.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Attendance
    while True:
        try:
            attendance = float(input("Enter Attendance Percentage (0-100): "))

            if 0 <= attendance <= 100:
                break
            else:
                print("Error: Attendance percentage must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    return cat1, cat2, final, internal, attendance


def display_result(student_num, total_marks, final_grade_analysis):

    print("\n-------------------------------------------")
    print(f"       STUDENT {student_num} FINAL RESULT")
    print("-------------------------------------------")

    if total_marks == "Debarred from Subject":

        print("STATUS: DEBARRED")
        print("Reason: Attendance below 75%.")
        print("Attendance Marks: 0")

    elif total_marks == "F":

        print("STATUS: F (Fail)")
        print("Reason: Final Exam score less than 40%.")

    else:

        print(f"Total Calculated Marks (out of 100): {total_marks:.2f}")
        print(f"Final Grade & Analysis: {final_grade_analysis}")

    print("-------------------------------------------\n")


def main():

    NUM_STUDENTS = int(input("How many students :- "))

    all_student_data = []
    numerical_scores = []

    for i in range(1, NUM_STUDENTS + 1):

        cat1_marks, cat2_marks, final_marks, internal_marks, attendance_percentage = get_student_input(i)

        result = calculate_result(
            cat1_marks,
            cat2_marks,
            final_marks,
            internal_marks,
            attendance_percentage
        )

        all_student_data.append({
            'id': i,
            'result': result
        })

        if isinstance(result, (float, int)):
            numerical_scores.append(result)

    # Class statistics
    if numerical_scores:
        mean_score = np.mean(numerical_scores)
        std_dev = np.std(numerical_scores)
    else:
        mean_score = 0
        std_dev = 0

    print("\n===========================================")
    print("        CLASS PERFORMANCE SUMMARY")
    print("===========================================")
    print(f"Class Average (Mean): {mean_score:.2f}")
    print(f"Standard Deviation (sigma): {std_dev:.2f}")

    s_threshold = mean_score + 1.5 * std_dev
    a_threshold = mean_score + 0.5 * std_dev

    print(f"S Threshold: {s_threshold:.2f}")
    print(f"A Threshold: {a_threshold:.2f}")

    print(f"Minimum Passing Mark: {mean_score - 2.0 * std_dev:.2f}")
    print("===========================================")

    # Display individual results
    for data in all_student_data:

        i = data['id']
        result = data['result']

        final_grade_analysis = ""

        if isinstance(result, (float, int)):
            final_grade_analysis = assign_grade_and_analysis(
                result,
                mean_score,
                std_dev
            )

        display_result(
            i,
            result,
            final_grade_analysis
        )


if __name__ == "__main__":
    main()
