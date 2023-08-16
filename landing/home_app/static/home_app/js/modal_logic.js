const btn = document.querySelectorAll('.modal_call');
const modal_block = document.querySelector('.modal_block');
const modal_wrapper = document.querySelector('.modal');
const modal_close_btn = document.querySelector('.close_btn');
const body = document.querySelector('html');

const service_btns = document.querySelectorAll('.modal_call_service');
const service_items = document.querySelectorAll('.services__item');
const services__item_content = document.querySelectorAll('.services__item_content');
const tonnerBlock = document.querySelector('.tonner_block');


let toggleModal = function toggleModal() {

    modal_block.classList.toggle('active');
    modal_wrapper.classList.toggle('anim');
    if (body.style.overflowY === 'hidden') {
        body.style.overflowY = 'visible';
    } else {
        body.style.overflowY = 'hidden';
    }
    
};

for (let i = 0; i < btn.length; ++i){
    btn[i].addEventListener('click', function (e){
    e.stopPropagation();
    toggleModal();
})
};


modal_close_btn.addEventListener('click', function (e){
    e.stopPropagation();
    toggleModal();
});


modal_block.addEventListener('click', function(e) {
    if (e.target === modal_block) {
        e.stopPropagation();
        toggleModal();
    }
});



for (let i = 0; i < service_btns.length; i++) {

    let toggleServicesContent = function toggleServicesContent(i) {
        services__item_content[i].classList.toggle("active");
    }

    tonnerBlock.addEventListener('click', function(e) {
        if (services__item_content[i].classList.contains = 'active') {
            services__item_content[i].classList.remove('active');
        }
        e.stopPropagation();
        tonnerBlock.classList.remove('active');
        service_items[i].style.top = '0px';
        service_items[i].style.width = '392px';
        service_items[i].style.height = 'auto';
        service_items[i].style.zIndex = '1';
        service_items[i].style.transform = 'scale(1)';
        service_items[i].style.position = 'relative';
        service_items[i].style.boxShadow = 'none';
        service_btns[i].style.display = 'inline';
        body.style.overflowY = 'visible';
    })

    service_btns[i].addEventListener('click', function(e) {
        e.stopPropagation();
        tonnerBlock.classList.add('active')
        service_items[i].style.zIndex = '1001';
        service_items[i].style.position = 'fixed';
        service_items[i].style.height = '50vh';
        service_items[i].style.width = '40vw';
        service_items[i].style.transition = 'all 0.3s ease !important';
        service_items[i].style.top = '150px';
        service_items[i].style.transform = 'translate(50%, -50%)';
        service_items[i].style.transform = 'scale(1.05)';
        service_items[i].style.boxShadow = 'rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px';
        service_btns[i].style.display = 'none'
        toggleServicesContent(i);
        body.style.overflowY = 'hidden';
        })
}


