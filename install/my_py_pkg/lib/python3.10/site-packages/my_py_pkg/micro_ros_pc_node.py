#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32

#now i want to subscribe to the topic micro_ros_int32_teensy and recive the data
class MicroRosPcNode(Node):
    def __init__(self):
        super().__init__("micro_ros_pc_node")
        self.publisher_ = self.create_publisher(Int32, "micro_ros_int32_pc", 10)
        self.timer_ = self.create_timer(1.0, self.publish_number)
        self.counter_ = 1
        
        self.subscription_ = self.create_subscription(
            Int32,
            "micro_ros_int32_teensy",
            self.listener_callback,
            10
        )


    def publish_number(self):
        msg = Int32()
        msg.data = self.counter_
        self.publisher_.publish(msg)
        self.get_logger().info(str(msg.data)+" is published")
        self.counter_ += 1
    
    def listener_callback(self, msg):
        self.get_logger().info("I heard: "+str(msg.data))

def main(args=None):
    rclpy.init(args=args)
    node = MicroRosPcNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()