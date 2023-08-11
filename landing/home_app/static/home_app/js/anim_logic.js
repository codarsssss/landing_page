

// Для горизонтальной анимации
const animBlocks = document.querySelectorAll('.anim_block');


// Проверка на наличие элементов, которые нужно анимировать
if (animBlocks.length > 0) {

    // Событие, при котором будет вызываться функция
    window.addEventListener('scroll', animOnScrollX);

    function animOnScrollX(params) {

        for (let i = 0; i < animBlocks.length; i++) {
            const animBlock = animBlocks[i];
            const animBlockHeight = animBlock.offsetHeight;

            const animBlockOffset = offset(animBlock).top;
            const animStart = 100;

            let animItemPoint = window.innerHeight - animBlockHeight / animStart;

            // Находится ли объект за пределами браузера (сверху)
            if (animBlockHeight > window.innerHeight) {
                animItemPoint = window.innerHeight - window.innerHeight / animStart;
            }

            if ((pageYOffset + window.innerHeight > animBlockOffset) && pageYOffset < (animBlockOffset + animBlockHeight)) {
                animBlock.classList.add('_active');
            }
        }

    }
    // Функция, которая позволяет определить положение объекта относительно окна браузера
    function offset(element) {
        const rect = element.getBoundingClientRect(),
            scrollLeft = window.scrollX || document.documentElement.scrollLeft,
            scrollTop = window.scrollY || document.documentElement.scrollTop;
        return {top: rect.top + scrollTop, left: rect.left + scrollLeft}
    }

    animOnScrollX();

}

// Для вертикальной анимаций
const animYBlocks = document.querySelectorAll('.animYBlocks');


// Проверка на наличие элементов, которые нужно анимировать
if (animYBlocks.length > 0) {

    // Событие, при котором будет вызываться функция
    window.addEventListener('scroll', animOnScrollY);
    window.addEventListener('resize', animOnScrollY);

    function animOnScrollY(params) {

        for (let i = 0; i < animYBlocks.length; i++) {
            const animBlock = animYBlocks[i];
            const animBlockHeight = animBlock.offsetHeight;
            const animBlockOffset = offset(animBlock).top;
            const animStart = 4;

            let animItemPoint = window.innerHeight - animBlockHeight / animStart;

            if (window.innerWidth <= 768) { // Примерная ширина для мобильных устройств
                animItemPoint = window.innerHeight - animBlockHeight / (animStart * 2);
            }

            // Находится ли объект за пределами браузера (сверху)
            if (animBlockHeight > window.innerHeight) {
                animItemPoint = window.innerHeight - window.innerHeight / animStart;
            }

            if ((pageYOffset > animBlockOffset - animItemPoint) && pageYOffset < (animItemPoint + animBlockHeight)) {
                animBlock.classList.add('_active');
            }
        }

    }
    // Функция, которая позволяет определить положение объекта относительно окна браузера
    function offset(element) {
        const rect = element.getBoundingClientRect(),
            scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
            scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        return {top: rect.top + scrollTop, left: rect.left + scrollLeft}
    }

    animOnScrollY();

}