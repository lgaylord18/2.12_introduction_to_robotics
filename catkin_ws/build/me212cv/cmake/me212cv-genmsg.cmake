# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "me212cv: 0 messages, 1 services")

set(MSG_I_FLAGS "")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(me212cv_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/robot/team2a/catkin_ws/src/me212cv/srv/DetectObject.srv" NAME_WE)
add_custom_target(_me212cv_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "me212cv" "/home/robot/team2a/catkin_ws/src/me212cv/srv/DetectObject.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(me212cv
  "/home/robot/team2a/catkin_ws/src/me212cv/srv/DetectObject.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/me212cv
)

### Generating Module File
_generate_module_cpp(me212cv
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/me212cv
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(me212cv_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(me212cv_generate_messages me212cv_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robot/team2a/catkin_ws/src/me212cv/srv/DetectObject.srv" NAME_WE)
add_dependencies(me212cv_generate_messages_cpp _me212cv_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(me212cv_gencpp)
add_dependencies(me212cv_gencpp me212cv_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS me212cv_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(me212cv
  "/home/robot/team2a/catkin_ws/src/me212cv/srv/DetectObject.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/me212cv
)

### Generating Module File
_generate_module_eus(me212cv
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/me212cv
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(me212cv_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(me212cv_generate_messages me212cv_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robot/team2a/catkin_ws/src/me212cv/srv/DetectObject.srv" NAME_WE)
add_dependencies(me212cv_generate_messages_eus _me212cv_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(me212cv_geneus)
add_dependencies(me212cv_geneus me212cv_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS me212cv_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(me212cv
  "/home/robot/team2a/catkin_ws/src/me212cv/srv/DetectObject.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/me212cv
)

### Generating Module File
_generate_module_lisp(me212cv
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/me212cv
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(me212cv_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(me212cv_generate_messages me212cv_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robot/team2a/catkin_ws/src/me212cv/srv/DetectObject.srv" NAME_WE)
add_dependencies(me212cv_generate_messages_lisp _me212cv_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(me212cv_genlisp)
add_dependencies(me212cv_genlisp me212cv_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS me212cv_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(me212cv
  "/home/robot/team2a/catkin_ws/src/me212cv/srv/DetectObject.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/me212cv
)

### Generating Module File
_generate_module_nodejs(me212cv
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/me212cv
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(me212cv_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(me212cv_generate_messages me212cv_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robot/team2a/catkin_ws/src/me212cv/srv/DetectObject.srv" NAME_WE)
add_dependencies(me212cv_generate_messages_nodejs _me212cv_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(me212cv_gennodejs)
add_dependencies(me212cv_gennodejs me212cv_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS me212cv_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(me212cv
  "/home/robot/team2a/catkin_ws/src/me212cv/srv/DetectObject.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/me212cv
)

### Generating Module File
_generate_module_py(me212cv
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/me212cv
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(me212cv_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(me212cv_generate_messages me212cv_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robot/team2a/catkin_ws/src/me212cv/srv/DetectObject.srv" NAME_WE)
add_dependencies(me212cv_generate_messages_py _me212cv_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(me212cv_genpy)
add_dependencies(me212cv_genpy me212cv_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS me212cv_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/me212cv)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/me212cv
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/me212cv)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/me212cv
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/me212cv)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/me212cv
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/me212cv)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/me212cv
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/me212cv)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/me212cv\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/me212cv
    DESTINATION ${genpy_INSTALL_DIR}
    # skip all init files
    PATTERN "__init__.py" EXCLUDE
    PATTERN "__init__.pyc" EXCLUDE
  )
  # install init files which are not in the root folder of the generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/me212cv
    DESTINATION ${genpy_INSTALL_DIR}
    FILES_MATCHING
    REGEX "${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/me212cv/.+/__init__.pyc?$"
  )
endif()
