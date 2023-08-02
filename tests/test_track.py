from lib.track import Track

'''When new track created, it returns its artist and title'''
def test_construct_track_and_return_artist_and_title():
    track = Track("My Title", "My Artist")
    assert track.title == "My Title"
    assert track.artist == "My Artist"

''''''
def test_formats_artist_and_title():
    track = Track("My Title", "My Artist")
    assert track.format() == "My Title by My Artist"