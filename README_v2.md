# Aprendizaje de Ajedrez - Sistema Educativo

**Versión:** 2.0 (Refactorizado)  
**Estado:** Producción  

## Descripción

Sistema educativo interactivo basado en consola para aprender conceptos fundamentales de ajedrez. Construido con arquitectura escalable y multiplataforma.

## Características

- **Tres Modos de Juego:**
  - Modo Desafío: Progresión lineal con 5 niveles
  - Modo Adivinanzas: Cuestionarios mixtos (en desarrollo)
  - Modo Libre: Acceso sin restricciones a cualquier nivel

- **Tres Niveles de Dificultad:**
  - Fácil: Sin límite de tiempo
  - Normal: 10 segundos por pregunta
  - Difícil: 5 segundos por pregunta con penalización (-1 punto por error)

- **Contenido Educativo:**
  - 5 niveles con 10 preguntas cada uno (50 preguntas totales)
  - Teoría estructurada para cada nivel
  - Explicaciones detalladas por respuesta

- **Gestión de Estado:**
  - Guardado automático de progreso
  - Recuperación de partidas
  - Sistema de contraseñas

- **Multiplataforma:**
  - Windows (con soporte msvcrt)
  - macOS
  - Linux
  - Limpieza de pantalla automática según SO

## Instalación

### Requisitos
- Python 3.8+
- pip

### Pasos

```bash
cd /ruta/del/proyecto

pip install -r requirements.txt

python main.py
```

## Estructura del Proyecto

```
src/
├── core/
│   ├── game.py              # Lógica principal del juego
│   ├── state.py             # Gestión de persistencia
│   ├── input_handler.py     # Entrada multiplataforma
│   └── quiz_manager.py      # Gestor de cuestionarios
├── theory/
│   └── level.py             # Módulos de teoría (niveles 1-5)
├── challenges/
│   └── challenge.py         # Módulos de desafíos/preguntas
├── utils/
│   ├── constants.py         # Configuración y constantes
│   ├── data.py              # Datos de preguntas y teoría
│   ├── display.py           # UI y visualización
│   └── free_play.py         # Modo libre (opcional)
└── main.py                  # Punto de entrada

main.py                      # Script de inicio (raíz)
requirements.txt             # Dependencias
README.md                    # Este archivo
```

## Niveles del Juego

### Nivel 1: Fundamentos
Qué es el ajedrez, objetivo, piezas y movimientos básicos

### Nivel 2: Notación y Conceptos
Notación algebraica, aperturas, movimientos especiales y empates

### Nivel 3: Tácticas
Estrategias tácticas, técnicas de juego y conceptos clave

### Nivel 4: Estrategia Avanzada
Maniobras, conceptos estratégicos y formas de juego

### Nivel 5: Historia
Historia del ajedrez y grandes maestros

## Cómo Jugar

### Primer Inicio
1. El juego solicita tu nombre de usuario
2. Elige una contraseña para recuperar tu partida
3. Selecciona un nivel de dificultad
4. Comienza a responder preguntas

### Progresión
- Necesitas 5+ puntos en cada nivel para desbloquearlo
- El progreso se guarda automáticamente
- Puedes interrumpir y retomar en cualquier momento

### Menú Principal
- **1:** Modo Desafío (progresión lineal)
- **2:** Modo Adivinanzas (ej. en desarrollo)
- **3:** Modo Libre (acceso a todos los niveles)
- **4:** Cargar o Borrar partida
- **5:** Instrucciones
- **6:** Créditos
- **7:** Salir

## Mejoras Implementadas en v2.0

### Arquitectura
- ✅ Separación clara de responsabilidades
- ✅ Código DRY (evitar repetición)
- ✅ Estructura modular y extensible

### Multiplataforma
- ✅ Soporte automático Windows/macOS/Linux
- ✅ Manejo de entrada independiente del SO
- ✅ Gestión de rutas multiplataforma

### Código
- ✅ Sintaxis mejorada y moderna
- ✅ Type hints para mejor legibilidad
- ✅ Gestión de excepciones robusta
- ✅ Variables bien nombradas

### Persistencia
- ✅ Almacenamiento en ~/.chess_learning_game (portátil)
- ✅ JSON para fácil lectura de datos
- ✅ Manejo seguro de contraseñas

### UX/UI
- ✅ Menús claros y navegables
- ✅ Colores significativos por nivel
- ✅ Animaciones de escritura lenta (por elegancia)
- ✅ Bordes y separadores visuales

## Cambios Técnicos Principales

### Antes (v1.0)
```python
# Código repetido en cada NIVEL*.py
def nivel1():
    if D == "1":
        def evaluar(): ...
    elif D == "2":
        def evaluar(): ...
    elif D == "3":
        def evaluar(): ...
```

### Ahora (v2.0)
```python
# Código centralizado y reutilizable
class QuizManager:
    def __init__(self, difficulty):
        self.config = DIFFICULTIES[difficulty]
    
    def ask_question(self, question, options, answer, explanation):
        # Lógica única para todos los casos
```

## Compatibilidad

- Windows 7+
- macOS 10.12+
- Todas las distribuciones Linux
- Python 3.8, 3.9, 3.10, 3.11, 3.12

## API (para desarrollo)

### Importar módulos
```python
from src.core.game import GameManager
from src.challenges.challenge import run_level_challenge
from src.theory.level import THEORY_MODULES
```

### Ejecutar un nivel directamente
```python
score = run_level_challenge(level=1, difficulty="1")
```

### Acceder a los datos
```python
from src.utils.data import CHALLENGES, THEORY_CONTENT
questions = CHALLENGES[1]  # 10 preguntas del nivel 1
theory = THEORY_CONTENT[1]  # Teoría del nivel 1
```

## Futuras Mejoras

- [ ] Interfaz gráfica (GUI)
- [ ] Análisis de progreso
- [ ] Logros y estadísticas
- [ ] Base de datos para múltiples usuarios
- [ ] Importación de partidas PGN
- [ ] Tablas de posiciones finales
- [ ] Pruebas unitarias

## Migrando del Código Antiguo

1. El código antiguo está en `archivosPython/`
2. Toda la funcionalidad ha sido migrada a `src/`
3. Los datos están centralizados en `src/utils/data.py`
4. El estado se guarda ahora en `~/.chess_learning_game/`

## Notas de Desarrollo

- No se han añadido comentarios innecesarios (código autodocumentado)
- Las constantes están centralizadas en `constants.py`
- Los mensajes se rehusilizan desde `data.py` y `display.py`
- Las pruebas pueden extenderse fácilmente

## Licencia

Abierto para uso educativo.

## Contacto / Soporte

Para reportar bugs o sugestiones, considera abrir un issue en el repositorio.

---

**Versión:** 2.0  
**Última actualización:** Abril 2026  
**Autor:** Refactorizado por IA
