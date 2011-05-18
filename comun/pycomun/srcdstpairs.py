#!/usr/bin/env python
#coding=utf-8
# srcdstpairs: Creates list of src dst pairs from a from element and to
# element
# Copyright (C) 2011 Joel Granados <joel.granados@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
import logging
import sys
import os.path
import os

class SrcDstPairs:
    FromToPaths = []

    def __init__(self, from_elem, to_elem, in_suffix="", out_suffix=".out"):
        if os.path.exists(to_elem) and not os.path.isdir(to_elem):
            sdplog.warning("Should NOT overwrite %s" % to_elem)
            return
        if not os.path.exists(from_elem):
            sdplog.warning("From element SHOULD exist")
            return

        to_elem_is_file = False
        if not os.path.exists(to_elem):
            to_elem_is_file = True #Therefore it's supposed to be a file

        if not os.path.isdir(from_elem): #file or link
            if to_elem_is_file:
                self.FromToPaths = [(from_elem, to_elem)]
            elif not to_elem_is_file:
                outname = os.path.join(to_elem,
                                       os.path.basename(from_elem)+out_suffix)
                if not os.paht.exists(outname):
                    self.FromToPaths = [(from_elem, outname)]
                else:
                    sdplog.warning("Should NOT overwrite %s" % outname)
                    return

        elif os.path.isdir(from_elem):
            if not to_elem_is_file: # to_elem is a dir.
                for entry in os.listdir(from_elem):
                    if entry.endswith(in_suffix):
                        inname = os.path.join(from_elem, entry)
                        outname = os.path.join(to_elem, entry+out_suffix)
                        if not os.path.exists(outname):
                            self.FromToPaths.append( (inname, outname) )
                        else:
                            sdplog.warning("Should NOT overwirte %s" % outname)
                            continue

            elif to_elem_is_file: # to_elem does not exists
                for entry in os.listdir(from_elem):
                    if entry.endswith(in_suffix):
                        inname = os.path.join(from_elem, entry)
                        self.FromToPaths = [(inname, to_elem)]
                        break
    @property
    def pairs(self):
        return self.FromToPaths

def initLogger():
    Logger = logging.getLogger("srcdstpairs")
    Logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)

    #FIXME: Add a file log when we add the config file.
    #handler = logging.FileHandler(config.log.filename)

    formatter = logging.Formatter("%(asctime)s -%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    Logger.addHandler(handler)

initLogger()
sdplog = logging.getLogger("srcdstpairs")
