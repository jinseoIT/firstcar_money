const Email = document.querySelector("#ID_Input")
const Nick = document.querySelector("#Nick_Input")
const PassWord = document.querySelector("#passWord_Input")
const PassWord_Access = document.querySelector("#passWord_Access_Input")
const Form = document.querySelector("#register_Form")
const Access_Button = document.querySelector("#Access_button")
const Cancel_Button = document.querySelector("#cancel_button")

function prevent(e) {
    e.preventDefault()
}

function Submit() {
    Form.addEventListener("submit", prevent)

    const regist_Data = {
        Email: Email.value,
        Nick: Nick.value,
        PassWord: PassWord.value,
        PassWord_Access: PassWord_Access.value
    }
    // # 이메일 형식이 아닌 경우
    const regExp = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
    const result = regist_Data.Email.match(regExp)
    if (result == null) {
        return alert("이메일 형식으로 작성해 주세요")
    }
    // # 닉네임, 패스워드, 패스워드 확인 칸이 비어있을 경우
    else if ("" == regist_Data.Nick || "" == regist_Data.PassWord || "" == regist_Data.PassWord_Access) {
        return alert("모든 칸을 작성해 주세요")
    } else {
        fetch("/user/register_Process", {
            method: 'POST',
            body: JSON.stringify(regist_Data),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => res.json())
            .then(data => {
                if (data.Success) {
                    alert(data.msg)
                    window.location='/'
                }
                else{
                    alert(data.msg)
                }
            })
            .catch(error => console.error('Error:', error));
    }
}

function Cancel() {
    Form.addEventListener("submit", prevent)
    window.location = "/"
}


Access_Button.addEventListener("click", Submit)
Cancel_Button.addEventListener("click", Cancel)