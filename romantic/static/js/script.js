var win, body;

$(function(){
	win = $(window);
	body = $('body');
	
	handleNewsScrolling();
	handleGoTop();
});


function handleNewsScrolling(){
	var newsArea = $('#news-area'),
		newsView = $('#mainpage-news .columns')
		leftArrow = $('#news-left-arrow'),
		rightArrow = $('#news-right-arrow'),
		oneNewWidth = 330,
		newRightMargin = 20,
		leftNewNum = 0,
		newsCount = 5,
		newsOnScreen = 3,
		maxLeftNewNum = 2,
		minLeftNewNum = 0,
		disableClass = 'disabled';

	recountAccordingToViewSize();
	win.resize(function(){
		recountAccordingToViewSize();
	});

	leftArrow.click(function () {
		if( isEnable(leftArrow) ){
			scrollNews('left');
		}
	});

	rightArrow.click(function () {
		if( isEnable(rightArrow) ){
			scrollNews('right');
		}
	});

	function scrollNews(direction){
		if( direction === 'right' ){
			leftNewNum++;
		} else if(direction === 'left' ) {
			leftNewNum--;
		}

		updateScrollPosition();
		updateArrows();
	}

	function isEnable(element){
		return !element.hasClass(disableClass);
	}

	function recountAccordingToViewSize(){
		newsOnScreen = Math.round( newsView.width() / oneNewWidth );
		maxLeftNewNum = newsCount - newsOnScreen;

		if(maxLeftNewNum < leftNewNum){
			leftNewNum = maxLeftNewNum;
			updateScrollPosition();
		}
		updateArrows();
	}

	function updateArrows(){
		rightArrow.toggleClass( disableClass, (leftNewNum >= maxLeftNewNum) );
		leftArrow.toggleClass( disableClass, (leftNewNum <= minLeftNewNum) );
	}

	function updateScrollPosition(){
		var leftPos = - (leftNewNum * oneNewWidth);
		newsArea.css('left', leftPos+'px');
	}

}



function handleGoTop(){
	var goTopBtn = $('#goTop');
	var showBtn = false;
	updateGoTopBtnShow();
	win.scroll(function(e){
		updateGoTopBtnShow();
	});

	function updateGoTopBtnShow(){
		var prevShowBtn = showBtn;

		showBtn = win.scrollTop() > win.height() * 2;
		if(prevShowBtn !== showBtn){
			goTopBtn.toggle(showBtn);
		}
	}

	goTopBtn.click(function(){
		body.animate({ scrollTop: 0 }, 'fast');
	});
}