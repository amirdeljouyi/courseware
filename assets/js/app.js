import _ from 'lodash';
import Slider from './slider';
// require('../scss/main.scss');
document.addEventListener('DOMContentLoaded', function () {
    var sliderOptions = {};
    var slider = new Slider(document.querySelector('.carousel'), sliderOptions),
        loopStarted = true,
        loop;

    document.querySelector('.slideshow__prev').addEventListener('click', function (event) {
        event.preventDefault();
        slider.prev();
    });

    document.querySelector('.slideshow__next').addEventListener('click', function (event) {
        event.preventDefault();
        slider.next();
    });
});