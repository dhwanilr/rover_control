#! usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class MotorNode(Node):
    def __init__(self):
        super().__init__('motor_node')
        self.subscription = self.create_subscription(
            String,
            '/cmd_vel',
            self.cmd_callback,
            10
        )

    def cmd_callback(self, msg):
        command = json.loads(msg.data)
        self.get_logger().info(f"Received command: {command['state']} with linear_x: {command['linear_x']} and angular_z: {command['angular_z']}")

def main(args=None):
    rclpy.init(args=args)
    node = MotorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()