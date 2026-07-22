# Exercise 28: Using enumerate with a custom start index
def format_task_list(tasks: list[str]) -> list[str]:
    return [f"{i}. {task}" for i, task in enumerate(tasks, start=1)]


# Exercise 29: Using zip inside a dict comprehension with filtering
def map_student_grades(names: list[str], scores: list[int]) -> dict[str, int]:
    return {
        name: score
        for name, score in zip(names, scores)
        if score >= 70
    }


# --- Verification Runs ---
if __name__ == "__main__":
    todo_list = ["Setup repo", "Write tests", "Deploy app"]
    print("Formatted Tasks:", format_task_list(todo_list))

    students = ["Spyros", "Alex", "Maria", "John"]
    grades = [85, 62, 91, 45]
    print("Passing Grades:", map_student_grades(students, grades))