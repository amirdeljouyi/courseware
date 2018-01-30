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
/******/ 	return __webpack_require__(__webpack_require__.s = 5);
/******/ })
/************************************************************************/
/******/ ({

/***/ 5:
/***/ (function(module, exports) {

var pageNum = 1;

pathname = (window.location.pathname).slice(1);
var course;

function createNode(element) {
    return document.createElement(element); // Create the type of element you pass in the parameters
}

function append(parent, el) {
    return parent.appendChild(el); // Append the second parameter(element) to the first one
}

const about = async() => {
    const response = await fetch('http://localhost:8000/api/' + pathname, {
        method: 'get'
    });
    course = await response.json();
    const courseElement = document.getElementById('course');
    courseElement.innerHTML = `
        <h4 class="inline text-tertiary-color br-b-tertiary">About This Course</h4>
        <div class="story mgn-b-2"><p>${course.about}</p></div>
        <h4 class="inline text-tertiary-color br-b-tertiary">Teachers</h4>
        <div class="row mgn-t-2 mgn-b-2" id="teachers"></div>
        <h4 class="inline text-tertiary-color br-b-tertiary">Degree</h4>
        <div class="story mgn-b-2">
            <p>
                <span class="capitalize">${course.degree}</span>
            </p>
        </div>
        <h4 class="inline text-tertiary-color br-b-tertiary">Term</h4>
        <div class="story mgn-b-2">
            <p>
                <span class="capitalize">${course.term}</span>
            </p>
        </div>
    `;
    requestTeacher();
}
about();

const requestTeacher = async() => {
    const teacherElement = document.getElementById('teachers');
    const response = await fetch('http://localhost:8000/api/course/' + course.id + '/teacher', {
        method: 'get'
    });
    const json = await response.json();
    teachers = JSON.parse(json);
    teachers.map(teacher => {
        let figure = createNode('figure'),
            figcaption = createNode('figcaption'),
            a = createNode('a'),
            pLevel = createNode('p'),
            pField = createNode('p'),
            pDegree = createNode('p'),
            img = createNode('img');
        figure.classList.add("col-xs-12", "col-sm-6", "card", "horizontally");
        img.src = "/static/img/" + teacher.img_url;
        img.classList.add('circle', 'md') // Add the source of the image to be the src of the img element
        a.innerHTML = `${teacher.firstname} ${teacher.lastname}`;
        a.href = "user/" + teacher.id;
        pLevel.innerHTML = `Level : ${teacher.level}`;
        pField.innerHTML =
            `Field of study : <span class="capitalize">${teacher.field_of_study}</span>`;
        pDegree.innerHTML =
            `Field of study : <span class="capitalize">${teacher.degree}</span>`;
        append(figcaption, a);
        append(figcaption, pLevel);
        append(figcaption, pField);
        append(figcaption, pDegree)
        append(figure, img)
        append(figure, figcaption)
        append(teacherElement, figure);
    });
}
document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.about').addEventListener('click', function (event) {
        event.preventDefault();
        about();
    });
    document.querySelector('.resources').addEventListener('click', function (event) {
        event.preventDefault();
        resource();
    });
    document.querySelector('.slides').addEventListener('click', function (event) {
        event.preventDefault();
        slide();
    });
    document.querySelector('.homework').addEventListener('click', function (event) {
        event.preventDefault();
        homework();
    });
    document.querySelector('.syllabus').addEventListener('click', function (event) {
        event.preventDefault();
        syllabus();
    });
    document.querySelector('.news').addEventListener('click', function (event) {
        event.preventDefault();
        news();
    });
    // document.querySelector('.resources').addEventListener('click', function (event) {
    //     event.preventDefault();
    //     resource();
    // });
});    

const resource = async() => {
    const response = await fetch('http://localhost:8000/api/course/' + course.id + '/resources', {
        method: 'get'
    });
    resources = await response.json();
    const courseElement = document.getElementById('course');
    courseElement.innerHTML = `
        <h4 class="inline text-tertiary-color br-b-tertiary">Resources</h4>
        <div class="story">
            <p> ${resources} </p>
        </div>
    `;
}

const slide = async() => {
    const response = await fetch('http://localhost:8000/api/course/' + course.id + '/slides', {
        method: 'get'
    });
    const courseElement = document.getElementById('course');
    courseElement.innerHTML = `
        <h4 class="inline text-tertiary-color br-b-tertiary">Slides</h4>
    `;
    const json = await response.json();
    slides = JSON.parse(json);
    slides.map(slide => {
        div = createNode('div');
        div.classList.add('story');
        div.innerHTML = ` 
        <p>
            <a href="/static/slide/'+${slide.url}">${slide.name}</a>
        </p>`;
        append(courseElement, div)
    })
}

const homework = async() => {
    const response = await fetch('http://localhost:8000/api/course/' + course.id + '/homework', {
        method: 'get'
    });
    homeworkJSON = await response.json();
    const courseElement = document.getElementById('course');
    courseElement.innerHTML = `
        <h4 class="inline text-tertiary-color br-b-tertiary">Homeworks</h4>
        <div class="story">
            <p> ${homeworkJSON} </p>
        </div>
    `;
}

const syllabus = async() => {
    const response = await fetch('http://localhost:8000/api/course/' + course.id + '/syllabus', {
        method: 'get'
    });
    syllabusJSON = await response.json();
    const courseElement = document.getElementById('course');
    courseElement.innerHTML = `
        <h4 class="inline text-tertiary-color br-b-tertiary">Syllabus</h4>
        <div class="story">
            <p> ${syllabusJSON} </p>
        </div>
    `;
}

const news = async() => {
    const response = await fetch('http://localhost:8000/api/course/' + course.id + '/news', {
        method: 'get'
    });
    const courseElement = document.getElementById('course');
    courseElement.innerHTML = `
        <h4 class="inline text-tertiary-color br-b-tertiary">News</h4>
        <section class="container-section container-section__primary">
            <div class="posts">
            </div>
        </section>
    `;
    const json = await response.json();
    posts = JSON.parse(json);
    posts.map(post => {
        figure = createNode('figure');
        figure.classList.add('post', 'post__full');
        figure.innerHTML = `
            <a class="post-link" href="/news/${post.id}"></a>
            <img src="/static/img/${post.img_url}">
            <figcaption>
            <h4 class="blog-post-title"> ${ post.title}</h2>
                <p>${post.content_mini}</p>
            </figcaption>
        `
        append(document.querySelector('.posts'), figure);
    });
}

/***/ })

/******/ });