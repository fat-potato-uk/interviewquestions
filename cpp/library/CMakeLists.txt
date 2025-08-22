cmake_minimum_required(VERSION 3.28)


add_library(library SHARED executor_service.cpp update.cpp update_callback.cpp)
target_include_directories(library PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/.." "/foo/bar" "..")

