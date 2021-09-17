// slider 변수
    const sliderContainer = document.querySelector('.slider-container');
    const progressBar = document.querySelector('.slider-container .progress');
    const thumb = document.querySelector('.slider-container .thumb');
    const thumbIndicator = document.querySelector('.slider-container .thumb-indicator');
    const sliderContainerWidth = sliderContainer.offsetWidth;
    const sliderContainerLeft = sliderContainer.offsetLeft;

     // slider 상태변화 변수
    let percentage = 10;
    let dragging = false;
    let translate;
    let unitRange = sliderContainerWidth / 10;
    let commonPrice = 0;
    const rangeArr = []
     for(let i=1; i<10; i+=1) {
         let num = sliderContainerLeft + unitRange * i
         rangeArr.push(num);
      }

     progressBar.style.transform = 'scaleX(' + percentage/100 + ')';
     thumb.style.transform = 'translate(' + (percentage/100 * sliderContainerWidth) + 'px)';

     const setPercentage = () => {
        progressBar.style.transform = 'scaleX(' + percentage/100 + ')';
        thumb.style.transform = 'translate(-50%) translateX(' + (percentage/100 * sliderContainerWidth) + 'px)';
        /* 연봉 변경 */
        let  price =   Math.floor( (percentage * 100) +2000 );
        commonPrice = price;
        document.querySelector('#price').innerText = price.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
     }

     thumb.addEventListener('mousedown', function(e) {
        dragging = true;
        thumbIndicator.classList.add('focus');
      });

     document.addEventListener('mousemove', function(e) {
        if (dragging) {
          if(e.clientX < sliderContainerLeft) {
            percentage = 0;
          } else if(e.clientX >= sliderContainerLeft &&  e.clientX <rangeArr[0] ){
            percentage = 10;
          }else if(e.clientX >= rangeArr[0] &&  rangeArr[1] > e.clientX){
            percentage = 20;
          }else if(e.clientX >= rangeArr[1] &&  rangeArr[2] > e.clientX){
            percentage = 30;
          }else if(e.clientX >= rangeArr[2] &&  rangeArr[3] > e.clientX){
            percentage = 40;
          }else if(e.clientX >= rangeArr[3] &&  rangeArr[4] > e.clientX){
            percentage = 50;
          }else if(e.clientX >= rangeArr[4] &&  rangeArr[5] > e.clientX){
            percentage = 60;
          }else if(e.clientX >= rangeArr[5] &&  rangeArr[6] > e.clientX){
            percentage = 70;
          }
          else if(e.clientX >= rangeArr[6] &&  rangeArr[7] > e.clientX){
            percentage = 80;
          }
          else if(e.clientX >= rangeArr[7] &&  rangeArr[8] > e.clientX){
            percentage = 90;
          }
          else if(e.clientX >= rangeArr[8]){
            percentage = 100;
          }
          else if (e.clientX > sliderContainerWidth + sliderContainerLeft) {
            percentage = 100;
          } else {
            translate = e.clientX - sliderContainerLeft;
            percentage = ( translate / sliderContainerWidth ) * 100;
          }
          setPercentage();
        }
      })

    document.addEventListener('mouseup', function(e) {
        if(dragging){
            getCarListFromMoney(commonPrice);
        }
        dragging = false;
        thumbIndicator.classList.remove('focus');
      })

    setPercentage();
