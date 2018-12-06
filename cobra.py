import pygame, time, random

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

#Variáveis#

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 155, 0)
verde2 = (0, 64, 0)
cinza = (147, 147, 147)
azul_claro = (30, 121, 145)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Classic 2.0')

icone = pygame.image.load('icone.png')
pygame.display.set_icon(icone)

img = pygame.image.load('cabeca.png')
#escolher o que capturar#
img2 = pygame.image.load('remy.png')
#img2 = pygame.image.load('galinha.png')
#img2 = pygame.image.load('aplle.png')

pygame.mixer.music.load("audiofundo.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

beep = pygame.mixer.Sound('beep.wav')

clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 15

direction = 'right'

font_um = pygame.font.Font('ComicSansMS3.ttf', 25)
font_dois = pygame.font.Font('ComicSansMS3.ttf', 35)
font_tres = pygame.font.Font('ComicSansMS3.ttf', 50)
font_quatro = pygame.font.Font('ComicSansMS3.ttf', 80)

def pausar():

    pause = True

    while pause:
        #o "pausar" ficará em cima
        mensagem_na_tela("O Jogo está pausado",
                          vermelho,
                          -100,
                          size="grande")
        mensagem_na_tela("Pressione J Para Jogar ou S Para Sair.",
                          preto,
                          25)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    pause = False
                elif event.key == pygame.K_s:
                    pygame.quit()
                    quit()
        clock.tick(60)

def placar(placar):
    text = font_um.render("Seu tamanho: "+str(placar), True, cinza)
    gameDisplay.blit(text, [0, 0])
    text = font_um.render("pressione P para pausar", placar, cinza)
    gameDisplay.blit(text, [520, 0])

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))
    randAppleY = round(random.randrange(0, display_height - AppleThickness))

    return randAppleX, randAppleY

def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    intro = False
                if event.key == pygame.K_s:
                    pygame.quit()
                    quit()


        gameDisplay.fill(branco)
        mensagem_na_tela("Bem-Vindo Ao Jogo :) !",
                          verde,
                          -170,
                          "grande")
        mensagem_na_tela("Regras Abaixo:",
                          preto,
                          -70,
                          "media")

        mensagem_na_tela("Seu objetivo é capturar o maior número de maçãs.",
                          preto,
                          0)

        mensagem_na_tela("Ao capturar uma mação você crescerá.",
                          preto,
                          40)

        mensagem_na_tela("Você não poderá encostar no próprio corpo ou ir para trás.",
                          preto,
                          80)

        mensagem_na_tela("Use as teclas W, A, S, D para andar.",
                          preto,
                          120)
        mensagem_na_tela("Disvirta-se :D",
                          azul_claro,
                          190)

        mensagem_na_tela("Pressione J Para Jogar, P para pausar ou S Para Sair.",
                          preto,
                          260)

        pygame.display.update()
        clock.tick(15)

def cobra(block_size, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, verde, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color, size):
    if size == 'pequena':
        textSurface = font_um.render(text, True, color)
    elif size == 'media':
        textSurface = font_dois.render(text, True, color)
    elif size == 'grande':
        textSurface = font_tres.render(text, True, color)
    elif size == 'enorme':
        textSurface = font_quatro.render(text, True, color)

    return textSurface, textSurface.get_rect()


def mensagem_na_tela(msg, color, y_displace=0, size = "pequena"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2 ), (display_height / 2 ) +y_displace
    gameDisplay.blit(textSurf, textRect)

pontos = 0
def Jogando():
    global direction, pontos
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()

    while not gameExit:

        while gameOver == True:

            gameDisplay.fill(branco)
            mensagem_na_tela("O Jogo Terminou :( !",
                             vermelho,
                             y_displace=-150,
                             size="grande")

            mensagem_na_tela("Seu tamanho final foi {}.".format(pontos),
                              preto,
                              y_displace=0,
                              size = "media")

            mensagem_na_tela("Pressione S Para Sair ou J Para Jogar Novamente.",
                              preto,
                              200,
                              size="pequena")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_j:
                        Jogando()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_d:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_w:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_s:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pausar()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(branco)

        gameDisplay.blit(img2, (randAppleX, randAppleY))


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList [0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True


        cobra(block_size, snakeList)

        placar(snakeLength)
        pontos = snakeLength
        pygame.display.update()


        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                beep.play()

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                beep.play()

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
Jogando()


#o que está abaixo sempre vai sobressair o que está em cima#