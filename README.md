# 🐍 Culebrita Nokia 1100

> **¿Recuerdas pasar horas jugando Snake en tu Nokia 1100?** Este proyecto revive ese clásico de los 2000 — ahora en tu computador, construido con Python y Pygame.

```
 ╔══════════════════════════════════╗
 ║          CULEBRITA               ║
 ║          Nokia 1100              ║
 ║                                  ║
 ║    ■ ■ ■ ■ ■ →          ●       ║
 ║                                  ║
 ║    Presiona ENTER para jugar     ║
 ╚══════════════════════════════════╝
```

## 🎮 Gameplay

| Característica | Detalle |
|---|---|
| **Controles** | Flechas del teclado ↑ ↓ ← → |
| **Objetivo** | Come las frutas rojas y crece lo más que puedas |
| **Dificultad** | La velocidad aumenta con cada fruta — ¿cuánto aguantas? |
| **Game Over** | Chocas contra una pared o contra ti mismo |
| **Puntaje** | +10 puntos por cada fruta |

## 🚀 Instalación

### Requisitos previos
- Python 3.11+
- [UV](https://docs.astral.sh/uv/) (gestor de paquetes)

### Pasos

```bash
# 1. Clona el repositorio
git clone https://github.com/AndresInsuasty/culebrita_nokia_1100.git
cd culebrita_nokia_1100

# 2. Instala las dependencias
uv sync

# 3. ¡Juega!
uv run python main.py
```

> **Sin UV?** También puedes usar pip:
> ```bash
> pip install pygame
> python main.py
> ```

## 🕹️ Cómo jugar

1. Presiona **ENTER** para iniciar la partida
2. Usa las **flechas del teclado** para dirigir la culebrita
3. Come las **frutas rojas** para crecer y sumar puntos
4. Evita chocar contra las **paredes** y contra **ti mismo**
5. Al perder, presiona **ENTER** para reintentar

> **Pro tip:** La culebrita no puede dar giros de 180°. Si vas a la derecha, no puedes ir directamente a la izquierda.

## 🎨 Estilo visual

Inspirado fielmente en el Nokia 1100:

- **Fondo negro** — como la pantalla del Nokia
- **Culebrita verde** — con cabeza más brillante para identificarla fácil
- **Fruta roja** — resalta sobre el fondo oscuro
- **Cuadrícula sutil** — da ese toque retro pixelado

## 🏗️ Estructura del proyecto

```
culebrita_nokia_1100/
├── main.py          # Todo el juego (~230 líneas)
├── pyproject.toml   # Configuración del proyecto (UV)
├── uv.lock          # Lock de dependencias
├── .python-version  # Python 3.11
├── .gitignore       # Archivos ignorados
└── README.md        # Este archivo
```

## 🛠️ Tecnologías

- **Python 3.11** — lenguaje principal
- **Pygame 2.6** — motor gráfico 2D
- **UV** — gestor de paquetes ultrarrápido

## 📝 Licencia

Proyecto de código abierto. Úsalo, modifícalo y compártelo libremente.

---

<p align="center">
  Hecho con 🐍 y nostalgia por los 2000
</p>
