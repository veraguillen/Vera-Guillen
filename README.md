# 🚀 Portfolio Vera Guillen - Static Site

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fveraguillen%2FVera-Guillen&env=FORMSPREE_ENDPOINT&envDescription=Configuraci%C3%B3n%20de%20Formspree%20para%20el%20formulario%20de%20contacto&envLink=https%3A%2F%2Fformspree.io%2F)

## 🚀 Despliegue en Vercel

Este proyecto está configurado para desplegarse fácilmente en Vercel. Sigue estos pasos:

1. Haz clic en el botón "Deploy" de arriba
2. Conecta tu cuenta de GitHub
3. Asegúrate de que la variable de entorno `FORMSPREE_ENDPOINT` esté configurada con tu endpoint de Formspree
4. Haz clic en "Deploy"

## 📝 Variables de Entorno

Asegúrate de configurar las siguientes variables de entorno en Vercel:

- `FORMSPREE_ENDPOINT`: Tu endpoint de Formspree (ej: `https://formspree.io/f/tu-id`)

## ✨ Características

- **100% Responsive**: Mobile-first, perfecto en todos los dispositivos (320px - 4K)
- **Navbar Fixed**: Menú superior fijo con hamburguesa en móvil
- **Scroll Suave**: Navegación fluida entre secciones
- **Diseño Moderno**: Tema cyberpunk/hacker con efectos visuales
- **Sin Dependencias**: HTML5, CSS3 y JavaScript vanilla puro
- **Optimizado**: CSS consolidado, imágenes responsive, carga rápida

## 📋 Estructura del Proyecto

```
portfolio/
├── index.html          # Página principal (SPA)
├── styles.css          # CSS consolidado y optimizado
├── main.js             # JavaScript para navbar y scroll
├── render.yaml         # Configuración para Render.com
├── assets/             # Recursos estáticos
│   ├── foto_perfil.jpg
│   └── proyectos/
└── README.md           # Este archivo
```

## 🚀 Despliegue en Render.com (GRATIS)

### Opción 1: Deploy Automático con render.yaml (RECOMENDADO)

1. **Sube tu código a GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/tu-usuario/tu-repo.git
   git push -u origin main
   ```

2. **Conecta con Render.com**
   - Ve a [render.com](https://render.com)
   - Inicia sesión con GitHub
   - Haz clic en "New +" → "Static Site"
   - Conecta tu repositorio

3. **Configuración**
   - **Name**: `portfolio-vera-guillen` (o el que prefieras)
   - **Branch**: `main` (o `master`)
   - **Build Command**: Dejar vacío o `echo "No build required"`
   - **Publish Directory**: `./` (raíz del proyecto)
   - Render detectará automáticamente `render.yaml`

4. **¡Listo!** Tu sitio estará en `https://tu-sitio.onrender.com`

### Opción 2: Deploy Manual

1. **Sube tu código a GitHub** (igual que arriba)

2. **Crea Static Site en Render**
   - Ve a [render.com](https://render.com)
   - "New +" → "Static Site"
   - Conecta tu repositorio

3. **Configuración Manual**
   - **Name**: `portfolio-vera-guillen`
   - **Branch**: `main`
   - **Build Command**: (dejar vacío)
   - **Publish Directory**: `./`

4. **Deploy** → Tu sitio estará live en menos de 2 minutos

## 🧪 Prueba Local

Para probar el sitio localmente antes de deployar:

### Opción 1: Servidor HTTP Simple (Python)
```bash
# Python 3
python -m http.server 8000

# Luego abre en el navegador:
# http://localhost:8000
```

### Opción 2: Servidor HTTP Simple (Node.js)
```bash
# Si tienes Node.js instalado
npx http-server -p 8000

# Luego abre en el navegador:
# http://localhost:8000
```

### Opción 3: Live Server (VS Code)
- Instala la extensión "Live Server" en VS Code
- Click derecho en `index.html` → "Open with Live Server"

## 📱 Responsive Design

El sitio está optimizado para:
- ✅ Móviles pequeños (< 576px)
- ✅ Móviles grandes (576px – 767px)
- ✅ Tablets (768px – 991px)
- ✅ Laptops (992px – 1199px)
- ✅ Escritorio grande (≥ 1200px)

## 🎨 Personalización

### Cambiar Colores
Edita las variables CSS en `styles.css`:
```css
:root {
    --accent-orange: #FF6A00;
    --accent-orange-glow: #FF8C2B;
    --bg-main: #0D1117;
    /* ... */
}
```

### Cambiar Contenido
Edita directamente `index.html`:
- Sección Hero: Líneas ~30-60
- Sobre Mí: Líneas ~62-120
- Habilidades: Líneas ~122-180
- Proyectos: Líneas ~182-280
- Contacto: Líneas ~282-320

### Cambiar Imagen de Perfil
Reemplaza `./assets/foto_perfil.jpg` con tu imagen (recomendado: 400x400px o mayor, formato JPG/PNG)

## 🔧 Tecnologías

- **HTML5**: Estructura semántica
- **CSS3**: Flexbox, Grid, Variables CSS, `clamp()`, Animaciones
- **JavaScript**: Vanilla JS (sin frameworks)
- **Deploy**: Render.com Static Site (gratis)

## 📝 Notas

- El sitio es 100% estático, no requiere backend
- Todas las rutas son relativas (`./assets/`, `./styles.css`, etc.)
- Optimizado para SEO con meta tags correctos
- Accesible: botones ≥ 44×44px, contraste adecuado
- Sin dependencias externas (excepto Google Fonts)

## 🐛 Solución de Problemas

### El menú hamburguesa no funciona
- Verifica que `main.js` esté cargado correctamente
- Abre la consola del navegador (F12) y busca errores

### Las imágenes no se ven
- Verifica que las rutas sean relativas: `./assets/foto_perfil.jpg`
- Asegúrate de que los archivos existan en la carpeta `assets/`

### El sitio no se ve bien en móvil
- Verifica que el viewport meta tag esté presente en `index.html`
- Abre las herramientas de desarrollador (F12) y prueba en modo responsive

### Render.com no despliega
- Verifica que `index.html` esté en la raíz del proyecto
- Asegúrate de que `render.yaml` esté correcto
- Revisa los logs de build en Render.com

## 📄 Licencia

Este proyecto es de uso personal.

## 👤 Autor

**Vera Guillen**
- 📧 Email: vera.guillen27@gmail.com
- 💻 GitHub: [@veraguillen](https://github.com/veraguillen)
- 💼 LinkedIn: [Vera Guillen](https://www.linkedin.com/in/vera-guillen-9b464a303/)

---

⭐ Si te gusta este portfolio, ¡dale una estrella en GitHub!
