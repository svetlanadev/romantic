var win, body;
$(function() {
    win = $(window);
    bodyHtml = $('body, html');
    handleNewsScrolling();
    handleGovernmentScrolling()
    handleGoTop();
});

function handleNewsScrolling() {
    var newsScroller = new ScrolledLine({
        element: $('#mainpage-news .scrolled-line'),
        oneItemWidth: 330,
        itemRightMargin: 40
    });
}

function handleGovernmentScrolling() {
    var governmentScroller = new ScrolledLine({
        element: $('#government .scrolled-line'),
        oneItemWidth: 292,
        itemRightMargin: 2
    });
}

function handleGoTop() {
    var goTopBtn = $('#goTop');
    var showBtn = false;
    updateGoTopBtnShow();
    win.scroll(function(e) {
        updateGoTopBtnShow();
    });

    function updateGoTopBtnShow() {
        var prevShowBtn = showBtn;
        showBtn = win.scrollTop() > win.height() * 2;
        if (prevShowBtn !== showBtn) {
            goTopBtn.toggle(showBtn);
        }
    }
    goTopBtn.click(function() {
        bodyHtml.animate({
            scrollTop: 0
        }, 'fast');
    });
}

function ScrolledLine(options) {
    var self = this;
    this.scrolledAreaEl = options.element.find('.scrolled-area');
    this.viewportEl = options.element.find('.viewport');
    this.nextBtnEl = options.element.find('.next-btn');
    this.prevBtnEl = options.element.find('.prev-btn');
    this.oneItemWidth = options.oneItemWidth;
    this.itemRightMargin = options.itemRightMargin;
    this.disableClass = options.disableClass || 'disabled';
    this.itemsCount = this.scrolledAreaEl.find('li').length;
    this.allItemsWidth = this.itemsCount * this.oneItemWidth;
    this.scrollPos = 0;
    this.maxScrollPos = 0;
    this.lastScrollPos = 0;
    this.handleResize();
    win.resize(function() {
        self.handleResize();
    });
    this.prevBtnEl.click(function() {
        if (self.isEnable(self.prevBtnEl)) {
            self.scroll('prev');
        }
    });
    this.nextBtnEl.click(function() {
        if (self.isEnable(self.nextBtnEl)) {
            self.scroll('next');
        }
    });
}
ScrolledLine.prototype.handleResize = function(direction) {
    var viewportWidth = this.viewportEl.width();
    this.maxScrollPos = this.allItemsWidth - this.itemRightMargin - viewportWidth;
    this.lastScrollPos = this.getLastScrollPos(this.maxScrollPos, this.oneItemWidth);
    this.updateScroll();
    this.updateArrows();
}
ScrolledLine.prototype.scroll = function(direction) {
    if (direction === 'next') {
        this.scrollPos += this.oneItemWidth;
    } else if (direction === 'prev') {
        this.scrollPos -= this.oneItemWidth;
    }
    this.updateScroll();
    this.updateArrows();
}
ScrolledLine.prototype.isEnable = function(element) {
    return !element.hasClass(this.disableClass);
}
ScrolledLine.prototype.updateArrows = function() {
    this.nextBtnEl.toggleClass(this.disableClass, (this.scrollPos >= this.maxScrollPos));
    this.prevBtnEl.toggleClass(this.disableClass, (this.scrollPos <= 0));
}
ScrolledLine.prototype.updateScroll = function() {
    var leftPos;
    if (this.scrollPos > this.maxScrollPos) {
        leftPos = this.maxScrollPos;
        this.scrollPos = this.lastScrollPos;
    } else {
        leftPos = this.scrollPos;
    }
    this.scrolledAreaEl.css('left', -leftPos + 'px');
}
ScrolledLine.prototype.getLastScrollPos = function(maxSrcoll, itemW) {
    var maxNumOfScrolledItems = (maxSrcoll - maxSrcoll % itemW) / itemW;
    return (maxNumOfScrolledItems + 1) * itemW;
}