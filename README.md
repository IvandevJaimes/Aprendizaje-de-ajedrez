# Aprendizaje de Ajedrez

Sistema educativo interactivo para consola que enseña conceptos de ajedrez mediante preguntas progresivas.

## Características

Tres modos de juego: Desafío (5 niveles progresivos), Adivinanzas y Modo Libre.
Tres dificultades: Fácil (sin límite), Normal (10s) y Difícil (5s con penalización).
50 preguntas totales (10 por nivel) con teoría y explicaciones.
Guardado automático de progreso con sistema de contraseñas.
Multiplataforma: Windows, macOS, Linux.

## Tecnologías

Python 3.8+, colorama (colores en terminal), threading (temporizadores), JSON (persistencia).

## Instalación

python main.py

## Estructura

src/core - Lógica del juego, gestión de estado, entrada
src/theory - Contenido teórico de cada nivel
src/challenges - Preguntas y evaluaciones
src/utils - Constantes, datos, visualización
main.py - Punto de entrada

## Uso

Selecciona modo, responde preguntas y progresa por los niveles.
Necesitas 5+ puntos para desbloquear cada nivel.
El progreso se guarda automáticamente. Almacenamiento: ~/.chess_learning_game

## Características Técnicas

Separación clara de responsabilidades, código modular sin repeticiones (DRY).
Soporte: Windows, macOS, Linux con entrada automática por SO.
Type hints, variables bien nombradas, código autodocumentado.

## Compatibilidad

Python 3.8+, Windows 7+, macOS 10.12+, Linux.
