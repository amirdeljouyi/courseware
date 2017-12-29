window.onscroll = function () {
    if (document.body.scrollTop >= 158 || document.documentElement.scrollTop >= 158){
        document.querySelector('.header').classList.add('minimize');
    }
    if (document.body.scrollTop < 158 && document.documentElement.scrollTop < 158){
        document.querySelector('.header').classList.remove('minimize');
    }
};
document.addEventListener('DOMContentLoaded', function () {
    showNavbar = false;
    
    document.querySelector('.bar').addEventListener('click', () => {
        if (showNavbar) {
            document.querySelector('.navbar').classList.remove('show');
            showNavbar = false;
        } else {
            document.querySelector('.navbar').classList.add('show');
            showNavbar = true;
        }
    });
});