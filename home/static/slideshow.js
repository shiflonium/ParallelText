var interval = 5000;
var imgDir = "../static/";
var imgNum = 0;

imgArray = new Array();
imgArray[imgNum++] = new imageItem(imgDir + "slide_04.png");
imgArray[imgNum++] = new imageItem(imgDir + "slide_02.png");
imgArray[imgNum++] = new imageItem(imgDir + "slide_03.png");
imgArray[imgNum++] = new imageItem(imgDir + "slide_04.png");
imgArray[imgNum++] = new imageItem(imgDir + "slide_05.png");

var totalimg = imgArray.length;

function imageItem(img_loc) {
	this.img_item = new Image();
	this.img_item.src = img_loc;
}

function get_imgItemLoc(imgObj) {
	return(imgObj.img_item.src)
}

function getNextImage() {
    imgNum = (imgNum+1) % totalimg;
    var new_img = get_imgItemLoc(imgArray[imgNum]);
    return(new_img);
}

function getPrevImage() {
    if(imgNum == 0)
        imgNum = totalimg-1;
    else
	    imgNum = (imgNum-1) % totalimg;

	var new_img = get_imgItemLoc(imgArray[imgNum]);
	return(new_img);
}

function prevImage(place) {
	var new_img = getPrevImage();
	document[place].src = new_img;
	timerID = setTimeout(recur_call, interval);
}

function nextImage(place) {
	var new_img = getNextImage();
	document[place].src = new_img;
	var recur_call = "nextImage('"+place+"')";
	timerID = setTimeout(recur_call, interval);
}

function playImage(place) {
	var recur_call = "nextImage('"+place+"')";
	timerID = setTimeout(recur_call, interval);
}

