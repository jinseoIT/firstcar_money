// console.log("what the fuck")


// document.addEventListener("DOMContentLoaded", get_carList)
//
// function get_carList() {
//     $.ajax({
//         type: "GET",
//         url: `/car/list`,
//         success: function (response) {
//             let car_lists= response.car_list
//             let ul = document.querySelector(".cars_name");
//             for (let i=0; i<car_lists.length; i++){
//                 let car_fuel = car_lists[i].car_fuel;
//                 let car_fuel_efficiency = car_lists[i].car_fuel_efficiency;
//                 let car_img = car_lists[i].car_img;
//                 let car_maker_img = car_lists[i].car_maker_img;
//                 let car_name = car_lists[i].car_name;
//                 let car_price = car_lists[i].car_price;
//                 let car_price_full = car_lists[i].car_price_full;
//                 let car_type = car_lists[i].car_type;
//
//                 let li_tag = document.createElement("li");
//                 li_tag.setAttribute("class", "cars");
//                 li_tag.innerHTML=car_name;
//                 ul.appendChild(li_tag)
//                 console.log(car_img)
//
//
//
//             }
//         }
//     })
// }


// 몽고 db에 데이터 넣어보기
const modifiy_input = document.querySelector(".motify_input");
const textarea = document.querySelector(".comment_area");
const submitBtn = document.querySelector(".submitBtn");
const ul_tag = document.querySelector(".comment_list");
const deleteBtn = document.querySelector(".delete");
const modifiBtn = document.querySelector(".modified");
let realComment = document.querySelector(".comment");
const confirmBtn = document.querySelector(".confirmBtn");
let nickname = "kyusikko";
let currentTime = "2021-09-15";

const listComment = function() {

    $.ajax({
        type: 'GET',
        url: '/api/comment-list',
        data: {},
        success: function (response) {
            console.log(response)
            let comment_list = response.comment;
            for (let i=0; i<comment_list.length; i++){
                let comment = comment_list[i].comment;
                let comment_currentTime = comment_list[i].currentTime;
                let comment_nickname= comment_list[i].nickname;
                // 몽고 db에서 object id 받아옴.
                let comment_id = comment_list[i]._id;
                console.log(`ObjectId : ${comment_id}`)
                let li_tag = document.createElement("li");
                li_tag.setAttribute("class","comment_group");
                let list_html = `<div class="id_time">
                                    <h3>${comment_nickname}</h3>
                                    <span>${comment_currentTime}</span>
                                </div>
                                <div class="comment">${comment}</div>
                                <div class="buttons-group">
                                    <button id = ${comment_id} class="modified" onclick="modifiList(this.id)"><i class="far fa-edit"></i></button>
                                    <button id = ${comment_id} class="delete" onclick="deleteList(this.id)" ><i class="fas fa-trash-alt"></i></button>
                                </div>`
                li_tag.innerHTML = list_html;
                ul_tag.appendChild(li_tag);


            }

        }
    })

}


const saveDb = function(){
    let comment = textarea.value;
    if (!comment){
        textarea.innerText="입력하라고오"
        alert("글을 써주세요")
        return
    }else{
        console.log(comment, nickname, currentTime)
        $.ajax({
                    type: "POST",
                    url: "/api/comment-add",
                    // 서버에 데이터를 전달해 준다.
                    data: {comment_give : comment,
                           nickname_give : nickname,
                           currentTime_give : currentTime


                    },

                    success: function (response) {

                        alert(response["msg"]);
                        console.log(response);
                        window.location.reload()
                    }
                })
        textarea.innerText=""
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

const modifiList = function(parameter){
    console.log(parameter)
    console.log("눌렸따")

    $.ajax({
                    type: "POST",
                    url: '/api/comment-modi',
                    // 서버에 데이터를 전달해 준다.
                    data: {
                        id_give : parameter
                    },

                    success: function (response) {
                        console.log(response.result);
                        let moText = response.result[0].comment;
                        modifiy_input.value= moText;
                        moText



                    }
                })

}


document.addEventListener("DOMContentLoaded", listComment)
submitBtn.addEventListener("click", saveDb);

