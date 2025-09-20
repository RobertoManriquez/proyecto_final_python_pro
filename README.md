# 🌱 Proyecto Medio Ambiente — Flask + HTML/CSS/JS  

Este proyecto es una aplicación web educativa creada con **Flask** (Python) y tecnologías web modernas (**HTML, CSS, JavaScript**).  
Su objetivo es **concientizar sobre el cuidado del medio ambiente** a través de secciones informativas, un cuestionario interactivo y un formulario de comentarios.  

Incluye:  
- Una **interfaz amigable** con secciones dinámicas.  
- Contenido educativo sobre residuos, reciclaje y acciones sustentables.  
- Un **cuestionario de 20 preguntas** (10 de hábitos + 10 de conocimientos) que calcula puntajes e interpreta los resultados.  
- Integración con **Formspree** para recopilar comentarios de los usuarios.  
- Animaciones, iconos externos y un diseño adaptable.  

---

## 🚀 Tecnologías utilizadas  

### Backend  
- **[Flask](https://flask.palletsprojects.com/)** → Framework ligero en Python para construir aplicaciones web.  
  - Maneja rutas (`@app.route`).  
  - Renderiza plantillas HTML.  
  - Permite usar variables dinámicas como el año actual en el footer.  

- **Módulos estándar de Python:**  
  - `datetime`: obtener el año actual automáticamente.  
  - `os`: acceder a variables del sistema, como el usuario que ejecuta la app.  

### Frontend  
- **HTML5** → estructura semántica del contenido.  
- **CSS3** → estilos personalizados (paleta oscura con verde ecológico).  
- **JavaScript** → control dinámico de secciones y cuestionario.  
- **Google Fonts (Inter)** → tipografía moderna.  
- **Font Awesome** → iconos ilustrativos (reciclaje, residuos, energía, etc.).  
- **AOS (Animate On Scroll)** → animaciones al hacer scroll.  

---

## 📂 Estructura del proyecto  

```
proyecto-medio-ambiente/
│
├── main.py                  # Código principal Flask (backend)
├── templates/
│   └── index.html           # Plantilla principal con todas las secciones
│
├── static/
│   ├── styles/
│   │   └── styles.css       # Estilos personalizados
│   └── images/              # Imágenes usadas en las secciones
│       ├── intro.jpg
│       ├── residuos.jpg
│       ├── reciclaje.jpg
│       └── acciones.jpg
│
└── README.md                # Documentación del proyecto
```

---

## 🖼️ Imágenes requeridas  

Coloca las siguientes imágenes dentro de `static/images/`:

1. **intro.jpg** → Naturaleza limpia, un paisaje verde.  
2. **residuos.jpg** → Clasificación de residuos (orgánicos, plásticos, vidrio, etc.).  
3. **reciclaje.jpg** → Imagen ilustrativa de reciclaje (contenedores, símbolos ♻️).  
4. **acciones.jpg** → Personas reciclando, usando bicicleta o bolsas reutilizables.  

*(Puedes usar imágenes libres de uso desde [Unsplash](https://unsplash.com/) o [Pexels](https://www.pexels.com/))*  

---

## ⚙️ Instalación y ejecución  

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/usuario/proyecto-medio-ambiente.git
   cd proyecto-medio-ambiente
   ```

2. **Crear entorno virtual (opcional pero recomendado)**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instalar dependencias**  
   ```bash
   pip install flask
   ```

4. **Ejecutar la aplicación**  
   ```bash
   python main.py
   ```

5. **Abrir en el navegador**  
   ```
   http://127.0.0.1:5001
   ```

---

## 🧩 Funcionalidades principales  

- **🏠 Home** → Bienvenida al sitio.  
- **🌍 Introducción** → Problemas ambientales actuales e impacto industrial.  
- **🗑️ Residuos** → Clasificación de residuos (orgánicos, plásticos, peligrosos, reciclables).  
- **♻️ Reciclaje** → Beneficios y economía circular.  
- **💡 Acciones** → Hábitos ecológicos cotidianos.  
- **❓ Cuestionario** → Evalúa hábitos y conocimientos ambientales (con interpretación automática).  
- **💬 Comentarios** → Formulario conectado a **Formspree**.  
- **📅 Footer dinámico** → Año actual cargado desde Python.  

---

## 📝 Detalles del cuestionario  

- **Parte A (hábitos):** mide cómo contribuye el usuario con acciones diarias (0–30 pts).  
- **Parte B (conocimientos):** mide el nivel de conocimiento sobre reciclaje y medio ambiente (0–30 pts).  

Cada respuesta vale entre **0 y 3 puntos**.  
Al final se muestra:  
- Puntaje obtenido.  
- Porcentaje sobre el total.  
- Una interpretación categórica:  
  - 🌱 Excelente  
  - 👍 Bueno  
  - 😶 Regular  
  - ⚠️ Bajo  
  - ‼️ Muy bajo  

---

## 🎨 Estilos (CSS destacados)  

- **Tema oscuro** (`--bg`, `--card`) con contraste en verde ecológico (`--accent`).  
- **Diseño responsivo** → compatible con escritorio y móvil.  
- **Botones (`.btn`)** con bordes redondeados y hover animado.  
- **Secciones dinámicas:** `.section-hidden` y `.section-visible`.  
- **Grid system:** usado en secciones como “Residuos” y “Reciclaje”.  

---

## 🔮 Posibles mejoras futuras  

- [ ] Agregar **base de datos (SQLite/PostgreSQL)** para guardar comentarios directamente.  
- [ ] Incluir **ranking de resultados del cuestionario** para comparar hábitos.  
- [ ] Internacionalización (i18n) para más idiomas.  
- [ ] Implementar un **modo claro/oscuro** con toggle.  
- [ ] Integrar **gráficos** con resultados del cuestionario (ej. Chart.js).  

---

## 👨‍💻 Autor  

**Roberto Manríquez**  
Proyecto educativo para fomentar la conciencia ambiental.  

📌 *Uso libre con fines educativos.*  
