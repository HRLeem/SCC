var sival = [{'name':'bob','age':'20'},{'name':'carry','age':'38'}]

function f1() {
    var name1 = $('#name').val();
    var age1 = $('#age').val();
    var new_person = {'name':name1, 'age':age1}
    sival.push(new_person);
    console.log(sival);
}

function f2() {
    var temp =''
    for (var i=0;i<sival.length; i++) {
        temp += '<li>이름' + sival[i].name + '</li><li>나이' + sival[i].age + '</li>'
    }
    $('#sival').append(temp);
}

console.log(sival);