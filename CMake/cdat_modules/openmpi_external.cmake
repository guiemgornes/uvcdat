
set(OPENMPI_source "${CMAKE_CURRENT_BINARY_DIR}/build/OPENMPI")
set(OPENMPI_install "${cdat_EXTERNALS}")

ExternalProject_Add(OPENMPI
  DOWNLOAD_DIR ${CMAKE_CURRENT_BINARY_DIR}
  SOURCE_DIR ${OPENMPI_source}
  INSTALL_DIR ${OPENMPI_install}
  URL ${OPENMPI_URL}/${OPENMPI_GZ}
  URL_MD5 ${OPENMPI_MD5}
  BUILD_IN_SOURCE 1
  PATCH_COMMAND ""
  CONFIGURE_COMMAND <SOURCE_DIR>/configure --prefix=<INSTALL_DIR> --disable-vt
  DEPENDS ${OPENMPI_deps}
  ${ep_log_options}
)
