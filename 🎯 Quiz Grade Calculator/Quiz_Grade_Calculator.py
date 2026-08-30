sub_grade = {}


def entry_point():
    print("=========== Quiz / Grade Calculator ===========")

    user_name = input("Enter student name: ").strip().capitalize()

    subjects_number = get_valid("How many subjects do you have: ")

    subjects = num_of_subjects(subjects_number)

    subjects_degree(subjects, sub_grade)

    check_input = input(
        "Do you want to calculate GPA? (y/n): "
    ).strip().lower()

    if check_input == "y":
        GPA_calc(sub_grade)
        display_grades(user_name, sub_grade, "G")

    elif check_input == "n":
        display_grades(user_name, sub_grade, "D")

    else:
        print("Please enter a valid input.")


def get_valid(message):
    while True:
        try:
            value = int(input(message))

            if value < 0:
                print("Please enter a number greater than or equal to 0.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def num_of_subjects(subjects_number):
    user_subjects = []

    for num in range(subjects_number):
        subject = input(
            f"Enter Subject {num + 1} Name: "
        ).strip().capitalize()

        user_subjects.append(subject)

    return user_subjects


def subjects_degree(sub_degree, sub_grade):
    for sub in sub_degree:
        while True:
            degree = get_valid(f"{sub} Grade: ")

            if degree > 100:
                print("Grade cannot be greater than 100.")
                continue

            sub_grade[sub] = {
                "Degree": degree
            }

            break


def GPA_calc(sub_grade):
    for sub in sub_grade:
        sub_hour = get_valid(f"Enter {sub} Hours: ")

        sub_grade[sub]["Hours"] = sub_hour

        degree = sub_grade[sub]["Degree"]

        # Convert degree to GPA points
        if degree >= 90:
            grade_point = 4.0
        elif degree >= 85:
            grade_point = 3.7
        elif degree >= 80:
            grade_point = 3.3
        elif degree >= 75:
            grade_point = 3.0
        elif degree >= 70:
            grade_point = 2.7
        elif degree >= 65:
            grade_point = 2.3
        elif degree >= 60:
            grade_point = 2.0
        elif degree >= 50:
            grade_point = 1.0
        else:
            grade_point = 0.0

        sub_grade[sub]["GPA"] = grade_point


def display_grades(user_name, sub_grade, token):
    print("\n======================================")
    print(f"Student: {user_name}")
    print("======================================")

    total = sum(value["Degree"] for value in sub_grade.values())
    average = total / len(sub_grade)

    if token == "G":

        print("Subject       Degree     Hours     GPA")
        print("--------------------------------------")

        for key, value in sub_grade.items():
            print(
                f"{key:<14}"
                f"{value['Degree']:<11}"
                f"{value['Hours']:<10}"
                f"{value['GPA']}"
            )

        total_hours = sum(
            value["Hours"] for value in sub_grade.values()
        )

        weighted_gpa = sum(
            value["GPA"] * value["Hours"]
            for value in sub_grade.values()
        ) / total_hours

        print("--------------------------------------")
        print(f"Total: {total}")
        print(f"Average: {average:.1f}%")
        print(f"GPA: {weighted_gpa:.2f}")

    else:

        print("Subject       Degree")
        print("--------------------")

        for key, value in sub_grade.items():
            print(
                f"{key:<14}{value['Degree']}"
            )

        print("--------------------")
        print(f"Total: {total}")
        print(f"Average: {average:.1f}%")

    if average >= 50:
        print("Status: PASS")
    else:
        print("Status: FAIL")


entry_point()