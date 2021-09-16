const login_out_li = document.querySelector("#login_out_li")
const join_member = document.querySelector("#join")

if (document.cookie.includes("token")==false){
    const login_out = document.createElement("a")
    const join = document.createElement("a")
        join.href="/register"
        join.innerText ="회원가입"
        login_out.href="/login"
        login_out.innerText ="로그인"

    login_out_li.append(login_out)
    join_member.append(join)
}
else{
    const login_out = document.createElement("a")
    const join = document.createElement("a")
        join.innerText = ""
        join.style.display = "none"
        login_out.href="/logout"
        login_out.innerText ="로그아웃"

    login_out_li.append(login_out)
    join_member.append(join)
}

