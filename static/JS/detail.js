console.log("what the fuck")


document.addEventListener("DOMContentLoaded", get_carList)

function get_carList() {
    $.ajax({
        type: "GET",
        url: `/car/list`,
        success: function (response) {
            let car_lists= response.car_list
            let ul = document.querySelector(".cars_name");
            for (let i=0; i<car_lists.length; i++){
                let car_fuel = car_lists[i].car_fuel;
                let car_fuel_efficiency = car_lists[i].car_fuel_efficiency;
                let car_img = car_lists[i].car_img;
                let car_maker_img = car_lists[i].car_maker_img;
                let car_name = car_lists[i].car_name;
                let car_price = car_lists[i].car_price;
                let car_price_full = car_lists[i].car_price_full;
                let car_type = car_lists[i].car_type;

                let li_tag = document.createElement("li");
                li_tag.setAttribute("class", "cars");
                li_tag.innerHTML=car_name;
                ul.appendChild(li_tag)
                console.log(car_img)



            }
        }
    })
}