const btn = document.querySelectorAll('.modal_call');
const modal_block = document.querySelector('.modal_block');
const modal_wrapper = document.querySelector('.modal');
const modal_close_btn = document.querySelector('.close_btn');
const body = document.querySelector('html');

const service_btns = document.querySelectorAll('.modal_call_service');
const modal_ids = document.querySelectorAll('.service_modal')
const service_modal_wrapper = document.querySelectorAll('.service_modal_wrapper');
const service_modal_close_btn = document.querySelectorAll('.service_modal_close_btn');

console.log(modal_ids)
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

    service_btns[i].addEventListener('click', function(e) {
        e.stopPropagation();
        console.log(i)
        modal_ids[i].style.opacity = '1';
        modal_ids[i].style.zIndex = '1001';
        service_modal_wrapper[i].style.zIndex = '1002';
        service_modal_wrapper[i].style.top = '0';
        service_modal_wrapper[i].style.opacity = '1';
        body.style.overflowY = 'hidden';
        })

    service_modal_close_btn[i].addEventListener('click', function(e){
        e.stopPropagation();
        modal_ids[i].style.opacity = '0';
        modal_ids[i].style.zIndex = '-100';
        service_modal_wrapper[i].style.zIndex = '-100';
        service_modal_wrapper[i].style.top = '-100px';
        service_modal_wrapper[i].style.opacity = '0';
        body.style.overflowY = 'visible';
    })
}


