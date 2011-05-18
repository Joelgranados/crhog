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
import os.path
import os

class SrcDstPairs:
    FromToPaths = []

    def __init__(self, from_elem, to_elem, in_suffix="", out_suffix=".out"):
        if os.path.exists(to_elem) and not os.path.isdir(to_elem):
            raise Exception("Will not overwrite %s" % to_elem)
        if not os.path.exists(from_elem):
            raise Exception("From element needs to exist")

        to_elem_is_file = False
        if not os.path.exists(to_elem):
            to_elem_is_file = True

        if not os.path.isdir(from_elem): #file or link
            if to_elem_is_file:
                self.FromToPaths = [(from_elem, to_elem)]
            elif not to_elem_is_file:
                outname = os.path.join(to_elem,
                                       os.path.basename(from_elem)+out_suffix)
                self.FromToPaths = [(from_elem, outname)]

        elif os.path.isdir(from_elem):
            if not to_elem_is_file: # to_elem is a dir.
                for entry in os.listdir(from_elem):
                    if entry.endswith(in_suffix):
                        inname = os.path.join(from_elem, entry)
                        outname = os.path.join(to_elem, entry+out_suffix)
                        self.FromToPaths.append( (inname, outname) )

            elif to_elem_is_file: # to_elem does not exists
                for entry in os.listdir(from_elem):
                    if entry.endswith(in_suffix):
                        inname = os.path.join(from_elem, entry)
                        self.FromToPaths = [(inname, to_elem)]
                        break
    @property
    def pairs(self):
        return self.FromToPaths
