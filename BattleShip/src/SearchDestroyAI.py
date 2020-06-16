from . import move, player, RandomAI
import random


class SearchDestroyAI(RandomAI.RandomAI):
    @classmethod
    def random_gen(cls, maker):
        r, c = maker.opponents[0].destroy[0]
        return r, c

    @classmethod
    def get_move(cls, maker):
        try:
            r, c = SearchDestroyAI.random_gen(maker)
            del maker.opponents[0].destroy[0]
            if (r, c) in maker.possible_locations:
                maker.possible_locations.remove((r, c))

        except IndexError:
            r, c = (random.choice(maker.possible_locations))
            maker.possible_locations.remove((r, c))

        coords = f'{r}, {c}'
        try:
            firing_location = move.Move.from_str(maker, coords)
        except ValueError:
            pass
        return firing_location