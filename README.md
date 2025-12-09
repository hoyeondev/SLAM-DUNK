# 🏀 SLAM-DUNK
SLAM DUNK 팀 프로젝트 레포지토리

## 목차
1. 📝 [개요](#1-개요)
2. 🛠 [기술 및 도구](#2-기술-및-도구)
3. ✨ [기능 구현](#3-기능-구현)
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
- **기능 요약**
   - RFID 기반 사용자 인증을 통해 안전하고 비대면으로 물품을 인계한다.
   - SLAM을 활용해 실내 환경을 자율적으로 탐색하고 최적 경로로 주행한다.
   - LiDAR 센서를 기반으로 주변 장애물을 감지하고 안전하게 회피한다.
   - 블루투스 스피커 연동을 통해 로봇의 주행·배달 상태를 실시간 음성으로 안내한다.
   - QR 코드를 활용해 로봇이 목적지에 정확히 도착했는지 추가적으로 검증한다.
   - 웹/서버 시스템을 통해 주문 관리, 로봇 제어, 실시간 상태 모니터링을 제공한다.
   - 픽업 감지 자동화를 통해 사용자가 물품을 수령하면 로봇이 스스로 복귀한다.
- **데모 영상** : [링크](https://drive.google.com/file/d/1teNeuA4PCNzczVyBMFRd4MRukm5wdZgx/view?usp=sharing)
- **발표 자료** : [링크](https://drive.google.com/file/d/17jwdtCK9oZEpcpXtljCrXIq7x8jNPi8A/view?usp=sharing)

---

## 2. 🛠기술 및 도구

### Scout mini
> **언어** : <img alt="python" src ="https://img.shields.io/badge/python-3776AB.svg?&style=flat-square&logo=python&logoColor=white"/> <img alt="cplusplus" src ="https://img.shields.io/badge/cplusplus-00599C.svg?&style=flat-square&logo=cplusplus&logoColor=white"/>  
> **환경** : <img alt="ros2 humble" src ="https://img.shields.io/badge/ROS2%20Humble-22314E.svg?&style=flat-square&logo=ros&logoColor=white"/> <img alt="ubuntu" src ="https://img.shields.io/badge/Ubuntu-E95420.svg?&style=flat-square&logo=ubuntu&logoColor=white"/> <img alt="vscode" src ="https://img.shields.io/badge/VSCode-007ACC.svg?&style=flat-square&logo=visualstudiocode&logoColor=white"/> <img alt="thonny" src ="https://img.shields.io/badge/Thonny-5A9EEA.svg?&style=flat-square&logo=python&logoColor=white"/>  
> **라이브러리** :  <img alt="nav2" src ="https://img.shields.io/badge/Navigation2-22314E.svg?&style=flat-square&logo=ros&logoColor=white"/> <img alt="opencv" src ="https://img.shields.io/badge/OpenCV-5C3EE8.svg?&style=flat-square&logo=opencv&logoColor=white"/> <img alt="rosbridge" src ="https://img.shields.io/badge/rosbridge-22314E.svg?&style=flat-square&logo=ros&logoColor=white"/>  
> **협업** :  <img alt="github" src ="https://img.shields.io/badge/GitHub-181717.svg?&style=flat-square&logo=github&logoColor=white"/> <img alt="slack" src ="https://img.shields.io/badge/Slack-4A154B.svg?&style=flat-square&logo=slack&logoColor=white"/>  
 

### Web

> **프론트엔드** :  <img alt="mustache" src ="https://img.shields.io/badge/Mustache-000000.svg?&style=flat-square&logo=mustache&logoColor=white"/> <img alt="bootstrap5" src ="https://img.shields.io/badge/Bootstrap%205-7952B3.svg?&style=flat-square&logo=bootstrap&logoColor=white"/> <img alt="javascript" src ="https://img.shields.io/badge/JavaScript-F7DF1E.svg?&style=flat-square&logo=javascript&logoColor=black"/>  
> **백엔드** :  <img alt="java" src ="https://img.shields.io/badge/Java-007396.svg?&style=flat-square&logo=java&logoColor=white"/> <img alt="h2" src ="https://img.shields.io/badge/H2%20Database-1A4C8B.svg?&style=flat-square&logo=h2&logoColor=white"/>  
> **환경** :  <img alt="intellij" src ="https://img.shields.io/badge/IntelliJ%20IDEA-000000.svg?&style=flat-square&logo=intellijidea&logoColor=white"/> <img alt="spring boot" src ="https://img.shields.io/badge/Spring%20Boot-6DB33F.svg?&style=flat-square&logo=springboot&logoColor=white"/> <img alt="gradle" src ="https://img.shields.io/badge/Gradle-02303A.svg?&style=flat-square&logo=gradle&logoColor=white"/>  
> **라이브러리** :  <img alt="websocket" src ="https://img.shields.io/badge/WebSocket-333333.svg?&style=flat-square&logo=websocket&logoColor=white"/> <img alt="rosbridge" src ="https://img.shields.io/badge/rosbridge-22314E.svg?&style=flat-square&logo=ros&logoColor=white"/> <img alt="restapi" src ="https://img.shields.io/badge/REST%20API-005571.svg?&style=flat-square&logo=apachespark&logoColor=white"/>  
> **협업** :  <img alt="github" src ="https://img.shields.io/badge/GitHub-181717.svg?&style=flat-square&logo=github&logoColor=white"/> <img alt="slack" src ="https://img.shields.io/badge/Slack-4A154B.svg?&style=flat-square&logo=slack&logoColor=white"/>  



---

## 3. ✨기능 구현

### 🔖주요 기능

**1. 웹 주문 시스템**
- 고객용 웹 UI에서 룸서비스 및 물품 주문
- 주문 내역 확인 및 실시간 상태 조회
- 관리자용 대시보드에서 주문 승인/관리

**2. 로봇 호출 및 연동**
- 관리자가 버튼 한 번으로 로봇 호출
- rosbridge(WebSocket) 기반 로봇 ↔ 서버 실시간 통신
- 로봇 상태(배터리, 위치 등)를 실시간 수신
  
**3. 자율주행 및 내비게이션**
- SLAM 기반 실내 지도 구축 및 경로 계획
- LiDAR 기반 장애물 감지 및 회피
- 목적지 도착 시 QR 코드로 최종 위치 검증

**4. 보안 인증 및 물품 인계**
- RFID 태그 기반 고객 인증
- 인증 후 로봇 도어 자동 개방
- 초음파 센서를 통한 물품 픽업 감지 → 자동 복귀

**5. 블루투스 기반 음성 안내 시스템 연동**
- 로봇 주행·배달 상태를 실시간으로 음성 출력
- 목적지 도착, 배달 완료 등 상황별 안내 메시지 제공
   
**6. 서버/시스템 구조**
- Spring Boot 기반 REST API 서버
- 데이터베이스를 통한 주문/고객/로봇 상태 저장
- 관리·운영용 웹 UI 제공


### 📕기능 흐름도
```css
[고객 주문] → [관리자 승인] → [로봇 호출] → 
[로봇 자율주행] → [QR 목적지 검증] → 
[RFID 인증] → [물품 수령] → [초음파센서 픽업 감지] → [로봇 복귀]
```

### 🧩구성요소

| 구분               | 구성요소                                   | 역할                               |
| ---------------- | -------------------------------------- | -------------------------------- |
| 👤 사용자           | 웹(고객 UI)                               | 상품 주문, 배달 상태 확인                  |
| 🌐 웹 서버          | Spring / mustache / WebSocket          | 주문 데이터 처리, ROS2 브리지와 통신          |
| 🤖 ROS2 브리지      | rosbridge_websocket / ros2 node        | 웹 서버 ↔ 로봇 간 ROS 메시지 전달           |
| 🚗 로봇            | Scout Mini (Nav2)                      | 자율주행 및 물품 운반                     |
| 💡 IoT 장치 | Raspberry Pi Pico (RFID + LED + Piezo) | 로봇 도착 알림, 고객 인증(RFID), 피드백 신호 처리 |
| 📦 백엔드 DB        | H2 Database                            | 주문 및 배달 상태 저장                    |
| 🏨 관리자           | 관리자 페이지                                | 주문 모니터링, 로봇 상태 관리                |


### 📜향후 개선 사항
- 라벨링 없는 객체 감지를 위한 카메라 기반 인식 추가
- 다중 로봇 운용 및 로봇 간 충돌 방지 알고리즘
