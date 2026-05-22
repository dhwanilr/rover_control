from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'rover_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        ('share/' + package_name, ['package.xml']),

        ('share/' + package_name + '/launch',
            ['launch/rover.launch.py']),
    ],

    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='dhwanilr',
    maintainer_email='dhwanilr@todo.todo',
    description='ROS2 rover application',
    license='MIT',

    extras_require={
        'test': [
            'pytest',
        ],
    },

    entry_points={
        'console_scripts': [
            'sensor_node = rover_control.sensor_node:main',
            'perception_node = rover_control.perception_node:main',
            'decision_node = rover_control.decision_node:main',
            'motor_node = rover_control.motor_node:main',
        ],
    },
)