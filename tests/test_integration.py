from lib.music_library import MusicLibrary
from lib.track import Track 

'''Given two tracks added, they are represented in the list'''
def test_adds_multiple_tracks_and_lists_them():
    music_library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 1")
    track_2 = Track("My Title 2", "My Artist 2")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.all() == [track_1, track_2]

'''Given two tracks added, if title for one of these tracks searched for, the title of that track is returned in the results'''
def test_searches_by_title():
    music_library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 1")
    track_2 = Track("My Title 2", "My Artist 2")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search_by_title("My Title 2") == [track_2]

'''Given two tracks added, if part of title of one track searched for, it returns matching track'''
def test_searches_by_part_of_title():
    music_library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 1")
    track_2 = Track("My Title 2", "My Artist 2")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search_by_title("1") == [track_1]
