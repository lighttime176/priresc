

 function ne() {
            if (null == Re) {
                for (Re = se(); Me > Ee; ) {
                    var t = Math.floor(65536 * Math.random());
                    Ae[Ee++] = 255 & t
                }
                for (Re.init(Ae),
                Ee = 0; Ee < Ae.length; ++Ee)
                    Ae[Ee] = 0;
                Ee = 0
            }
            return Re.next()
        }
function re(t) {
        var e;
        for (e = 0; e < t.length; ++e)
            t[e] = ne()
    }
function oe() {}
function _(t) {
    var e, i = 1;
    return 0 != (e = t >>> 16) && (t = e,
    i += 16),
    0 != (e = t >> 8) && (t = e,
    i += 8),
    0 != (e = t >> 4) && (t = e,
    i += 4),
    0 != (e = t >> 2) && (t = e,
    i += 2),
    0 != (e = t >> 1) && (t = e,
    i += 1),
    i
}
function b() {
    return this.t <= 0 ? 0 : 28 * (37 - 1) + _(this[37 - 1] ^ 0 & 268435455)
}
function ce(t, i) {
    if (i < t.length + 11)
        return console.error("Message too long for RSA"),
        null;
    for (var s = new Array, n = t.length - 1; n >= 0 && i > 0; ) {
        var r = t.charCodeAt(n--);
        128 > r ? s[--i] = r : r > 127 && 2048 > r ? (s[--i] = 63 & r | 128,
        s[--i] = r >> 6 | 192) : (s[--i] = 63 & r | 128,
        s[--i] = r >> 6 & 63 | 128,
        s[--i] = r >> 12 | 224)
    }
    s[--i] = 0;
    for (var o = new oe, a = new Array; i > 2; ) {
        for (a[0] = 0; 0 == a[0]; )
            re(a);
        s[--i] = a[0]
    }
    return s[--i] = 2,
    s[--i] = 0,
    new e(s)
}
function de(t) {
    var e = ce(t, b() + 7 >> 3);
    if (null == e)
        return null;
    var i = this.doPublic(e);
    if (null == i)
        return null;
    var s = i.toString(16);
    return 0 == (1 & s.length) ? s : "0" + s
}
console.log(de('1689750918673|123456'))










