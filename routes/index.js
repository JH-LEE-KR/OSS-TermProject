var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'MWD' , url: "/images/1.jpg"});
});

/* predict() 의 결과를 querystring으로 받아 그것에 맞는 이미지와 음성파일을 보내준다. */
/* /data?id=n 의 형태로 id값을 전달해 준다. */
router.get('/data', function(req, res, next){

  id = req.query.id;

  data = {
    image : "/images/"+id+".jpg",
    audio : "/audio/"+id+".mp3"
  }
  //데이터 확인
  console.log(data);
  //보내주기.
  res.send(data);
});

module.exports = router;

