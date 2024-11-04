# Install script for directory: /home/peiyao/peiyao/no_rcm_keyboard_controller/src/no_rcm_keyboard_controller/no_rcm_key_publisher_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/peiyao/peiyao/no_rcm_keyboard_controller/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/no_rcm_key_publisher_msgs/msg" TYPE FILE FILES "/home/peiyao/peiyao/no_rcm_keyboard_controller/src/no_rcm_keyboard_controller/no_rcm_key_publisher_msgs/msg/no_rcm_key_publisher_msgs.msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/no_rcm_key_publisher_msgs/cmake" TYPE FILE FILES "/home/peiyao/peiyao/no_rcm_keyboard_controller/build/no_rcm_keyboard_controller/no_rcm_key_publisher_msgs/catkin_generated/installspace/no_rcm_key_publisher_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/peiyao/peiyao/no_rcm_keyboard_controller/devel/include/no_rcm_key_publisher_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/peiyao/peiyao/no_rcm_keyboard_controller/devel/share/roseus/ros/no_rcm_key_publisher_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/peiyao/peiyao/no_rcm_keyboard_controller/devel/share/common-lisp/ros/no_rcm_key_publisher_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/peiyao/peiyao/no_rcm_keyboard_controller/devel/share/gennodejs/ros/no_rcm_key_publisher_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/peiyao/peiyao/no_rcm_keyboard_controller/devel/lib/python2.7/dist-packages/no_rcm_key_publisher_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/peiyao/peiyao/no_rcm_keyboard_controller/devel/lib/python2.7/dist-packages/no_rcm_key_publisher_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/peiyao/peiyao/no_rcm_keyboard_controller/build/no_rcm_keyboard_controller/no_rcm_key_publisher_msgs/catkin_generated/installspace/no_rcm_key_publisher_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/no_rcm_key_publisher_msgs/cmake" TYPE FILE FILES "/home/peiyao/peiyao/no_rcm_keyboard_controller/build/no_rcm_keyboard_controller/no_rcm_key_publisher_msgs/catkin_generated/installspace/no_rcm_key_publisher_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/no_rcm_key_publisher_msgs/cmake" TYPE FILE FILES
    "/home/peiyao/peiyao/no_rcm_keyboard_controller/build/no_rcm_keyboard_controller/no_rcm_key_publisher_msgs/catkin_generated/installspace/no_rcm_key_publisher_msgsConfig.cmake"
    "/home/peiyao/peiyao/no_rcm_keyboard_controller/build/no_rcm_keyboard_controller/no_rcm_key_publisher_msgs/catkin_generated/installspace/no_rcm_key_publisher_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/no_rcm_key_publisher_msgs" TYPE FILE FILES "/home/peiyao/peiyao/no_rcm_keyboard_controller/src/no_rcm_keyboard_controller/no_rcm_key_publisher_msgs/package.xml")
endif()

