# 👨‍🎓 Student Marks Program: Easy Guide

This is a **Python program** that calculates student results. It uses marks from **CAT1, CAT2, Final Exam, Internal Assessment, and Attendance**.

The program also provides useful class-level information such as the **class average**, **standard deviation**, **S Threshold**, **A Threshold**, and the **final letter grade**.

---

## ✅ What the Program Does

Here’s a simple list of what this tool can do:

* **Handle Many Students:** Takes marks and information for multiple students.
* **CAT1 & CAT2 Calculation:** Converts CAT1 and CAT2 marks from 50 to their respective 15-mark weight.
* **Attendance Check:** Checks whether the student has at least 75% attendance.
* **Calculate Total Marks:** Adds all weighted marks to calculate the final score out of 100.
* **Check for Failure:** Checks whether the student fails because of attendance or Final Exam marks.
* **Give a Final Grade:** Assigns a letter grade (**S, A, B, C, D, E, F**).
* **Analyze the Class:** Calculates the **average**, **standard deviation**, **S Threshold**, **A Threshold**, and minimum passing threshold.

---

## 🔢 How We Count the Marks (Out of 100)

The marks are converted according to their final weight to obtain a total score out of **100**.

| Part of the Grade  | Max Score (Input) | Counted As (Final Weight) |
| :----------------- | :---------------: | :-----------------------: |
| **CAT1**           |      50 marks     |          15 marks         |
| **CAT2**           |      50 marks     |          15 marks         |
| **Final Exam**     |     100 marks     |          30 marks         |
| **Internal Marks** |      35 marks     |          35 marks         |
| **Attendance**     |     Based on %    |          5 marks          |
| **Total**          |         —         |       **100 marks**       |

### 📌 Mark Conversion

**CAT1:**

```text
CAT1 Contribution = (CAT1 Marks / 50) × 15
```

**CAT2:**

```text
CAT2 Contribution = (CAT2 Marks / 50) × 15
```

**Final Exam:**

```text
Final Exam Contribution = (Final Exam Marks / 100) × 30
```

**Internal Marks:**

```text
Internal Contribution = Internal Marks
```

**Attendance:**

```text
Attendance ≥ 75% → 5 marks
Attendance < 75% → 0 marks + Debarred
```

---

## 🛑 Failing / Debarment Rules

It is important to know the conditions under which a student can fail or be debarred.

### 1. Attendance Rule

If attendance is **75% or above**, the student receives:

```text
5 Attendance Marks
```

There are **no separate 1/2/3/4-mark attendance slabs**.

If attendance is **below 75%**:

```text
Attendance Marks = 0
Status = DEBARRED
```

The student is therefore debarred from the subject.

### 2. Final Exam Rule

If the student scores **less than 40 marks out of 100** in the Final Exam:

```text
Status = F (Fail)
```

---

## 📊 Relative Grading System

The final grade is determined using the **class average (Mean)** and **Standard Deviation (σ)**.

The program calculates the following thresholds:

```text
S Threshold = Mean + 1.5 × σ

A Threshold = Mean + 0.5 × σ

B Threshold = Mean - 0.5 × σ

C Threshold = Mean - 1.0 × σ

D Threshold = Mean - 1.5 × σ

E Threshold = Mean - 2.0 × σ
```

The grades are assigned as follows:

| Grade | Condition               |
| :---: | :---------------------- |
| **S** | Marks ≥ Mean + 1.5σ     |
| **A** | Marks ≥ Mean + 0.5σ     |
| **B** | Marks ≥ Mean - 0.5σ     |
| **C** | Marks ≥ Mean - 1.0σ     |
| **D** | Marks ≥ Mean - 1.5σ     |
| **E** | Marks ≥ Mean - 2.0σ     |
| **F** | Marks below E threshold |

---

## 📈 Class Performance Summary

After entering all students' marks, the program calculates:

* **Class Average (Mean)**
* **Standard Deviation (σ)**
* **S Threshold**
* **A Threshold**
* **Minimum Passing Mark**

Example:

```text
===========================================
        CLASS PERFORMANCE SUMMARY
===========================================
Class Average (Mean): 68.42
Standard Deviation (sigma): 8.35
S Threshold: 80.95
A Threshold: 72.60
Minimum Passing Mark: 51.72
===========================================
```

These values are calculated from the marks of the students who have valid numerical results.

---

## 🚀 How to Start the Program

You need two simple steps before running the program.

### 1. Install NumPy

NumPy is required for calculating the **mean** and **standard deviation**.

Run:

```bash
pip install numpy
```

You only need to install it once.

### 2. Run the Program

Run the Python file using:

```bash
python code.py
```

The program will then ask you to enter the student details.

For each student, it will ask for:

```text
CAT1 Marks (out of 50)
CAT2 Marks (out of 50)
Final Exam Marks (out of 100)
Internal Assessment Marks (out of 35)
Attendance Percentage
```

---

## 📁 Project Files

The project contains the following files:

* `code.py` — Main Python program containing the result calculation and grading logic.
* `README.md` — This guide explaining the project and its working.
* `statement.md` — Document explaining the main problem statement/task.

---

## 📝 Example Calculation

Suppose a student has:

```text
CAT1       = 40 / 50
CAT2       = 42 / 50
Final      = 65 / 100
Internal   = 30 / 35
Attendance = 82%
```

The weighted marks will be:

```text
CAT1       = (40 / 50) × 15 = 12.00
CAT2       = (42 / 50) × 15 = 12.60
Final      = (65 / 100) × 30 = 19.50
Internal   = 30.00
Attendance = 5.00
```

Therefore:

```text
Total = 12.00 + 12.60 + 19.50 + 30.00 + 5.00

Total = 79.10 / 100
```

The student's final grade is then determined using the class **Mean** and **Standard Deviation**.

---

## ⚠️ Important

A student with attendance below **75%** is **Debarred**, regardless of their marks.

For example:

```text
Attendance = 74%

Attendance Marks = 0
Status = DEBARRED
```

Whereas:

```text
Attendance = 75%

Attendance Marks = 5
Status = Eligible
```

There is no separate attendance score between **1 and 4 marks**.

---
