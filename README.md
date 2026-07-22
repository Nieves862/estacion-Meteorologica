# 🌦️ Proyecto: Estación Meteorológica e Industrial — Eco-Intelligence

> **Año de Desarrollo:** 2026  
> **Especialidad:** Programación III / Robótica / Club de Ciencias — 5to Año (Escuela PRoA Sede Río III)  
> *Desarrollo integral de una estación meteorológica autónoma, conectando hardware embebido, software POO y ciencia de datos.*

---

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-C%2B%2B-00979D?style=for-the-badge&logo=arduino&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Workbench-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-Analytics-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Google Colab](https://img.shields.io/badge/Google_Colab-Data_Science-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)

---

## 📌 Presentación de la Docente
| Apellido y Nombre | E-mail | GitHub |
| :--- | :--- | :---: |
| **VILLALBA, Valeria Nieves** | `vnvillalba@escuelasproa.edu.ar` | [🐙 Ver Perfil GitHub](https://github.com/Nieves862) |

---

## 📂 Estructura del Repositorio

El proyecto está organizado de forma modular para reflejar las diferentes capas de la arquitectura:

* 📊 `analisis_ipynb/` — Cuadernos de Google Colab para prototipado, limpieza de datasets y análisis exploratorio (EDA).
* 🤖 `arduino_ino/` — Código fuente (`.ino`) para microcontrolador Arduino UNO R3 (Lectura multisensor, alertas y LCD I2C).
* 📈 `dashboard_pbix/` — Reportes y tableros interactivos en Power BI para monitoreo histórico de patrones ambientales.
* 🗄️ `database_sql/` — Scripts de creación, modelado relacional, DDL/DML y consultas analíticas en MySQL Workbench.
* 📄 `docs/` — Documentación técnica del proyecto, arquitectura de software, requerimientos y diagramas UML.
* 🐍 `python_app/` — Aplicación backend desarrollada en Python bajo el paradigma de **Programación Orientada a Objetos (POO)**.

---

## 🛠️ Tecnologías e Integración Curricular

Este proyecto articula las tres áreas clave de la especialidad técnica para consolidar un sistema informático de extremo a extremo (*End-to-End*):

### 🔬 Club de CIENCIAS (Análisis y Persistencia de Datos)
* **Google Colab** (`Pandas`, `Matplotlib`, `Seaborn`) — Procesamiento estadístico del dataset, imputación de nulos y normalización.
* **MySQL Workbench** — Diseño relacional, normalización (3FN) e implementación de la base de datos para el histórico de mediciones.
* **Power BI** — Análisis visual de variables meteorológicas, detección de anomalias y toma de decisiones orientada a datos.

### 🐍 PROGRAMACIÓN III (Lógica de Software y Backend)
* **Visual Studio Code** — Entorno de desarrollo integrado (IDE) principal del backend.
* **Python 3** — Arquitectura de software orientada a objetos (clases, objetos, encapsulamiento y herencia) para abstraer el hardware.
* **Conectores** (`PySerial` / `mysql-connector-python`) — Pipeline de comunicación para ingesta en tiempo real y persistencia relacional.

### 🤖 ROBÓTICA (Hardware Embebido y Simulación)
* **Arduino IDE** — Programación embebida en **C++** controlando muestreo analógico y lógica de actuación.
* **Tinkercad** — Simulación del circuito, balance de carga en sensores y lógica de control de estados de alerta.
* **Hardware Utilizado**: Arduino UNO R3, sensor de temperatura/humedad TMP36, sensor de gas/humo serie MQ, pantalla LCD 16x2 (I2C con chip MCP23008 / PCF8574), Buzzer piezoeléctrico y LEDs de señalización.

---

## 🚀 Estado del Arte / Funcionalidades Logradas
1. **Modelado y Limpieza de Datos:** Dataset inicial normalizado, libre de duplicados y estructurado para exportación SQL.
2. **Controlador Físico de Estados:** Simulación funcional en Tinkercad con procesamiento analógico en C++, clasificación de rangos térmicos y de calidad de aire, alarmas sonoras y diagnóstico local en LCD.
3. **Backend Modular POO:** Abstracción del circuito físico en componentes de software Python mediante clases y métodos de comunicación serial.

---

## 🏁 Pasos para Ejecutar la Simulación

1. **Simulación en Tinkercad:**
   * Acceder al código fuente dentro de `arduino_ino/estacion_meteo.ino`.
   * Cargar el circuito correspondiente en la plataforma Tinkercad y verificar las conexiones de los sensores `TMP36` (A0) y `MQ` (A1).
2. **Monitor Serie / Ingesta:**
   * El microcontrolador emite por consola serie la trama: `Humedad,Temperatura,Gas` (Ejemplo: `50,24,522`).

---

## 🛡️ Buenas Prácticas de Desarrollo Incorporadas
* Control de versiones profesional mediante Git con **commits semánticos** (`feat:`, `fix:`, `docs:`).
* Uso de `.gitignore` optimizado para omitir entornos virtuales (`.venv/`), archivos compilados (`__pycache__/`, `.pyc`) y temporales del sistema.
* Arquitectura modular y extensible para facilitar el mantenimiento y escalabilidad del proyecto.
