
// 쿠키는 전체 데이터가 문자열로 되있어서, 쪼개서 key 넣으면 value가 나오는 함수
const getCookieValue = (key) => {
  let cookieKey = key + "=";
  let result = "";
  const cookieArr = document.cookie.split(";");

  for(let i = 0; i < cookieArr.length; i++) {
    if(cookieArr[i][0] === " ") {
      cookieArr[i] = cookieArr[i].substring(1);
    }

    if(cookieArr[i].indexOf(cookieKey) === 0) {
      result = cookieArr[i].slice(cookieKey.length, cookieArr[i].length);
      return result;
    }
  }
  return result;
}



const textarea = document.querySelector(".comment_area");
const submitBtn = document.querySelector(".submitBtn");
const ul_tag = document.querySelector(".comment_list");
const modal = document.querySelector(".modalOutside");
const modalCutBtn = document.querySelector(".cancelBtn");
const loginModal = document.querySelector(".loginModal");
const closeBtn = document.querySelector(".닫기");
const car_id_value = document.querySelector("#carid_info").value;


// 로컬 스토리지 접근
// 로컬 스토리지에 있는 userInfo를 json 형태로 역 직렬화
// 로그인 한 유저의 아이디 및 닉네임을 받아옴.
const userInfo = JSON.parse(localStorage.getItem("userInfo"))
const userID = userInfo.userId;
const userName = userInfo.userName;
// console.log(userID, userName)

// 쿠키 접근 테스트
// 쿠키에 있는 토큰 값을 가져온다.
console.log(document.cookie)
const token = getCookieValue("token");
// console.log(token)


// 가짜 데이터
// let nickname = "kyusikko";
// let currentTime = "2021-09-15";

const listComment = function() {

    $.ajax({
        type: 'GET',
        url: '/api/comment-list',
        data: {},
        success: function (response) {
            // 유저정보 및 댓글 모든 정보들이 response 안에 담겨있음.
            console.log(response)
            let comment_list = response.comment;
            for (let i=0; i<comment_list.length; i++){
                let cmmt = comment_list[i];
                let comment = comment_list[i].comment;
                let comment_currentTime = comment_list[i].reg_dt;
                let comment_nickname= comment_list[i].nickname;
                // 몽고 db에서 object id도 받아옴 ( 문자열 )
                let comment_id = comment_list[i]._id;
                // console.log(`ObjectId : ${comment_id}`)
                // 카드형식으로 반복문을 돌리기 위해 하는 사전작업
                let li_tag = document.createElement("li");
                li_tag.setAttribute("class","comment_group");
                let list_html = `<div class="id_time">
                                    <h3>${comment_nickname}</h3>
                                    <span>${comment_currentTime}</span>
                                </div>
                                <div class="comment">${comment}</div>
                                <div class="buttons-group">
                                    <!--        수정 버튼               -->
                                    <button id = ${comment_id} class="modified" 
                                    onclick="openModal('${cmmt._id}','${cmmt.nickname}', '${cmmt.comment}', '${cmmt.reg_dt}')">
                                    <i class="far fa-edit"></i>
                                    </button>
                                     <!--        삭제 버튼               -->
                                    <button id = ${comment_id} class="delete" onclick="deleteList(this.id)" ><i class="fas fa-trash-alt"></i></button>
                                </div>`
                li_tag.innerHTML = list_html;
                ul_tag.appendChild(li_tag);
            }
        }
    })
}


// 제출 버튼을 눌렀을때, 유저 정보들 및 댓글 내용이 서버로 넘어간다.
const saveDb = function(){
    let comment = textarea.value;
    if (!comment){

        alert("글을 써주세요")
        return
    }else{
        console.log(`유저아이디 : ${userID}, 유저 닉네임 : ${userName},  유저 토큰 : ${token}, 유저 댓글 ${comment}`)
        $.ajax({
                    type: "POST",
                    url: "/api/comment-add",
                    // 서버에 데이터를 전달해 준다.
                    data: {comment_give : comment,
                           nickname_give : userName,
                           userId_give : userID,
                           token_give : token,
                    },
                    success: function (response) {
                        alert(response["msg"]);
                        console.log(response);
                        window.location.reload()
                    }
                })
        }
    }

const deleteList = function(parameter){
    console.log(parameter)

     $.ajax({
                    type: "POST",
                    url: "/api/comment-delete",
                    // 서버에 데이터를 전달해 준다.
                    data: {
                        id_give : parameter
                    },

                    success: function (response) {
                        alert(response["msg"]);
                        console.log(response);
                        window.location.reload()
                    }
                })

}

const openModal = function(...obj){
    modal.classList.remove('modalOutside-hide');
    // 0. id, 1. nick , 2. content, 3. regDt
    // console.log(obj)

    const cmmtId = document.querySelector('#modal_cmmt_id');
    const nick = document.querySelector('#modal_nickName');
    const content = document.querySelector('#modal_content');
    const regDt = document.querySelector('#modal_reg_dt');

    cmmtId.value = obj[0];
    nick.innerText = obj[1];
    content.value = obj[2];
    regDt.innerText = obj[3];
}

const updateCmmt =  () => {
    const cmmtId = document.querySelector('#modal_cmmt_id');
    const nick = document.querySelector('#modal_nickName');
    const content = document.querySelector('#modal_content');
    const regDt = document.querySelector('#modal_reg_dt');
    let obj = {
        "cmmtId" : cmmtId.value,
        "nick" : nick.innerText,
        "content" : content.value ,
        "regDt" : regDt.innerText
    }

    // 서버에 데이터를 전달해 준다;
    fetch("/api/comment-modify", {
            method: 'POST',
            body: JSON.stringify(obj),
            headers: {'Content-Type': 'application/json' }
        }).then(res => res.json())
            .then(data => {
                // console.log(data)
                window.location.reload();
            })
            .catch(error => console.error('Error:', error));
}


const carIdCheck = function(){
    console.log(car_id_value)

     $.ajax({
                    type: "POST",
                    url: "/api/carInfo-check",
                    // 서버에 데이터를 전달해 준다.
                    data: {
                        // 자동차 고유 값
                        carId_give : car_id_value
                    },
                    success: function (response) {
                        car_info = response.carInfo[0]
                        console.log(car_info)
                        let car_age = car_info.car_age;
                        let car_fuel = car_info.car_fuel;
                        let car_fuel_basic = car_info.car_fuel_basic;
                        let car_fuel_efficiency = car_info.car_fuel_efficiency;
                        let car_img = car_info.car_img;
                        let car_maker_img = car_info.car_maker_img;
                        let car_name = car_info.car_name;
                        let car_price = car_info.car_price;
                        let car_price_full = car_info.car_price_full;
                        let car_type = car_info.car_type;
                        let parent_tag = document.querySelector(".car_detail");
                        let child_tag = document.createElement("div");
                        child_tag.setAttribute("class", "img_info");
                        console.log(parent_tag,child_tag);
                        child_tag.innerHTML=`
                        <div class="container">
                    <div class="row">
                        <div class="col-12 col-lg-6">
                            <div class="img_button">
                                <div class="car_img">
                                    <img class="car_photo" src=${car_img}
                                         alt=${car_name}>
                                </div>
                                <button class="like">좋아요</button>
                            </div>
                        </div>
                        <div class="col-12 col-lg-6">
                            <div class="info">
                                <div class="company_logo">
                                    <button><img class="logo_photo"
                                            src=${car_maker_img}
                                            alt=${car_name}></button>
                                </div>
                                <div class="description">
                                    <h1>${car_name}</h1>
                                    <strong>${car_age}형</strong>
                                    <ul>
                                         <li><span>가격</span>${car_price_full}</li>
                                         <li><span>연비</span>${car_fuel_efficiency}</li>
                                         <li><span>연료</span>${car_fuel}</li>
                                         <li><span>차타입</span>${car_type}</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    `
                    parent_tag.appendChild(child_tag)
                    }
                })

}
let like = document.querySelector(".like");
console.log(like)
// 모달 닫는 함수.
const closeModal = ()=>{
    modal.classList.add('modalOutside-hide')

}
const closeLoginModal = ()=>{
    loginModal.classList.add('modalOutside-hide')
}


// 텍스트 에어리어에 포커스를 클릭했을때! 토큰 기준으로 모달on/off 확인함
const auth =(e)=>{
    e.preventDefault()
    // 토큰이 없으면!
    if(!token){
        loginModal.classList.remove("modalOutside-hide");
        closeBtn.addEventListener("click",closeLoginModal);
        // textarea.disabled= true;
    }else
        console.log("로그인 됬어!");
}


modalCutBtn.addEventListener("click", closeModal)
document.addEventListener("DOMContentLoaded", listComment)
//document.addEventListener("DOMContentLoaded", carIdCheck)
submitBtn.addEventListener("click", saveDb);
textarea.addEventListener("click", auth);




