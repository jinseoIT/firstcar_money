const Email = document.querySelector("#ID_Input")
const PassWord = document.querySelector("#passWord_Input")
const Form = document.querySelector("#register_Form")
const Login_button = document.querySelector("#Login_button")
const Regist_button = document.querySelector("#Regist_button")


function Prevent(e) {
    e.preventDefault()
}

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

        fetch("/user/login-Process", {
            method: 'POST',
            body: JSON.stringify(regist_Data),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => res.json())
            .then(data => {
                    if (data.success) {
                        document.cookie = "token" + '=' + data.Token + ";  path=/";
                        localStorage.setItem("userInfo", JSON.stringify(data.userInfo));
                        window.location = "/"
                    } else {
                        alert(data.msg)
                    }
            })
            .catch(error => console.error('Error:', error));
    }
}

function Regist() {
    Form.addEventListener("submit", Prevent)
    window.location = "/user/register"
}


Login_button.addEventListener("click", Login)
Regist_button.addEventListener("click", Regist)