const btn = document.querySelectorAll('.modal_call');
const modal_block = document.querySelector('.modal_block');
const modal_wrapper = document.querySelector('.modal');
const modal_close_btn = document.querySelector('.close_btn');


let toggleModal = function toggleModal() {
    modal_block.classList.toggle('active');
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
