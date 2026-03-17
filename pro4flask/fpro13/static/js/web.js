
// 함수(화살표함수) 객체 생성 후 $에 할당
const $ = (sel) => document.querySelector(sel);


$("#sendBtn").addEventListener("click", async () => { 
    const name = $("#name").value.trim();
    const age = $("#age").value.trim();

    const params = new URLSearchParams({name, age}); 
    const url = `/api/friend?${params.toString()}`;

    $("#result").textContent = "요청 중....";
    
    try {
        const res = await fetch(url, {
            method: "GET",
            headers: {"Accept": "application/json"}
        });

        const data = await res.json();

        if (!res.ok || data.ok === false) {
            
            $("#result").innerHTML = `<span class="error">에러 : ${data.error}</span>`;
            return;
        }
        
        $("#result").innerHTML = `
            <div>이름 : ${data.name}</div>
            <div>나이 : ${data.age}</div>
            <div>연령대 : ${data.age_group}</div>
            <div>메세지 : ${data.message}</div>
        `;
    } catch(err) {
        $("#result").innerHTML = `<span class="error">네트워크, 파싱 오류 : ${err}</span>`;
    }
});