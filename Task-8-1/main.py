import requests
from functools import total_ordering
# from pprint import pprint


@total_ordering
class Heroes:

    def __init__(self, name):
        self.name = name
        self.id = ''
        self.intelligence = ''

    def __str__(self):
        text = f'{self.name}  id = {self.id}  intelligence = {self.intelligence}'
        return text

    def __lt__(self, other):
        if isinstance(other, Heroes):
            return int(self.intelligence) < int(other.intelligence)
        else:
            return 'Ошибка, один из объектов не относится к классу Heroes!'

    def __eq__(self, other):
        if isinstance(other, Heroes):
            return int(self.intelligence) == int(other.intelligence)
        else:
            return 'Ошибка, один из объектов не относится к классу Heroes!'


def data_acquisition(name: str) -> object:
    """ Посылает запрос на сайт на поиск по имени и возвращает объект класса Heroes,
        который содержит интересующие нас характеристики: Имя, id - героя и значение параметра intelligence,
        а также выводит их в консоль.
    """
    url = 'https://superheroapi.com/api/2619421814940190/search/' + name
    resp = requests.get(url)
    data = resp.json()
    if data['response'] == 'success':
        for hero_data in data['results']:
            if hero_data['name'] == name:
                hero = Heroes(name)
                hero.id = hero_data['id']
                hero.intelligence = hero_data['powerstats']['intelligence']
                print(hero)
                return hero
    else:
        print(f'Ошибка! Героя с именем {name} не найдено!')


def comparison_heroes(heroes_list: list) -> object:
    """ Находит героя с наибольшим значением параметра интелект из представленного списка героев,
        записывает соответствующее сообщение и данные героя в файл 'winner.txt' в текущий каталог,
        выводит их в консоль, а также возвращает победителя как объект класса Heroes.

        heroes_list - список героев, состоящий из объектов класса Heroes
    """
    winner = heroes_list[0]
    for hero in heroes_list:
        if hero > winner:
            winner = hero
    with open('winner.txt', 'w', encoding='utf-8') as result:
        result_str = f'Самый умный супергерой - {winner.name}  id = {winner.id}  intelligence = {winner.intelligence}'
        result.write(result_str)
    print('\n', result_str)
    return winner


def reading_file(file_path: str) -> list:
    """ Считывает имена героев из файла с указанным именем/путем и возвращает список, состоящий
        из объектов класса Heroes.

        file_path - имя или путь к файлу из которого нужно считать имена, интересующих нас героев.
    """
    heroes_list = []
    with open(file_path, encoding="utf-8") as source_file:
        for hero_name in source_file:
            if hero_name.strip() == '':
                continue
            else:
                hero = data_acquisition(hero_name.strip())
                if isinstance(hero, Heroes):
                    heroes_list += [hero]
    return heroes_list


if __name__ == "__main__":
    file = 'list-of-heroes.txt'
    comparison_heroes(reading_file(file))
