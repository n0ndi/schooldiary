import logging


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
    except MultipleObjectsReturned:
        logging.exception("Уточните ФИО")
    except DoesNotExist:
        logging.exception("Такого ученика не существует")


def create_commendation(schoolkid, subject):
    commendation_phrases = ["Молодец!", "Отлично!", "Хорошо!", "Гораздо лучшечем я ожидал!", "Ты меня приятно удивил!"]
    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter
    subject = Subject.objects.get(title__contains=subject, year_of_study=year_of_study)
    lessons = Lesson.objects.filter(year_of_study=year_of_study,group_letter=group_letter, subject=subject)
    lesson = random.choice(lessons)
    teacher = lesson.teacher
    date = lesson.date
    commendation = Commendation.objects.create(teacher=teacher, subject=subject, schoolkid=schoolkid, text=random.choice(commendation_phrases), created=date)
    return commendation
