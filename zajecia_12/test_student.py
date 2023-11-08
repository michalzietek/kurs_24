def test_calculate_grades(student):
    assert student.calculate_grades() == 20


def test_show_proper_age(student):
    assert student.age == 20



