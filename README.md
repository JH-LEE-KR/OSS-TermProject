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
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="readme_img/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Mask-Wearing Discriminator!</h3>

  <p align="center">
    구글 Teachable Machine 2.0을 이용하여 마스크 착용 검사 및 출입부 작성 기능을 제공합니다.
    <br />
    <!--여기 뭐 넣을지 생각해보자-->
    <a href="http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://teachablemachine.withgoogle.com">Teachable Machine 2.0</a>
    ·
    <a href="https://www.w3schools.com/">W3schools</a>
    ·
    <a href="http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#precautions">Precautions</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#reference">Reference</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
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
* [Teachable Machine](https://teachablemachine.withgoogle.com)




<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```
3. Enter your API in `index.ejs`
   ```JS
    const URL = 'ENTER YOUR Teachable Machine Model Url';
   ```
4. Start Server in npm located.
   ```sh
   npm start
   ```
### Initial setting
1. Main page 접속<br>
  1.1 https://localhost:3000을 통해 Main page에 접속합니다.<br><br>
2. 카메라 허용<br>
  2.1 카메라 허용 메시지가 표시되면 허용을 선택합니다.<br><br>

<!-- USAGE EXAMPLES -->
## Usage
<!-- 사진 순서별로 정렬할 수 있도록. -->
[![Product Name Screen Shot][product-screenshot1]]()<br><br>
[![Product Name Screen Shot][product-screenshot2]]()<br><br>
[![Product Name Screen Shot][product-screenshot3]]()<br><br>
1. 마스크 착용 판별 기능<br>
  1.1. 카메라 정면을 바라보고 서있는다. <br>
  1.2. 마스크 착용 여부에 따라 영상 출력부 우측의 이미지가 변하고 소리가 출력된다.<br>
<br>
2. 출입내역 기록 기능<br>
  2.1. 처음 페이지에 접속하여 출입내역을 작성할 곳의 위치를 입력한다.<br>
  2.2. 건물에 출입하는 인원들은 캠 앞에서서 이름, 전화번호, 신분을 선택하고 제출을 누른다.<br/>
  2.3. 이때 마스크를 착용하지 않았다면 작성한 내용을 제출이 불가능하다.<br><br>
3. 출입내역 저장 기능<br>
  3.1 지금까지 기록한 내용들을 '저장' 버튼을 눌러 파일을 생성한다.<br>
  3.2 생성한 파일을 '다운로드'를 통해 로컬에 저장한다.<br><br>




<!-- ROADMAP -->
## Roadmap

See the [open issues](http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject/issues) for a list of proposed features (and known issues).



<!-- PRECAUTION -->
## Precautions
아래 주의사항에 유의하여 사용해주세요.<br>
**1. 마스크 착용 여부 판별에 웹캠의 실시간 영상 데이터를 사용. 브라우저의 웹캠 접근 권한 허용 필수. 웹캠 없이도 출입자 인적사항 기록은 가능하나 마스크 착용 여부 판별은 불가.**<br>
**2. 인터넷 브라우저별로 json 및 txt 파일 생성 방법이 달라 Internet Explorer에서는 출입자 인적사항 기록은 가능하나 저장은 불가**<br>
**3. Internet Explorer에서 대화 상자(Prompt)의 출력 방식이 Chrome 과는 달라 대화 상자 출력 불가. 따라서 초기에 위치 입력이 불가**<br> 
**4. 출입자 인적사항을 기록한 파일을 다운로드 시 반드시 로컬의 Download 폴더에 저장됨. 저장 경로 변경 불가.**<br> 
**5. 웹캠 앞에서의 재빠른 움직임은 마스크 착용 여부를 정확히 판별하지 못할 수 있음.**<br> 


<!-- CONTRIBUTING -->
## Contributing

해당 프로젝트에 기여하고 싶다면 아래의 절차를 따라주세요. <br>
**어떠한 기여도 환영입니다!!**.<br>
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- Reference -->
## Reference
<a href="https://teachablemachine.withgoogle.com">Teachable Machine 2.0</a>
    ·
<a href="https://www.w3schools.com/">W3schools</a>
    ·
<a href="https://devdocs.io/express/">Express</a>
    ·
<a href="https://devdocs.io/node/">Node.js</a>


<!-- LICENSE -->
## License

<!-- 라이센스 나중에 올리고 링크 수정 필요-->
GPL-v3.0 라이센스를 적용합니다. 자세한 정보는 [License][license-url]를 확인해주세요.<br>



<!-- CONTACT -->
## Contact
Taeyoung Kim - rlaxodud9809@khu.ac.kr<br>
Jaeho Lee - dlwogh9344@khu.ac.kr


Project Link: [http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject](http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject)



<!-- ACKNOWLEDGEMENTS -->
<!--## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)-->





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!--[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject/graphs/master/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew -->

[license-url]: http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject/blob/master/LICENSE.txt
[product-screenshot1]: ./readme_img/1.png
[product-screenshot2]: ./readme_img/2.png
[product-screenshot3]: ./readme_img/3.png
