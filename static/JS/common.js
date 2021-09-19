 const toTopEl = document.querySelector('#to-top');

        window.addEventListener('scroll', _.throttle(function () {

            if (window.scrollY > 700) {
                //버튼 보이기!
                gsap.to(toTopEl, .2, {
                    x: 0
                });
            } else {
                //버튼 숨기기!
                gsap.to(toTopEl, .2, {
                    x: 100
                });
            }
        }, 300));
        // _.throttle(함수, 시간)

        toTopEl.addEventListener('click', function () {
            gsap.to(window, .7, {
                scrollTo: 0
            });
        });