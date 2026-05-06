# Proyecto: Búsqueda por Funciones Hash (50,000 Datos)

Este repositorio contiene la implementación de una **Tabla Hash con Encadenamiento** para la búsqueda eficiente de números enteros.

##  Archivos del Proyecto
* `Metodo_Busqueda.py`: Código fuente en Python.
* `Datos.txt`: Archivo original con 50,000 enteros.
* `datos_ordenados.txt`: Archivo generado tras el proceso de ordenamiento.
* `README.md`: Documentación técnica.

##  Funcionamiento
1. El programa lee los números de `Datos.txt`.
2. Los ordena ascendentemente y los guarda en un nuevo archivo.
3. Construye una tabla hash de 5,000 cubetas usando la función: `posicion = numero % 5000`.
4. Permite realizar búsquedas midiendo el tiempo de respuesta en milisegundos.

##  Análisis de Complejidad
* **Tiempo de Búsqueda (Promedio):** $O(1)$. El acceso a la cubeta es directo.
* **Tiempo de Búsqueda (Peor Caso):** $O(n)$. Si hay demasiadas colisiones en una sola cubeta.
* **Espacio:** $O(n + m)$. Donde $n$ son los elementos y $m$ las cubetas de la tabla.

##  Casos de Uso
¿Cuándo es mejor usar este método?
* Cuando la **velocidad de búsqueda** es crítica y se realizan miles de consultas por segundo.
* En sistemas donde los datos no cambian constantemente pero se consultan mucho (ej. diccionarios, bases de datos de solo lectura).
* Para implementar **Cachés de memoria** de alto rendimiento.

##  Comparativa: Hash vs Búsqueda Binaria
| Característica | Tabla Hash | Búsqueda Binaria |
| :--- | :--- | :--- |
| Complejidad | $O(1)$ | $O(\log n)$ |
| Requiere orden | No | Sí |
| Uso de Memoria | Mayor (por las cubetas) | Menor (solo el arreglo) |
