# Import the "arcade" library
import arcade

arcade.open_window(1000, 800, "dibujo") #medidas pantalla
arcade.set_background_color(arcade.color.BLUE_GRAY) # color del fondo

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 1000, 200, 0, arcade.color.JUNGLE_GREEN) #color suleo

# --- Dibujo---
arcade.draw_circle_filled(500, 210, 120, arcade.color.WOOD_BROWN) #cuerpo
arcade.draw_circle_filled(500, 360, 70, arcade.color.WOOD_BROWN)  #cabeza
              #OREJAS
arcade.draw_circle_filled(435, 420, 25, arcade.color.WOOD_BROWN)  #oreja derecha
arcade.draw_circle_filled(435, 420, 15, arcade.color.PINK)  #oreja derecha por dentro
arcade.draw_circle_filled(565, 420, 25, arcade.color.WOOD_BROWN)  #oreja izq
arcade.draw_circle_filled(565, 420, 15, arcade.color.PINK)  #oreja izq por dentro
              #OJOS
arcade.draw_circle_filled(470, 380, 15, arcade.color.WHITE)  #der
arcade.draw_circle_filled(470, 380, 6, arcade.color.BLACK)  #der por dentro
arcade.draw_circle_filled(530, 380, 15, arcade.color.WHITE)  # izq
arcade.draw_circle_filled(530, 380, 6, arcade.color.BLACK)  #izq por dentro

              #MORRO
arcade.draw_circle_filled(500, 340, 30, arcade.color.BROWN_NOSE)  #der

            #NARIZ
arcade.draw_circle_filled(500, 350, 9, arcade.color.BLACK)

            #BOCA
arcade.draw_circle_filled(495, 330, 9, arcade.color.BLACK)
arcade.draw_circle_filled(495, 333, 9, arcade.color.BROWN_NOSE)
arcade.draw_circle_filled(505, 330, 9, arcade.color.BLACK)
arcade.draw_circle_filled(505, 333, 9, arcade.color.BROWN_NOSE)
arcade.draw_circle_filled(500, 333, 8, arcade.color.BROWN_NOSE)
arcade.draw_rectangle_filled(500, 331,2.5, 12, arcade.color.BLACK)

            #BRAZOS
arcade.draw_circle_filled(410, 250, 40, arcade.color.BROWN_NOSE) #DER
arcade.draw_circle_filled(410, 240, 20, arcade.color.PASTEL_BROWN) #DER DENTRO
arcade.draw_circle_filled(382, 255, 7, arcade.color.PASTEL_BROWN) #DER DENTRO1
arcade.draw_circle_filled(397, 274, 7, arcade.color.PASTEL_BROWN) #DER DENTRO2
arcade.draw_circle_filled(421, 274, 7, arcade.color.PASTEL_BROWN) #DER DENTRO3
arcade.draw_circle_filled(438, 255, 7, arcade.color.PASTEL_BROWN) #DER DENTRO4

arcade.draw_circle_filled(590, 250, 40, arcade.color.BROWN_NOSE) #IZQ
arcade.draw_circle_filled(590, 240, 20, arcade.color.PASTEL_BROWN) #IZQ DENTRO
arcade.draw_circle_filled(562, 255, 7, arcade.color.PASTEL_BROWN) #IZQ DENTRO1
arcade.draw_circle_filled(577, 274, 7, arcade.color.PASTEL_BROWN) #IZQ DENTRO2
arcade.draw_circle_filled(602, 274, 7, arcade.color.PASTEL_BROWN) #IZQ DENTRO3
arcade.draw_circle_filled(618, 255, 7, arcade.color.PASTEL_BROWN) #IZQ DENTRO4

            #PATAS
arcade.draw_circle_filled(420, 90, 50, arcade.color.BROWN_NOSE) #DER
arcade.draw_circle_filled(420, 80, 25, arcade.color.PASTEL_BROWN) #DER DENTRO

arcade.draw_circle_filled(382, 95, 9, arcade.color.PASTEL_BROWN) #DER DENTRO1
arcade.draw_circle_filled(404, 120, 9, arcade.color.PASTEL_BROWN) #DER DENTRO2
arcade.draw_circle_filled(433, 120, 9, arcade.color.PASTEL_BROWN) #DER DENTRO3
arcade.draw_circle_filled(455, 95, 9, arcade.color.PASTEL_BROWN) #DER DENTRO4

arcade.draw_circle_filled(570, 90, 50, arcade.color.BROWN_NOSE) #IZQ
arcade.draw_circle_filled(570, 80, 25, arcade.color.PASTEL_BROWN) #IZQ DENTRO

arcade.draw_circle_filled(532, 95, 9, arcade.color.PASTEL_BROWN) #DER DENTRO1
arcade.draw_circle_filled(554, 120, 9, arcade.color.PASTEL_BROWN) #DER DENTRO2
arcade.draw_circle_filled(584, 120, 9, arcade.color.PASTEL_BROWN) #DER DENTRO3
arcade.draw_circle_filled(606, 95, 9, arcade.color.PASTEL_BROWN) #DER DENTRO4

            #PINO
arcade.draw_rectangle_filled(875, 240, 50, 90, arcade.color.DARK_BROWN)   #troco
arcade.draw_triangle_filled(800, 400, 950, 400, 875, 500, arcade.color.AMAZON)
arcade.draw_triangle_filled(775, 340, 975, 340, 875, 440, arcade.color.AMAZON)
arcade.draw_triangle_filled(750, 280, 1000, 280, 875, 380, arcade.color.AMAZON)

            #FLOR
arcade.draw_rectangle_filled(100, 200, 5, 50, arcade.color.GREEN) #TALLO
arcade.draw_circle_filled(100, 220, 9, arcade.color.YELLOW) #CENTRO DE LA FLOR
arcade.draw_circle_filled(109, 210, 6, arcade.color.BARBIE_PINK) #PETALOS7
arcade.draw_circle_filled(114, 221, 6, arcade.color.BARBIE_PINK) #PETALOS6
arcade.draw_circle_filled(110, 231, 6, arcade.color.BARBIE_PINK) #PETALOS5
arcade.draw_circle_filled(99, 235, 6, arcade.color.BARBIE_PINK) #PETALOS4
arcade.draw_circle_filled(89, 230, 6, arcade.color.BARBIE_PINK) #PETALOS3
arcade.draw_circle_filled(85, 219, 6, arcade.color.BARBIE_PINK) #PETALOS2
arcade.draw_circle_filled(91, 209, 6, arcade.color.BARBIE_PINK) #PETALOS1


            #SOL
arcade.draw_circle_filled(200, 620, 100, arcade.color.YELLOW)

            #NUBE
arcade.draw_circle_filled(500, 720, 30, arcade.color.WHITE)
arcade.draw_circle_filled(540, 720, 30, arcade.color.WHITE)
arcade.draw_circle_filled(580, 720, 30, arcade.color.WHITE)
arcade.draw_circle_filled(580, 700, 30, arcade.color.WHITE)
arcade.draw_circle_filled(540, 700, 30, arcade.color.WHITE)
arcade.draw_circle_filled(500, 700, 30, arcade.color.WHITE)
arcade.draw_circle_filled(470, 710, 30, arcade.color.WHITE)
arcade.draw_circle_filled(610, 710, 30, arcade.color.WHITE)


arcade.draw_circle_filled(800, 620, 30, arcade.color.WHITE)
arcade.draw_circle_filled(840, 620, 30, arcade.color.WHITE)
arcade.draw_circle_filled(880, 620, 30, arcade.color.WHITE)
arcade.draw_circle_filled(880, 600, 30, arcade.color.WHITE)
arcade.draw_circle_filled(840, 600, 30, arcade.color.WHITE)
arcade.draw_circle_filled(800, 600, 30, arcade.color.WHITE)
arcade.draw_circle_filled(770, 610, 30, arcade.color.WHITE)
arcade.draw_circle_filled(910, 610, 30, arcade.color.WHITE)


            #MONTAÑA
arcade.draw_triangle_filled(150, 200, 350, 200, 250, 300, arcade.color.ENGLISH_GREEN)
arcade.draw_triangle_filled(220, 270, 280, 270, 250, 300, arcade.color.WHITE)


# --- final ---
arcade.finish_render()
arcade.run()
