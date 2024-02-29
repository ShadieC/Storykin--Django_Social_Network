function MouseWheelHandler(e, element) {
    var delta = 0;
    if (typeof e === 'number') {
        delta = e;
    } else {
        if (e.deltaX !== 0) {
            delta = e.deltaX;
        } else {
            delta = e.deltaY;
        }
        e.preventDefault();
    }

    element.scrollLeft -= (delta);

}

window.onload = function() {
    var carousel = {};
    carousel.e = document.getElementById('carousel');
    carousel.items = document.getElementById('carousel-items');
    carousel.leftScroll = document.getElementById('left-scroll-buttom');
    carousel.rightScroll = document.getElementById('right-scroll-buttom');

    carousel.items.addEventListener("mousewheel", handleMouse, false);
    carousel.items.addEventListener("scroll", scrollEvent);
    carousel.leftScroll.addEventListener("click", leftScrollClick);
    carousel.rightScroll.addEventListener("click", rightScrollClick);
    /* carousel.leftScroll.addEventListener("mousedown", leftScrollClick);
     carousel.rightScroll.addEventListener("mousedown", rightScrollClick);*/

    setLeftScrollOpacity();
    setRightScrollOpacity();

    function handleMouse(e) {
        MouseWheelHandler(e, carousel.items);
    }

    function leftScrollClick() {
        MouseWheelHandler(100, carousel.items);
    }

    function rightScrollClick() {
        MouseWheelHandler(-100, carousel.items);
    }

    function scrollEvent(e) {
        setLeftScrollOpacity();
        setRightScrollOpacity();
    }

    function setLeftScrollOpacity() {
        if (isScrolledAllLeft()) {
            carousel.leftScroll.style.opacity = 0;
        } else {
            carousel.leftScroll.style.opacity = 1;
        }
    }

    function isScrolledAllLeft() {
        if (carousel.items.scrollLeft === 0) {
            return true;
        } else {
            return false;
        }
    }

    function isScrolledAllRight() {
        if (carousel.items.scrollWidth > carousel.items.offsetWidth) {
            if (carousel.items.scrollLeft + carousel.items.offsetWidth === carousel.items.scrollWidth) {
                return true;
            }
        } else {
            return true;
        }

        return false;
    }

    function setRightScrollOpacity() {
        if (isScrolledAllRight()) {
            carousel.rightScroll.style.opacity = 0;
        } else {
            carousel.rightScroll.style.opacity = 1;
        }
    }
}
