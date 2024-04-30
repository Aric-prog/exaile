import os,sys 
import shutil
import tempfile
from typing import NamedTuple, Tuple
import pathlib

from gi.repository import Gio

import pytest
import xl.playlist as pl
from xl.playlist import Playlist, PlaylistExportOptions
from xl.trax.track import Track

import logging

logging.basicConfig(level=logging.DEBUG)

m3u_converter = pl.M3UConverter()
asx_converter = pl.ASXConverter()
pls_converter = pl.PLSConverter()
xspf_converter = pl.XSPFConverter()

_all_converters = {
    'm3u' : m3u_converter,
    'asx' : asx_converter,
    'pls' : pls_converter,
    'xspf' : xspf_converter,
}

_relative_options = [
    PlaylistExportOptions(relative=True),
    PlaylistExportOptions(relative=False)
]

def get_path_to_test():
    path = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        'data') + os.extsep
    )
    return path

def get_uri_to_test():
    path = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        'data') + os.extsep
    )

    return Gio.File.new_for_path(path).get_uri()

def get_playlist_uri(playlist_name: str, ext: str):
    local_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        'data',
        playlist_name)
        + os.extsep
        + ext
    )
    
    return Gio.File.new_for_path(local_path).get_uri()

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

def _foo_name(tracknum:int, ext: str) -> Tuple[str, str, str]:
    local_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'data',
            'music',
            'foo',
            f'0%s—foo' % tracknum,
        )
        + os.extsep
        + ext
    )

    return ext, local_path, Gio.File.new_for_path(local_path).get_uri()

_playlist_converters = [
    ('m3u', m3u_converter), 
    ('asx', asx_converter), 
    ('pls', pls_converter), 
    ('xspf', xspf_converter)
]

_playlist_uri = [
    get_playlist_uri('bravely', 'm3u'),
    get_playlist_uri('bravely', 'pls'),
    get_playlist_uri('bravely', 'xspf'),
    get_playlist_uri('bravely', 'asx'),
    get_playlist_uri('truly', 'm3u'),
    get_playlist_uri('truly', 'pls'),
    get_playlist_uri('truly', 'xspf'),
    get_playlist_uri('truly', 'asx'),
    get_playlist_uri('foo', 'm3u'),
    get_playlist_uri('foo', 'pls'),
    get_playlist_uri('foo', 'xspf'),
    get_playlist_uri('foo', 'asx'),
]

_nonstandard_metadata_tracks = [
    # Maximum int
    TrackData(*_non_unicode_name(1, 'flac')),
    # 0 int
    TrackData(*_non_unicode_name(2, 'flac')),
    # string escape
    TrackData(*_non_unicode_name(3, 'flac')),
]

_different_datatype_tracks = [
    TrackData(*_fname('aac')),
    TrackData(*_fname('aiff')),
    TrackData(*_fname('au')),
    TrackData(*_fname('flac')),
    TrackData(*_fname('mp3')),
    TrackData(*_fname('mp4')),
    TrackData(*_fname('mpc')),
    TrackData(*_fname('ogg')),
    TrackData(*_fname('spx')),
    TrackData(*_fname('wav')),
    TrackData(*_fname('wma')),
    TrackData(*_fname('wv')),
    TrackData(*_foo_name(1, 'ogg')),
    TrackData(*_foo_name(2, 'ogg')),
    TrackData(*_foo_name(3, 'ogg')),
]

_test_playlists = []

_repeat_modes = ['disabled', 'all', 'track']
_shuffle_modes = ['disabled', 'track', 'album', 'random']
_dynamic_modes = ['disabled', 'enabled']


def create_test_playlists(track_list, pl_name):
    tracks = []
    for i in track_list:
        tracks.append(Track(i.uri))
    return Playlist(pl_name, tracks)

_test_playlists.append(create_test_playlists(_different_datatype_tracks, "testing"))
_test_playlists.append(create_test_playlists(_nonstandard_metadata_tracks, "nonstandard"))

@pytest.fixture(params=_relative_options)
def playlist_export_options(request):
    return request.param

@pytest.fixture(params=_different_datatype_tracks + _nonstandard_metadata_tracks)
def test_track(request):
    '''Provides TrackData objects for each test track'''
    return request.param

@pytest.fixture(params=_repeat_modes)
def repeat_modes(request):
    return request.param

@pytest.fixture(params=_shuffle_modes)
def shuffle_modes(request):
    return request.param

@pytest.fixture(params=_dynamic_modes)
def dynamic_modes(request):
    return request.param

@pytest.fixture(params=_playlist_uri)
def playlist_uri(request):
    return request.param

@pytest.fixture(params=_test_playlists)
def test_playlist(request):
    return request.param

@pytest.fixture(params=_test_playlists)
def test_playlist_copy(request):
    return request.param

@pytest.fixture(params=_playlist_converters)
def playlist_converter(request):
    return request.param

@pytest.fixture()
def all_converters():
    return _all_converters
