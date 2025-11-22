# 🧪 PRUEBA LOCAL - PASO A PASO

## 📋 PASO 1: Verificar que los archivos existan

Abre la terminal (PowerShell) en la carpeta del proyecto y ejecuta:

```powershell
cd "C:\Users\veram\OneDrive\Escritorio\portfolio"
dir index.html, styles.css, main.js
```

Deberías ver los 3 archivos listados.

## 📋 PASO 2: Iniciar servidor HTTP local

### Opción A: Python (RECOMENDADO - MÁS FÁCIL)

1. **Abre PowerShell** en la carpeta del proyecto:
   ```powershell
   cd "C:\Users\veram\OneDrive\Escritorio\portfolio"
   ```

2. **Inicia el servidor**:
   ```powershell
   python -m http.server 8000
   ```

3. **Deberías ver**:
   ```
   Serving HTTP on :: port 8000 (http://[::]:8000/) ...
   ```

4. **NO CIERRES esta ventana** (déjala abierta)

### Opción B: Si Python no funciona

Si no tienes Python o da error, usa Node.js:

```powershell
npx http-server -p 8000
```

## 📋 PASO 3: Abrir en el navegador

1. **Abre tu navegador** (Chrome, Firefox, Edge, etc.)

2. **Ve a la dirección**:
   ```
   http://localhost:8000
   ```
   O también puedes probar:
   ```
   http://127.0.0.1:8000
   ```

3. **Deberías ver**:
   - Navbar fija en la parte superior con "Vera Guillen"
   - Sección Hero con tu nombre y foto de perfil
   - Todas las secciones funcionando

## 📋 PASO 4: Verificar funcionalidades

### ✅ Navbar
- [ ] Navbar visible en la parte superior
- [ ] Logo "Vera Guillen" a la izquierda
- [ ] Menú horizontal a la derecha (en desktop)

### ✅ Menú Hamburguesa (en móvil)
1. **Abre DevTools** (presiona `F12`)
2. **Activa modo móvil** (presiona `Ctrl+Shift+M` o click en el icono de móvil)
3. **Cambia el ancho a menos de 992px** (por ejemplo, 375px)
4. [ ] Deberías ver el botón hamburguesa (3 líneas) a la derecha
5. [ ] Click en el hamburguesa → el menú se abre desde la izquierda
6. [ ] Click fuera del menú → el menú se cierra
7. [ ] Click en un enlace → el menú se cierra y hace scroll suave

### ✅ Scroll Suave
- [ ] Click en "Sobre Mí" → hace scroll suave a esa sección
- [ ] Click en "Habilidades" → hace scroll suave
- [ ] Click en "Proyectos" → hace scroll suave
- [ ] Click en "Contacto" → hace scroll suave

### ✅ Responsive
1. **En DevTools** (F12), prueba estos tamaños:
   - [ ] 320px (móvil pequeño) - Todo se ve bien
   - [ ] 375px (iPhone) - Todo se ve bien
   - [ ] 768px (tablet) - Grid cambia a 2 columnas
   - [ ] 1024px (laptop) - Todo se ve bien
   - [ ] 1920px (desktop) - Todo se ve bien

2. **Verifica que NO haya scroll horizontal**:
   - [ ] En ningún tamaño de pantalla hay scroll horizontal
   - [ ] Todo el contenido cabe dentro del viewport

### ✅ Imágenes
- [ ] La imagen de perfil se ve correctamente
- [ ] Si la imagen no carga, aparece un placeholder con "VG"

### ✅ Secciones
- [ ] Sección Hero visible
- [ ] Sección Sobre Mí visible con 4 cards
- [ ] Sección Habilidades visible con categorías
- [ ] Sección Proyectos visible con 5 proyectos
- [ ] Sección Contacto visible con 3 tarjetas
- [ ] Footer visible al final

## 📋 PASO 5: Verificar consola (sin errores)

1. **Abre DevTools** (F12)
2. **Ve a la pestaña "Console"**
3. [ ] No debería haber errores en rojo
4. [ ] Si hay errores, cópialos y revísalos

## 📋 PASO 6: Verificar Network (archivos cargados)

1. **En DevTools** (F12), ve a la pestaña "Network"
2. **Recarga la página** (F5)
3. **Verifica que estos archivos se carguen correctamente**:
   - [ ] `index.html` → Status 200
   - [ ] `styles.css` → Status 200
   - [ ] `main.js` → Status 200
   - [ ] `assets/foto_perfil.jpg` → Status 200 (o 404 si no existe, pero no debe romper)

## 🐛 SOLUCIÓN DE PROBLEMAS

### ❌ "python no se reconoce como comando"
**Solución**: Instala Python o usa Node.js:
```powershell
npx http-server -p 8000
```

### ❌ "No se puede acceder a localhost:8000"
**Solución**: 
1. Verifica que el servidor esté corriendo (deberías ver el mensaje en la terminal)
2. Prueba con `http://127.0.0.1:8000`
3. Verifica que el puerto 8000 no esté ocupado

### ❌ "El CSS no se aplica"
**Solución**:
1. Verifica que `styles.css` exista en la raíz
2. Abre DevTools → Network → recarga y verifica que `styles.css` se carga (200 OK)
3. Verifica la ruta en `index.html`: debe ser `./styles.css`

### ❌ "El menú hamburguesa no funciona"
**Solución**:
1. Abre DevTools → Console
2. Verifica que `main.js` se carga (Network → Status 200)
3. Busca errores en la consola
4. Verifica la ruta en `index.html`: debe ser `./main.js`

### ❌ "Las imágenes no se ven"
**Solución**:
1. Verifica que `assets/foto_perfil.jpg` exista
2. Si no existe, el placeholder "VG" debería aparecer
3. Verifica la ruta en `index.html`: debe ser `./assets/foto_perfil.jpg`

### ❌ "Hay scroll horizontal"
**Solución**:
1. Abre DevTools → Elements
2. Inspecciona qué elemento causa el overflow
3. Verifica que `overflow-x: hidden` esté en `html` y `body` en `styles.css`

## ✅ CUANDO TODO FUNCIONE

Si todo funciona correctamente:
1. ✅ Navbar visible y funcional
2. ✅ Menú hamburguesa funciona en móvil
3. ✅ Scroll suave funciona
4. ✅ Todas las secciones visibles
5. ✅ Sin errores en consola
6. ✅ Responsive en todos los tamaños

**¡Entonces estás listo para hacer deploy en Render.com!**

## 🛑 PARA DETENER EL SERVIDOR

Cuando termines de probar:
1. Ve a la terminal donde está corriendo el servidor
2. Presiona `Ctrl+C`
3. El servidor se detendrá

---

**¿Necesitas ayuda?** Revisa los errores en la consola (F12) y compártelos.

