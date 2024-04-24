from unittest.mock import patch

from gi.repository import Gio, GLib

import xl.collection
import xl.trax.search
import xl.trax.track as track
import xl.trax.util
from xl.playlist import PlaylistExportOptions, export_playlist
import xl.playlist as pl
import hashlib

from xl.nls import gettext as _

relative_options = PlaylistExportOptions(
    relative=True
)

class TestConverter:
    def test_import_playlist(self, playlist_converter):
        ext, converter = playlist_converter
        assert converter.import_from_file(r'file:///D:/Repositories/forked_exaile/exaile/custom_tests/pytest/data/bravely.' + ext)
        assert converter.import_from_file(r'file:///D:/Repositories/forked_exaile/exaile/custom_tests/pytest/data/truly.' + ext)
        
    def test_absolute_export(self, playlist_converter, test_playlist):
        ext, converter = playlist_converter
        assert converter.export_to_file(test_playlist, r'file:///D:/Repositories/forked_exaile/exaile/custom_tests/pytest/data/output/testing.' + ext, None) is None
        assert converter.export_to_file(test_playlist, r'file:///D:/Repositories/forked_exaile/exaile/custom_tests/pytest/data/output/testing.' + ext, None) is None
    
    def test_relative_export(self, playlist_converter, test_playlist):
        ext, converter = playlist_converter    
        assert converter.export_to_file(test_playlist, r'file:///D:/Repositories/forked_exaile/exaile/custom_tests/pytest/data/output/testing.' + ext, relative_options) is None
        assert converter.export_to_file(test_playlist, r'file:///D:/Repositories/forked_exaile/exaile/custom_tests/pytest/data/output/testing.' + ext, relative_options) is None
    
    def test_valid_playlist(self, valid_playlist_uri):
        print(valid_playlist_uri)
        assert clkasjdf

    