set(NUMPY_MAJOR 1)
set(NUMPY_MINOR 9)
set(NUMPY_PATCH 0b1)
set(NUMPY_MAJOR_SRC 1)
set(NUMPY_MINOR_SRC 9)
set(NUMPY_PATCH_SRC 0b1)
set(NUMPY_URL ${LLNL_URL})
set(NUMPY_GZ numpy-${NUMPY_MAJOR_SRC}.${NUMPY_MINOR_SRC}.${NUMPY_PATCH_SRC}.tar.gz)
set(NUMPY_MD5 d763325ad0bc1975d09fdee3b31d2bca)
set(NUMPY_SOURCE ${NUMPY_URL}/${NUMPY_GZ})

set (nm NUMPY)
string(TOUPPER ${nm} uc_nm)
set(${uc_nm}_VERSION ${${nm}_MAJOR_SRC}.${${nm}_MINOR_SRC}.${${nm}_PATCH_SRC})
add_cdat_package(NUMPY "" "" OFF)
set(NUMPY ${pkgconfig_pkg} ${python_pkg} ${clapack_pkg} ${lapack_pkg})
