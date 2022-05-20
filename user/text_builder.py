def user_university_view(univ_list):
    if len(univ_list) != 0:
        text = '<b>Оберіть університет</b>\nСписок університетів:\n\n'
        for i, j in enumerate(univ_list, 1):
            text += f'{str(i)}) {j[1]}\n'
    else:
        text = '<b>На данний момент не знайдено жодного університету</b>'

    return text


def user_faculty_view(faculty_list):
    if len(faculty_list) != 0:
        text = '<b>Оберіть факультет</b>\nСписок факультетів:\n\n'
        for i, j in enumerate(faculty_list, 1):
            text += f'{str(i)}) {j[1]}\n'
    else:
        text = '<b>На данний момент не знайдено жодного факультет</b>'

    return text


def user_department_view(department_list):
    if len(department_list) != 0:
        text = '<b>Оберіть кафедру</b>\nСписок кафедр:\n\n'
        for i, j in enumerate(department_list, 1):
            text += f'{str(i)}) {j[1]}\n'
    else:
        text = '<b>На данний момент не знайдено жодної кафедри</b>'

    return text


def user_specialty_view(specialty_list):
    if len(specialty_list) != 0:
        text = '<b>Оберіть сеціальностей</b>\nСписок сеціальностей:\n\n'
        for i, j in enumerate(specialty_list, 1):
            text += f'{str(i)}) {j[1]}\n'
    else:
        text = '<b>На данний момент не знайдено жодної сеціальності</b>'

    return text


def user_topics_view(topics_list):
    if topics_list is not None:
        text = '<b>Список тем:</b>\n\n'
        for i, j in enumerate(topics_list, 1):
            text += f'{str(i)}) {j[1]}, {j[2]}\n'
    else:
        text = '<b>На данний момент не знайдено жодної теми</b>'

    return text
