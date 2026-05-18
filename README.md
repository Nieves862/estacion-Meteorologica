# 🌦️ Proyecto: Estación Meteorológica — Eco-Intelligence

> **Año de Desarrollo: 2026** > **Especialidad:** Programación III/ Robótica/ Club de Ciencias — 5to Año (Escuela PRoA)  
> *Desarrollo integral de una estación meteorológica autónoma, conectando hardware, software y ciencia de datos.*

---

## 📌 Presentación de la Profesora
| Apellido y Nombre | E-mail | GitHub |
| :--- | :--- | :---: |
| **VILLALBA, Valeria Nieves** | vnvillalba@escuelasproa.edu.ar | [🐙 Ver Perfil](https://github.com/Nieves862) |

---

## 📂 Estructura del Proyecto

El repositorio está organizado de forma modular para reflejar las diferentes capas de la aplicación:

* 📊 **`analisis_ipynb/`** — Cuadernos de Google Colab para el prototipado, limpieza de datasets y análisis exploratorio.
* 🤖 **`arduino_ino/`** — Código fuente (.ino) desarrollado para el microcontrolador Arduino UNO R3 (hasta ahora Alertas y LCD).
* 📈 **`dashboard_pbix/`** — Reportes y tableros interactivos en Power BI para el monitoreo histórico.
* 🗄️ **`database_sql/`** — Scripts de creación, modelado y consultas en MySQL Workbench.
* 📄 **`docs/`** — Documentación técnica del proyecto, requerimientos y leyes de software.
* 🐍 **`python_app/`** — Aplicación de escritorio desarrollada en Python bajo el paradigma de **Programación Orientada a Objetos (POO)**.

---

## 🛠️ Tecnologías e Integración

Este proyecto une tres áreas clave de la especialidad para formar un sistema informático completo:

### 🔬 Club de CIENCIAS (Análisis y Persistencia)
* **Google Colab** `(Pandas, Matplotlib, Seaborn)` — Procesamiento estadístico del dataset limpio del formulario.
* **MySQL Workbench** — Diseño, normalización e implementación de la base de datos relacional para el histórico de mediciones.
* **Power BI** — Análisis visual del clima, patrones ambientales y toma de decisiones orientada a datos.

### 🐍 PROGRAMACIÓN III (Lógica de Software)
* **Visual Studio Code** — Entorno de desarrollo integrado (IDE) principal del backend.
* **Python 3** — Implementación de arquitectura de software basada en clases, objetos y herencia (**POO**) para modelar los componentes físicos.
* **Conectores** `(PySerial / MySQL-Connector)` — Creación del "puente" de comunicación para capturar datos en tiempo real y persistirlos.

### 🤖 ROBÓTICA (Hardware y Simulación)
* **Arduino IDE** — Programación embebida en **C++** controlando tiempos de muestreo y actuadores.
* **Tinkercad** — Simulación del circuito, distribución de potencia y lógica de control de alertas de estados.
* **Hardware utilizado**: Arduino UNO R3, sensores de temperatura/humedad, Display LCD 16x2 (I2C), Buzzer piezoeléctrico y luces LED indicadoras.

---

## 🚀 Estado del Arte / Funcionalidades Logradas
1. **Modelado de Datos:** Dataset inicial normalizado, libre de duplicados y estructurado para su exportación a base de datos.
2. **Controlador de Estados Físico:** Simulación funcional en Tinkercad que clasifica rangos térmicos, activa alarmas sonoras y reporta diagnósticos en tiempo real por pantalla LCD de forma autónoma.
3. **Backend Modular:** Arquitectura de software en Python que abstrae el hardware en código mediante programación orientada a objetos.

---

### 🛡️ Buenas Prácticas de Desarrollo Incorporadas
* Uso estricto de `.gitignore` para omitir archivos temporales del sistema (`__pycache__/`, `.pyc`).
* Commits semánticos y estructurados para el control de versiones en Git.


