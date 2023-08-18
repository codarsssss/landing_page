const btn = document.querySelectorAll('.modal_call');
const modal_block = document.querySelector('.modal_block');
const modal_wrapper = document.querySelector('.modal');
const modal_close_btn = document.querySelector('.close_btn');
const body = document.querySelector('html');

const service_btns = document.querySelectorAll('.modal_call_service');
const service_items = document.querySelectorAll('.services__item');
const services__item_content = document.querySelectorAll('.services__item_content');
const services_title = document.querySelectorAll('.service_title');
const tonnerBlock = document.querySelector('.tonner_block');

const original_back_img_service_item = []



for (let i = 0; i < service_btns.length; i++) {
    original_back_img_service_item.push(getComputedStyle(service_items[i]).backgroundImage)

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
        service_items[i].style.overflowY = 'hidden';
        service_items[i].style.backgroundImage = original_back_img_service_item[i];
        body.style.overflowY = 'visible';

        if (window.innerWidth >= 1001) {
            services_title[i].style.maxWidth = '371px'
        } else {
            services_title[i].style.maxWidth = '260px'
        }
    })

    service_btns[i].addEventListener('click', function(e) {
        e.stopPropagation();
        tonnerBlock.classList.add('active')
        service_items[i].style.zIndex = '1001';
        service_items[i].style.position = 'fixed';
        service_items[i].style.height = '70%';
        service_items[i].style.width = '18%';
        service_items[i].style.transition = 'all 0.3s ease !important';
    
        if (window.innerWidth <= 376) {
            service_items[i].style.top = '80px';
        } else {
            service_items[i].style.top = '100px';
        }

        service_items[i].style.transform = 'translate(50%, -50%)';
        service_items[i].style.transform = 'scale(1.05)';
        service_items[i].style.boxShadow = 'rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px';
        service_items[i].style.overflowY = 'scroll'
        service_items[i].style.overflowX = 'hidden'
        service_items[i].style.backgroundImage = 'none'        

        service_btns[i].style.display = 'none'

        services_title[i].style.width = '100%'
        services_title[i].style.maxWidth = '100%'
        toggleServicesContent(i);
        body.style.overflowY = 'hidden';
        })
}


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

    for (let item = 0; item < service_items.length; item++) {

    if (services__item_content[item].classList.contains = 'active') {
        services__item_content[item].classList.remove('active');
    }
    e.stopPropagation();

    tonnerBlock.classList.remove('active');
    service_items[item].style.top = '0px';
    service_items[item].style.width = '392px';
    service_items[item].style.height = 'auto';
    service_items[item].style.zIndex = '1';
    service_items[item].style.transform = 'scale(1)';
    service_items[item].style.position = 'relative';
    service_items[item].style.boxShadow = 'none';
    service_btns[item].style.display = 'inline';
    service_items[item].style.overflowY = 'hidden';
    service_items[item].style.backgroundImage = original_back_img_service_item[item];
    body.style.overflowY = 'visible';

    if (window.innerWidth >= 1001) {
        services_title[item].style.maxWidth = '371px'
    } else {
        services_title[item].style.maxWidth = '260px'
    }}
    
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
