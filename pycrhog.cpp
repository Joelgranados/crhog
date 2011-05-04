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

#include <Python.h>
#include <include/cv.h>
#include "crhog.h"

using namespace cv;

static PyObject*
Crhog_get_version ( PyObject *self, PyObject *args )
{
  PyObject * ver_mes;
  ver_mes = PyString_FromFormat (
    "%s, Version: %d.%d.", CRHOG_NAME, CRHOG_VER_MAJOR, CRHOG_VER_MINOR );
  return ver_mes;
}

static PyObject*
Crhog_calculate_hog ( PyObject *self, PyObject *args )
{
  char *img_file;

  if ( !PyArg_ParseTuple ( args, "s", &img_file ) )
    CRHOG_RETPYERR ( "Invalid params for Crhog_get_cropped_images." );

  struct stat file_stat;
  if ( stat ( img_file, &file_stat ) != 0 )
    CRHOG_RETPYERR ( "Image file does not exist." );

  HOGFactory hf( imread ( img_file ) );
  vector<long> c_hog = hf.calculate_hog ();

  /* return list with the hog values */
  PyObject *py_hog = PyList_New ( c_hog.size() );

  int i = 0;
  for ( vector<long>::iterator iter = c_hog.begin() ;
        iter != c_hog.end() ; iter++, i++ )
    if ( PyList_SetItem ( py_hog, i, PyLong_FromLong(c_hog[i]) ) == -1 )
      CRHOG_RETPYERR ( "Error creating hog list element." );

  return py_hog;
}

static PyMethodDef Crhog_methods[] = {
  {"version", (PyCFunction)Crhog_get_version, METH_NOARGS,
    "Return the version of the library." },
  {"calculate_hog", (PyCFunction)Crhog_calculate_hog, METH_VARARGS,
    "Return a list that represents the HOG." },
  {NULL}  /* Sentinel */
};

PyMODINIT_FUNC
initpycrhog (void)
{
  (void) Py_InitModule3 ( "pycrhog", Crhog_methods, CRHOG_NAME );
}
