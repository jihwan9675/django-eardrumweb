# django - eardrum web

### 프로젝트명

- 딥러닝 기반 중이염 진단 웹 서비스 구축

### 프로젝트 참여원

- 신지환

### 사용 기술

- Django
- Nginx
- Gunicorn
- PostgreSQL
- AWS EC2
- Tensorflow/Keras

### 프로젝트

- 졸업 논문을 위해 만들었던 중이염 진단 웹을 Django로 다시 작성하고, 기존에는 한개의 처리만 할 수 있었지만 비동기적인 처리를 위해 WSGI 미들웨어로 Gunicorn, Reverse Proxy로 Nginx를 사용하였고 딥러닝 모델의 로드 시간을 고려하여 싱글톤 패턴을 고려하여 작성했다. 그리고 AWS EC2를 통해 배포 하였다.

### 프로젝트 시행목적

- 앞서 Flask를 기반으로 작성한 프로젝트를 웹 백엔드 개발자 공부를 하며 배운 django로 프레임워크를 변경하는 작업을 할 것이다. 여러 사용자가 동시에 접근 가능하도록 Nginx, Gunicorn를 사용하여 WS, WAS를 구성하였다.
- 중이염은 3세 이하에서 3명 중 2명 비율로 1회 이상 앓게 되고, 3명 중 1명의 비율로 3회 이상 앓는 매우 흔한 질환이다. 국내에서 급성중이염에 대한 발병률은 정확하지 않으나 외국의 보고에 의하면 생후 1세까지 62%, 생후 3세까지 83%가 최소 1회 이상 걸린다고 하였다. 국내에서는 중이염의 발병률에 대한 전국 규모의 연구에서 15세 미만 대상군에서 급성중이염은 0.08%, 삼출성중이염은 1.22%의 유 병율이 보고된 바 있다 (Kimet al., 1993). 2008년 국민건강보험 심사평가원의 통계 자료에 따르면, 중이염은 10세 미만의 환자들이 의사를 찾는 빈도에서 10위, 그리고 병,의원을 찾는 빈도에서 6위를 차지한다. 유소아 중이염은 다른 상기도감 염과는 달리 전문적인 의학적 지식과 더불어 적절히 치료되지 못하였을 때 발생할 수 있는 합병증 및 후유증 동반될 수 있다고 한다.
- 따라서 가정에서도 간편하게 진단을 할 수 있는 혹은 의사의 진단을 도울 수 있는 진단 웹 서비스를 구축할 것이다.

### 프로젝트 개요

- 다음과 같이 6가지의 카테고리로 분류를 한다.

    ![Untitled](https://user-images.githubusercontent.com/69146451/115763234-3f4d5800-a3df-11eb-878f-485f97ed12be.png)

- 서버구성은 다음과 같다.
    
    <img width="956" alt="_2021-04-22__9 36 07" src="https://user-images.githubusercontent.com/69146451/115763209-3a88a400-a3df-11eb-9d89-a0c1bf8923b1.png">

### 실행화면

1. 진단 화면(/predcit)

    ![ezgif com-gif-maker](https://user-images.githubusercontent.com/69146451/115763256-43797580-a3df-11eb-8d61-68e73dc7bc83.gif)

2. 조회(/board)

    ![django - eardrum c7f9a291c1624aff8947b86ce4d8c7a6](https://user-images.githubusercontent.com/69146451/115763280-47a59300-a3df-11eb-85de-0a8376e408df.gif)

3. 고막을 못찾는 사진일 경우

    ![django - eardrum c7f9a291c1624aff8947b86ce4d8c7a6 1](https://user-images.githubusercontent.com/69146451/115763985-fe097800-a3df-11eb-8279-4fb16a9b1547.gif)

- 모바일과 Desktop 환경에서 모두 접근 가능한 웹으로 서비스를 제공할 예정이다.

### 프로젝트 시행 후 얻을 수 있는 이익

- 의료 AI가 부각되고 4차 산업 시대에 맞춰서 정부에서도 많은 지원을 하고 있는 이 시점에서 이러한 기술들이 발전하고 제시된다면 인프라가 구축되어 병원에서 의사를 도와 빠르고 정확한 진단을 내릴 수 있게 만들고 코로나-19로 비대면이라는 키워드가 핵심이 되어가는 현 시점에 많은 수요를 요할 것으로 판단한다.

### 데이터 출처

- 순천향대학교 천안병원에서 제공받았으며 고막 이미지의 총 데이터 량은 4,808장이다.
- 순천향대학교 천안병원 연구윤리심의위원회(Institutional review board, 이하 IRB)의 심의 를 거쳐 대상자의 의무기록을 후향적으로 조사하였다(IRB No. SCHCA 2020-02-022).

### 논문

[졸업 논문](https://jihwan9675.github.io/Graduationpaper-Korean/)

[SCI](https://www.techscience.com/csse/v46n2/51616)
