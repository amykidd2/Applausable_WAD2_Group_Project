function imageSrcUpdate() {
    var parts = "{{ album.albumCover }}".split('/');
var lastSegment = parts.pop() || parts.pop();  // handle potential trailing slash
document.getElementById("myField").src = " {{MEDIA_URL }}" + "album_covers/" + lastSegment;
}


