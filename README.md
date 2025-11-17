# 🏀 SLAM-DUNK
SLAM DUNK 팀 프로젝트 작업 관리 레포지토리

- [작업 로그](/logs/)
- [문서 모음](/docs/)
- [SLAM-DUNK Drive](https://drive.google.com/drive/folders/1HWarJ3esT4nADFtnINjBP2QkNW5H7jF1)
- [scout mini 패키지 github](https://github.com/ngyh-1002/scout_robot)
- [web 소스 github](https://github.com/mina607/slamdunk-webservice)

## 주요 구성요소

| 구분               | 구성요소                                   | 역할                               |
| ---------------- | -------------------------------------- | -------------------------------- |
| 👤 사용자           | 웹(고객 UI)                               | 상품 주문, 배달 상태 확인                  |
| 🌐 웹 서버          | Spring / mustache / WebSocket          | 주문 데이터 처리, ROS2 브리지와 통신          |
| 🤖 ROS2 브리지      | rosbridge_websocket / ros2 node        | 웹 서버 ↔ 로봇 간 ROS 메시지 전달           |
| 🚗 로봇            | Scout Mini (Nav2)                      | 자율주행 및 물품 운반                     |
| 💡 IoT 장치(객실 단말) | Raspberry Pi Pico (RFID + LED + Piezo) | 로봇 도착 알림, 고객 인증(RFID), 피드백 신호 처리 |
| 📦 백엔드 DB        | H2 Database                            | 주문 및 배달 상태 저장                    |
| 🏨 관리자           | 관리자 페이지                                | 주문 모니터링, 로봇 상태 관리                |
