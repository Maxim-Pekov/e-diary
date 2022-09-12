def delete_chastisements(schoolkid):
    from datacenter.models import Chastisement
    chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisement.delete()


def fix_marks(schoolkid):
    from datacenter.models import Mark
    marks = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    for mark in marks:
        mark.points = 5
        mark.save()


def create_commendation(schoolkid):
    import random
    from datacenter.models import Subject, Lesson, Commendation, Teacher
    commendations = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
                     'Великолепно!']
    lesson = ['Изобразительное искусство', 'Чтение', 'Труд', 'Математика', 'Чистописание', 'Физкультура', 'Музыка',
              'Природоведение']

    commendation = random.choice(commendations)
    lessonn = random.choice(lesson)
    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter
    lessons = Lesson.objects.filter(year_of_study=year_of_study, group_letter=group_letter, subject__title=lessonn)
    lessons_count = len(lessons)
    teacher_name = lessons[lessons_count - 1].teacher
    subject_title = lessons[lessons_count - 1].subject.title
    date = lessons[lessons_count - 1].date
    teacher = Teacher.objects.get(full_name=teacher_name)
    subject = Subject.objects.get(title=subject_title, year_of_study=year_of_study)
    Commendation.objects.create(teacher=teacher, subject=subject, created=date, text=commendation, schoolkid=schoolkid)


def get_schoolkid(full_name):
    from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
    from datacenter.models import Schoolkid
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
    except MultipleObjectsReturned:
        print('Найдено несколько учеников по заданным параметрам Имени')
    except ObjectDoesNotExist:
        print('Не найдено ни одного ученика по заданным параметрам Имени')
    return schoolkid
