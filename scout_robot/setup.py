from setuptools import find_packages, setup

package_name = 'scout_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['rooms.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hoyeon',
    maintainer_email='hoyeon@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'assign_order_node = scout_robot.assign_order_node:main',
            'nav2_commander = scout_robot.nav2_commander:main',
            'aruco_detector = scout_robot.aruco:main'
        ],
    },
)
