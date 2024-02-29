function getTestimonialSettings(){
        return {
          dots: false,
          infinite: true,
          speed: 1000,
          autoplay:false,
          loop:true,
          arrows: false,
          touchMove:true,
          slidesToShow: 1,
          slidesToScroll: 1,
          responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                infinite: true,
                dots: false,
                arrow:false
              }
            },
            {
              breakpoint: 600,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows:false
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows:false,
              }
            }
          ]
        }
    };

function getNewsSettings(){
        return {
          centerMode: true,
          centerPadding: '10px',
          infinite: true,
          speed: 1000,
          autoplay:true,
          loop:true,
          arrows: false,
          touchMove:true,
          slidesToShow: 1,
          responsive: [
            {
              breakpoint: 575,
              settings: {
                centerMode: true,
                centerPadding: '2px',
                slidesToShow: 1,
                arrows:false,
              }
            }
          ]
        }
    };

function getSliderSettings(){
        return {
            speed: 500,
            slidesToShow: 4,
            slidesToScroll: 4,
            dots:true,
            arrows:false,
            infinite: false,
            touchMove:true,
            responsive: [
              {
                breakpoint: 1300,
                settings: {
                  slidesToShow: 3,
                  slidesToScroll: 3,
                  infinite: true,
                  dots: true
                }
              },
              {
                breakpoint: 1029,
                settings: {
                  slidesToShow: 2,
                  slidesToScroll: 2
                }
              },
                         {
             breakpoint: 480,
             settings: {
               slidesToShow: 1,
               slidesToScroll: 1
             }
           }
            ]
        }
    };

function getVideoSliderSettings(){
        return {
            speed: 500,
            slidesToShow: 3,
            slidesToScroll: 3,
            dots:true,
            arrows:false,
            infinite: false,
            touchMove:true,
            responsive: [
              {
                breakpoint: 1024,
                settings: {
                  slidesToShow: 3,
                  slidesToScroll: 3,
                  infinite: true,
                  dots: true
                }
              },
              {
                breakpoint: 800,
                settings: {
                  slidesToShow: 2,
                  slidesToScroll: 2
                }
              },
              {
                breakpoint: 480,
                settings: {
                  slidesToShow: 1,
                  slidesToScroll: 1
                }
              }
              // You can unslick at a given breakpoint now by adding:
              // settings: "unslick"
              // instead of a settings object

            ]
        }
    };

function getFeatureSettings(){
        return {
            speed: 500,
            slidesToShow: 4,
            slidesToScroll: 4,
            dots:true,
            arrows:false,
            infinite: true,
            touchMove:true,
            responsive: [
              {
                breakpoint: 3000,
                settings: {
                  slidesToShow: 4,
                  slidesToScroll: 4,
                  infinite: true,
                  dots: true
                }
              },
              {
                breakpoint: 1024,
                settings: {
                  slidesToShow: 4,
                  slidesToScroll: 4,
                  infinite: true,
                  dots: true
                }
              },
              {
                breakpoint: 600,
                settings: {
                  slidesToShow: 2,
                  slidesToScroll: 2
                }
              },
              {
                breakpoint: 480,
                settings: {
                  slidesToShow: 1,
                  slidesToScroll: 1
                }
              }
            ]
        }
    };

function getMustReadsSettings(){
        return {
            speed: 500,
            slidesToShow: 4,
            slidesToScroll: 4,
            dots:true,
            arrows:false,
            infinite: false,
            touchMove:true,
            responsive: [
              {
                breakpoint: 1024,
                settings: {
                  slidesToShow: 3,
                  slidesToScroll: 3,
                  infinite: true,
                  dots: true
                }
              },
              {
                breakpoint: 800,
                settings: {
                  slidesToShow: 2,
                  slidesToScroll: 2
                }
              },
              {
                breakpoint: 480,
                settings: {
                  slidesToShow: 1,
                  slidesToScroll: 1
                }
              }
            ]
        }
    };

function SliderControls(){
  $('.books-prev').click(function(e){ 
    e.preventDefault(); 
    $('.slider').slick('slickPrev');
  } );
  
  $('.books-next').click(function(e){
    e.preventDefault(); 
    $('.slider').slick('slickNext');
  });

  //Video Slider
  $('.videos-prev').click(function(e){ 
    e.preventDefault(); 
    $('.video-slider').slick('slickPrev');
  } );
  
  $('.videos-next').click(function(e){
    e.preventDefault(); 
    $('.video-slider').slick('slickNext');
  });
}; 

function fixCategoriesBlurry() {
    const element = document.getElementById('categories');

    if (element.scrollWidth >= element.clientWidth ) {
        $(".blurry-prev").addClass("dissapear");
        element.addEventListener("scroll", function(){
            const position = document.getElementById('categories').scrollLeft;
            if (position < 0.5 ) {
                $(".blurry-prev").addClass("dissapear");
            } else if ( element.scrollWidth - element.clientWidth == Math.ceil(element.scrollLeft) )  {
                $(".blurry-next").addClass("dissapear");
            } else {
                $(".blurry-prev").removeClass("dissapear");
                $(".blurry-next").removeClass("dissapear");
            }
        });

    } else {
        $(".blurry-next").addClass("dissapear");
        $(".blurry-prev").addClass("dissapear");
    }
};

function fixLifeCategoriesBlurry() {
    const element = document.querySelector("#lifecategories");

    if (element.scrollWidth >= element.clientWidth ) {
        $(".life-prev").addClass("dissapear");
        element.addEventListener("scroll", function(){
            const position = document.getElementById('lifecategories').scrollLeft;
            if (position < 0.5 ) {
                $(".life-prev").addClass("dissapear");
            } else if ( element.scrollWidth - element.clientWidth == Math.ceil(element.scrollLeft) )  {
                $(".life-next").addClass("dissapear");
            } else {
                $(".life-prev").removeClass("dissapear");
                $(".life-next").removeClass("dissapear");
            }
        });

    } else {
        $(".life-next").addClass("dissapear");
        $(".life-prev").addClass("dissapear");
    }
};

function fixSearchCategoriesBlurry() {
    const element = document.querySelector("#searchcategories");

    if (element.scrollWidth > element.clientWidth ) {
        $(".mysearch-prev").addClass("dissapear");
        element.addEventListener("scroll", function(){
            const position = document.getElementById('searchcategories').scrollLeft;
            if (position < 0.5 ) {
                $(".mysearch-prev").addClass("dissapear");
                $(".mysearch-next").removeClass("dissapear");
            } else if ( element.scrollWidth - element.clientWidth == Math.ceil(element.scrollLeft) )  {
                $(".mysearch-next").addClass("dissapear");
                $(".mysearch-prev").removeClass("dissapear");
            } else {
                $(".mysearch-prev").removeClass("dissapear");
                $(".mysearch-next").removeClass("dissapear");
            }
        });

    } else {
        $(".mysearch-next").addClass("dissapear");
        $(".mysearch-prev").addClass("dissapear");
    }
};
 
function fixTrendingArticlesBlurry() {   
    const element = document.querySelector("#home_article_list");

    if (element.scrollWidth > element.clientWidth ) {
        $(".ta-before").addClass("remove");
        element.addEventListener("scroll", function(){
            const position = document.getElementById('home_article_list').scrollLeft;
            if (position < 0.5 ) {
                $(".ta-before").addClass("remove");
            } else if ( element.scrollWidth - element.clientWidth == Math.ceil(element.scrollLeft) )  {
                $(".ta-after").addClass("remove");
            } else {
                $(".ta-before").removeClass("remove");
                $(".ta-after").removeClass("remove");
            }
        });

    } else {
        $(".ta-after").addClass("remove");
        $(".ta-before").addClass("remove");
    }
};

function fixLifeArticlesBlurry(id) {   
    const element = document.getElementById(id);

    if (element.scrollWidth > element.clientWidth ) {
        $(".la-before").addClass("remove");
        element.addEventListener("scroll", function(){
            const position = document.getElementById(id).scrollLeft;
            if (position < 0.5 ) {
                $(".la-before").addClass("remove");
            } else if ( element.scrollWidth - element.clientWidth == Math.ceil(element.scrollLeft) )  {
                $(".la-after").addClass("remove");
            } else {
                $(".la-before").removeClass("remove");
                $(".la-after").removeClass("remove");
            }
        });

    } else {
        $(".la-after").addClass("remove");
        $(".la-before").addClass("remove");
    }
};

function fixListingArticlesBlurry() {   
    const element = document.querySelector("#listing_article_list");

    if (element.scrollWidth > element.clientWidth ) {
        $(".lta-before").addClass("remove");
        element.addEventListener("scroll", function(){
            const position = document.getElementById('listing_article_list').scrollLeft;
            if (position < 0.5 ) {
                $(".lta-before").addClass("remove");
            } else if ( element.scrollWidth - element.clientWidth == Math.ceil(element.scrollLeft) )  {
                $(".lta-after").addClass("remove");
            } else {
                $(".lta-before").removeClass("remove");
                $(".lta-after").removeClass("remove");
            }
        });

    } else {
        $(".lta-after").addClass("remove");
        $(".lta-before").addClass("remove");
    }
};

function scrollCategories() {
    const buttonRight = document.getElementById('slideRight');
    const buttonLeft = document.getElementById('slideLeft');
    const element = document.getElementById('categories');
    var spaceLeft = -(Math.ceil(element.scrollLeft) - element.scrollWidth + element.clientWidth);
    spaceLeft = parseInt( spaceLeft );
    
    buttonRight.onclick = function () {
        if (spaceLeft < 200){
            element.scrollLeft += spaceLeft;
        } else {
            element.scrollLeft += 200;
        }
    };
    buttonLeft.onclick = function () {
        if (element.scrollLeft < 200){
            element.scrollLeft -= element.scrollLeft;
        } else {
            element.scrollLeft -= 200;
        }
    };
};

function scrollLifeCategories() {
    const buttonRight = document.getElementById('lifeslideRight');
    const buttonLeft = document.getElementById('lifeslideLeft');
    const element = document.getElementById('lifecategories');
    var spaceLeft = -(Math.ceil(element.scrollLeft) - element.scrollWidth + element.clientWidth);
    spaceLeft = parseInt( spaceLeft );
    
    buttonRight.onclick = function () {
        if (spaceLeft < 200){
            element.scrollLeft += spaceLeft;
        } else {
            element.scrollLeft += 200;
        }
    };
    buttonLeft.onclick = function () {
        if (element.scrollLeft < 200){
            element.scrollLeft -= element.scrollLeft;
        } else {
            element.scrollLeft -= 200;
        }
    };
};

function scrollSearchCategories() {
    const buttonRight = document.getElementById('searchslideRight');
    const buttonLeft = document.getElementById('searchslideLeft');
    const element = document.getElementById('searchcategories');
    var spaceLeft = -(Math.ceil(element.scrollLeft) - element.scrollWidth + element.clientWidth);
    spaceLeft = parseInt( spaceLeft );
    
    buttonRight.onclick = function () {
        if (spaceLeft < 200){
            element.scrollLeft += spaceLeft;
        } else {
            element.scrollLeft += 200;
        }
    };
    buttonLeft.onclick = function () {
        if (element.scrollLeft < 200){
            element.scrollLeft -= element.scrollLeft;
        } else {
            element.scrollLeft -= 200;
        }
    };
};

function ExchangeCategoriesBlurry() {
    if (window.innerWidth >= 940) {
        if($("#right").length){
            document.getElementById('categories').id = 'left';
            document.getElementById('slideLeft').id = 'left_slideLeft' ;
            document.getElementById('slideRight').id = 'left_slideRight' ;
            document.getElementById('left_slideLeft').classList.remove("blurry-prev");
            document.getElementById('left_slideRight').classList.remove("blurry-next");
            document.getElementById('left_slideLeft').classList.remove("dissapear");
            document.getElementById('left_slideRight').classList.remove("dissapear");



            document.getElementById('right').id = 'categories' ;
            document.getElementById('right_slideLeft').id = 'slideLeft' ;
            document.getElementById('right_slideRight').id = 'slideRight' ;
            document.getElementById('slideLeft').classList.add("blurry-prev");
            document.getElementById('slideRight').classList.add("blurry-next");

            fixCategoriesBlurry();
            scrollCategories();
        }

    } else {

        if($("#left").length){
            document.getElementById('categories').id = 'right';
            document.getElementById('slideLeft').id = 'right_slideLeft' ;
            document.getElementById('slideRight').id = 'right_slideRight' ;
            document.getElementById('right_slideLeft').classList.remove("blurry-prev");
            document.getElementById('right_slideRight').classList.remove("blurry-next");
            document.getElementById('right_slideLeft').classList.remove("dissapear");
            document.getElementById('right_slideRight').classList.remove("dissapear");



            document.getElementById('left').id = 'categories' ;
            document.getElementById('left_slideLeft').id = 'slideLeft' ;
            document.getElementById('left_slideRight').id = 'slideRight' ;
            document.getElementById('slideLeft').classList.add("blurry-prev");
            document.getElementById('slideRight').classList.add("blurry-next");

            fixCategoriesBlurry();
            scrollCategories();
        }

    }
};

function ExchangeLifeCategoriesBlurry() {
    if (window.innerWidth >= 940) {
        if($("#liferight").length){
            document.getElementById('Phases_Heading_Two').style.display ="flex";
            document.getElementById('lifecategories').id = 'lifeleft';
            document.getElementById('lifeslideLeft').id = 'life_left_slideLeft' ;
            document.getElementById('lifeslideRight').id = 'life_left_slideRight' ;
            document.getElementById('life_left_slideLeft').classList.remove("life-prev");
            document.getElementById('life_left_slideRight').classList.remove("life-next");
            document.getElementById('life_left_slideLeft').classList.remove("blurry-prev");
            document.getElementById('life_left_slideRight').classList.remove("blurry-next");
            document.getElementById('life_left_slideLeft').classList.remove("dissapear");
            document.getElementById('life_left_slideRight').classList.remove("dissapear");

            document.getElementById('liferight').id = 'lifecategories' ;
            document.getElementById('life_right_slideLeft').id = 'lifeslideLeft' ;
            document.getElementById('life_right_slideRight').id = 'lifeslideRight' ;
            document.getElementById('lifeslideLeft').classList.add("life-prev");
            document.getElementById('lifeslideRight').classList.add("life-next");
            document.getElementById('lifeslideLeft').classList.add("blurry-prev");
            document.getElementById('lifeslideRight').classList.add("blurry-next");

            scrollLifeCategories();
            fixLifeCategoriesBlurry();
        } 

    } else {

        if($("#lifeleft").length){
            document.getElementById('lifecategories').id = 'liferight';
            document.getElementById('lifeslideLeft').id = 'life_right_slideLeft' ;
            document.getElementById('lifeslideRight').id = 'life_right_slideRight' ;
            document.getElementById('life_right_slideLeft').classList.remove("life-prev");
            document.getElementById('life_right_slideRight').classList.remove("life-next");
            document.getElementById('life_right_slideLeft').classList.remove("blurry-prev");
            document.getElementById('life_right_slideRight').classList.remove("blurry-next");
            document.getElementById('life_right_slideLeft').classList.remove("dissapear");
            document.getElementById('life_right_slideRight').classList.remove("dissapear");

            document.getElementById('lifeleft').id = 'lifecategories' ;
            document.getElementById('life_left_slideLeft').id = 'lifeslideLeft' ;
            document.getElementById('life_left_slideRight').id = 'lifeslideRight' ;
            document.getElementById('lifeslideLeft').classList.add("life-prev");
            document.getElementById('lifeslideRight').classList.add("life-next");
            document.getElementById('lifeslideLeft').classList.add("blurry-prev");
            document.getElementById('lifeslideRight').classList.add("blurry-next");

            scrollLifeCategories();
            fixLifeCategoriesBlurry();
        }

    }
};

function clear() {
    const menu = document.querySelector("#option");
    menu.style.visibility = "hidden";
    menu.style.top =  "0px";
    menu.style.left = "0px";
    $(".current-more").removeClass("current-more");
    if($(".modal_option").length){
        const modalOption = document.querySelector(".modal_option");
        modalOption.style.display = 'none';
        modalOption.style.top =  "0px";
        modalOption.style.left = "0px";
    }
    const user_details = document.querySelector(".user-details");
    const username_icon = document.querySelector(".username-icon");

    if($(".username-icon").length){  
        if (user_details.classList.contains("open")) {
            user_details.classList.remove('open');
        }     
    }

    const notify = document.querySelector(".notify");
    const notify_icon = document.querySelector(".notify_icon");

    if($(".notify_icon").length){      
        if (notify.classList.contains("open")) {
            notify.classList.remove("open");
        } 
    }
};

function notifications() {
    clear();
    const notify = document.querySelector(".notify");
    const notify_icon = document.querySelector(".notify_icon");

    if($(".notify_icon").length){      
        if (notify.classList.contains("open")) {
            
        } else {
           notify.classList.add('open'); 
        }
    }
};

function searchBar() {
    if (window.innerWidth > 575) {
        $(".search-bar").removeClass("dissapear");
    } else {
        $(".search-bar").addClass("dissapear");
    }
};

var isReading = false;
var textread = ''

function readAloud(post) {
    var postText = document.getElementById(post).textContent;

    if (!isReading) {
        responsiveVoice.speak(postText, 'US English Male');
        isReading = true;
        textread = postText
    } else {
        if (textread == postText) {
            responsiveVoice.pause();
            isReading = false;
            textread = ''
        } else {
            responsiveVoice.pause();
            responsiveVoice.speak(postText, 'US English Male');
            isReading = true;
            textread = postText 
        }
    }
}

$(function () {
    $(".sidebar-link").click(function () {
        $(".sidebar-link").removeClass("is-active");
        $(this).addClass("is-active");
    });
});


$(window).resize(function () {
    if (window.innerWidth > 1090) {
       $(".sidebar").removeClass("sb-collapse");
    } else {
       $(".sidebar").addClass("sb-collapse");
    }

    if (window.innerWidth > 575) {
        $(".user-settings").removeClass("dissapear");
        $(".search-bar").removeClass("dissapear");
    } else {
        const wrapper = document.querySelector(".wrapper");
        if ($(".wrapper").length){
            if (wrapper.classList.contains("full-screen-search")) {
                $(".user-settings").addClass("dissapear");  
                $(".search-bar").removeClass("dissapear");
            } else {
                $(".search-bar").addClass("dissapear");
            }
        }
    }

    if ($(".show-emotions").length){
        ExchangeCategoriesBlurry();
    }

    if ($(".search-main").length){;
    const element = document.getElementById('searchcategories');
        if (element.scrollWidth > element.clientWidth ) {
            $(".mysearch-prev").addClass("dissapear");
            const position = document.getElementById('searchcategories').scrollLeft;
            if (position < 0.5 ) {
                $(".mysearch-prev").addClass("dissapear");
                $(".mysearch-next").removeClass("dissapear");
            } else if ( element.scrollWidth - element.clientWidth == Math.ceil(element.scrollLeft) )  {
                $(".mysearch-next").addClass("dissapear");
                $(".mysearch-prev").removeClass("dissapear");
            } else {
                $(".mysearch-prev").removeClass("dissapear");
                $(".mysearch-next").removeClass("dissapear");
            }
        } else {
            $(".mysearch-next").addClass("dissapear");
            $(".mysearch-prev").addClass("dissapear");
        }
    }

    if ($(".show-phases").length){
        ExchangeLifeCategoriesBlurry();
    }

}).resize();

const allVideos = document.querySelectorAll(".video");

allVideos.forEach((v) => {
    v.addEventListener("mouseover", () => {
        const video = v.querySelector("video");
        video.play();
    });
    v.addEventListener("mouseleave", () => {
        const video = v.querySelector("video");
        video.pause();
    });
});

function hideNotification() {
    var notiBar = document.getElementById("notification");
    notiBar.classList.remove("animation");
    void notiBar.offsetHeight;
}

function showNotification(text) {
    var notiBar = document.getElementById("notification");
    notiBar.innerHTML = text;
    notiBar.classList.add("animation");
    setTimeout(hideNotification, 9000);
}

function copyToClipboard(input) {
    navigator.permissions.query({ name: "clipboard-read" }).then((result) => {
        if (result.state == "granted" || result.state == "prompt") {
            var copyText = document.getElementById(input);
            navigator.clipboard.writeText(copyText.value).then(() => {
                // Alert the user that the action took place
                clear();
                showNotification("Copied to clipboard");
            });
        } else {
            var text = document.getElementById(input).value;
            if (window.clipboardData && window.clipboardData.setData) {
                // Internet Explorer-specific code path to prevent textarea being shown while dialog is visible.
                return window.clipboardData.setData("Text", text);
                showNotification("Copied to clipboard");
            }
            else if (document.queryCommandSupported && document.queryCommandSupported("copy")) {
                var textarea = document.createElement("textarea");
                textarea.textContent = text;
                textarea.style.position = "fixed";  // Prevent scrolling to bottom of page in Microsoft Edge.
                document.body.appendChild(textarea);
                textarea.select();
                try {
                    return document.execCommand("copy");  // Security exception may be thrown by some browsers.
                }
                catch (ex) {
                    console.warn("Copy to clipboard failed.", ex);
                    return prompt("Copy to clipboard: Ctrl+C, Enter", text);
                }
                finally {
                    document.body.removeChild(textarea);
                    showNotification("Copied to clipboard");
                }
            }
        }
    });
}

























