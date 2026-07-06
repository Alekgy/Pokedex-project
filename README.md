# 🚀 Refactoring Project: Pokedex Web App 

Este proyecto fue uno de mis primeros desarrollos al iniciar mi carrera en programación. Originalmente, era una aplicación web básica en **Flask** con funciones incompletas (solo mostraba nombres mediante iteraciones ineficientes en Pandas) y código acoplado a un blog en desuso. 

Con el tiempo y la experiencia adquirida, decidí tomar este proyecto antiguo de mi portafolio para **refactorizarlo por completo, optimizar su rendimiento y aplicar buenas prácticas de desarrollo de software**, transformándolo en una aplicación dinámica, intuitiva y lista para producción.

📌 **Demo en Vivo:** [pokedex-project-phi.vercel.app](https://pokedex-project-phi.vercel.app/)

---

## 🛠️ Tecnologías y Herramientas Utilizadas
* **Backend:** Python 3.x, Flask (Framework micro-web).
* **Frontend:** HTML5, CSS3 (Custom Grid Layout & Flexbox), Jinja2 (Motor de plantillas dinámicas).
* **Data Source:** Estructuras JSON nativas.
* **Despliegue:** Vercel.

---

## 📈 Evolución y Mejoras Implementadas (La Refactorización)

### 1. Optimización del Flujo de Datos y Backend
* **Adiós a dependencias innecesarias:** Originalmente, el proyecto utilizaba la librería `pandas` (`iterrows`) para procesar un archivo `pokedex.json` local en cada petición HTTP, lo cual generaba una carga computacional ineficiente. Se reemplazó por el manejo de colecciones y diccionarios nativos de Python (`json`, `set`), optimizando drásticamente los tiempos de respuesta.
* **Eliminación de Código Muerto:** Se removieron por completo módulos huérfanos, configuraciones antiguas de bases de datos relacionales (PostgreSQL/SQLAlchemy) y vistas inactivas (un antiguo sistema de Blog), dejando una base de código limpia y de responsabilidad única.

### 2. Arquitectura de Navegación Dinámica y Experiencia de Usuario (UX)
* **Búsqueda por Atributos:** Se eliminó la rigidez de buscar Pokémon únicamente ingresando IDs manuales. Ahora, la aplicación extrae dinámicamente todos los tipos de Pokémon disponibles del JSON para listarlos como filtros interactivos.
* **Buscador Inteligente e Internacional (Multilingüe):** Se implementó una barra de búsqueda unificada en el backend capaz de procesar tanto IDs numéricos como texto. El buscador inspecciona todas las llaves de traducción del JSON, permitiendo encontrar un Pokémon sin importar si el usuario escribe su nombre en inglés, francés, japonés o chino, controlando además la insensibilidad a mayúsculas.

### 3. Rediseño Frontend y UI Dinámica
* **UI Adaptativa (CSS Grid & Flexbox):** La interfaz inicial plana fue sustituida por un catálogo simétrico de tarjetas cuadradas auto-ajustables (responsivas) que muestran miniaturas e información de manera ordenada sin generar desbordamientos de pantalla.
* **Fondos con Degradados Dinámicos:** Utilizando la lógica del motor Jinja2 en el servidor, el fondo de la pantalla de resultados muta dinámicamente. Si el Pokémon tiene un solo tipo, adopta su color representativo; si es un Pokémon híbrido (doble tipo), el backend calcula y renderiza un degradado (`linear-gradient`) horizontal exacto combinando ambas identidades.
* **Control de Scroll:** Se eliminaron las restricciones rígidas de altura en los contenedores para evitar barras de desplazamiento internas molestas, centralizando la tarjeta principal mediante Flexbox.

---

## 🚀 Despliegue en Vercel

El proyecto está configurado para producción y optimizado para la arquitectura Serverless de **Vercel** mediante un archivo de configuración `vercel.json` y el manejo adecuado del enrutamiento de archivos estáticos (`/static`).

### Pasos para Ejecución Local:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/pokedex-flask.git
   cd pokedex-flask
   ```
2. **Crear y activar entorno virtual:**

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```
3. **Instalar dependencias:**

```bash
pip install -r requirements.txt
```
4. **Ejecutar servidor de desarrollo:**

```bash
flask --app main run --debug
```
5. **Abrir en el navegador:** http://127.0.0.1:5000/