//메인 검색창 클릭 시 포커스 이동
let searchBar = document.querySelector('.searchBar');
searchBar.onclick = function(){
    let prevInfo = searchBar.value;
    document.querySelector('.sch_focus').classList.remove('hide');
    document.querySelector('.focusSearchBar').value = prevInfo;
    document.querySelector('#wrap').classList.add('hide');
}
//최근 검색 기록을 클릭 시 입력창에 자동 입력
let history = document.querySelectorAll('.history li');
let contents = document.querySelectorAll('.history li a');
let date = document.querySelectorAll('.date');
for(let i = 0; i<history.length; i++){
    history[i].onclick = function(){
        let getString = contents[i].innerText;
        document.querySelector('.focusSearchBar').value = getString;
    }
}
//검색 기록 삭제
let removeHistory = document.querySelector('.remove_history');
removeHistory.onclick = function(e){
    for(let i = 0; i<history.length; i++){
        contents[i].innerText = "";
        date[i].innerText = "";
    }
     e.preventDefault();

        $.ajax({
            url: '{% url 'search:clear_history' %}',
            type: 'POST',
            dataType: 'json',
            success: function(data) {
                if (data.success) {
                    // 검색 기록이 성공적으로 삭제된 경우에만 메시지 표시
                    alert('검색 기록이 삭제되었습니다.');
                }
            },
            error: function() {
                // 오류 처리
            }
        });
    document.querySelector('.history ul').classList.add('hide');
    document.querySelector('.none_history').classList.remove('hide');
}
//닫기 시 메인으로
let removeSchFocus = document.querySelector('.remove_sch_focus');
removeSchFocus.onclick = function(){
    document.querySelector('#wrap').classList.remove('hide');
    document.querySelector('.sch_focus').classList.add('hide');
    document.querySelector('.search input').value = "";
}