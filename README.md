# 🏀 SLAM-DUNK
SLAM DUNK 팀 프로젝트 레포지토리

## 목차
1. 📝 [개요](#1-개요)
2. 기술 및 도구
3. 기능 구현
4. 기타
   - [작업 로그](/logs/)
   - [문서 모음](/docs/)
   - [SLAM-DUNK Drive](https://drive.google.com/drive/folders/1HWarJ3esT4nADFtnINjBP2QkNW5H7jF1)
   - [scout mini 패키지 github](https://github.com/ngyh-1002/scout_robot)
   - [web 소스 github](https://github.com/mina607/slamdunk-webservice)
    
---

## 1. 📝개요
- **프로젝트명** : 호텔 서비스 자동화를 위한 RFID 기반의 자율주행 배달로봇 시스템 - Serving GO
- **인원** : 4인
  |팀장|팀원|팀원|팀원|
  |----|----|----|----|
  |박호연|남궁영훈|최미나|소재민|
- **주제** : RFID 기반 보안 인증을 결합한 실내 자율주행 배달 로봇 시스템 개발
- **제작 기간** : 2025.09.22 ~ 2025.11.27
- **주요 기능**
   - RFID 기반 사용자 인증을 통해 안전하고 비대면으로 물품을 인계한다.
   - SLAM을 활용해 실내 환경을 자율적으로 탐색하고 최적 경로로 주행한다.
   - LiDAR 센서를 기반으로 주변 장애물을 감지하고 안전하게 회피한다.
   - QR 코드를 활용해 로봇이 목적지에 정확히 도착했는지 추가적으로 검증한다.
   - 웹/서버 시스템을 통해 주문 관리, 로봇 제어, 실시간 상태 모니터링을 제공한다.
   - 픽업 감지 자동화를 통해 사용자가 물품을 수령하면 로봇이 스스로 복귀한다.
- **데모 영상** : [링크](https://drive.google.com/file/d/1teNeuA4PCNzczVyBMFRd4MRukm5wdZgx/view?usp=sharing)

---


## 주요 구성요소

| 구분               | 구성요소                                   | 역할                               |
| ---------------- | -------------------------------------- | -------------------------------- |
| 👤 사용자           | 웹(고객 UI)                               | 상품 주문, 배달 상태 확인                  |
| 🌐 웹 서버          | Spring / mustache / WebSocket          | 주문 데이터 처리, ROS2 브리지와 통신          |
| 🤖 ROS2 브리지      | rosbridge_websocket / ros2 node        | 웹 서버 ↔ 로봇 간 ROS 메시지 전달           |
| 🚗 로봇            | Scout Mini (Nav2)                      | 자율주행 및 물품 운반                     |
| 💡 IoT 장치 | Raspberry Pi Pico (RFID + LED + Piezo) | 로봇 도착 알림, 고객 인증(RFID), 피드백 신호 처리 |
| 📦 백엔드 DB        | H2 Database                            | 주문 및 배달 상태 저장                    |
| 🏨 관리자           | 관리자 페이지                                | 주문 모니터링, 로봇 상태 관리                |
