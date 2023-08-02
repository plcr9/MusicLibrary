from lib.music_library import MusicLibrary

'''Initially, there are no music tracks'''
def test_initially_has_no_track():
    music_library = MusicLibrary()
    assert music_library.all() == []

'''Initially, searching for tracks returns an empty list'''
def test_initially_searches_return_empty():
    music_library = MusicLibrary()
    assert music_library.search_by_title("what") == []
