# Creator of Histogram of Oriented Gradient.
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

from comun.pycomun.srcdstpairs import SrcDstPairs
from subprocess import Popen,PIPE
import os
import logging
import sys

def create_hog ( from_elem, to_elem, fromExt="png", winSize=(256,256),
        cellSize=(8,8), blockSize=(2,2), stride=(8,8), binSize=9 ):
    #FIXME: make sure that is to_elem does not exists, the directories leading up to it do
    for filePair in SrcDstPairs(from_elem, to_elem, in_suffix=fromExt,
            out_suffix=".txt").pairs:
        dump_hog_args = [
                "./dump_rhog",
                "-W", "%d,%d"%(winSize[0],winSize[1]),
                "-C", "%d,%d"%(cellSize[0],cellSize[1]),
                "-G", "%d,%d"%(stride[0],stride[1]),
                "-B", "%d"%binSize,
                "-N", "%d,%d"%(blockSize[0],blockSize[1]),
                filePair[0],
                filePair[1] ]
        crhoglog.debug("Executing %s"%dump_hog_args)
        (stdout,stderr) = Popen(dump_hog_args,
                stdout=PIPE, stderr=PIPE).communicate()

        if stderr is not '':
            crhoglog.error(stderr)
            raise Exception("Error in the dump_hog command execution")

        # Our Hacked dump_hog creates a output file and a output.txt file
        os.remove(filePair[1])
        os.rename(filePair[1]+".txt", filePair[1])

def initLogger():
    Logger = logging.getLogger("crhog")
    Logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)

    #FIXME: Add a file log when we add the config file.
    #handler = logging.FileHandler(config.log.filename)

    formatter = logging.Formatter("%(asctime)s -%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    Logger.addHandler(handler)

initLogger()
crhoglog = logging.getLogger("crhog")
