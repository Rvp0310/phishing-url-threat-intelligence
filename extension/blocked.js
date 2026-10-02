const params = new URLSearchParams(
    window.location.search
);

const url = params.get("url");

if (url) {
    document.getElementById("url").textContent = url;
}

const target = params.get("target");

if (target) {
    document.getElementById("target").textContent = target;
}