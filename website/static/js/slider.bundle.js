/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 2);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 1 */,
/* 2 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__slider__ = __webpack_require__(3);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__slider___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0__slider__);
//import _ from 'lodash';

__webpack_require__(0);
document.addEventListener('DOMContentLoaded', function () {
    var sliderOptions = {};
    var slider = new __WEBPACK_IMPORTED_MODULE_0__slider___default.a(document.querySelector('.carousel'), sliderOptions),
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

/***/ }),
/* 3 */
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(4);

class Slider {
    constructor(sliderElement, sliderOptions = {}) {
        this.sliderElement = sliderElement;
        this.transitionEndCallback = null;
        this.init(sliderOptions);
    }

    init(sliderOptions) {
        this.slides = Array.prototype.slice.call(this.sliderElement.children).filter((slide) => {
            if (slide.offsetParent !== null)
                return slide.classList.contains("carousel__slide");
            return false;
        });

        this.slidesCount = this.slides.length;
        if (this.slidesCount === 0) {
            throw new DOMException("Slider does not contain any children (slides)");
        }
        this.currentSlide = 0;

        this.options = this._getOptions(sliderOptions);

        this.numberOfClones = this.options.numberOfVisibleSlides + 1;
        
        this._build();
        this._createSlideClones(this.numberOfClones);
        this._transitionEnd();
        this.sliderElement.style.width = (this.slides.length + this.numberOfClones * 2 ) / this.options.numberOfVisibleSlides * 100 + "%";
        this.slide(1);
    }

    slide(index) {
        this.currentSlide = index;
        this.sliderElement.classList.add("slideshow__slider--animate");

        this._moveTo(this.currentSlide);

        if (this.currentSlide > this.slidesCount) {
            this.transitionEndCallback = () => {
                this.currentSlide = 1;
            };

            return this.currentSlide;
        }
        if (this.currentSlide <= 0) {
            this.transitionEndCallback = () => {
                this.currentSlide = this.slidesCount;
            };
        }

        return this.currentSlide;
    }

    next() {
        return this.slide(this.currentSlide + 1);
    }

    prev() {
        return this.slide(this.currentSlide - 1);
    }

    _build() {
        this.sliderElement.classList.add("slideshow__slider");

        const basis = 100 / (this.numberOfClones * 2 + this.slidesCount);
        // Add slide class and basis to each slide
        this.slides.forEach((slide) => {
            slide.classList.add("slideshow__slide");
            slide.style.flexBasis = basis + "%";
        });
        
    }

    _createSlideClones(numberOfClones) {
        while (this.options.numberOfVisibleSlides > this.slides.length) {
            this._cloneNodes(this.slides);
            this.slides = this.slides.concat(this.slides);
            this.slidesCount = this.slides.length;
        }

        let firstElements = this.slides.slice(0, numberOfClones),
            lastElements = this.slides.slice(-1 * numberOfClones);

        firstElements = this._fillMissing(firstElements, numberOfClones, this.slides[0]);
        lastElements = this._fillMissing(lastElements, numberOfClones, this.slides[this.slides.length - 1]);

        this._cloneNodes(firstElements);

        lastElements.reverse().forEach((el) => {
            const clone = el.cloneNode(true);
            clone.classList.add("slideshow__clone");
            this.sliderElement.insertBefore(clone, this.sliderElement.firstChild);
        });

        return numberOfClones;
    }

    _cloneNodes(nodesList) {
        nodesList.forEach((el) => {
            const clone = el.cloneNode(true);
            clone.classList.add("slideshow__clone");
            this.sliderElement.appendChild(clone);
        });
    }

    _fillMissing(arr, filledArrayLength, fillElement) {
        while (arr.length < filledArrayLength) {
            arr.push(fillElement);
        }

        return arr;
    }

    _transitionEnd() {
        const eventList = [
            "MSTransitionEnd",
            "msTransitionEnd",
            "transitionend",
            "webkitTransitionEnd"
        ];
        eventList.forEach((event) => {
            this.sliderElement.addEventListener(event, () => {
                if (this._isFunction(this.transitionEndCallback)) {
                    // Clear the callback if needed. We want to make sure that it"s executed only once.
                    this.transitionEndCallback = this.transitionEndCallback();

                    // Remove animating class and do magic for infinite sliding.
                    this.sliderElement.classList.remove("slideshow__slider--animate");
                    this._moveTo(this.currentSlide);
                }
            });
        });
    }

    _isFunction(obj) {
        return Boolean(obj && obj.constructor && obj.call && obj.apply);
    }

    _moveTo(index) {
        this.sliderElement.style.transform = "translate3d(-" + this._calculatePosition(index) + "%, 0, 0)";
    }

    _calculatePosition(index) {
        return 100 * (index + this.numberOfClones - 1) / (this.slidesCount + this.numberOfClones * 2);
    }

    _getOptions(options) {
        const defaultOptions = {
            numberOfVisibleSlides: 1
        };
        return Object.assign(defaultOptions, options);
    }
}

module.exports = Slider;

/***/ }),
/* 4 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ })
/******/ ]);