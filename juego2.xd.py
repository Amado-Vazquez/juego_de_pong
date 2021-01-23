import pygame,sys
pygame.init()
GREEN=(   0, 255,   0)
RED= ( 255,   0,   0)
BLUE= (   0,  0,  255)


ventana=(800,600)
pantalla = pygame.display.set_mode(ventana)
Clock= pygame.time.Clock()
#Datos de mi jugador
coor_x= 30
coor_y=500-45
player_widith= 20
player_height= 100
player_xspeed= 0
#Datos pelota
pelota_x= 400
pelota_y= 300
pelota_x_speed= 6
pelota_y_speed = 3



game_over = False
while not game_over:
	for event in pygame.event.get():
		if event.type ==  pygame.QUIT:
			game_over= True
		#Teclado
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				player_xspeed = 5
			if event.key == pygame.K_a:
				player_xspeed = -5
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_d:
				player_xspeed = 0
			if event.key == pygame.K_a:
				player_xspeed = 0
	if pelota_y >500 or pelota_y<10:
		pelota_y_speed*= -1
	if pelota_x >780 or pelota_x<10:
		pelota_x_speed*= -1
	

	if  coor_x > 780 or coor_x <10:
		player_xspeed *= -1






	
	coor_x += player_xspeed
	pelota_x += pelota_x_speed
	pelota_y += pelota_y_speed


			




	pantalla.fill(GREEN)
	jugador= pygame.draw.rect(pantalla,BLUE,(coor_x,coor_y,player_height,player_widith))
	pelota= pygame.draw.circle(pantalla,RED,(pelota_x,pelota_y),10)
	if pelota.colliderect(jugador):
		pelota_x_speed *= -1
	


		


	pygame.display.flip()
	Clock.tick(100)
pygame.quit()

