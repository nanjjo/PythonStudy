import pygame

pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정\
pygame.display.set_caption("abc")

#배경이미지 불러오기
background = pygame.image.load("C:\\Users\\mussy\\OneDrive\\바탕 화면\\PythonStudy\\pygame_basic\\background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\mussy\\OneDrive\\바탕 화면\\PythonStudy\\pygame_basic\\character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
charater_x_pos = (screen_width / 2) - (character_width / 2)
charater_y_pos = screen_height - character_height

#이동할 좌표
to_x = 0
to_y = 0

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():    #이벤트가 발생하였는가
        if event.type == pygame.QUIT: #창을 닫았을 때
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌렸는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
            
        if event.type == pygame.KEYUP: #방향 키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            
    charater_x_pos += to_x
    charater_y_pos += to_y

    # 가로 경계값 처리
    if charater_x_pos < 0:
        charater_x_pos = 0
    elif charater_x_pos > (screen_width - character_width):
        charater_x_pos = (screen_width - character_width)
    
    # 세로 경계값 처리
    if charater_y_pos < 0:
        charater_y_pos = 0
    elif charater_y_pos > (screen_height - character_height):
        charater_y_pos = (screen_height - character_height)
    

    screen.blit(background, (0, 0)) #x, y  위치에 배경그리기

    screen.blit(character, (charater_x_pos, charater_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기

#pygame 종료
pygame.quit()
