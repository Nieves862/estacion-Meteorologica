-- SQL
CREATE DATABASE estacionmetereologica_proa;

USE estacionmetereologica_proa;

CREATE TABLE mediciones (
    id_mediciones INT AUTO_INCREMENT PRIMARY KEY,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    temperatura INT, 		 -- El DHT11 mide de 1 en 1 grado, un INT es más que suficiente y eficiente
    humedad INT      		 -- ¡Perfecto! Como es entera, guardamos un INT (ocupa poquísimo espacio)
);

-- Consulta de prueba (para verificar que se creó vacía)
SELECT * FROM mediciones;

SELECT * FROM mediciones ORDER BY id_mediciones DESC;

INSERT INTO mediciones (temperatura, humedad) 
VALUES (12, 86);

-- SQL
SELECT 
    fecha_hora, 
    temperatura,
    humedad,
    CASE 
        WHEN temperatura > 30 THEN 'ALERTA: CALOR'
        WHEN temperatura < 15 THEN 'ALERTA: FRIO'
        ELSE 'ESTADO OPTIMO'
    END AS diagnostico_clima
FROM mediciones;
