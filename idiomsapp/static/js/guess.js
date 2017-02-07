var startNum;
var currentNum;
var tick = 0;
var wrongIdioms = [];
var reql;
var counter;


$("#tick").click(function(){
    idiom = $('div ul:visible:last')
    idiom.next().show();
    tick = tick + 1;
})

$("#cross").click(function(){
    idiom = $('div ul:visible:last')
    var idiom_text = idiom.text()
    wrongIdioms.push(idiom_text)
    idiom.css({"color": "red"});
    idiom.next().show();
})


function addClassDelayed(jqObj, c, to) {
    setTimeout(function() { jqObj.addClass(c); }, to);
}

function anim() {
  addClassDelayed($("#countdown"), "puffer", 600);
  if (currentNum< 0)  {
    countdownFinished();
  } else currentNum--;
  $('#countdown').html(currentNum+1);
  $('#countdown').removeClass("puffer");
}

$(function() {
  startNum = 120;
  currentNum = startNum;
  $("#countdown").html(currentNum); // init first time based on n
  counter = self.setInterval(function(){anim()},1000);
});

function countdownFinished() {
   clearInterval(counter);
   $("#tick").hide();
   $("#cross").hide();
   $(".idiomsHolder").css({"opacity": 0.2});
   $('#countdown').hide()
   var result = $(".result").text()+tick;
   $(".result").text(result).css({
        "color": "#AAAAAA", "font-size":"200%"
    })
   $(".result").show();
   $(".restart").show();
}
