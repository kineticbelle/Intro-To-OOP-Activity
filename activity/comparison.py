def get_student_with_more_classes(student_a, student_b):
    try:
        return student_a if student_a.num_classes > student_b.num_classes else student_b
    except:
        return "Something went wrong. Try again."