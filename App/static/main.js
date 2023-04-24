
async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

async function main(){
    const users = await getUserData();
    loadTable(users);
}

main();

var timerInterval;
      var timeLeft = 0;
      
      function startTimer() {
        var minutes = document.getElementById("minutes").value;
        var seconds = document.getElementById("seconds").value;
        timeLeft = parseInt(minutes) * 60 + parseInt(seconds);
        
        timerInterval = setInterval(function() {
          var minutesLeft = Math.floor(timeLeft / 60);
          var secondsLeft = timeLeft % 60;
          
          document.getElementById("timer").innerHTML = minutesLeft + ":" + (secondsLeft < 10 ? "0" : "") + secondsLeft;
          
          if (timeLeft == 0) {
            clearInterval(timerInterval);
            document.getElementById("timer").innerHTML = "Done!";
            var audio = new Audio('http://soundbible.com/grab.php?id=1705&type=wav');
            audio.play();
          } else {
            timeLeft--;
          }
        }, 1000);
      }
      
      function pauseTimer() {
        clearInterval(timerInterval);
      }
      
      function resetTimer() {
        clearInterval(timerInterval);
        document.getElementById("minutes").value = "0";
        document.getElementById("seconds").value = "0";
        document.getElementById("timer").innerHTML = "0:00";
      }
      
      function resumeTimer() {
        startTimer();
      }


window.addEventListener("scroll", function() {
  var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  var body = document.querySelector("body");
  var startColor = "#ff8c00";
  var endColor = "#ffa500";
  var colorDiff = endColor.substring(1).split("").map(function(c, i) {
    return (parseInt(c, 16) - parseInt(startColor.substring(1).split("")[i], 16)) / 100;
  });
  var newColor = startColor;
  if (scrollTop > 0) {
    newColor = "#" + colorDiff.map(function(c, i) {
      return Math.round(parseInt(startColor.substring(1).split("")[i], 16) + (c * scrollTop)).toString(16);
    }).join("");
  }
  body.style.background = "linear-gradient(to bottom, " + newColor + ", " + endColor + ")";
});