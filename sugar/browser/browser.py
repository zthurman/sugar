#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import dbus

import sugar.env

from sugar.session.LogWriter import LogWriter
from sugar.browser.BrowserShell import BrowserShell

log_writer = LogWriter("Web")
log_writer.start()

gtk.rc_parse(sugar.env.get_data_file('browser.rc'))

session_bus = dbus.SessionBus()
bus_name = dbus.service.BusName('com.redhat.Sugar.Browser', bus=session_bus)
shell = BrowserShell(bus_name)
shell.start()
