const CryptoJS = require('crypto-js');


function encryptAES(IdVal) {
	return CryptoJS.AES.encrypt(IdVal, "lzYW5qaXVqa").toString();
}
console.log(encryptAES("123"))





