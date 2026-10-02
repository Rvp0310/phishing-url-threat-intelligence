let urlTargets = {};

fetch(chrome.runtime.getURL("url_targets.json"))
    .then(response => response.json())
    .then(data => {
        urlTargets = data;
        console.log("Target mapping loaded.");
    });

chrome.webNavigation.onBeforeNavigate.addListener(async (details) => {

    if (details.frameId !== 0) {
        return;
    }

    const url = details.url;

    try {
        const response = await fetch(
            "http://127.0.0.1:5000/check?url=" +
            encodeURIComponent(url)
        );

        const result = await response.json();

        if (result.phishing) {

            console.log("Phishing URL detected:", url);

            const target = urlTargets[url] || "Unknown";

            chrome.tabs.update(details.tabId, {
                url: chrome.runtime.getURL(
                    "blocked.html?url=" +
                    encodeURIComponent(url) +
                    "&target=" +
                    encodeURIComponent(target)
                )
            });
        }

    } catch (error) {
        console.error(
            "Could not connect to phishing detector:",
            error
        );
    }
});