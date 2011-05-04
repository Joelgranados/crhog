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
#include <opencv/cv.h>

using namespace cv;

/*{{{ VirtualHOGFactory class*/
class VirtualHOGFactory {
  public:
    VirtualHOGFactory ();
    VirtualHOGFactory ( const string& );
    VirtualHOGFactory ( const Mat& );
    virtual bool calculate_hog () = 0; /* OverrideMe! */
    virtual ~VirtualHOGFactory () {};

  private:
    const Mat img;
    vector<long> hog;
};
/*}}} VirtualHOGFactory class*/

/*{{{ OpenCVHOGCalculator class*/
class OpenCVHOGCalculator : public VirtualHOGFactory {
  public:
    OpenCVHOGCalculator ();
    OpenCVHOGCalculator ( const string& );
    OpenCVHOGCalculator ( const Mat& );
    virtual bool calculate_hog ();
    virtual ~OpenCVHOGCalculator ();
};
/*}}} OpenCVHOGCalculator class*/

/*{{{ HOGFactory class */
typedef OpenCVHOGCalculator HOGFactory;
/*}}} HOGFactory class */
