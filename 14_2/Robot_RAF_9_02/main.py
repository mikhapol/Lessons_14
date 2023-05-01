import json


class Raf9:
    def __init__(self):
        self.ingredients = ['lemon', 'mint', 'ice', 'soda', 'orange', 'tomato']
        self.get_cocktails_from_db()

    def __call__(self, *args, **kwargs):
        while True:
            self.__help_text()
            command = input('Введите команду: ')
            if command == '0':
                print('До свидания')
                break
            elif command == '1':
                current_ings = self.choose_ingredients()
                chose_cocktail = self.find_cocktail(current_ings)
                # print(chose_cocktail)
                if chose_cocktail is None:
                    self.save_cocktail(current_ings)
                else:
                    print(f'Вы выбрали {chose_cocktail} коктейль')
            else:
                print(f'Не знаю такой команды')

    def __help_text(self):
        print('Доступные команды')
        print('1 - выбрать ингредиенты')
        print('0 - выход')

    def save_cocktail(self, current_ings):
        self.cocktails.append({
            'name': 'unnamed',
            "ingredients": current_ings
        })

        with open('cocktails.json', 'w') as json_file:
            json.dump(self.cocktails, json_file)

    def get_cocktails_from_db(self):
        with open('cocktails.json', 'r') as json_file:
            self.cocktails = json.load(json_file)

    def find_cocktail(self, current_ings):
        for c in self.cocktails:
            # print(c.get('ingredients'))
            # print(current_ings)
            if c.get('ingredients') == current_ings:
                return c.get('name')

        return None

    def choose_ingredients(self):
        chose_ings = []
        print('Список ингредиентов')
        i = 0
        for ing in self.ingredients:
            i += 1
            print(f'{i}. {ing}')

        print('0 - для выхода')

        while True:
            command = input('Введите команду: ')
            if command == '0':
                return chose_ings
            else:
                if command.isdigit():
                    number = int(command)
                    if number > len(self.ingredients):
                        print('Такого ингредиента в списке нет')
                    else:
                        chose_ings.append(self.ingredients[number - 1])
                else:
                    print('Введите НОМЕР ингредиента')


if __name__ == '__main__':
    raf9 = Raf9()
    raf9()

    assert 'mojito' == raf9.find_cocktail(['ice', 'soda', 'mint'])
