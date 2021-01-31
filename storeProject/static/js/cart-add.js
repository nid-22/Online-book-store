function incrementValue()
{
    // var value = parseInt(document.getElementById('number').value, 10);
    // value = isNaN(value) ? 0 : value;
    // if(value<10){
    //     value++;
            //document.getElementById('number').value = value;
    var value = parseInt(document.getElementsByClassName('badge')[0].innerHTML,10)
    console.log(value)   
    if(value<10){
        value++;
        document.getElementsByClassName('badge')[0].innerHTML = value
        console.log(value)
    }
}
function decrementValue()
{
    var value = parseInt(document.getElementById('number').value, 10);
    value = isNaN(value) ? 0 : value;
    if(value>1){
        value--;
            document.getElementById('number').value = value;
    }

}