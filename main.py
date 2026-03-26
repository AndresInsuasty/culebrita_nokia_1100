import pygame
import random
import sys

# --- Constantes ---
ANCHO_VENTANA = 600
ALTO_VENTANA = 400
TAMANO_CELDA = 20
COLUMNAS = ANCHO_VENTANA // TAMANO_CELDA  # 30
FILAS = ALTO_VENTANA // TAMANO_CELDA  # 20

# Colores (R, G, B)
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
VERDE_OSCURO = (0, 150, 0)
ROJO = (220, 30, 30)
BLANCO = (255, 255, 255)
GRIS = (40, 40, 40)

# Velocidad
VELOCIDAD_INICIAL = 8
INCREMENTO_VELOCIDAD = 0.5

# Direcciones
ARRIBA = (0, -1)
ABAJO = (0, 1)
IZQUIERDA = (-1, 0)
DERECHA = (1, 0)


class Juego:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pygame.time.Clock()
        self.fuente_grande = pygame.font.SysFont("arial", 48, bold=True)
        self.fuente_media = pygame.font.SysFont("arial", 24)
        self.fuente_pequena = pygame.font.SysFont("arial", 18)
        self.estado = "inicio"
        self.nueva_partida()

    def nueva_partida(self):
        centro_x = COLUMNAS // 2
        centro_y = FILAS // 2
        self.culebrita = [
            (centro_x, centro_y),
            (centro_x - 1, centro_y),
            (centro_x - 2, centro_y),
        ]
        self.direccion = DERECHA
        self.siguiente_direccion = DERECHA
        self.puntaje = 0
        self.velocidad = VELOCIDAD_INICIAL
        self.fruta = self.generar_fruta()

    def generar_fruta(self):
        while True:
            posicion = (
                random.randint(0, COLUMNAS - 1),
                random.randint(0, FILAS - 1),
            )
            if posicion not in self.culebrita:
                return posicion

    def procesar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.KEYDOWN:
                if self.estado == "inicio":
                    if evento.key == pygame.K_RETURN:
                        self.estado = "jugando"

                elif self.estado == "jugando":
                    if evento.key == pygame.K_UP and self.direccion != ABAJO:
                        self.siguiente_direccion = ARRIBA
                    elif evento.key == pygame.K_DOWN and self.direccion != ARRIBA:
                        self.siguiente_direccion = ABAJO
                    elif evento.key == pygame.K_LEFT and self.direccion != DERECHA:
                        self.siguiente_direccion = IZQUIERDA
                    elif evento.key == pygame.K_RIGHT and self.direccion != IZQUIERDA:
                        self.siguiente_direccion = DERECHA

                elif self.estado == "game_over":
                    if evento.key == pygame.K_RETURN:
                        self.nueva_partida()
                        self.estado = "jugando"

        return True

    def mover(self):
        self.direccion = self.siguiente_direccion
        cabeza_x, cabeza_y = self.culebrita[0]
        nueva_cabeza = (
            cabeza_x + self.direccion[0],
            cabeza_y + self.direccion[1],
        )

        # Verificar colision con paredes
        if (
            nueva_cabeza[0] < 0
            or nueva_cabeza[0] >= COLUMNAS
            or nueva_cabeza[1] < 0
            or nueva_cabeza[1] >= FILAS
        ):
            self.estado = "game_over"
            return

        # Verificar colision consigo misma
        if nueva_cabeza in self.culebrita:
            self.estado = "game_over"
            return

        self.culebrita.insert(0, nueva_cabeza)

        # Verificar si comio fruta
        if nueva_cabeza == self.fruta:
            self.puntaje += 10
            self.velocidad += INCREMENTO_VELOCIDAD
            self.fruta = self.generar_fruta()
        else:
            self.culebrita.pop()

    def dibujar_cuadricula(self):
        for x in range(0, ANCHO_VENTANA, TAMANO_CELDA):
            pygame.draw.line(self.pantalla, GRIS, (x, 0), (x, ALTO_VENTANA))
        for y in range(0, ALTO_VENTANA, TAMANO_CELDA):
            pygame.draw.line(self.pantalla, GRIS, (0, y), (ANCHO_VENTANA, y))

    def dibujar(self):
        self.pantalla.fill(NEGRO)

        if self.estado == "inicio":
            self.dibujar_pantalla_inicio()
        elif self.estado == "jugando":
            self.dibujar_pantalla_juego()
        elif self.estado == "game_over":
            self.dibujar_pantalla_game_over()

        pygame.display.flip()

    def dibujar_pantalla_inicio(self):
        titulo = self.fuente_grande.render("CULEBRITA", True, VERDE)
        subtitulo = self.fuente_media.render("Nokia 1100", True, GRIS)
        instruccion = self.fuente_pequena.render(
            "Presiona ENTER para jugar", True, BLANCO
        )

        self.pantalla.blit(
            titulo,
            (ANCHO_VENTANA // 2 - titulo.get_width() // 2, 120),
        )
        self.pantalla.blit(
            subtitulo,
            (ANCHO_VENTANA // 2 - subtitulo.get_width() // 2, 180),
        )
        self.pantalla.blit(
            instruccion,
            (ANCHO_VENTANA // 2 - instruccion.get_width() // 2, 280),
        )

    def dibujar_pantalla_juego(self):
        self.dibujar_cuadricula()

        # Dibujar culebrita
        for i, (x, y) in enumerate(self.culebrita):
            color = VERDE if i == 0 else VERDE_OSCURO
            rect = pygame.Rect(
                x * TAMANO_CELDA, y * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA
            )
            pygame.draw.rect(self.pantalla, color, rect)
            pygame.draw.rect(self.pantalla, NEGRO, rect, 1)

        # Dibujar fruta
        fruta_rect = pygame.Rect(
            self.fruta[0] * TAMANO_CELDA,
            self.fruta[1] * TAMANO_CELDA,
            TAMANO_CELDA,
            TAMANO_CELDA,
        )
        pygame.draw.rect(self.pantalla, ROJO, fruta_rect)
        pygame.draw.rect(self.pantalla, NEGRO, fruta_rect, 1)

        # Dibujar puntaje
        texto_puntaje = self.fuente_pequena.render(
            f"Puntaje: {self.puntaje}", True, BLANCO
        )
        self.pantalla.blit(texto_puntaje, (10, 5))

    def dibujar_pantalla_game_over(self):
        titulo = self.fuente_grande.render("GAME OVER", True, ROJO)
        puntaje = self.fuente_media.render(
            f"Puntaje final: {self.puntaje}", True, BLANCO
        )
        instruccion = self.fuente_pequena.render(
            "Presiona ENTER para reiniciar", True, BLANCO
        )

        self.pantalla.blit(
            titulo,
            (ANCHO_VENTANA // 2 - titulo.get_width() // 2, 120),
        )
        self.pantalla.blit(
            puntaje,
            (ANCHO_VENTANA // 2 - puntaje.get_width() // 2, 200),
        )
        self.pantalla.blit(
            instruccion,
            (ANCHO_VENTANA // 2 - instruccion.get_width() // 2, 280),
        )

    def ejecutar(self):
        ejecutando = True
        while ejecutando:
            ejecutando = self.procesar_eventos()

            if self.estado == "jugando":
                self.mover()

            self.dibujar()
            self.reloj.tick(self.velocidad)

        pygame.quit()
        sys.exit()


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Culebrita - Nokia 1100")
    juego = Juego(pantalla)
    juego.ejecutar()


if __name__ == "__main__":
    main()
