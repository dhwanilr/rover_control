#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class DecisionNode(Node):
    def __init__(self):
        super().__init__('decision_node')
        self.subscription = self.create_subscription(
            String, 
            '/obstacle_info', 
            self.obstacle_callback, 
            10
        )
        self.publisher = self.create_publisher(String, '/cmd_vel', 10)
        self.get_logger().info('Decision node has been started.')

    def obstacle_callback(self, msg):
        obstacle_info = json.loads(msg.data)
        command = {
            'linear_x':0.0,
            'angular_z':0.0,
            'state': 'STOPPED'
        }

        if obstacle_info['front_blocked']:
            if not obstacle_info['left_blocked']:
                command['angular_z'] = 0.5
                command['state'] = 'TURNING_LEFT'
            elif not obstacle_info['right_blocked']:
                command['angular_z'] = -0.5
                command['state'] = 'TURNING_RIGHT'
            else:
                command['state'] = 'STOPPED'
        else:
            command['linear_x'] = 1.0
            command['state'] = 'MOVING_FORWARD'
        
        cmd_msg = String()
        cmd_msg.data = json.dumps(command)
        self.get_logger().info(f'Decision made: {cmd_msg.data}')
        self.publisher.publish(cmd_msg)

def main(args=None):
    rclpy.init(args=args)
    node = DecisionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()