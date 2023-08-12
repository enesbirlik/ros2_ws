#!/usr/bin/env python3
#The number_counter node subscribes to the “/number” topic. It keeps a counter variable. Every time a new number is received, it’s added to the counter. The node also has a publisher on the “/number_count” topic. When the counter is updated, the publisher directly publishes the new value on the topic.

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberCounter(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.subscriber_ = self.create_subscription(Int64, "number", self.callback_number, 10)
        self.get_logger().info("Number Counter has been started")
        self.counter_ = 0
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)

    def callback_number(self, msg):
        self.counter_ = msg.data
        self.get_logger().info(str(self.counter_))
        self.publish_number_count()

    def publish_number_count(self):
        msg = Int64()
        msg.data = self.counter_
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = NumberCounter()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()