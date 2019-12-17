import math

class RecipeIngredient:
    def __init__(self, text):
        split = text.split(' ')
        self.name = split[1].strip()
        self.amount = int(split[0].strip())

    def __str__(self):
        return '{} {}'.format(self.amount, self.name)


class Recipe:
    def __init__(self, result):
        self.result = result
        self.sources = []

    def add(self, source):
        self.sources.append(source)

    def __str__(self):
        return '{} => {}'.format(','.join([str(x) for x in self.sources]), self.result)

    def is_target(self, name):
        return self.result.name == name

    def is_fuel(self):
        return self.result.name == 'FUEL'

    def consist_of_ore(self):
        return len(self.sources) == 1 and self.sources[0].name == 'ORE'

    def get_amount(self, amount, spare):
        if spare > amount:
            return [], spare - amount

        multiplier = math.ceil((amount - spare) / self.result.amount)
        needed = [(s.name, multiplier * s.amount) for s in self.sources]
        spare_value = multiplier * self.result.amount - (amount - spare)
        return needed, spare_value


def find_recipe_by_name(recipes, name):
    for r in recipes:
        if r.is_target(name):
            return r


def get_needed_and_spare(curr_recipe, needed_amount, spare_list):
    spare = spare_list.get(curr_recipe.result.name, 0)
    needed, spare = curr_recipe.get_amount(needed_amount, spare)
    spare_list[curr_recipe.result.name] = spare
    return needed


def main():
    with open('input.txt', 'r') as input_file:
        recipes = []
        for line in input_file:
            split1 = line.strip().split(" => ")
            result_ing = RecipeIngredient(split1[1])
            recipe = Recipe(result_ing)
            for s in split1[0].split(', '):
                recipe.add(RecipeIngredient(s))

            recipes.append(recipe)
    spare = {}
    available_ore = 1000000000000
    rounds = 0
    while True:
        needed_ing = {'FUEL': 1}

        while not(len(needed_ing.keys()) == 1 and list(needed_ing.keys())[0] == 'ORE'):
            for key in list(needed_ing):
                if key == 'ORE':
                    continue
                current = find_recipe_by_name(recipes, key)
                needed = get_needed_and_spare(current, needed_ing[key], spare)
                for n in needed:
                    val = needed_ing.get(n[0], 0)
                    needed_ing[n[0]] = val + n[1]
                needed_ing.pop(key, None)

        available_ore -= needed_ing['ORE']
        if available_ore > 0:
            rounds += 1
            if rounds % 1000 == 0:
                print('round: {} money: {}'.format(rounds, available_ore))
        else:
            print('End: {}'.format(rounds))
            break


if __name__ == "__main__":
    main()
