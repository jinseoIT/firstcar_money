const login_out_li = document.querySelector("#login_out_li")

if (document.cookie.includes("token")==false){
const login_out = document.createElement("a")
login_out.href="/user/login"
login_out.innerText ="로그인"

login_out_li.append(login_out)

}
else{
const login_out = document.createElement("a")
login_out.href="/user/logout"
login_out.innerText ="로그아웃"

login_out_li.append(login_out)

}