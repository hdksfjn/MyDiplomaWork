def university_name_text_builder(admin_temp_data, add=False):
    if add:
        return f'Ви обрали університет:\n <b>- {admin_temp_data["university_name"]}</b>'
    else:
        return f'Ви додали та обрали університет:\n<b>{admin_temp_data["university_name"]}</b>'


def faculty_name_text_builder(admin_temp_data, add=False):
    if add:
        return f'Ви обрали факультет:\n\n <b>- {admin_temp_data["university_name"]}</b>\n   <b>└{admin_temp_data["faculty_name"]}</b>'
    else:
        return f'Ви додали та обрали факультет:\n\n <b>- {admin_temp_data["university_name"]}</b>\n   <b>└{admin_temp_data["faculty_name"]}</b>'


def department_name_text_builder(admin_temp_data, add=False):
    if add:
        return f'Ви обрали кафедру:\n\n <b>- {admin_temp_data["university_name"]}</b>\n   <b>└{admin_temp_data["faculty_name"]}</b>\n      <b>└{admin_temp_data["department_name"]}</b>'
    else:
        return f'Ви додали та обрали кафедру:\n\n <b>- {admin_temp_data["university_name"]}</b>\n   <b>└{admin_temp_data["faculty_name"]}</b>\n      <b>└{admin_temp_data["department_name"]}</b>'


def specialty_name_text_builder(admin_temp_data, add=False):
    if add:
        return f'Ви обрали спеціальність:\n\n <b>- {admin_temp_data["university_name"]}</b>\n   <b>└{admin_temp_data["faculty_name"]}</b>\n      <b>└{admin_temp_data["department_name"]}</b>\n         <b>└{admin_temp_data["specialty_name"]}</b>'
    else:
        return f'Ви додали та обрали спеціальність:\n\n <b>- {admin_temp_data["university_name"]}</b>\n   <b>└{admin_temp_data["faculty_name"]}</b>\n      <b>└{admin_temp_data["department_name"]}</b>\n         <b>└{admin_temp_data["specialty_name"]}</b>'


def topics_name_text_builder(admin_temp_data, add=False):
    if add:
        return f'Ви обрали тему:\n\n <b>- {admin_temp_data["university_name"]}</b>\n   <b>└{admin_temp_data["faculty_name"]}</b>\n    <b>└{admin_temp_data["department_name"]}</b>\n     <b>└{admin_temp_data["faculty_name"]}</b>'
    else:
        return f'Ви додали та обрали тему:\n\n <b>- {admin_temp_data["university_name"]}</b>\n   <b>└{admin_temp_data["faculty_name"]}</b>\n    <b>└{admin_temp_data["department_name"]}</b>\n     <b>└{admin_temp_data["faculty_name"]}</b>'


def admin_university_view(univ_list):
    if len(univ_list) != 0:
        text = '<b>Оберіть або додайте університет</b>\nСписок університетів:\n\n'
        for i, j in enumerate(univ_list, 1):
            text += f'{str(i)}) {j[1]}\n'
    else:
        text = '<b>Додайте університет</b>'

    return text


def admin_faculty_view(faculty_list):
    if len(faculty_list) != 0:
        text = '<b>Оберіть або додайте факультет</b>\nСписок факультетів:\n\n'
        for i, j in enumerate(faculty_list, 1):
            text += f'{str(i)}) {j[1]}\n'
    else:
        text = '<b>Додайте факультет</b>'

    return text


def admin_department_view(department_list):
    if len(department_list) != 0:
        text = '<b>Оберіть або додайте кафедру</b>\nСписок кафедр:\n\n'
        for i, j in enumerate(department_list, 1):
            text += f'{str(i)}) {j[1]}\n'
    else:
        text = '<b>Додайте кафедру</b>'

    return text


def admin_specialty_view(specialty_list):
    if len(specialty_list) != 0:
        text = '<b>Оберіть або додайте спеціальність</b>\nСписок спеціальностей:\n\n'
        for i, j in enumerate(specialty_list, 1):
            text += f'{str(i)}) {j[1]}\n'
    else:
        text = '<b>Додайте спеціальність</b>'

    return text


def admin_topics_view(topics_list):
    if topics_list is not None:
        text = '<b>Список тем:</b>\n\n'
        for i, j in enumerate(topics_list, 1):
            text += f'{str(i)}) {j[1]}, {j[2]}, {j[3]}\n'
    else:
        text = '<b>Додайте тему</b>'

    return text


def university_view(univ_list):
    if len(univ_list) != 0:
        text = '<b>Оберіть або додайте університет</b>\nСписок університетів:\n\n'
        for i, j in enumerate(univ_list, 1):
            text += f'{str(i)}) {j[1]}\n'
    else:
        text = '<b>Додайте університет</b>'

    return text
