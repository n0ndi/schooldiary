import logging


COMMENDATION_PHRASES = ["Молодец!", "Отлично!", "Хорошо!", "Гораздо лучшечем я ожидал!", "Ты меня приятно удивил!"]


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    marks.update(points=5)


def remove_chastisement(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def get_schoolkid(full_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
        return schoolkid
    except Model.MultipleObjectsReturned:
        print("Уточните ФИО")
    except Model.DoesNotExist:
        print("Такого ученика не существует")


def create_commendation(schoolkid, subject):
    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter
    try:
        subject = Subject.objects.get_object_or_404(title__contains=subject, year_of_study=year_of_study)
    except Model.MultipleObjectsReturned:
        print("Уточните урок")
        return None
    lessons = Lesson.objects.filter(year_of_study=year_of_study,group_letter=group_letter, subject=subject)
    lesson = random.choice(lessons)
    teacher = lesson.teacher
    date = lesson.date
    commendation = Commendation.objects.create(teacher=teacher, subject=subject, schoolkid=schoolkid, text=random.choice(COMMENDATION_PHRASES), created=date)
    return commendation
