# CMake by Example

CMake is the meta build tool that uses a single script(CMakeLists.txt) and generates a Makefile. The Makefiles provide a build system that can be used to manage the compilation and re-compilation of programs that are written in any programming language. When we working on big projects that have multiple sub-directories or that project has to be deployed on multiple platforms, Makefile will be very handy.

But, There are times when Makefiles become overly complex for the task. So, CMake simply generates the Makefiles for your projects.

To build a project with CMake, We have to install CMake utils,

```bash
sudo apt-get install cmake
```

Then, Check the version of CMake,

```bash
cmake --version
```

## A Project with Single file

```bash
# Create a myApp1 directory
mkdir myApp1
cd myApp1
```

The myApp1 project is containe simple hello_world.c file and CMakeLists.txt file.

```c
/* hello_world.c */
#include <studio.h>

int main()
{
    printf("Hello World\n");
    return 0;
}
```

Then, We by creating a CMakeLists.txt file in the root of our project.

```bash
# Inserts the current version of CMake
cmake_minimum_required(VERSION 2.8)
# project() directive which defines the name of the project
project(myApp1)
# Adding build targets (A build target defines an executable or a library that the CMake script helps you build)
add_executable(hello_world hello_world.c)
# To install our binary into the bin directory of the install
install(TARGETS myApp1 DESTINATION _install)
```

Its, Time to build our first app,

```bash
mkdir _build
cd _build
#Call Cmake
cmake ..
```