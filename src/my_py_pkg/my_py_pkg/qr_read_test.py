#usr/bin/env python3
import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np

class QrCodeReader(Node):

    def __init__(self):
        super().__init__("qr_code_reader")

        # Yayıncı nesnesi oluşturun
        self.publisher = self.create_publisher(Image, "/image", 10)
        self.bridge = CvBridge()
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # Görüntüyü yükle ve işle
        try:
            cv_image = cv2.imread("your_image.jpg")
            if cv_image is not None:
                # Görüntüyü ROS mesajına dönüştür
                image_msg = self.bridge.cv2_to_imgmsg(cv_image, encoding="bgr8")
                # Görüntüyü yayınla
                self.publisher.publish(image_msg)
            else:
                self.get_logger().warn("Görüntü yüklenemedi.")
        except Exception as e:
            self.get_logger().error(f"Hata: {e}")

def main(args=None):
    rclpy.init(args=args)
    qr_code_reader = QrCodeReader()
    rclpy.spin(qr_code_reader)
    qr_code_reader.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
