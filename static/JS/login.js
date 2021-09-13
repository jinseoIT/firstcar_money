const Email = document.querySelector("#ID_Input")
const PassWord = document.querySelector("#passWord_Input")
const Form = document.querySelector("#register_Form")

function Login(e) {
    e.preventDefault()

    const regist_Data = {
        Email: Email.value,
        PassWord: PassWord.value,
    }
    //이메일 형식이 아닐때
    const regExp = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
    const result = regist_Data.Email.match(regExp)
    if (result == null) {
        return alert("이메일 형식으로 작성해 주세요")
    }
    // # 패스워드 칸이 비었을때
    else if ("" == regist_Data.PassWord) {
        return alert("모든 칸을 작성해 주세요")
    } else {

        fetch("/user/login_Process", {
            method: 'POST',
            body: JSON.stringify(regist_Data),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => res.json())
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error));
    }
}

Form.addEventListener("submit", Login)