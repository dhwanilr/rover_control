#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
import json

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.publisher = self.create_publisher(String, '/scan', 10)
        self.timer = self.create_timer(1.0, self.publish_sensor_data)
        self.get_logger().info('Sensor node has been started.')

    def publish_sensor_data(self):
        scan_data = {
            'left': round(random.uniform(0.5, 2.0), 2),
            'front': round(random.uniform(0.5, 2.0), 2),
            'right': round(random.uniform(0.5, 2.0), 2)
        }
        msg = String()
        msg.data = json.dumps(scan_data)
        self.publisher.publish(msg)
        self.get_logger().info(f'Published sensor data: {msg.data}')
    
def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
