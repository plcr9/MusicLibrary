from lib.music_library import MusicLibrary

'''Initially, there are no music tracks'''
def test_initially_has_no_track():
    music_library = MusicLibrary()
    assert music_library.all() == []
