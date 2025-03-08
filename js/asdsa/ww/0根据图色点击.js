

requestScreenCapture();
var jietu =captureScreen("/storage/emulated/0/脚本/pic/首页" + ".jpg");
//toastLog("截屏完成"); 

// var src = images.read("/storage/emulated/0/脚本/pic/首页.jpg");//读取图片
// var clip = images.clip(src, 339, 158,442-339,231-158);//剪切图片
// images.save(clip, "/storage/emulated/0/脚本/pic/首页_clip.jpg"); //保存图片
// toastLog("clip ok");

var img_small = images.read("/storage/emulated/0/脚本/pic/首页_clip.jpg");//读取图片
var img_big = images.read("/storage/emulated/0/脚本/pic/首页.jpg");
var res = findImage(img_big, img_small);//在 大图片 中查找 小图片 的位置（模块匹配），找到时返回位置坐标(Point)，找不到时返回null。
if (res) {
  toastLog("找到了，坐标：" + res.x + "----" + res.y);
  click(1046,1875);//点击坐标
}
else {
  toastLog("未找到");
}
