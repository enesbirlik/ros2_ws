// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interfaces:srv/ComputeMyRectangleArea.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__COMPUTE_MY_RECTANGLE_AREA__BUILDER_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__COMPUTE_MY_RECTANGLE_AREA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_interfaces/srv/detail/compute_my_rectangle_area__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_ComputeMyRectangleArea_Request_with
{
public:
  explicit Init_ComputeMyRectangleArea_Request_with(::my_robot_interfaces::srv::ComputeMyRectangleArea_Request & msg)
  : msg_(msg)
  {}
  ::my_robot_interfaces::srv::ComputeMyRectangleArea_Request with(::my_robot_interfaces::srv::ComputeMyRectangleArea_Request::_with_type arg)
  {
    msg_.with = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::ComputeMyRectangleArea_Request msg_;
};

class Init_ComputeMyRectangleArea_Request_length
{
public:
  Init_ComputeMyRectangleArea_Request_length()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ComputeMyRectangleArea_Request_with length(::my_robot_interfaces::srv::ComputeMyRectangleArea_Request::_length_type arg)
  {
    msg_.length = std::move(arg);
    return Init_ComputeMyRectangleArea_Request_with(msg_);
  }

private:
  ::my_robot_interfaces::srv::ComputeMyRectangleArea_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::ComputeMyRectangleArea_Request>()
{
  return my_robot_interfaces::srv::builder::Init_ComputeMyRectangleArea_Request_length();
}

}  // namespace my_robot_interfaces


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_ComputeMyRectangleArea_Response_area
{
public:
  Init_ComputeMyRectangleArea_Response_area()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_robot_interfaces::srv::ComputeMyRectangleArea_Response area(::my_robot_interfaces::srv::ComputeMyRectangleArea_Response::_area_type arg)
  {
    msg_.area = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::ComputeMyRectangleArea_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::ComputeMyRectangleArea_Response>()
{
  return my_robot_interfaces::srv::builder::Init_ComputeMyRectangleArea_Response_area();
}

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__COMPUTE_MY_RECTANGLE_AREA__BUILDER_HPP_
