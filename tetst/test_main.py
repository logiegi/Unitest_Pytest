from unittest import TestCase
import pytest
from data.data_collection import unique_name, top3, super_names
from data.settings.basic_data import mentors


class DataCollections(TestCase):
    def setUp(self) -> None:
        self.mentors = mentors

    def test_one(self):
        res = unique_name(self.mentors)
        expected = "Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, " \
                   "Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, " \
                   "Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, " \
                   "Юрий"
        self.assertEqual(res, expected)

    def test_two(self):
        res = top3(self.mentors)
        expected = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
        self.assertEqual(res, expected)


@pytest.mark.parametrize(
    'mentors_, expected', [
        [mentors, "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Антон, Евгений, "
                  "Максим\n"
                  "На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр, "
                  "Евгений, Елена, Кирилл, Максим, Олег, Роман\n"
                  "На курсах 'Python-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Александр, "
                  "Евгений\n"
                  "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Денис, Евгений, "
                  "Максим\n"]
    ]
)
def test_super_names(mentors_, expected):
    res = super_names(mentors)
    assert res == expected
