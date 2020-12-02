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

  <h3 align="center">MWD Readme!!</h3>

  <p align="center">
    구글 Teachable Machine 2.0을 이용하여 마스크 착용 검사 및 출입부 작성 기능을 제공합니다.
    <br />
    <!--여기 뭐 넣을지 생각해보자-->
    <a href="http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject">View Demo</a>
    ·
    <a href="http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject/issues">Report Bug</a>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

구글 Teachable Machine 2.0을 이용하여 마스크 착용 검사 및 출입부 작성 기능을 제공합니다.


### Built With

* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Nodejs](https://nodejs.org)
 - [express](https://github.com/expressjs/express)
 - [ejs](https://github.com/mde/ejs)
* [Teachable Machine](https://teachablemachine.withgoogle.com)




<!-- GETTING STARTED -->
## Getting Started

1. main page 접속<br>
  1.1 <urL>을 통해 접속합니다.<br><br>
2. 카메라 허용<br>
  2.1 카메라 허용 메시지가 표시되면 허용을 선택합니다.<br><br>

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


<!-- USAGE EXAMPLES -->
## Usage

[![Product Name Screen Shot][product-screenshot1]]()<br><br>
[![Product Name Screen Shot][product-screenshot2]]()<br><br>
[![Product Name Screen Shot][product-screenshot3]]()<br><br>
1. 마스크 착용 판별 기능<br>
  1.1. 카메라 정면을 바라보고 서있는다. <br>
  1.2. 마스크 착용 여부에 따라 캠 우측의 이미지가 변하고 소리가 출력된다.<br>
<br>
2. 출입내역 기록 기능<br>
  2.1. 처음 페이지에 접속하여 출입내역을 작성할 곳의 위치를 입력한다.<br>
  2.2. 건물에 출입하는 인원들은 캠 앞에서서 이름, 전화번호, 신분을 선택하고 제출을 누른다.<br/>
  2.3. 이때 마스크를 착용하지 않았다면 작성한 내용을 제출이 불가능하다.<br><br>
3. 출입내역 저장 기능<br>
  3.1 지금까지 기록한 내용들을 '저장' 버튼을 눌러 파일을 생성한다.<br>
  3.2 생성한 파일을 '다운로드'를 통해 로컬에 저장한다.<br><br>

더 많은 정보를 원하신다면, [Teachablemachine Documentation](https://teachablemachine.withgoogle.com) 를 참고해주세요.



<!-- ROADMAP -->
## Roadmap

See the [open issues](http://khuhub.khu.ac.kr/MWD/2020-02-OSS-TermProject/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

해당 프로젝트에 기여하고 싶다면 아래의 절차를 따라주세요. <br>
**어떠한 기여도 환영입니다!!**.<br>
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



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
