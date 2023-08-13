// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_robot_interfaces:srv/ComputeMyRectangleArea.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__COMPUTE_MY_RECTANGLE_AREA__STRUCT_H_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__COMPUTE_MY_RECTANGLE_AREA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/ComputeMyRectangleArea in the package my_robot_interfaces.
typedef struct my_robot_interfaces__srv__ComputeMyRectangleArea_Request
{
  double length;
  double with;
} my_robot_interfaces__srv__ComputeMyRectangleArea_Request;

// Struct for a sequence of my_robot_interfaces__srv__ComputeMyRectangleArea_Request.
typedef struct my_robot_interfaces__srv__ComputeMyRectangleArea_Request__Sequence
{
  my_robot_interfaces__srv__ComputeMyRectangleArea_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__srv__ComputeMyRectangleArea_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/ComputeMyRectangleArea in the package my_robot_interfaces.
typedef struct my_robot_interfaces__srv__ComputeMyRectangleArea_Response
{
  double area;
} my_robot_interfaces__srv__ComputeMyRectangleArea_Response;

// Struct for a sequence of my_robot_interfaces__srv__ComputeMyRectangleArea_Response.
typedef struct my_robot_interfaces__srv__ComputeMyRectangleArea_Response__Sequence
{
  my_robot_interfaces__srv__ComputeMyRectangleArea_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__srv__ComputeMyRectangleArea_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__COMPUTE_MY_RECTANGLE_AREA__STRUCT_H_
