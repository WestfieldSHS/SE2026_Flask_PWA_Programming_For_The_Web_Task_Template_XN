const assets = [
  "/",
  "/explore",
  "/add.html",
  "/static/css/style.css",
  "/static/js/app.js",
  "/static/images/hero_divers.jpg",
  "/static/images/logo.png",
  "/static/images/favicon.png",
  "/static/icons/icon-128x128.png",
  "/static/icons/icon-192x192.png",
  "/static/icons/icon-384x384.png",
  "/static/icons/icon-512x512.png",
];

const CATALOGUE_ASSETS = "catalogue-assets-v2";

self.addEventListener("install", (installEvt) => {
  installEvt.waitUntil(
    caches
      .open(CATALOGUE_ASSETS)
      .then((cache) => {
        console.log("Caching assets:", cache);
        return cache.addAll(assets);
      })
      .then(() => self.skipWaiting())
      .catch((e) => {
        console.log("Cache error:", e);
      })
  );
});

self.addEventListener("activate", function (evt) {
  evt.waitUntil(
    caches
      .keys()
      .then((keyList) => {
        return Promise.all(
          keyList.map((key) => {
            if (key !== CATALOGUE_ASSETS) {
              console.log("Removed old cache:", key);
              return caches.delete(key);
            }
          })
        );
      })
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", function (evt) {
  evt.respondWith(
    fetch(evt.request).catch(() => {
      return caches.open(CATALOGUE_ASSETS).then((cache) => {
        return cache.match(evt.request);
      });
    })
  );
});
