// 각종 요소
const code = document.querySelector("#code");
const sang = document.querySelector("#sang");
const su = document.querySelector("#su");
const dan = document.querySelector("#dan");

const msg = document.querySelector("#msg");
const tbody = document.querySelector("#tbody");

const btnAdd = document.querySelector("#btnAdd");
const btnUpdate = document.querySelector("#btnUpdat");
const btnDelete = document.querySelector("#btnDelete");
const btnReloade = document.querySelector("#btnReloade");

function setMsg(text){
    msg.textContent = text;
}

// 입력 폼 초기화 함수
function clearForm(){
    code.value = "";
    sang.value = "";
    su.value = "";
    dan.value = "";
}

// 전체 자료 읽기
async function loadAll(){
    const res = await fetch("/api/sangdata");
    const data = await res.json();

    alert(data);
}