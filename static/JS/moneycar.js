const Money = document.querySelector("#yourMoney")
const Form = document.querySelector("#moneyForm")


function prevent(e){
    e.preventDefault()
     fetch(`/money/cars?money=${Money.value}`)
         // .then(res => res.json())
         //    .then(data => {
         //
         //    })
         //    .catch(error => console.error('Error:', error));

}

Form.addEventListener("submit", prevent)