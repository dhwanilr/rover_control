#! usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cc_app',
            executable='sensor_node',
            name='sensor_node'
        ),
        Node(
            package='cc_app',
            executable='perception_node',
            name='perception_node'
        ),
        Node(
            package='cc_app',
            executable='decision_node',
            name='decision_node'
        ),
        Node(
            package='cc_app',
            executable='motor_node',
            name='motor_node'
        )
    ])
