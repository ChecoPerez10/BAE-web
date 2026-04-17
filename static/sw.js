// Service Worker para JumpRush PWA
const CACHE_NAME = 'jumprush-cache-v1';
const STATIC_CACHE = 'jumprush-static-v1';
const DYNAMIC_CACHE = 'jumprush-dynamic-v1';

// Archivos a cachear en la instalacion
const STATIC_ASSETS = [
  '/',
  '/static/css/estilos.css',
  '/static/js/principal.js',
  '/static/images/jumprush_portada.jpg',
  '/static/images/escenario_bosque.jpg',
  '/static/images/escenario_desierto.jpg',
  '/static/images/escenario_ciudad.jpg',
  '/static/images/player_aventurero.jpg',
  '/static/images/player_ninja.jpg',
  '/static/images/player_robot.jpg',
  '/static/manifest.json',
  'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap'
];

// Instalacion del Service Worker
self.addEventListener('install', (event) => {
  console.log('[SW] Instalando Service Worker...');
  event.waitUntil(
    caches.open(STATIC_CACHE)
      .then((cache) => {
        console.log('[SW] Cacheando archivos estaticos');
        return cache.addAll(STATIC_ASSETS);
      })
      .then(() => self.skipWaiting())
  );
});

// Activacion del Service Worker
self.addEventListener('activate', (event) => {
  console.log('[SW] Activando Service Worker...');
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== STATIC_CACHE && name !== DYNAMIC_CACHE)
          .map((name) => {
            console.log('[SW] Eliminando cache antiguo:', name);
            return caches.delete(name);
          })
      );
    }).then(() => self.clients.claim())
  );
});

// Estrategia de cache: Cache First con fallback a Network
self.addEventListener('fetch', (event) => {
  // Ignorar peticiones a extensiones de Chrome y otros
  if (!event.request.url.startsWith('http')) return;
  
  event.respondWith(
    caches.match(event.request)
      .then((cachedResponse) => {
        if (cachedResponse) {
          // Retornar desde cache
          return cachedResponse;
        }
        
        // Hacer peticion a la red
        return fetch(event.request)
          .then((networkResponse) => {
            // No cachear si no es una respuesta valida
            if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
              return networkResponse;
            }
            
            // Clonar la respuesta para cachearla
            const responseToCache = networkResponse.clone();
            
            caches.open(DYNAMIC_CACHE)
              .then((cache) => {
                cache.put(event.request, responseToCache);
              });
            
            return networkResponse;
          })
          .catch(() => {
            // Si falla la red y es una pagina HTML, mostrar offline page
            if (event.request.headers.get('accept').includes('text/html')) {
              return caches.match('/');
            }
          });
      })
  );
});

// Escuchar mensajes del cliente
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

// Sincronizacion en background (para futuras funcionalidades)
self.addEventListener('sync', (event) => {
  console.log('[SW] Sincronizacion en background:', event.tag);
});

// Notificaciones push (para futuras funcionalidades)
self.addEventListener('push', (event) => {
  console.log('[SW] Notificacion push recibida');
  const options = {
    body: event.data ? event.data.text() : 'Nueva actualizacion de JumpRush!',
    icon: '/static/images/icon-192.png',
    badge: '/static/images/icon-72.png',
    vibrate: [100, 50, 100],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: 1
    }
  };
  
  event.waitUntil(
    self.registration.showNotification('JumpRush', options)
  );
});
