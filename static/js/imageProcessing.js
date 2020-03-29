function imageSrcUpdate() {
    var parts = MyGlobal.var_2.split('/');
    var lastSegment = parts.pop() || parts.pop();  // handle potential trailing slash
    document.getElementById("bla").innerHTML = MyGlobal.var_1 + "album_covers/" + lastSegment;
}


