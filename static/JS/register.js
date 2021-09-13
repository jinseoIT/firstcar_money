const Email = document.querySelector("#ID_Input")
const Nick = document.querySelector("#Nick_Input")
const PassWord = document.querySelector("#passWord_Input")
const PassWord_Access = document.querySelector("#passWord_Access_Input")
const Form = document.querySelector("#register_Form")



function Submit(e){
    e.preventDefault()

    const regist_Data = {
        Email : Email.value,
        Nick : Nick.value,
        PassWord : PassWord.value,
        PassWord_Access : PassWord_Access.value

    }
    fetch("/user/register_Process", {
  method: 'POST',
  body: JSON.stringify(regist_Data),
  headers:{
    'Content-Type': 'application/json'
  }
}).then(res => res.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
}

Form.addEventListener("submit", Submit)