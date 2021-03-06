##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RPtw(RPackage):
    """Parametric Time Warping aligns patterns, i.e. it aims to put
    corresponding features at the same locations. The algorithm
    searches for an optimal polynomial describing the warping. It is
    possible to align one sample to a reference, several samples to
    the same reference, or several samples to several references.
    One can choose between calculating individual warpings, or one
    global warping for a set of samples and one reference. Two
    optimization criteria are implemented: RMS (Root Mean Square
    error) and WCC (Weighted Cross Correlation). Both warping of
    peak profiles and of peak lists are supported."""

    homepage = "https://cran.r-project.org/package=ptw"
    url      = "https://cran.rstudio.com/src/contrib/ptw_1.9-12.tar.gz"
    list_url = "https://cran.rstudio.com/src/contrib/Archive/ptw"

    version('1.9-12', 'ddff887752d789ea72db3ee235ae7c67')

    depends_on('r-nloptr', type=('build', 'run'))
