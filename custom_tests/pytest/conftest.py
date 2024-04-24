import os,sys 
import shutil
import tempfile
from typing import NamedTuple, Tuple
import pathlib

from gi.repository import Gio

import pytest
import xl.playlist as pl
from xl.playlist import Playlist
from xl.trax.track import Track

import logging

logging.basicConfig(level=logging.DEBUG)

m3u_converter = pl.M3UConverter()
asx_converter = pl.ASXConverter()
pls_converter = pl.PLSConverter()
xspf_converter = pl.XSPFConverter()



def get_all_playlist_uri():
    uri_list = []
    local_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        'custom_tests',
        'pytest',
        'data',
    ) + os.extsep)

    for file in os.listdir(local_path):
        filename = os.fsdecode(file)
        if(len(filename.split('.')) == 1): continue
        uri_list.append(pathlib.Path(os.path.abspath(file)).as_uri())
    return uri_list

@pytest.fixture(autouse=True)
def exaile_test_cleanup():
    """
    Teardown/setup of various Exaile globals
    """

    yield

    Track._Track__the_cuts = ['the', 'a']

    Track._Track__tracksdict.clear()

class TrackData(NamedTuple):
    ext: str
    filename: str
    uri: str
    size: int
    writeable: bool
    has_cover: bool
    has_tags: bool

def _fname(ext: str) -> Tuple[str, str, str]:
    local_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'data',
            'music',
            'delerium',
            'chimera',
            '05 - Truly',
        )
        + os.extsep
        + ext
    )

    return ext, local_path, Gio.File.new_for_path(local_path).get_uri()

def _non_unicode_name(tracknum:int, ext: str) -> Tuple[str, str, str]:
    local_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'data',
            'music',
            'bravely',
            f'0%s. Linked Horizon — 虚ろな月の下で [Vocalized Version]' % tracknum,
        )
        + os.extsep
        + ext
    )

    return ext, local_path, Gio.File.new_for_path(local_path).get_uri()

_nonstandard_metadata_tracks = [
    # Maximum int
    TrackData(*_non_unicode_name(1, 'flac'), size=20762, writeable=True, has_cover=True, has_tags=True),
    # 0 int
    TrackData(*_non_unicode_name(2, 'flac'), size=20762, writeable=True, has_cover=True, has_tags=True),
    # string escape
    TrackData(*_non_unicode_name(3, 'flac'), size=20762, writeable=True, has_cover=True, has_tags=True),
]

_playlist_converters = [
    ('m3u', m3u_converter), 
    ('asx', asx_converter), 
    ('pls', pls_converter), 
    ('xspf', xspf_converter)
]

_playlist_uri = get_all_playlist_uri()

_different_datatype_tracks = [
    # fmt: off
    TrackData(*_fname('aac'),  size=9404,  writeable=True, has_cover=True, has_tags=True),
    TrackData(*_fname('aiff'), size=21340, writeable=True, has_cover=True, has_tags=True),
    TrackData(*_fname('au'),   size=16425, writeable=False, has_cover=False, has_tags=False),
    TrackData(*_fname('flac'), size=20668, writeable=True, has_cover=True, has_tags=True),
    TrackData(*_fname('mp3'),  size=7495,  writeable=True, has_cover=True, has_tags=True),
    TrackData(*_fname('mp4'),  size=7763,  writeable=True, has_cover=True, has_tags=True),
    TrackData(*_fname('mpc'),  size=6650,  writeable=True, has_cover=False, has_tags=True),
    TrackData(*_fname('ogg'),  size=17303, writeable=True, has_cover=True, has_tags=True),
    TrackData(*_fname('spx'),  size=1000,  writeable=True, has_cover=False, has_tags=True),
    TrackData(*_fname('wav'),  size=46124, writeable=False, has_cover=False, has_tags=False),
    TrackData(*_fname('wma'),  size=4929,  writeable=True, has_cover=False, has_tags=True),
    TrackData(*_fname('wv'),   size=32293, writeable=True, has_cover=False, has_tags=True),
    # fmt: on
]

_writeable_tracks = [t for t in _different_datatype_tracks if t.writeable]

@pytest.fixture(params=_different_datatype_tracks)
def test_track(request):
    '''Provides TrackData objects for each test track'''
    return request.param

@pytest.fixture(params=_writeable_tracks)
def writeable_track(request):
    '''Provides TrackData objects for each test track that is writeable'''
    return request.param

@pytest.fixture(params=_nonstandard_metadata_tracks)
def nonstandard_track(request):
    return request.param

@pytest.fixture(params=_playlist_uri)
def test_playlist(request):
    tracks = []
    for i in _different_datatype_tracks:
        tracks.append(Track(i.uri))
    return Playlist("test playlist", tracks)

# @pytest.fixture()
# def valid_playlist_uri(request):
    
@pytest.fixture(params=_playlist_converters)
def playlist_converter(request):
    return request.param

@pytest.fixture
def test_tracks():
    """
    Returns an object that can be used to retrieve test track data
    """

    class _TestTracks:
        def get(self, ext):
            return [x for x in _different_datatype_tracks if x.filename.endswith(ext)][0]

    return _TestTracks()
