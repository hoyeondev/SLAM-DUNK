import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import String
import cv2
from pyzbar import pyzbar
from nav2_simple_commander.robot_navigator import BasicNavigator
from ament_index_python.packages import get_package_share_directory
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler
import os
import yaml

class RoomNavigator(Node):
    def __init__(self):
        super().__init__('room_navigator')
        self.navigator = BasicNavigator()
        self.bridge = CvBridge()
        self.qr_detected = False


        package_share = get_package_share_directory('scout_robot')
        yaml_path = os.path.join(package_share, 'rooms.yaml')
        
        # 좌표 읽기
        with open(yaml_path, 'r') as f:
            rooms = yaml.safe_load(f)['rooms']
        self.start_pose = [
            rooms['start']['x'],
            rooms['start']['y'],
            rooms['start']['theta']
        ]
        self.room1_pose = [
            rooms['room1']['x'],
            rooms['room1']['y'],
            rooms['room1']['theta']
        ]

        self.start_pose_coords = rooms['start']

        # --- 초기 위치 PoseStamped 생성 ---
        initial_pose = PoseStamped()
        initial_pose.header.frame_id = "map"
        initial_pose.pose.position.x = self.start_pose_coords['x']
        initial_pose.pose.position.y = self.start_pose_coords['y']
        initial_pose.pose.position.z = 0.0

        q = quaternion_from_euler(0, 0, self.start_pose_coords['theta'])
        initial_pose.pose.orientation.x = q[0]
        initial_pose.pose.orientation.y = q[1]
        initial_pose.pose.orientation.z = q[2]
        initial_pose.pose.orientation.w = q[3]

        # --- Nav2에 초기 위치 설정 ---
        self.navigator.setInitialPose(initial_pose)

        # --- Nav2 활성화까지 대기 ---
        self.navigator.waitUntilNav2Active()
        
        # 1) 명령 구독
        self.command_sub = self.create_subscription(
            String,
            '/room_command',
            self.command_callback,
            10
        )

        # 2) QR 코드 인식 구독
        # self.image_sub = self.create_subscription(
        #     Image,
        #     '/camera/image_raw',
        #     self.image_callback,
        #     10
        # )

    def command_callback(self, msg):
        if msg.data == "go_room1":
            self.get_logger().info("room1 이동 명령 수신. 출발합니다.")

            # 리스트 → PoseStamped 변환
            x, y, theta = self.room1_pose
            pose = PoseStamped()
            pose.header.frame_id = "map"
            pose.header.stamp = self.get_clock().now().to_msg()

            pose.pose.position.x = x
            pose.pose.position.y = y
            pose.pose.position.z = 0.0

            # theta → quaternion
            qx, qy, qz, qw = quaternion_from_euler(0, 0, theta)
            pose.pose.orientation.x = qx
            pose.pose.orientation.y = qy
            pose.pose.orientation.z = qz
            pose.pose.orientation.w = qw
            # room1 이동
            self.navigator.goToPose(pose)
            self.navigator.waitUntilNav2Active()
            self.get_logger().info("room1 도착!")

        if msg.data == "go_home":

                      # 리스트 → PoseStamped 변환
            x, y, theta = self.start_pose
            pose = PoseStamped()
            pose.header.frame_id = "map"
            pose.header.stamp = self.get_clock().now().to_msg()

            pose.pose.position.x = x
            pose.pose.position.y = y
            pose.pose.position.z = 0.0

            # theta → quaternion
            qx, qy, qz, qw = quaternion_from_euler(0, 0, theta)
            pose.pose.orientation.x = qx
            pose.pose.orientation.y = qy
            pose.pose.orientation.z = qz
            pose.pose.orientation.w = qw
            # 출발점 복귀
            self.navigator.goToPose(pose)
            self.navigator.waitUntilNav2Active()
            self.get_logger().info("출발점 도착! 완료!")

def main():
    rclpy.init()
    node = RoomNavigator()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
