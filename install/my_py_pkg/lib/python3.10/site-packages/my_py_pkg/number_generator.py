#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberGenerator(Node): 
    def publish_number(self):
        msg = Int64()
        msg.data = self.number
        self.publisher_.publish(msg)
        self.number += 1

    def __init__(self):
        super().__init__("number_publsiher")
        self.publisher_ = self.create_publisher(Int64, "number", 10)
        self.timer_ = self.create_timer(1.0, self.publish_number)
        self.number = 0
        self.get_logger().info("Number Publisher has been started")


def main(args=None):
    rclpy.init(args=args)
    node = NumberGenerator()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()