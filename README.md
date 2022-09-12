# e-diary

Это скрипт для исправления оценок и заметок в электронном дневнике школы

## Как он работает:

1. Вы скачиваете скрипт. Вставляете файл `fix_marks.py` в корневую директорию джанго проекта электронного дневника школы
   рядом с manage.py
2. Запускаете джанго сайт командой

```python
python3 manage.py runserver
```

3. В терминале запускате shell командой:

```python
python3 manage.py shell
```

4. В shell импортируете скрипт командой:

```python
from fix_marks import fix_marks, delete_chastisements, create_commendation, get_schoolkid
```

5. Затем с помошью функции `get_schoolkid` из БД достаете объект ученика присваивая его переменной `schoolkid`,
   параметрами в функцию передаете ФИО, если передать только фамилию скрипт тоже сработает, но может найти более одого
   ученика и тогда скрипт завершится с ошибкой.

```python
schoolkid = get_schoolkid('ФИО')
```

6. Если хотите заменить все 2ки и 3ки на 5ки, запустите функцию ниже

```python
fix_marks(schoolkid)
```

7. Если хотите добавить похвалу от имени учителя случайного урока, то запустите функцию ниже

```python
create_commendation(schoolkid)
```

8. Если хотите удалить все замечания учителей, то запустите функцию ниже

```python
delete_chastisements(schoolkid)
```

## Установка

Используйте данную инструкцию как установить этот скрипт


1. Установить

```python
git clone https://github.com/Maxim-Pekov/e-diary.git
```

2. Скопируйте скрипт `fix_marks.py` в корневую папку джанго проекта вашего электронного дневника рядом с `model.py`
3. Далее следуйте инструкции, как он работает
---
## About me

[<img align="left" alt="maxim-pekov | LinkedIn" width="30px" src="https://img.icons8.com/color/48/000000/linkedin-circled--v3.png" />https://www.linkedin.com/in/maxim-pekov/](https://www.linkedin.com/in/maxim-pekov/)
</br>

<img align="left" alt="maxim-pekov" width="28px" src="https://upload.wikimedia.org/wikipedia/commons/5/5c/Telegram_Messenger.png" />
@MaxPekov
</br>

[//]: # (Карточка профиля: )
![](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Maxim-Pekov&theme=solarized_dark)

[//]: # (Статистика языков в коммитах:)

[//]: # (Статистика языков в репозиториях:)
![](https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=Maxim-Pekov&theme=solarized_dark)
![](https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Maxim-Pekov&theme=solarized_dark)


[//]: # (Статистика профиля:)

[//]: # (Данные по коммитам за сутки:)
![](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Maxim-Pekov&theme=solarized_dark)
![](https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=Maxim-Pekov&theme=solarized_dark)

[//]: # ([![trophy]&#40;https://github-profile-trophy.vercel.app/?username=Maxim-Pekov&#41;]&#40;https://github.com/ryo-ma/github-profile-trophy&#41;)

