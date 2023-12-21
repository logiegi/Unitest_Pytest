from data.settings.basic_data import courses


def unique_name(mentors):
    all_list = []
    [all_list.extend(x) for x in mentors]
    all_names_list = [x.split(" ")[0].strip() for x in all_list]
    all_names_set = set(all_names_list)
    all_names_sorted = sorted(list(all_names_set))
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'


def top3(mentors):
    all_list = []
    [all_list.extend(x) for x in mentors]
    all_names_list = [x.split(" ")[0].strip() for x in all_list]
    all_names_set = set(all_names_list)
    popular = [[all_names_list.count(x), x] for x in all_names_set]
    popular.sort(key=lambda x: x[0], reverse=True)
    top_3 = [f"{str(x[1])}: {str(x[0])} раз(а)" for x in popular[:3]]
    return ", ".join(top_3)


def super_names(mentors):
    mentors_names = []

    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(name.split()[0])
        mentors_names.append(course_names)

    pairs = []
    list_mentors = []

    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 == id2:
                continue
            intersection_set = set(mentors_names[id1]).intersection(set(mentors_names[id2]))
            if len(intersection_set) > 0:
                pair = {courses[id1], courses[id2]}
                if pair not in pairs:
                    pairs.append(pair)
                    names_sorted = sorted(intersection_set)
                    list_mentors.append(
                        f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(names_sorted)}\n")
    return f'{list_mentors[0]}{list_mentors[1]}{list_mentors[2]}{list_mentors[3]}'
