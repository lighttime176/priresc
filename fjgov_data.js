const CryptoJS = require('crypto-js');


Data = "MZphJmFlelDpw2aSCfdFb/P3tx6u8VHU/M7MqPRS6y6RaH/5IbXivLEiR9o33DJkTcSPLypQCFpPR82kvps4XAS/QiDAsPVBMK4HU3LUuLyxQLn42XoQKtsRU3nLrOppUcsUCaY8vfPxRtOB4RmS8utPv1yghJtEXPzFsqCxHdcMCUo/o0DpzF5NzSMvlvmYDctx2SVncj3BldMoJn2SZLwPyk2NghU08KyffZyPMaiTmaAeX42LAu8//RhilPgFkR4WUfSd2JSf5WLW1LG0xNJQXx0V1mwtdekmdeH1VkFuapV7vq+eUWCydb4g4fzb+gAwJL8FCmRzBol9j8tdr3ikRFVEttwRl9PG7/ihq/YjCAvWr4S4BAHs4ZRtfo3RMCYFHi+jPkAJWSDArZGriI069tqw9zN04c5G6N4DVQSHwOvm0/JnTWjrIJ/7YTGM+e6lE0DCglS3dHuwxQEGYp3tfxIqnuEMZglV+8rpeVwPoZcWzE3A+0zqJ1ypmhsLk6ZKqpp1jnwvnzCyc3XEvvNlC++1BOPDxaBjjWc94/mcXO37RwjEVQx/h6sCIRJzo9Qwpe2emcsK/ZvAN2433cXPrdZXn1RTWnYkI/NfUMAfib+W54hkccA1krMstvc3oahDlYhOlTlv2OmGoknLoBaWnXiU3Dv51apgdZ4XBpBfN4HOzY12/zq4cnd1u319dBu0fRETiadFXqAUE9nRbmqZtQ4L7/byasPdOOxOagv7nIH4bvcXpfXDqhz6CMDL9Ei+N/dyRWlt3BX/bUPQ6H9E89HbmeJqJFPXZ1HeSHR2Ijl601S2B03lYQcrysSwWh8kzM1D/0N3Dm5z1R3kxvJ5iYpjfPBZH6ozU/4F4E42z1BInZRHViDc79MM6yNB433MMaAl5jsQBSDy33gBwlmx21J35xzmHdsLjmCuVstWvzWgVYOrRCD3dChIoueE"


e = {
    "ts": 1689497066771,
    "type": "12",
    "IS_IMPORT": 1,
    "pageSize": 3
}

function u(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}
function l(t) {
    for (var e = Object.keys(t).sort(u), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]]instanceof Object || t[e[a]]instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}
function md5 (text) {
    return CryptoJS.MD5(text);
}
function d(t) {
    for (var e in t)
        "" !== t[e] && void 0 !== t[e] || delete t[e];
    var n = "B3978D054A72A7002063637CCDF6B2E5" + l(t);
    return md5(n).toString().toLocaleLowerCase()
}
ls ={}
function main_1() {
    const timestamp = (new Date).getTime()
    //console.log("1:")
    console.log(timestamp)
    //console.log("2:")
    console.log(Date.now()) //1642471441587
    e['ts'] = timestamp
    portal_sig = d(e)
    console.log(portal_sig)
    ls['ts'] = timestamp
    ls['portal_sig'] = portal_sig
    return ls
}
console.log(main_1())
