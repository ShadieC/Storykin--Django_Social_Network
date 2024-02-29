function home() {
    $(".main-container").removeClass("show-emotions");
    $(".main-container").removeClass("show-profile");
    $(".main-container").removeClass("show-phases");
    $(".main-container").removeClass("show-question");
    $(".main-container").removeClass("show-forum");
    $(".main-container").removeClass("show-article");
    $(".main-container").removeClass("show-feedback");
    $(".main-container").removeClass("show-achievements");
    $(".main-container").removeClass("show-donations");
    $(".main-container").removeClass("show-search");
    $(".main-container").addClass("show-home");
    $(".main-container").scrollTop(0);
    $(".sidebar-link").removeClass("is-active");
    $(".home-button").addClass("is-active");
    $(".nav__link").removeClass("active-bn-link");
    $(".nav__link").removeClass("active-donate-link");
    $(".nav__home").addClass("active-bn-link");
    $(".header").removeClass("search-active");
    $(".header").addClass("header-shadow");
    clear();
}

function fullSearch() {
    $(".wrapper").addClass("full-screen-search");
    $(".user-settings").addClass("dissapear");
    $(".small-screen-logo").addClass("dissapear");
    $('.header').addClass('search-active');
    $(".search-bar").removeClass("dissapear");
    $(".main-container").scrollTop(0);
    clear();
}

function reversefullSearch() {
    $(".wrapper").removeClass("full-screen-search");
    $(".user-settings").removeClass("dissapear");
    $(".small-screen-logo").removeClass("dissapear");
    $('.header').removeClass('search-active');
    $(".search-bar").addClass("dissapear");
    $(".main-container").scrollTop(0);
    const mainContainer = document.querySelector(".main-container");
    if (mainContainer.classList.contains("show-search")) {
        window.history.go(-1);;
    }     
    clear();
}

function emotions() {
    $(".main-container").removeClass("show-phases");
    $(".main-container").removeClass("show-profile");
    $(".main-container").removeClass("show-donations");
    $(".main-container").removeClass("show-forum");
    $(".main-container").removeClass("show-question");
    $(".main-container").removeClass("show-article");
    $(".main-container").removeClass("show-achievements");
    $(".main-container").removeClass("show-home");
    $(".main-container").removeClass("show-feedback");
    $(".main-container").removeClass("show-search");
    $(".main-container").addClass("show-emotions");
    $(".main-container").scrollTop(0);
    $(".sidebar-link").removeClass("is-active");
    $(".emotions-button").addClass("is-active");
    $(".nav__link").removeClass("active-bn-link");
    $(".nav__link").removeClass("active-donate-link");
    $(".nav__emotions").addClass("active-bn-link");
    $(".header").removeClass("search-active");
    $(".blurry-after").removeClass("blurry-before");
    $(".header").removeClass("header-shadow");
    clear();
}

function phases() {
    $(".main-container").removeClass("show-emotions");
    $(".main-container").removeClass("show-donations");
    $(".main-container").removeClass("show-profile");
    $(".main-container").removeClass("show-article");
    $(".main-container").removeClass("show-forum");
    $(".main-container").removeClass("show-question");
    $(".main-container").removeClass("show-feedback");
    $(".main-container").removeClass("show-achievements");
    $(".main-container").removeClass("show-search");
    $(".main-container").removeClass("show-home");
    $(".main-container").addClass("show-phases");
    $(".main-container").scrollTop(0);
    $(".sidebar-link").removeClass("is-active");
    $(".phases-button").addClass("is-active");
    $(".nav__link").removeClass("active-bn-link");
    $(".nav__link").removeClass("active-donate-link");
    $(".nav__phases").addClass("active-bn-link");
    $(".header").removeClass("search-active");
    $(".header").removeClass("header-shadow");
    clear();
}

function donations() {
    $(".main-container").removeClass("show-emotions");
    $(".main-container").removeClass("show-achievements");
    $(".main-container").removeClass("show-phases");
    $(".main-container").removeClass("show-profile");
    $(".main-container").removeClass("show-forum");
    $(".main-container").removeClass("show-question");
    $(".main-container").removeClass("show-article");
    $(".main-container").removeClass("show-search");
    $(".main-container").removeClass("show-feedback");
    $(".main-container").removeClass("show-home");
    $(".main-container").addClass("show-donations");
    $(".main-container").scrollTop(0);
    $(".sidebar-link").removeClass("is-active");
    $(".donations-button").addClass("is-active");
    $(".nav__link").removeClass("active-bn-link");
    $(".nav__link").removeClass("active-donate-link");
    $(".nav__donations").addClass("active-donate-link");
    $(".header").removeClass("search-active");
    $(".header").addClass("header-shadow");
    clear();
}

function article() {
    $(".main-container").removeClass("show-emotions");
    $(".main-container").removeClass("show-achievements");
    $(".main-container").removeClass("show-phases");
    $(".main-container").removeClass("show-profile");
    $(".main-container").removeClass("show-question");
    $(".main-container").removeClass("show-donations");
    $(".main-container").removeClass("show-forum");
    $(".main-container").removeClass("show-feedback");
    $(".main-container").removeClass("show-search");
    $(".main-container").removeClass("show-home");
    $(".main-container").addClass("show-article");
    $(".main-container").scrollTop(0);
    $(".sidebar-link").removeClass("is-active");
    $(".nav__link").removeClass("active-bn-link");
    $(".nav__link").removeClass("active-donate-link");
    $(".header").removeClass("search-active");
    $(".header").addClass("header-shadow");
    clear();
}

function achievements() {
    $(".main-container").removeClass("show-emotions");
    $(".main-container").removeClass("show-phases");
    $(".main-container").removeClass("show-donations");
    $(".main-container").removeClass("show-profile");
    $(".main-container").removeClass("show-forum");
    $(".main-container").removeClass("show-feedback");
    $(".main-container").removeClass("show-question");
    $(".main-container").removeClass("show-article");
    $(".main-container").removeClass("show-search");
    $(".main-container").removeClass("show-home");
    $(".main-container").addClass("show-achievements");
    $(".main-container").scrollTop(0);
    $(".sidebar-link").removeClass("is-active");
    $(".achievements-button").addClass("is-active");
    $(".nav__link").removeClass("active-bn-link");
    $(".nav__achievements").addClass("active-bn-link");
    $(".nav__link").removeClass("active-donate-link");
    $(".header").removeClass("search-active");
    $(".header").addClass("header-shadow");
    clear();
}

function user() {
    $(".main-container").removeClass("show-emotions");
    $(".main-container").removeClass("show-article");
    $(".main-container").removeClass("show-phases");
    $(".main-container").removeClass("show-donations");
    $(".main-container").removeClass("show-forum");
    $(".main-container").removeClass("show-home");
    $(".main-container").removeClass("show-question");
    $(".main-container").removeClass("show-search");
    $(".main-container").removeClass("show-feedback");
    $(".main-container").removeClass("show-achievements");
    $(".main-container").addClass("show-profile");
    $(".main-container").scrollTop(0);
    $(".sidebar-link").removeClass("is-active");
    $(".nav__link").removeClass("active-bn-link");
    $(".nav__link").removeClass("active-donate-link");
    $(".header").removeClass("search-active");
    $(".header").removeClass("header-shadow");
    clear();
}

function forum() {
    $(".main-container").removeClass("show-emotions");
    $(".main-container").removeClass("show-achievements");
    $(".main-container").removeClass("show-phases");
    $(".main-container").removeClass("show-profile");
    $(".main-container").removeClass("show-donations");
    $(".main-container").removeClass("show-article");
    $(".main-container").removeClass("show-home");
    $(".main-container").removeClass("show-search");
    $(".main-container").removeClass("show-feedback");
    $(".main-container").removeClass("show-question");
    $(".main-container").addClass("show-forum");
    $(".main-container").scrollTop(0);
    $(".sidebar-link").removeClass("is-active");
    $(".nav__link").removeClass("active-bn-link");
    $(".nav__link").removeClass("active-donate-link");
    $(".header").removeClass("search-active");
    $(".header").removeClass("header-shadow");
    clear();
}

function question() {
    $(".main-container").removeClass("show-emotions");
    $(".main-container").removeClass("show-article");
    $(".main-container").removeClass("show-phases");
    $(".main-container").removeClass("show-donations");
    $(".main-container").removeClass("show-forum");
    $(".main-container").removeClass("show-home");
    $(".main-container").removeClass("show-achievements");
    $(".main-container").removeClass("show-profile");
    $(".main-container").removeClass("show-feedback");
    $(".main-container").addClass("show-question");
    $(".main-container").scrollTop(0);
    $(".sidebar-link").removeClass("is-active");
    $(".nav__link").removeClass("active-bn-link");
    $(".nav__link").removeClass("active-donate-link");
    $(".header").removeClass("search-active");
    $(".header").addClass("header-shadow");
    clear();
}

function search() {
    $(".main-container").removeClass("show-emotions");
    $(".main-container").removeClass("show-article");
    $(".main-container").removeClass("show-phases");
    $(".main-container").removeClass("show-donations");
    $(".main-container").removeClass("show-forum");
    $(".main-container").removeClass("show-home");
    $(".main-container").removeClass("show-achievements");
    $(".main-container").removeClass("show-profile");
    $(".main-container").removeClass("show-question");
    $(".main-container").removeClass("show-feedback");
    $(".main-container").addClass("show-search");
    $(".main-container").scrollTop(0);
    $(".sidebar-link").removeClass("is-active");
    $(".nav__link").removeClass("active-bn-link");
    $(".nav__link").removeClass("active-donate-link");
    $(".header").addClass("search-active");
    $(".header").removeClass("header-shadow");
    clear();
}

function feedback() {
    $(".main-container").removeClass("show-emotions");
    $(".main-container").removeClass("show-profile");
    $(".main-container").removeClass("show-phases");
    $(".main-container").removeClass("show-question");
    $(".main-container").removeClass("show-forum");
    $(".main-container").removeClass("show-article");
    $(".main-container").removeClass("show-achievements");
    $(".main-container").removeClass("show-donations");
    $(".main-container").removeClass("show-search");
    $(".main-container").removeClass("show-home");
    $(".main-container").addClass("show-feedback");
    $(".main-container").scrollTop(0);
    $(".sidebar-link").removeClass("is-active");
    $(".nav__link").removeClass("active-bn-link");
    $(".nav__link").removeClass("active-donate-link");
    $(".header").removeClass("search-active");
    clear();
    $(".header").addClass("header-shadow");
}