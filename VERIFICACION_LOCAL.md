# ✅ VERIFICACIÓN LOCAL - INSTRUCCIONES

## 🧪 CÓMO PROBAR EN LOCAL

### Opción 1: Python HTTP Server (RECOMENDADO)
```bash
# En la terminal, desde la carpeta del proyecto:
python -m http.server 8000

# Luego abre en el navegador:
# http://localhost:8000
```

### Opción 2: Node.js HTTP Server
```bash
# Si tienes Node.js:
npx http-server -p 8000

# Luego abre:
# http://localhost:8000
```

### Opción 3: VS Code Live Server
- Instala extensión "Live Server"
- Click derecho en `index.html` → "Open with Live Server"

## ✅ CHECKLIST DE VERIFICACIÓN

### 1. Estructura de Archivos
- [x] `index.html` existe en la raíz
- [x] `styles.css` existe en la raíz
- [x] `main.js` existe en la raíz
- [x] `render.yaml` existe en la raíz
- [x] `assets/foto_perfil.jpg` existe

### 2. Funcionalidades
- [ ] Navbar visible y fija
- [ ] Menú hamburguesa aparece en móvil (< 992px)
- [ ] Menú hamburguesa se abre/cierra correctamente
- [ ] Animación X funciona al cerrar
- [ ] Scroll suave funciona al hacer clic en enlaces
- [ ] Menú se cierra al hacer clic fuera
- [ ] Menú se cierra al hacer clic en un enlace
- [ ] Imagen de perfil se ve correctamente
- [ ] Todas las secciones son accesibles
- [ ] Footer visible

### 3. Responsive
- [ ] Prueba en 320px (móvil pequeño)
- [ ] Prueba en 375px (iPhone)
- [ ] Prueba en 768px (tablet)
- [ ] Prueba en 1024px (laptop)
- [ ] Prueba en 1920px (desktop)
- [ ] No hay scroll horizontal en ningún tamaño
- [ ] Grid se colapsa correctamente (2→1 columna)

### 4. Errores en Consola
- [ ] Abre DevTools (F12)
- [ ] Ve a la pestaña "Console"
- [ ] No debe haber errores en rojo
- [ ] Verifica que `main.js` se carga correctamente

### 5. Errores de Red
- [ ] Abre DevTools (F12)
- [ ] Ve a la pestaña "Network"
- [ ] Recarga la página (F5)
- [ ] Verifica que `styles.css` se carga (200 OK)
- [ ] Verifica que `main.js` se carga (200 OK)
- [ ] Verifica que `assets/foto_perfil.jpg` se carga (200 OK)

## 🐛 PROBLEMAS COMUNES Y SOLUCIONES

### El menú hamburguesa no aparece
**Solución**: Abre DevTools, ve a "Console" y verifica que `main.js` se carga. Si hay error, verifica la ruta: debe ser `./main.js`

### Las imágenes no se ven
**Solución**: Verifica que la ruta sea `./assets/foto_perfil.jpg` (relativa, no absoluta)

### El CSS no se aplica
**Solución**: Verifica que la ruta en `index.html` sea `./styles.css` y que el archivo exista

### El scroll suave no funciona
**Solución**: Verifica que `main.js` se carga correctamente y que no hay errores en la consola

### Hay scroll horizontal
**Solución**: Verifica que `overflow-x: hidden` esté en `html` y `body` en `styles.css`

## 📱 PRUEBAS EN DISPOSITIVOS REALES

### Chrome DevTools
1. Abre DevTools (F12)
2. Click en el icono de dispositivo móvil (Ctrl+Shift+M)
3. Prueba diferentes dispositivos:
   - iPhone SE (375px)
   - iPhone 12 Pro (390px)
   - iPad (768px)
   - iPad Pro (1024px)

### Dispositivos Reales
- Prueba en tu móvil abriendo `http://[tu-ip]:8000`
- Para encontrar tu IP: `ipconfig` (Windows) o `ifconfig` (Mac/Linux)

## ✅ RESULTADO ESPERADO

Al abrir `http://localhost:8000` deberías ver:
1. Navbar fija en la parte superior
2. Sección Hero con tu nombre y foto
3. Sección Sobre Mí con cards
4. Sección Habilidades con categorías
5. Sección Proyectos con 5 proyectos
6. Sección Contacto con 3 tarjetas
7. Footer al final

Todo debe funcionar perfectamente en todos los tamaños de pantalla.

