"""  Модуль, в котором профилируем вызовы """


import weakref
from random import choices
import cProfile
import pstats

from lru_cache import LRUCache


class CertificateOrdinal:
    """  Класс, реализующий школьный аттестат """

    def __init__(self, alg, geom, chem, phys, bio, geog, hist):
        self.algebra = alg
        self.geometry = geom
        self.chemistry = chem
        self.physics = phys
        self.biology = bio
        self.geography = geog
        self.history = hist


class CertificateSlots:
    """  Класс, реализующий школьный аттестат с помощью слотов """

    __slots__ = ('algebra', 'geometry', 'chemistry', 'physics', 'biology',
                 'geography', 'history')

    def __init__(self, alg, geom, chem, phys, bio, geog, hist):
        self.algebra = alg
        self.geometry = geom
        self.chemistry = chem
        self.physics = phys
        self.biology = bio
        self.geography = geog
        self.history = hist


def ordinal_stat(num, grades):
    """  Функция, создающая LRU кэш аттестатов для num учеников """

    ordinal_cache = LRUCache(num)

    for i in range(num):
        ordinal_cache.set(f'stugent_{i}',
                          CertificateOrdinal(*choices(grades, k=7)))


def slots_stat(num, grades):
    """  Функция, создающая LRU кэш аттестатов со слотами для num учеников """

    slots_cache = LRUCache(num)

    for i in range(num):
        slots_cache.set(f'stugent_{i}',
                        CertificateSlots(*choices(grades, k=7)))


def weakref_stat(num, grades):
    """  Функция, создающая LRU кэш weakref аттестатов для num учеников """

    weakref_cache = LRUCache(num)

    for i in range(num):
        cert = CertificateOrdinal(*choices(grades, k=7))
        weakref_cache.set(f'stugent_{i}', weakref.ref(cert))


if __name__ == "__main__":
    N = 100000
    grades_list = [2, 3, 4, 5]
    pr = cProfile.Profile()
    pr.enable()

    ordinal_stat(N, grades_list)
    slots_stat(N, grades_list)
    weakref_stat(N, grades_list)

    pr.disable()
    ps = pstats.Stats(pr)
    ps.print_stats()
