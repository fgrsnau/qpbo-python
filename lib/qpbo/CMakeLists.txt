cmake_minimum_required(VERSION 3.13)
cmake_policy(VERSION 3.13)
project(libqpbo)

include(GNUInstallDirs)

set(QPBO_VERSION_MAJOR 1)
set(QPBO_VERSION_MINOR 4)
set(QPBO_VERSION_PATCH 0)
set(QPBO_VERSION_STRING "${QPBO_VERSION_MAJOR}.${QPBO_VERSION_MINOR}.${QPBO_VERSION_PATCH}")

set(SRC_FILES qpbo.cpp qpbo_extra.cpp qpbo_maxflow.cpp qpbo_postprocessing.cpp)

add_library(qpbo_shared SHARED ${SRC_FILES})
add_library(qpbo_static STATIC ${SRC_FILES})
set_target_properties(
	qpbo_shared qpbo_static
	PROPERTIES
		OUTPUT_NAME qpbo
		VERSION "${QPBO_VERSION_STRING}")

install(TARGETS qpbo_shared qpbo_static DESTINATION "${CMAKE_INSTALL_LIBDIR}")
install(FILES block.h                   DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/qpbo")
install(FILES qpbo.h                    DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/qpbo")

set(prefix     "${CMAKE_INSTALL_PREFIX}")
set(libdir     "${CMAKE_INSTALL_LIBDIR}")
set(includedir "${CMAKE_INSTALL_INCLUDEDIR}")
set(version    "${QPBO_VERSION_STRING}")

configure_file(libqpbo.pc.in libqpbo.pc @ONLY)
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/libqpbo.pc" DESTINATION "${CMAKE_INSTALL_LIBDIR}/pkgconfig")
