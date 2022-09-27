import random

from datacenter.models import Subject, Lesson, Commendation, Teacher, Chastisement, Mark, Schoolkid
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


def delete_chastisements(schoolkid):
    chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisement.delete()


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(points=5)


def create_commendation(schoolkid):
    commendations = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
                     'Великолепно!']
    lessons_title = ['Изобразительное искусство', 'Чтение', 'Труд', 'Математика', 'Чистописание', 'Физкультура', 'Музыка',
              'Природоведение']

    commendation = random.choice(commendations)
    lesson = random.choice(lessons_title)
    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter
    lessons = Lesson.objects.filter(year_of_study=year_of_study, group_letter=group_letter, subject__title=lesson)
    lessons_count = len(lessons)
    if lessons_count:
        teacher_name = lessons[lessons_count - 1].teacher
        subject_title = lessons[lessons_count - 1].subject.title
        date = lessons[lessons_count - 1].date
        teacher = Teacher.objects.get(full_name=teacher_name)
        subject = Subject.objects.get(title=subject_title, year_of_study=year_of_study)
        Commendation.objects.create(teacher=teacher, subject=subject, created=date, text=commendation, schoolkid=schoolkid)


def get_schoolkid(full_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
    except MultipleObjectsReturned:
        print('Найдено несколько учеников по заданным параметрам Имени')
    except ObjectDoesNotExist:
        print('Не найдено ни одного ученика по заданным параметрам Имени')
    return schoolkid
