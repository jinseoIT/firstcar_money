const drag = document.querySelector("#drag");

const d1000 = document.querySelector("#d1000");
const d2000 = document.querySelector("#d2000");
const d3000 = document.querySelector("#d3000");
const d4000 = document.querySelector("#d4000");
const d5000 = document.querySelector("#d5000");
const d6000 = document.querySelector("#d6000");
const d7000 = document.querySelector("#d7000");
const d8000 = document.querySelector("#d8000");
const d9000 = document.querySelector("#d9000");
const your_min_Money = document.querySelector("#your-min-Money");


drag.style.position = "relative"

function prices(area_price, e) {
    drag.style.left = e.clientX - 20 + "px"
    your_min_Money.value = area_price + "만원"
}

function range(e, price) {
    if (e.path[0].id === "d" + price)
        return prices(price, e)
}


function show_price(e) {

    range(e, e.path[0].id.replace("d", ""))

}


function point_image(e) {
    const img = new Image();

    e.dataTransfer.setDragImage(img, 0, 0);

}




drag.addEventListener("dragstart", point_image)
d1000.addEventListener("dragover", show_price)
d2000.addEventListener("dragover", show_price)
d3000.addEventListener("dragover", show_price)
d4000.addEventListener("dragover", show_price)
d5000.addEventListener("dragover", show_price)
d6000.addEventListener("dragover", show_price)
d7000.addEventListener("dragover", show_price)
d8000.addEventListener("dragover", show_price)
d9000.addEventListener("dragover", show_price)

// d1000.addEventListener("drop", )
// d2000.addEventListener("drop", )
// d3000.addEventListener("drop", )
// d4000.addEventListener("drop", )
// d5000.addEventListener("drop", )
// d6000.addEventListener("drop", )
// d7000.addEventListener("drop", )
// d8000.addEventListener("drop", )
// d9000.addEventListener("drop", )
