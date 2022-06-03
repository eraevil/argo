window.onload = function () {
    var drag = document.querySelectorAll('.controlPanel')
    for (var i = 0; i < drag.length; i++) {
        (function (j) {
            drag[j].onmousedown = function runs(e) {
                var e = e || window.event;
                var diffX = e.clientX - drag[j].offsetLeft;
                var diffY = e.clientY - drag[j].offsetTop;
                if (typeof drag.setCapture != 'undefined') {
                    drag.setCapture();
                }
                pauseEvent(e);

                function pauseEvent(e) {
                    if (e.stopPropagation) e.stopPropagation()
                    if (e.preventDefault) e.preventDefault();
                    e.cancelBubble = true;
                    e.returnValue = false;
                    return false;
                }

                document.onmousemove = function (e) {
                    var e = e || window.event;
                    var left = e.clientX - diffX;
                    var top = e.clientY - diffY;

                    if (left < 0) {
                        left = 0;
                    } else if (left > window.innerWidth - drag[j].offsetWidth) {
                        left = window.innerWidth - drag[j].offsetWidth;
                    }
                    if (top < 0) {
                        top = 0;
                    } else if (top > window.innerHeight - drag[j].offsetHeight) {
                        top = window.innerHeight - drag[j].offsetHeight;
                    }

                    drag[j].style.left = left + 'px';
                    drag[j].style.top = top + 'px';
                    if (e.preventDefault) {
                        e.preventDefault();
                    }
                };
                document.onmouseup = function (e) { //当鼠标弹起来的时候不再移动
                    this.onmousemove = null;
                    this.onmouseup = null; //预防鼠标弹起来后还会循环（即预防鼠标放上去的时候还会移动）

                    //修复低版本ie bug
                    if (typeof drag[j].releaseCapture != 'undefined') {
                        drag[j].releaseCapture();
                    }
                    sel = document.querySelectorAll('#featuretype')
                    console.log()
                    sel.orig_index = sel.style.zIndex
                };
            };
        })(i)

    }

};