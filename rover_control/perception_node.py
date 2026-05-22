#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class PerceptionNode(Node):
    def __init__(self):
        super().__init__('perception_node')
        self.subscription = self.create_subscription(
            String,
            '/scan',
            self.scan_callback,
            10
        )
        self.publisher = self.create_publisher(String, '/obstacle_info', 10)
        self.get_logger().info('Perception node has been started.')

    def scan_callback(self, msg):
        scan_data = json.loads(msg.data)
        obstacle_info = {
            'left_blocked': scan_data['left'] < 0.9,
            'front_blocked': scan_data['front'] < 0.9,
            'right_blocked': scan_data['right'] < 0.9
        }

        obstacle_msg = String()
        obstacle_msg.data = json.dumps(obstacle_info)
        self.get_logger().info(f'Processed obstacle info: {obstacle_msg.data}')
        self.publisher.publish(obstacle_msg)

def main(args=None):
    rclpy.init(args=args)
    node = PerceptionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()