#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from my_robot_interfaces.srv import SetLed
from functools import partial

class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery")
        self.battery_state_ = "full"
        self.last_battery_state_cahnged = self.get_current_time_seconds()
        self.battery_timer_ = self.create_timer(0.1, self.battery_state_publisher)
        self.get_logger().info("Battery node has been started.")

    def get_current_time_seconds(self):
        secs, nsecs =self.get_clock().now().seconds_nanoseconds()
        return secs + nsecs * 10 ** -9

    def battery_state_publisher(self):
        time_now = self.get_current_time_seconds()
        if self.battery_state_ == "full" and time_now - self.last_battery_state_cahnged > 4:
            self.battery_state_ = "empty"
            self.last_battery_state_cahnged = time_now
            self.get_logger().info("Battery is empty! Charging battery...")
            self.call_set_led_server(2, 1)
        elif self.battery_state_ == "empty" and time_now - self.last_battery_state_cahnged > 6:
            self.battery_state_ = "full"
            self.last_battery_state_cahnged = time_now
            self.get_logger().info("Battery is full! Using battery...")
            self.call_set_led_server(2, 0)

    def call_set_led_server(self, led_number, state):
        client = self.create_client(SetLed, "set_led")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Set Led...")

        request = SetLed.Request()
        request.led_number = led_number
        request.state = state

        future = client.call_async(request)
        future.add_done_callback(
            partial(self.calback_call_set_led_server, led_number=led_number, state=state)
        )

    def calback_call_set_led_server(self, future, led_number, state):
        try:
            response = future.result()
            self.get_logger().info("Led number: " + str(led_number) + " state: " + str(state))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))
        

def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
