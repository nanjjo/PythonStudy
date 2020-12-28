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

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():    #이벤트가 발생하였는가
        if event.type == pygame.QUIT: #창을 닫았을 때
            running = False

    screen.blit(background, (0, 0)) #x, y  위치에 배경그리기

    pygame.display.update() # 게임화면을 다시 그리기

#pygame 종료
pygame.quit()
