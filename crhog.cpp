/* Creator of Histogram of Oriented Gradient.
 * Copyright (C) 2011 Joel Granados <joel.granados@gmail.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
 */

#include <include/cv.h>
#include <sys/stat.h>

using namespace cv;

/*{{{ VirtualHOGFactory class*/
VirtualHOGFactory::VirtualHOGFactory ()
  img(Mat::zeros(1,1,CV_8U)),hog(vector<long>) {}

VirtualHOGFactory::VirtualHOGFactory ( const string& filename )
  hog(vector<long>)
{
  struct stat file_stat;
  if ( stat ( filename.data(), &file_stat ) == 0 )
    this->img = imread ( filename );
  //FIXME: what happens if the file does not exist?
}

VirtualHOGFactory::VirtualHOGFactory ( const Mat& image )
  img(image),hog(vector<long>) {}

/*}}} VirtualHOGFactory class*/

/*{{{ OpenCVHOGCalculator class*/
OpenCVHOGCalculator::OpenCVHOGCalculator:VirtualHOGFactory () {}

OpenCVHOGCalculator::OpenCVHOGCalculator ( const string& filename ):
  VirtualHOGFactory ( filename ) {};

OpenCVHOGCalculator::OpenCVHOGCalculator ( const Mat& image ):
  VirtualHOGFactory ( image ) {};

bool
OpenCVHOGCalculator::calculate_hog ()
{
  //FIXME: implement this function.
  return true;
}
/*}}} OpenCVHOGCalculator class*/
