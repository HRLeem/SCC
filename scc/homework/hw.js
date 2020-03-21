function check() {
    /*
    이름, 수량, 주소, 번호 중 하나라도 입력되어 있지 않으면 alert
    입력 안한 곳에 포커스가 맞춰지도록 ---> test 결과 복수의 대상에게 focus 가 맞춰지는게 아닌듯함
                                        그렇다면, 복수의 대상에서 border로 표시를 주고 첫번째에게 focus를 맞추자
                                        그다음 주문하기를 눌러서 정상 처리가 되면 border는 사라지게 
    */
    let msg = ''
    let josa = '이'
    let no_val = [];
    for (let i = 1; i < 5; i++) {

        if (!$('#check' + i).val()) {
            console.log($('#check' + i).attr('placeholder'));
            msg += $('#check' + i).attr('placeholder');
            msg += ', '
            no_val.push(i)

            //안쓴거 쓰라고 border색 바꾸기
            $('#check' + i).css('border', '1px solid  #FEB2B2');
        } else {
            //썻으면 잘했다고 되돌려주기    
            $('#check' + i).css('border', '1px solid  #dbdbdb');
        }
        if (i > 2 && !$('#check' + i).val()) {
            josa = "가"
        }
    }
    console.log(no_val[0])
    /*
    주문자 이름, 주문 수량    으로 끝날때 '이'
    주소, 전화번호      로 끝날때 '가'

    안된놈이 마지막일때 , 떼기  ( 이/가 앞에 ,가 안붙도록 )
     */
    if ( no_val[0] ) {
        msg = msg.substr(0, msg.length - 2);
        alert(msg + josa + ' 입력되지 않았습니다');

        $('#check' + no_val[0]).focus();
        console.log(no_val)
    } else if (!no_val[0]) {
        $('.merong').css('visibility', 'inherit')
        alert('주문이 완료되었습니다!');
        let temp = '<tr>';
        for (var i = 1; i < 5; i++) {
            temp += '<td>' + $('#check' + i).val() + '</td>'
        }
        temp += '</tr>';
        $('#jumunja_info').append(temp);
        // 주문 완료시에 박스 초기화
        $('input').val('');
        $('select').val('disabled selected');
    }
}