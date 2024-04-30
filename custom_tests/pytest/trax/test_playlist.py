from unittest.mock import patch

from gi.repository import Gio, GLib
import pytest

from custom_tests.pytest.conftest import get_path_to_test, get_uri_to_test
import xl.collection
import xl.trax.search
import xl.trax.track as track
import xl.trax.util
from xl.playlist import Playlist, PlaylistExportOptions, export_playlist
import xl.playlist as pl
import hashlib
import os

from xl.nls import gettext as _

test_folder_uri = get_uri_to_test()

# @pytest.mark.skip()
class TestPlaylist:
    def test_import_playlist(self, playlist_converter):
        ext, converter = playlist_converter
        
        assert converter.import_from_file(f'{test_folder_uri}/bravely.' + ext)
        assert converter.import_from_file(f'{test_folder_uri}/truly.' + ext)

    def test_export(self, playlist_converter, test_playlist: pl.Playlist, playlist_export_options):
        ext, converter = playlist_converter
        assert converter.export_to_file(test_playlist, f'{test_folder_uri}/output/testing.' + ext, playlist_export_options) is None
        assert converter.export_to_file(test_playlist, f'{test_folder_uri}/output/testing.' + ext, playlist_export_options) is None
    
    def test_valid_playlist(self, playlist_uri):
        assert pl.is_valid_playlist(playlist_uri)

    def test_import_and_export(self, all_converters, playlist_converter, playlist_uri, playlist_export_options):
        ext, converter = playlist_converter
        playlist_ext = playlist_uri.split('.')[1]
        playlist = all_converters[playlist_ext].import_from_file(playlist_uri)

        assert converter.export_to_file(playlist, f'{test_folder_uri}/output/testing.' + ext, playlist_export_options) is None

    def test_save_playlist(self, test_playlist: pl.Playlist):
        path = f'{get_path_to_test()}/output/output.playlist'
        test_playlist.save_to_location(path)
        assert os.path.exists(path)

    def test_load_playlist(self, test_playlist: pl.Playlist):
        path = f'{get_path_to_test()}/output/{test_playlist.name}.playlist'
        empty_playlist = pl.Playlist("test playlist", [])
        empty_playlist.load_from_location(path)
        for i in range(len(empty_playlist)):
            assert empty_playlist[i].get_basename() == test_playlist[i].get_basename()

    def test_save_and_load_playlist(self, test_playlist: pl.Playlist):
        path = f'{get_path_to_test()}/output/output.playlist'
        assert test_playlist.save_to_location(path) is None

        empty_playlist = pl.Playlist("test playlist", [])
        empty_playlist.load_from_location(path)
    
        for i in range(len(empty_playlist)):
            assert empty_playlist[i].get_basename() == test_playlist[i].get_basename()
            
    def test_clear_playlist(self, test_playlist: pl.Playlist):
        test_playlist.clear()
        assert len(test_playlist) == 0

    def test_append(self, test_playlist: pl.Playlist, test_track):
        track = xl.trax.Track(uri=test_track.uri)
        test_playlist.append(track)
        assert test_playlist[-1] == track

    def test_get_dynamic_mode(self, test_playlist: pl.Playlist):
        assert test_playlist.get_dynamic_mode() == 'disabled'
    
    def test_set_dynamic_mode(self, test_playlist: pl.Playlist, dynamic_modes):
        assert test_playlist.set_dynamic_mode(dynamic_modes) is None
        assert test_playlist.get_dynamic_mode() == dynamic_modes

    def test_get_repeat_mode(self, test_playlist: pl.Playlist):
        assert test_playlist.get_repeat_mode() == 'disabled'
    
    def test_set_repeat_mode(self, test_playlist: pl.Playlist, repeat_modes):
        assert test_playlist.set_repeat_mode(repeat_modes) is None
        assert test_playlist.get_repeat_mode() == repeat_modes

    def test_get_shuffle_mode(self, test_playlist: pl.Playlist):
        assert test_playlist.get_shuffle_mode() == 'disabled'
    
    def test_set_shuffle_mode(self, test_playlist: pl.Playlist, shuffle_modes):
        assert test_playlist.set_shuffle_mode(shuffle_modes) is None
        assert test_playlist.get_shuffle_mode() == shuffle_modes

    def test_is_track_in_playlist(self, test_playlist: pl.Playlist, test_track):
        nonexistent_track = xl.trax.Track(test_track.uri)
        assert test_playlist.__contains__(nonexistent_track) == False
        test_playlist.randomize()
        existent_track = test_playlist.get_current()
        assert test_playlist.__contains__(existent_track) == False

    def test_extend_playlist(self, test_playlist: pl.Playlist, test_track):
        track = xl.trax.Track(test_track.uri)
        test_playlist.extend([track])
        assert test_playlist.pop() == track

    