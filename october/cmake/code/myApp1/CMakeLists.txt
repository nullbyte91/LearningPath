# Inserts the current version of CMake
cmake_minimum_required(VERSION 2.8)
# project() directive which defines the name of the project
project(myApp1)
# Adding build targets (A build target defines an executable or a library that the CMake script helps you build)
add_executable(hello_world hello_world.c)
# To install our binary into the bin directory of the install
install(TARGETS hello_world DESTINATION /bin)
#
