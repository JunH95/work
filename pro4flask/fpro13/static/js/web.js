// 함수(화살표함수) 객체 생성 후 $에 할당

const $ = (sel) => document.querySelector(sel);
// function $(sel){
//     return document.querySelector(sel)
// }
// ex) $("#sendBtn") 하면 document.querySelector(sel)가 실행

$("#sendBtn").addEventlistener("click", abc);

function abc(){
    alert("a");
}