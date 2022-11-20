# main.py
#
# Copyright 2022 Seyed Hosein Mousavi Fard
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from .window import LibraryWindow


class LibraryApplication(Adw.Application):

    def __init__(self):
        super().__init__(application_id='ir.hajmousa.Library',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.create_action('quit', self.quit, ['<primary>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = LibraryWindow(application=self)
        win.present()

    def on_about_action(self, widget, _):
        about = Adw.AboutWindow(transient_for=self.props.active_window,
                                application_name='Library',
                                application_icon='ir.hajmousa.Library',
                                developer_name='Seyyed Hosein Mousavi Fard',
                                version='0.1.0',
                                developers=['Seyyed Hosein Mousavi Fard'],
                                copyright='© 2022 Seyyed Hosein Mousavi Fard',
                                license_type=Gtk.License.GPL_3_0)
        about.present()

    def on_preferences_action(self, widget, _):
        print('app.preferences action activated')

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version):
    app = LibraryApplication()
    return app.run(sys.argv)
