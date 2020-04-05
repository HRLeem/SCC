function call_orders() {
    console.log('18181818')
    $.ajax({
        type: "GET"
        , url: '/take_orders'
        , data: {}
        , success: function (res) {
            console.log('1212121212');
            let temp = '';
            if (res['result'] == 'success') {
                console.log('3333333');
                let orders = res['orders'];
                console.log(orders);
                for (let i = 0; i < orders.length; i++) {
                    temp += '<tr>';
                    temp += '<td>' + orders[i]['name'] + '</td>'
                    temp += '<td>' + orders[i]['quantity'] + '</td>'
                    temp += '<td>' + orders[i]['address'] + '</td>'
                    temp += '<td>' + orders[i]['phone'] + '</td>'
                    temp += '</tr>';
                }
                $('#jumunja_info').append(temp);
            }
        }
    })

}


function check() {
    var status = 0;
    /* 주문하기를 눌러서 정상 처리가 되면 border는 사라지게 
    */
    let msg = ''
    let josa = '이'
    let no_val = [];
    for (let i = 1; i < 5; i++) {

        if (!$('#check' + i).val()) {
            // console.log($('#check' + i).attr('placeholder'));
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
    // console.log(no_val[0])
    /*
    주문자 이름, 주문 수량    으로 끝날때 '이'
    주소, 전화번호      로 끝날때 '가'
    안된놈이 마지막일때 , 떼기  ( 이/가 앞에 ,가 안붙도록 )
     */
    if (no_val[0]) {
        msg = msg.substr(0, msg.length - 2);
        alert(msg + josa + ' 입력되지 않았습니다');

        $('#check' + no_val[0]).focus();
        // console.log(no_val)
    } else if (!no_val[0]) {
        $('.merong').css('visibility', 'inherit')
        // alert('주문이 완료되었습니다!');
        let temp = '<tr>';
        for (var i = 1; i < 5; i++) {
            temp += '<td>' + $('#check' + i).val() + '</td>'
        }
        temp += '</tr>';
        $('#jumunja_info').append(temp);

        /* 모든것이 준비되면 DB에 쓰기 */
        let name = $('#check1').val()
        let quantity = $('#check2').val()
        let address = $('#check3').val()
        let phone = $('#check4').val()
        $.ajax({
            type: "POST"
            , url: "/order"
            , data: {
                name_give: name
                , quantity_give: quantity
                , address_give: address
                , phone_give: phone
            }
            , success: function (res) {
                if (res['result'] == 'success') {
                    alert(res['msg']);
                } else {
                    alert('주문과정 중 알수없는 에러가 발생하였습니다.')
                }
            }
        })

        // 주문 완료시에 박스 초기화
        $('input').val('');
        $('select').val('disabled selected');
    }




}