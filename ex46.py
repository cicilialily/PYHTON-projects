class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

def add_paths(self, paths):
 self.paths.update(paths)

from nose.tools import*
from ex46.py import Room

def test_room():
    gold = Room("goldroom",
                """this room has gold in it you can grab. there's
                 door to the north.""")

    assert_equal(gold.name, "goldroom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("center", "test room in the center")
    north = Room("north", "test ro0m in the north")
    south = Room("south", ":test room in the south")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("start", "you go west and down the hole")
    west = Room("trees", "there are tress here, you can go east")
    down = Room("dungeon", "its dark down here, you can go up")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'),start)
    assert_equal(start.go('down').go('up'),start)
