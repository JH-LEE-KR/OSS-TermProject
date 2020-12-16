<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!--
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]-->



<!-- PROJECT LOGO -->
<br />
<p align="center">
<a href="http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject/">
  <img src="/readme_img/camera.png"  width="80" height="80">
  </a>
  </p>
  <h3 align="center">Mask-Wearing Discriminator!</h3>

  <p align="center">
    웹캠을 이용한 실시간 마스크 착용 판별 및 출입부 작성 기능을 제공합니다.
  </p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#connect-to-server">Connect to Server</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#initial-setting">Initial setting</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#precautions">Precautions</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#reference">Reference</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

전례 없는 COVID-19가 창궐함에 따라 전염을 막기 위한 마스크 착용은 필수 불가결의 의무가 되었고, 출입자 통제 및 기록, 마스크 착용 여부 판별에 대한 업무가 증가하고 있다.<br>
그래서, 우리는 인공지능을 활용해 이러한 업무를 뒷받침할 수 있는 간단한 시스템을 제작해보게 되었다.<br><br>

쉽고 빠르게 머신러닝을 가능케 하는 오픈소스인 구글의 Teachable Machine 2.0을 이용한 마스크 착용 판별 프로그램입니다.<br>
Teachable Machine 2.0을 이용해 마스크 착용을 유형별로 학습시킨 모델을 만들었습니다.<br>
이 프로그램은 웹캠을 통해 입력되는 사람의 얼굴을 실시간으로 인식해 마스크 착용 여부를 판별합니다.<br>
마스크 착용 판별 이외에 출입자 인적사항 기록 기능과 기록을 파일화해 저장하는 기능도 제공합니다.<br>


### Built With
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Nodejs](https://nodejs.org)
 - [express](https://github.com/expressjs/express)
 - [ejs](https://github.com/mde/ejs)
* [python](https://www.python.org)
  * [selenium](https://selenium-python.readthedocs.io)
* [Teachable Machine](https://teachablemachine.withgoogle.com)
* [Kakao TTS API](https://developers.kakao.com/docs/latest/ko/voice/common)

### Directory Structure
<img src="/readme_img/structure.png"><br><br>


<!-- GETTING STARTED -->
## Getting Started

### Connect to Server
 *  https://www.khumwd.ml:8080 에 오시면 바로 실행이 가능합니다

### Installation

#### (배포 이전)Local 에서 실행하는 방법입니다.

1. Repository Clone 하기
   ```sh
   git clone http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject.git
   ```
2. 모델 만들기
    1. 파이썬 모듈 설치하기(파이썬이 설치된 폴더에서)
    ```sh
    pip install -r requirements.txt
    ```
    2. 크롬 드라이버 설치<br>
     https://chromedriver.chromium.org/downloads 에 접속하여 자신의 크롬 브라우져와 맞는 버전 다운받기
    3. `google.py`에 크롬드라이버 경로 설정하기
    ```python
    chromedriver_path = "경로"
    ```
    4. `google.py`실행하기
    ```sh
    python google.py
    ```
    5.모델 만들기<br>
    https://teachablemachine.withgoogle.com 에 접속하여 /python/model 에 저장된 크롤링된 이미지들을 넣어 모델을 만든다
    <br><br>
3. 로컬서버 실행하기
  1. NPM 패키지 설치하기
   ```sh
   npm install
   ```
   2. `index.ejs`에 API 넣기
   ```JS
    const URL = 'Teachable Machine 모델의 Url을 입력';
   ```
   3. NPM을 이용해 서버 시작하기
   ```sh
   npm start
   ```

### Initial setting
1. Main page 접속<br>
  1.1 로컬서버를 직접 열어 https://localhost:3000 으로 Main page에 접속하거나, https://www.khumwd.ml:8080 를 통해 Main page에 접속합니다.<br><br>
2. 카메라 허용<br>
  2.1 카메라 권한 요청 메시지가 표시되면 허용을 선택합니다.<br><br>

<!-- USAGE EXAMPLES -->
## Usage
<!-- 사진 순서별로 정렬할 수 있도록. -->
사용하는 장소를 입력해 준다.<br>
<img src="/readme_img/1.png"><br><br>

1. 마스크 착용 판별 기능<br>
  1.1. 카메라 정면을 바라보고 서있는다. <br>
  1.2. 마스크 착용 여부에 따라 영상 출력부 우측의 이미지가 변하고 소리가 출력된다.<br>
  * 정상 착용 예시<br>
  <img src="/readme_img/정상.jpg"><br><br>
  * 불량 착용 예시<br>
  <img src="/readme_img/불량.jpg"><br><br>

2. 출입내역 기록 기능<br>
  2.1. 처음 페이지에 접속하여 출입내역을 작성할 곳의 위치를 입력한다.<br>
  2.2. 건물에 출입하는 인원들은 캠 앞에서서 이름, 전화번호, 신분을 선택하고 제출을 누른다.<br/>
  2.3. 이때 마스크를 착용하지 않았다면 작성한 내용을 제출이 불가능하다.<br><br>
  * 인적 사항 입력란<br>
  <img src="/readme_img/인적사항.jpg"><br><br>

3. 출입내역 저장 기능<br>
  3.1 지금까지 기록한 내용들을 '저장' 버튼을 눌러 파일을 생성한다.<br>
  3.2 생성한 파일을 '다운로드'를 통해 로컬에 저장한다.<br><br>
  * 다운로드 예시<br>
  <img src="/readme_img/다운로드.jpg"><br><br>



<!-- ROADMAP -->
## Roadmap

제안된 기능 및 발견된 오류 목록은 [Issues](http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject/issues) 를 참조하십시오.



<!-- PRECAUTION -->
## Precaution
아래 주의사항에 유의해 사용해 주세요. <br>
**1. 마스크 착용 여부 판별에 웹캠의 실시간 영상 데이터를 사용. 브라우저의 웹캠 접근 권한 허용 필수. 웹캠 없이도 출입자 인적사항 기록은 가능하나 마스크 착용 여부 판별은 불가.**<br>
**2. 인터넷 브라우저별로 json 및 txt 파일 생성 방법이 달라 Internet Explorer에서는 출입자 인적사항 기록은 가능하나 저장은 불가**<br>
**3. Internet Explorer에서 대화 상자(Prompt)의 출력 방식이 Chrome 과는 달라 대화 상자 출력 불가. 따라서 초기에 위치 입력이 불가**<br>
**4. 출입자 인적사항을 기록한 파일을 다운로드 시 반드시 로컬의 Download 폴더에 저장됨. 저장 경로 변경 불가.**<br>
**5. 웹캠 앞에서의 재빠른 움직임은 마스크 착용 여부를 정확히 판별하지 못할 수 있음.**<br>
**6. 크롬 브라우저의 특성상 첫 음성 출력에 소요되는 시간이 지연될 수 있음.**<br>

<!-- CONTRIBUTING -->
## Contributing

해당 프로젝트에 기여하고 싶다면 아래의 절차를 따라주세요. <br>
**어떠한 기여도 환영입니다!!**.<br>
1. 프로젝트를 fork 해주세요.
2. branch를 만들어주세요. (`git checkout -b feature/AmazingFeature`)
3. 변경사항을 commit 해주세요. (`git commit -m 'Add some AmazingFeature'`)
4. branch에 push 해주세요. (`git push origin feature/AmazingFeature`)
5. merge request 해주세요.

<!-- Reference -->
## Reference
<a href="https://teachablemachine.withgoogle.com">Teachable Machine 2.0</a>
    ·
<a href="https://www.w3schools.com/">W3schools</a>
    ·
<a href="https://devdocs.io/express/">Express</a>
    ·
<a href="https://devdocs.io/node/">Node.js</a>
    ·
<a href="https://selenium-python.readthedocs.io">selenium</a>
    .
<a href="https://developers.kakao.com/docs/latest/ko/voice/common">Kakao TTS API</a>
    .
<a href="https://jquery.com/">Jquery</a>
    .
<a href="http://bootstrapk.com/">Bootstrap</a>
    .
<a href="https://www.youtube.com/watch?v=1b7pXC1-IbE">조코딩</a>



<!-- LICENSE -->
## License

<!-- 라이센스 나중에 올리고 링크 수정 필요-->
MIT 라이센스를 적용합니다. 자세한 정보는 [License][license-url]를 확인해주세요.<br>



<!-- CONTACT -->
## Contact
[Taeyoung Kim] rlaxodud9809@khu.ac.kr<br>
[Jaeho Lee] dlwogh9344@khu.ac.kr<br>


Project Link: [http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject](http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject)



[license-url]: http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject/blob/master/LICENSE.txt
