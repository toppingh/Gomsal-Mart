//댓글 글자수 카운팅
$(document).ready(function () {
  $('#textBox').keyup(function (e) {
    let content = $(this).val();

    // 글자수 세기
    if (content.length == 0 || content == '') {
      $('.textCount').text('0자');
    } else {
      $('.textCount').text(content.length + '자');
    }

    // 글자수 제한
    if (content.length > 200) {
      // 200자 부터는 타이핑 되지 않도록
      $(this).val(content.substring(0, 200));
      // 200자 넘으면 알림창 뜨도록
      alert('글자수는 200자까지 입력 가능합니다.');
    }
  });
});

document.addEventListener("DOMContentLoaded", function() {
  const stars = document.querySelectorAll(".star");
  const starImages = [
    "/static/image/unstar.png",
    "/static/image/star.png"
  ];

   const ratingInput = document.getElementById("ratingInput");

  stars.forEach(star => {
    star.addEventListener("click", function() {
      const rating = parseInt(this.getAttribute("data-value"));

      stars.forEach((s, index) => {
        const img = s.querySelector("img");
        img.src = index < rating ? starImages[1] : starImages[0];
      });

      ratingInput.value = rating;
    });
  });
});