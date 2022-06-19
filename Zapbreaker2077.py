# importa as bibliotecas que serao utilizadas no codigo
import pygame
import time
import shelve
import numpy as np
# starta o pygame
pygame.init()
# tamanho da janela
screenWidth = 640
screenHeight = 1000
# janela onde vai ser displayadas as coisa
gameWindow = pygame.display.set_mode((screenWidth, screenHeight))
# o nominho da janela
pygame.display.set_caption("Zapbreaker 2077")
# icone do lado do nome
pygame.display.set_icon(pygame.image.load('images/sprites/zap.png'))
# contador de quadros por segundo, fluidez de atualizacao da tela
fps = pygame.time.Clock()


class Paddle:
    def __init__(self, xAxisPos, yAxisPos, type):
        # formato da plataforma
        self.spriteWidth = 90
        self.spriteHeight = 24
        # posicao inicial da plataforma
        self.xAxisPos = xAxisPos - (self.spriteWidth // 2)
        self.yAxisPos = yAxisPos - (self.spriteHeight // 2)
        # velocidade de movimento da plataforma
        self.speed = 13
        # contador pra definir os quadros
        self.spriteCount = 0
        self.rect = pygame.Rect(self.xAxisPos, self.yAxisPos, self.spriteWidth, self.spriteHeight)
        self.paddleSprite1 = [pygame.image.load('images/sprites/paddle1a.png'), pygame.image.load('images/sprites/paddle1b.png'),
                         pygame.image.load('images/sprites/paddle1c.png'), pygame.image.load('images/sprites/paddle1d.png'),
                         pygame.image.load('images/sprites/paddle1e.png')]
        self.paddleSprite2 = [pygame.image.load('images/sprites/paddle2a.png'), pygame.image.load('images/sprites/paddle2b.png'),
                         pygame.image.load('images/sprites/paddle2c.png'), pygame.image.load('images/sprites/paddle2d.png'),
                         pygame.image.load('images/sprites/paddle2e.png')]
        if type == 1:
            self.paddleSprite = self.paddleSprite1
        else:
            self.paddleSprite = self.paddleSprite2

    def constructPaddle(self, gameWindow):
        if self.spriteCount + 1 >= 25:
            self.spriteCount = 0
        self.rect = pygame.Rect(self.xAxisPos, self.yAxisPos, self.spriteWidth, self.spriteHeight)
        gameWindow.blit(self.paddleSprite[self.spriteCount // 5], (self.xAxisPos, self.yAxisPos))
        self.spriteCount += 1


class Brick:
    def __init__(self, xAxisPos, yAxisPos, resistance):
        self.xAxisPos = xAxisPos
        self.yAxisPos = yAxisPos
        self.resistance = resistance
        self.brickRemainingResistance = self.resistance
        self.spriteWidth = 60
        self.spriteHeight = 25
        self.rect = pygame.Rect(self.xAxisPos, self.yAxisPos, self.spriteWidth, self.spriteHeight)

    def constructBrick(self, gameWindow, gameLevel):
        if self.resistance == 4:
            brickSprite = pygame.image.load('images/sprites/tileMetal.png')
            gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
        if 1 <= gameLevel.levelNumber <= 4:
            if self.resistance == 3:
                if self.brickRemainingResistance == 1:
                    brickSprite = pygame.image.load('images/sprites/tileGreenStrongBreak.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
                elif self.brickRemainingResistance == 2:
                    brickSprite = pygame.image.load('images/sprites/tileGreenBreak.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
                elif self.brickRemainingResistance == 3:
                    brickSprite = pygame.image.load('images/sprites/tileGreen.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
            elif self.resistance == 2:
                if self.brickRemainingResistance == 1:
                    brickSprite = pygame.image.load('images/sprites/tileOrangeStrongBreak.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
                elif self.brickRemainingResistance == 2:
                    brickSprite = pygame.image.load('images/sprites/tileOrange.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
            elif self.resistance == 1:
                if self.brickRemainingResistance == 1:
                    brickSprite = pygame.image.load('images/sprites/tilePink.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))

        if 5 <= gameLevel.levelNumber <= 7:
            if self.resistance == 3:
                if self.brickRemainingResistance == 1:
                    brickSprite = pygame.image.load('images/sprites/tileRedStrongBreak.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
                elif self.brickRemainingResistance == 2:
                    brickSprite = pygame.image.load('images/sprites/tileRedBreak.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
                elif self.brickRemainingResistance == 3:
                    brickSprite = pygame.image.load('images/sprites/tileRed.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
            elif self.resistance == 2:
                if self.brickRemainingResistance == 1:
                    brickSprite = pygame.image.load('images/sprites/tileYellowStrongBreak.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
                elif self.brickRemainingResistance == 2:
                    brickSprite = pygame.image.load('images/sprites/tileYellow.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
            elif self.resistance == 1:
                if self.brickRemainingResistance == 1:
                    brickSprite = pygame.image.load('images/sprites/tileBrown.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))

        if 8 <= gameLevel.levelNumber <= 10:
            if self.resistance == 3:
                if self.brickRemainingResistance == 1:
                    brickSprite = pygame.image.load('images/sprites/tileBlueStrongBreak.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
                elif self.brickRemainingResistance == 2:
                    brickSprite = pygame.image.load('images/sprites/tileBlueBreak.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
                elif self.brickRemainingResistance == 3:
                    brickSprite = pygame.image.load('images/sprites/tileBlue.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
            elif self.resistance == 2:
                if self.brickRemainingResistance == 1:
                    brickSprite = pygame.image.load('images/sprites/tilePurpleStrongBreak.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
                elif self.brickRemainingResistance == 2:
                    brickSprite = pygame.image.load('images/sprites/tilePurple.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))
            elif self.resistance == 1:
                if self.brickRemainingResistance == 1:
                    brickSprite = pygame.image.load('images/sprites/tileWhite.png')
                    gameWindow.blit(brickSprite, (self.xAxisPos, self.yAxisPos))


class Ball:
    def __init__(self):
        self.radius = 23
        self.xAxisPos = (screenWidth // 2) - self.radius
        self.yAxisPos = screenHeight - (gamePlatform1.spriteWidth + (self.radius * 4))
        self.speed = np.array(([10], [10]))
        self.yAxisReflection = np.array([[1, 0], [0, -1]])
        self.xAxisReflection = np.array([[-1, 0], [0, 1]])
        self.xAxisLastPos = 0
        self.yAxisLastPos = 0
        self.brokenBricks = 0
        self.ballDirection = 0
        self.reflection = 1
        self.ballsRemaining = 3
        self.brickDamage = 1
        self.special = 1
        self.ballType = 1
        self.accumulatedScore = 0
        self.spriteCount = 0
        self.rect = pygame.Rect(self.xAxisPos, self.yAxisPos, (self.radius * 2), (self.radius * 2))
        self.BallSprite1 = [pygame.image.load('images/sprites/ball1a.png'), pygame.image.load('images/sprites/ball1b.png'), pygame.image.load('images/sprites/ball1c.png'), pygame.image.load('images/sprites/ball1d.png'),
                            pygame.image.load('images/sprites/ball1e.png'), pygame.image.load('images/sprites/ball1f.png'), pygame.image.load('images/sprites/ball1g.png'), pygame.image.load('images/sprites/ball1h.png'),
                            pygame.image.load('images/sprites/ball1i.png'), pygame.image.load('images/sprites/ball1j.png'), pygame.image.load('images/sprites/ball1k.png'), pygame.image.load('images/sprites/ball1l.png'),
                            pygame.image.load('images/sprites/ball1m.png'), pygame.image.load('images/sprites/ball1n.png')]
        self.BallSprite2 = [pygame.image.load('images/sprites/ball2a.png'), pygame.image.load('images/sprites/ball2b.png'), pygame.image.load('images/sprites/ball2c.png'), pygame.image.load('images/sprites/ball2d.png'),
                            pygame.image.load('images/sprites/ball2e.png'), pygame.image.load('images/sprites/ball2f.png'), pygame.image.load('images/sprites/ball2g.png'), pygame.image.load('images/sprites/ball2h.png'),
                            pygame.image.load('images/sprites/ball2i.png'), pygame.image.load('images/sprites/ball2j.png'), pygame.image.load('images/sprites/ball2k.png'), pygame.image.load('images/sprites/ball2l.png'),
                            pygame.image.load('images/sprites/ball2m.png'), pygame.image.load('images/sprites/ball2n.png')]
        self.BallSprite3 = [pygame.image.load('images/sprites/ball3a.png'), pygame.image.load('images/sprites/ball3b.png'), pygame.image.load('images/sprites/ball3c.png'), pygame.image.load('images/sprites/ball3d.png'),
                            pygame.image.load('images/sprites/ball3e.png'), pygame.image.load('images/sprites/ball3f.png'), pygame.image.load('images/sprites/ball3g.png'), pygame.image.load('images/sprites/ball3h.png'),
                            pygame.image.load('images/sprites/ball3i.png'), pygame.image.load('images/sprites/ball3j.png'), pygame.image.load('images/sprites/ball3k.png'), pygame.image.load('images/sprites/ball3l.png'),
                            pygame.image.load('images/sprites/ball3m.png'), pygame.image.load('images/sprites/ball3n.png')]
        self.hitBrickSound = pygame.mixer.Sound('sounds/effects/Mario_Jumping-Mike_Koenig.wav')
        self.hitMetalSound = pygame.mixer.Sound('sounds/effects/stephan_schutze-anvil_impact.wav')

    def constructBall(self, gameWindow, gameLevel):
        global storyLose, menuControl, effectsSoundControl, gameBricks
        # starter speed
        self.xAxisPos += self.speed.item(0, 0)
        self.yAxisPos -= self.speed.item(1, 0)
        self.rect = pygame.Rect(self.xAxisPos, self.yAxisPos, (self.radius * 2), (self.radius * 2))


        # array pra gerar parametros de saída da tela
        endBallMatrix = np.array([0, self.yAxisPos])
        normalizedEndBallMatrix = np.linalg.norm(endBallMatrix)
        # array pra gerar parametros de reflexao na parede esquerda
        leftWallBallMatrix = np.array([self.xAxisPos, 0])
        normalizedLeftWallBallMatrix = np.linalg.norm(leftWallBallMatrix)
        # array pra gerar parametrod de reflexao na parede direita
        rightWallBallMatrix = np.array([self.xAxisPos + (self.radius * 2), 0])
        normalizedRightWallBallMatrix = np.linalg.norm(rightWallBallMatrix)

        # sai da tela
        if normalizedEndBallMatrix >= screenHeight - 80 or normalizedEndBallMatrix < 65:
            # self.reflection = np.arctan2(self.yAxisPos - self.yAxisLastPos, self.xAxisPos - self.xAxisLastPos)
            # self.speed = self.yAxisReflection @ self.speed
            if self.ballsRemaining > 1:
                self.ballsRemaining -= 1
                gameMenu.reset()
            else:
                gameWindow.blit(endGameTextUnder, (((screenWidth / 2) - 176), ((screenHeight / 2) - 56)))
                gameWindow.blit(endGameTextAbove, (((screenWidth / 2) - 174), ((screenHeight / 2) - 54)))
                pygame.display.update()
                time.sleep(2)
                storyLose = 1
                menuControl = 7
        # zapbreaked
        elif gameBall.yAxisPos < 50 or gameBall.yAxisPos > screenHeight - 50 or gameBall.xAxisPos < -23 or gameBall.xAxisPos > screenWidth - 23:
            gameWindow.blit(breakTextUnder, (30, ((screenHeight // 2) - 54)))
            gameWindow.blit(breakTextAbove, (34, ((screenHeight // 2) - 50)))
            gameWindow.blit(rebootingTextUnder, (((screenWidth // 2) - 106), ((screenHeight // 2) + 32)))
            gameWindow.blit(rebootingTextAbove, (((screenWidth // 2) - 110), ((screenHeight // 2) + 30)))
            pygame.display.update()
            if self.ballsRemaining > 1:
                self.ballsRemaining -= 1
            time.sleep(2)
            gameMenu.reset()
        # colisao paredes laterais
        elif normalizedLeftWallBallMatrix < 20 or normalizedRightWallBallMatrix > screenWidth - 20:
            self.reflection = np.arctan2(self.yAxisPos - self.yAxisLastPos, self.xAxisPos - self.xAxisLastPos)
            self.speed = self.xAxisReflection @ self.speed
            self.xAxisLastPos = self.xAxisPos
            self.yAxisLastPos = self.yAxisPos
            if effectsSoundControl == 1:
                self.hitMetalSound.play()
        # colisao plataforma1
        elif self.rect.colliderect(gamePlatform1.rect):
            # elif normalizedPaddle1BallMatrix <= self.radius + (gamePlatform1.spriteWidth // 2):
            self.reflection = np.arctan2(self.yAxisPos - self.yAxisLastPos, self.xAxisPos - self.xAxisLastPos)
            if self.reflection < 0:
                if self.xAxisPos + self.radius > gamePlatform1.xAxisPos + (gamePlatform1.spriteWidth // 2):
                    self.speed = self.yAxisReflection @ self.xAxisReflection @ self.speed
                else:
                    self.speed = self.yAxisReflection @ self.speed
            else:
                if self.xAxisPos + self.radius < gamePlatform1.xAxisPos + (gamePlatform1.spriteWidth // 2):
                    self.speed = self.yAxisReflection @ self.xAxisReflection @ self.speed
                else:
                    self.speed = self.yAxisReflection @ self.speed
            if effectsSoundControl == 1:
                self.hitMetalSound.play()
        # colisao plataforma2
        elif self.rect.colliderect(gamePlatform2.rect):
            # elif normalizedPaddle2BallMatrix <= self.radius + gamePlatform2.spriteWidth:
            self.reflection = np.arctan2(self.yAxisPos - self.yAxisLastPos, self.xAxisPos - self.xAxisLastPos)
            if self.reflection < 0:
                if self.xAxisPos + self.radius > gamePlatform2.xAxisPos + (gamePlatform2.spriteWidth // 2):
                    self.speed = self.yAxisReflection @ self.xAxisReflection @ self.speed
                else:
                    self.speed = self.yAxisReflection @ self.speed
            else:
                if self.xAxisPos + self.radius < gamePlatform2.xAxisPos + (gamePlatform2.spriteWidth // 2):
                    self.speed = self.yAxisReflection @ self.xAxisReflection @ self.speed
                else:
                    self.speed = self.yAxisReflection @ self.speed
            if effectsSoundControl == 1:
                self.hitMetalSound.play()
            # self.xAxisLastPos = self.xAxisPos
            # self.yAxisLastPos = self.yAxisPos
        # colisao blocos
        for tile in gameBricks:
            if self.rect.colliderect(tile.rect):
                self.reflection = np.arctan2(self.yAxisPos - self.yAxisLastPos, self.xAxisPos - self.xAxisLastPos)
                self.xAxisLastPos = self.xAxisPos
                self.yAxisLastPos = self.yAxisPos
                if tile.brickRemainingResistance != 0:
                    if tile.xAxisPos <= self.xAxisPos + self.radius <= tile.xAxisPos + tile.spriteWidth:
                        if self.yAxisPos <= tile.yAxisPos + tile.spriteHeight or (self.yAxisPos + (self.radius * 2)) >= tile.spriteHeight:
                            self.speed = self.yAxisReflection @ self.speed
                    else:
                        if self.xAxisPos <= tile.xAxisPos + tile.spriteWidth or (self.xAxisPos + (self.radius * 2)) >= tile.xAxisPos:
                            self.speed = self.xAxisReflection @ self.speed
                    if tile.brickRemainingResistance < 4:
                        tile.brickRemainingResistance -= self.brickDamage
                        if tile.brickRemainingResistance < 0:
                            tile.brickRemainingResistance = 0
                        self.accumulatedScore += (10 * self.special)
                        if effectsSoundControl == 1:
                            self.hitBrickSound.play()
                    else:
                        if effectsSoundControl == 1:
                            self.hitMetalSound.play()
                if tile.brickRemainingResistance == 0:
                    self.brokenBricks += 1
                    gameBricks.pop(gameBricks.index(tile))
        # verifica se a fase acabou
        if self.brokenBricks == gameLevel.totalBricks:
            saveFile = shelve.open('data/saves/savedGameState')
            if storyActive == 1:
                if playerNumber == 1:
                    saveFile["playerOnePoints"] += gameBall.accumulatedScore
                elif playerNumber == 2:
                    saveFile["playerTwoPoints"] += gameBall.accumulatedScore
                elif playerNumber == 3:
                    saveFile["playerThreePoints"] += gameBall.accumulatedScore
                elif playerNumber == 4:
                    saveFile["playerFourPoints"] += gameBall.accumulatedScore
                elif playerNumber == 5:
                    saveFile["playerFivePoints"] += gameBall.accumulatedScore
            else:
                if playerNumber == 1:
                    saveFile["playerOnePoints"] = gameBall.accumulatedScore
                elif playerNumber == 2:
                    saveFile["playerTwoPoints"] = gameBall.accumulatedScore
                elif playerNumber == 3:
                    saveFile["playerThreePoints"] = gameBall.accumulatedScore
                elif playerNumber == 4:
                    saveFile["playerFourPoints"] = gameBall.accumulatedScore
                elif playerNumber == 5:
                    saveFile["playerFivePoints"] = gameBall.accumulatedScore
            saveFile.close()
            menuControl = 7
        # alterna os sprites da bola
        if self.spriteCount + 1 >= 29:
            self.spriteCount = 0
        if self.ballType == 2:
            gameWindow.blit(self.BallSprite2[self.spriteCount // 2], (self.xAxisPos, self.yAxisPos))
        elif self.ballType == 3:
            gameWindow.blit(self.BallSprite3[self.spriteCount // 2], (self.xAxisPos, self.yAxisPos))
        else:
            gameWindow.blit(self.BallSprite1[self.spriteCount // 2], (self.xAxisPos, self.yAxisPos))
        self.spriteCount += 1


class Button:
    def __init__(self, baseSprite, selectionSprite, xAxisPos, yAxisPos, width, height):
        self.baseSprite = baseSprite
        self.selectionSprite = selectionSprite
        self.xAxisPos = xAxisPos
        self.yAxisPos = yAxisPos
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.xAxisPos, self.yAxisPos, self.width, self.height)

    def constructButton(self, gameWindow):
        # if self.xAxisPos < pygame.mouse.get_pos()[0] < self.xAxisPos + self.width and self.yAxisPos < pygame.mouse.get_pos()[1] < self.yAxisPos + self.height:
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            gameWindow.blit(pygame.image.load(self.selectionSprite), (self.xAxisPos, self.yAxisPos))
            return True
        else:
            gameWindow.blit(pygame.image.load(self.baseSprite), (self.xAxisPos, self.yAxisPos))


class Level:
    def __init__(self, levelNumber, levelName):
        self.levelNumber = levelNumber
        self.levelName = levelName
        if self.levelNumber == 1:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/musics/Divide.mp3')
            self.totalBricks = 18
            self.gameMatrix = np.array([[1, 1, 1, 1, 1, 1],
                                        [1, 1, 1, 1, 1, 1],
                                        [1, 1, 1, 1, 1, 1]])

        elif self.levelNumber == 2:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/musics/Acid Spit.mp3')
            self.totalBricks = 21
            self.gameMatrix = np.array([[0, 1, 1, 1, 0],
                                        [1, 1, 1, 1, 1],
                                        [1, 1, 2, 1, 1],
                                        [1, 1, 1, 1, 1],
                                        [0, 1, 1, 1, 0]])

        elif self.levelNumber == 3:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/musics/Quixotic.mp3')
            self.totalBricks = 20
            self.gameMatrix = np.array([[0, 1, 0, 0, 1, 0],
                                        [1, 2, 2, 2, 2, 1],
                                        [0, 2, 3, 3, 2, 0],
                                        [1, 2, 2, 2, 2, 1],
                                        [0, 1, 0, 0, 1, 0]])

        elif self.levelNumber == 4:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/musics/Sexualizer.mp3')
            self.totalBricks = 18
            self.gameMatrix = np.array([[2, 2, 4, 2, 2],
                                        [2, 2, 0, 2, 2],
                                        [2, 4, 4, 4, 2],
                                        [2, 2, 0, 2, 2],
                                        [2, 2, 4, 2, 2]])

        elif self.levelNumber == 5:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/musics/NARC.mp3')
            self.totalBricks = 29
            self.gameMatrix = np.array([[2, 0, 3, 0, 2, 0, 3, 0, 2, 0],
                                        [0, 2, 3, 2, 0, 2, 3, 2, 0, 2],
                                        [3, 0, 2, 0, 3, 0, 2, 0, 3, 0],
                                        [0, 2, 3, 2, 0, 2, 3, 2, 0, 2],
                                        [2, 0, 3, 0, 2, 0, 3, 0, 2, 0]])

        elif self.levelNumber == 6:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/musics/Technoir.mp3')
            self.totalBricks = 36
            self.gameMatrix = np.array([[1, 1, 1, 1, 1, 1],
                                        [1, 2, 2, 2, 2, 1],
                                        [1, 2, 3, 3, 2, 1],
                                        [1, 2, 3, 3, 2, 1],
                                        [1, 2, 2, 2, 2, 1],
                                        [1, 1, 1, 1, 1, 1]])

        elif self.levelNumber == 7:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/musics/Decade Dance.mp3')
            self.totalBricks = 28
            self.gameMatrix = np.array([[4, 1, 3, 3, 1, 4],
                                        [1, 3, 2, 2, 3, 1],
                                        [3, 3, 4, 4, 3, 3],
                                        [3, 3, 4, 4, 3, 3],
                                        [1, 3, 2, 2, 3, 1],
                                        [4, 1, 3, 3, 1, 4]])

        elif self.levelNumber == 8:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/musics/Fahkeet.mp3')
            self.totalBricks = 30
            self.gameMatrix = np.array([[4, 0, 1, 0, 2, 0, 1, 0, 4],
                                        [0, 0, 1, 0, 2, 0, 1, 0, 0],
                                        [4, 0, 3, 0, 2, 0, 3, 0, 4],
                                        [1, 0, 1, 2, 4, 2, 1, 0, 1],
                                        [1, 0, 1, 2, 4, 2, 1, 0, 1],
                                        [4, 0, 3, 0, 2, 0, 3, 0, 4],
                                        [0, 0, 1, 0, 2, 0, 1, 0, 0],
                                        [4, 0, 1, 0, 2, 0, 1, 0, 4]])

        elif self.levelNumber == 9:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/musics/She Swallowed Burning Coals.mp3')
            self.totalBricks = 77
            self.gameMatrix = np.array([[2, 3, 1, 1, 1, 3, 1, 1, 1, 3, 2],
                                        [2, 1, 3, 1, 1, 3, 1, 1, 3, 1, 2],
                                        [2, 1, 1, 1, 3, 2, 3, 1, 1, 1, 2],
                                        [2, 3, 3, 3, 2, 2, 2, 3, 3, 3, 2],
                                        [2, 1, 1, 1, 3, 2, 3, 1, 1, 1, 2],
                                        [2, 1, 3, 1, 1, 3, 1, 1, 3, 1, 2],
                                        [2, 3, 1, 1, 1, 3, 1, 1, 1, 3, 2]])

        elif self.levelNumber == 10:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/musics/Roller Mobster.mp3')
            self.totalBricks = 1
            self.gameMatrix = np.array([[0, 0, 0, 4, 0, 0, 0],
                                        [0, 4, 0, 4, 0, 4, 0],
                                        [0, 0, 0, 0, 0, 0, 0],
                                        [4, 4, 0, 1, 0, 4, 4],
                                        [0, 0, 0, 0, 0, 0, 0],
                                        [0, 4, 0, 4, 0, 4, 0],
                                        [0, 0, 0, 4, 0, 0, 0]])

        self.xFirstBlockPos = (screenWidth / 2) - ((self.gameMatrix.shape[0] / 2) * 65)
        self.yFirstBlockPos = (screenHeight / 2) - ((self.gameMatrix.shape[1] / 2) * 35)

    def constructLevel(self):
        global menuMusic, storyMusic, endMusic
        for lines in range(0, np.size(self.gameMatrix, 0)):
            for columns in range(0, np.size(self.gameMatrix, 1)):
                if self.gameMatrix.item(lines, columns) != 0:
                    gameBricks.append(Brick((self.xFirstBlockPos + (lines * 65)), (self.yFirstBlockPos + (columns * 35)), self.gameMatrix.item(lines, columns)))
        if musicSoundControl == 1:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play(-1)
            pygame.mixer.music.pause()
        menuMusic = 0
        storyMusic = 0
        endMusic = 0


class Menu:
    def __init__(self):
        self.storyButton = Button('images/buttons/story.png', 'images/buttons/storySelected.png', 120, 400, 400, 120)
        self.freeplayButton = Button('images/buttons/freeplay.png', 'images/buttons/freeplaySelected.png', 120, 550, 400, 120)
        self.instructionsButton = Button('images/buttons/instructions.png', 'images/buttons/instructionsSelected.png', 120, 700, 400, 120)
        self.highscoresButton = Button('images/buttons/highscores.png', 'images/buttons/highscoresSelected.png', 120, 850, 400, 120)
        self.musicOnButton = Button('images/buttons/musicOn.png', 'images/buttons/musicOnSelected.png', 25, 600, 80, 120)
        self.musicOffButton = Button('images/buttons/musicOff.png', 'images/buttons/musicOffSelected.png', 25, 600, 80, 120)
        self.effectsOnButton = Button('images/buttons/effectsOn.png', 'images/buttons/effectsOnSelected.png', 535, 600, 80, 120)
        self.effectsOffButton = Button('images/buttons/effectsOff.png', 'images/buttons/effectsOffSelected.png', 535, 600, 80, 120)
        self.newGameButton = Button('images/buttons/newgameButton.png', 'images/buttons/newgameButtonSelected.png', 120, 400, 400, 120)
        self.loadGameButton = Button('images/buttons/loadgameButton.png', 'images/buttons/loadgameButtonSelected.png', 120, 600, 400, 120)
        self.level1Button = Button('images/buttons/level1.png', 'images/buttons/level1Selected.png', 80, 335, 200, 80)
        self.level2Button = Button('images/buttons/level2.png', 'images/buttons/level2Selected.png', 360, 335, 200, 80)
        self.level3Button = Button('images/buttons/level3.png', 'images/buttons/level3Selected.png', 80, 445, 200, 80)
        self.level4Button = Button('images/buttons/level4.png', 'images/buttons/level4Selected.png', 360, 445, 200, 80)
        self.level5Button = Button('images/buttons/level5.png', 'images/buttons/level5Selected.png', 80, 555, 200, 80)
        self.level6Button = Button('images/buttons/level6.png', 'images/buttons/level6Selected.png', 360, 555, 200, 80)
        self.level7Button = Button('images/buttons/level7.png', 'images/buttons/level7Selected.png', 80, 665, 200, 80)
        self.level8Button = Button('images/buttons/level8.png', 'images/buttons/level8Selected.png', 360, 665, 200, 80)
        self.level9Button = Button('images/buttons/level9.png', 'images/buttons/level9Selected.png', 80, 775, 200, 80)
        self.level10Button = Button('images/buttons/level10.png', 'images/buttons/level10Selected.png', 360, 775, 200, 80)
        self.resumeButton = Button('images/buttons/resume.png', 'images/buttons/resumeSelected.png', 179, 365, 280, 110)
        self.restartButton = Button('images/buttons/restart.png', 'images/buttons/restartSelected.png', 179, 515, 280, 110)
        self.instructionsPausedButton = Button('images/buttons/instructionsPaused.png', 'images/buttons/instructionsPausedSelected.png', 179, 665, 280, 110)
        self.continueButton = Button('images/buttons/continue.png', 'images/buttons/continueSelected.png', 179, 670, 280, 110)
        self.retryButton = Button('images/buttons/retry.png', 'images/buttons/retrySelected.png', 179, 670, 280, 110)
        self.menuButton = Button('images/buttons/menu.png', 'images/buttons/menuSelected.png', 179, 820, 280, 110)
        self.returnButton = Button('images/buttons/return.png', 'images/buttons/returnSelected.png', 80, 885, 480, 80)

    def mainMenu(self):
        global gameRunning, menuControl, musicSoundControl, effectsSoundControl, menuMusic, endMusic

        if menuMusic == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/musics/Interlude.mp3')
            if musicSoundControl == 1:
                pygame.mixer.music.play(-1)
            endMusic = 0
            menuMusic = 1

        gameWindow.blit(pygame.image.load('images/backgrounds/backgroundMenu.png'), (0, 0))
        self.storyButton.constructButton(gameWindow)
        self.freeplayButton.constructButton(gameWindow)
        self.instructionsButton.constructButton(gameWindow)
        self.highscoresButton.constructButton(gameWindow)
        if musicSoundControl == 1:
            self.musicOnButton.constructButton(gameWindow)
        else:
            self.musicOffButton.constructButton(gameWindow)
        if effectsSoundControl == 1:
            self.effectsOnButton.constructButton(gameWindow)
        else:
            self.effectsOffButton.constructButton(gameWindow)
        pygame.display.update()

        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.storyButton.constructButton(gameWindow):
                menuControl = 2
            elif self.freeplayButton.constructButton(gameWindow):
                menuControl = 3
            elif self.instructionsButton.constructButton(gameWindow):
                menuControl = 4
            elif self.highscoresButton.constructButton(gameWindow):
                menuControl = 5
            if musicSoundControl == 1:
                if self.musicOnButton.constructButton(gameWindow):
                    pygame.mixer.music.pause()
                    musicSoundControl = 0
            elif musicSoundControl == 0:
                if self.musicOffButton.constructButton(gameWindow):
                    pygame.mixer.music.unpause()
                    musicSoundControl = 1
            if effectsSoundControl == 1:
                if self.effectsOnButton.constructButton(gameWindow):
                    effectsSoundControl = 0
            elif effectsSoundControl == 0:
                if self.effectsOffButton.constructButton(gameWindow):
                    effectsSoundControl = 1
        elif event.type == pygame.QUIT:
            gameRunning = False

    def storyMenu(self):
        global gameRunning, menuControl, storyActive, storyLevel, gameLevel, backgroundGame, startTime, beginTimer, menuMusic, storyMusic, endMusic
        global story1count, story2count, story3count, story4count, story5count, story6count, story7count, story8count, story9count, story10count, story11count
        if storyActive == 0:
            saveFile = shelve.open('data/saves/savedGameState')
            if playerNumber == 1:
                saveFile["playerOnePoints"] = 0
            elif playerNumber == 2:
                saveFile["playerTwoPoints"] = 0
            elif playerNumber == 3:
                saveFile["playerThreePoints"] = 0
            elif playerNumber == 4:
                saveFile["playerFourPoints"] = 0
            elif playerNumber == 5:
                saveFile["playerFivePoints"] = 0
            gameWindow.blit(pygame.image.load('images/backgrounds/backgroundStoryLoad.jpg'), (0, 0))
            self.newGameButton.constructButton(gameWindow)
            self.loadGameButton.constructButton(gameWindow)
            self.returnButton.constructButton(gameWindow)
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.newGameButton.constructButton(gameWindow):
                    storyLevel = 1
                    saveFile["storyLevel"] = storyLevel
                    storyActive = 1
                elif self.loadGameButton.constructButton(gameWindow):
                    storyActive = 1
                elif self.returnButton.constructButton(gameWindow):
                    menuControl = 1
            elif event.type == pygame.QUIT:
                gameRunning = False
            saveFile.close()
        if storyActive == 1:
            if storyLevel == 1 or storyLevel == 3 or storyLevel == 5 or storyLevel == 7 or storyLevel == 9:
                if storyMusic == 0:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('sounds/musics/blizzard.mp3')
                    if musicSoundControl == 1:
                        pygame.mixer.music.play(-1)
                    menuMusic = 0
                    storyMusic = 1
            elif storyLevel == 2 or storyLevel == 4 or storyLevel == 6 or storyLevel == 8 or storyLevel == 10:
                if storyMusic == 0:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('sounds/musics/Detection.mp3')
                    if musicSoundControl == 1:
                        pygame.mixer.music.play(-1)
                    menuMusic = 0
                    storyMusic = 1
            else:
                if endMusic == 0:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('sounds/musics/Dust.mp3')
                    if musicSoundControl == 1:
                        pygame.mixer.music.play(-1)
                    menuMusic = 0
                    endMusic = 1
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if storyLevel == 1:
                    story1count += 1
                elif storyLevel == 2:
                    story2count += 1
                elif storyLevel == 3:
                    story3count += 1
                elif storyLevel == 4:
                    story4count += 1
                elif storyLevel == 5:
                    story5count += 1
                elif storyLevel == 6:
                    story6count += 1
                elif storyLevel == 7:
                    story7count += 1
                elif storyLevel == 8:
                    story8count += 1
                elif storyLevel == 9:
                    story9count += 1
                elif storyLevel == 10:
                    story10count += 1
                elif storyLevel == 11:
                    story11count += 1
            elif event.type == pygame.QUIT:
                gameRunning = False
            if storyLevel == 1:
                if story1count == 1:
                    gameWindow.blit(pygame.image.load('images/story/story1a.png'), (0, 0))
                elif story1count == 2:
                    gameWindow.blit(pygame.image.load('images/story/story1b.png'), (0, 0))
                elif story1count == 3:
                    gameWindow.blit(pygame.image.load('images/story/story1c.png'), (0, 0))
                elif story1count == 4:
                    gameWindow.blit(pygame.image.load('images/story/story1d.png'), (0, 0))
                elif story1count == 5:
                    gameWindow.blit(pygame.image.load('images/story/story1e.png'), (0, 0))
                elif story1count == 6:
                    gameWindow.blit(pygame.image.load('images/story/story1f.png'), (0, 0))
                elif story1count == 7:
                    backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel1.jpg')
                    gameLevel = Level(1, "No Talk")
                    gameLevel.constructLevel()
                    startTime = pygame.time.get_ticks()
                    menuControl = 8
                    beginTimer = 1
                    story1count = 1
            elif storyLevel == 2:
                if story2count == 1:
                    gameWindow.blit(pygame.image.load('images/story/story2a.png'), (0, 0))
                elif story2count == 2:
                    gameWindow.blit(pygame.image.load('images/story/story2b.png'), (0, 0))
                elif story2count == 3:
                    gameWindow.blit(pygame.image.load('images/story/story2c.png'), (0, 0))
                elif story2count == 4:
                    gameWindow.blit(pygame.image.load('images/story/story2d.png'), (0, 0))
                elif story2count == 5:
                    backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel2.jpg')
                    gameLevel = Level(2, "Down Under")
                    gameLevel.constructLevel()
                    startTime = pygame.time.get_ticks()
                    menuControl = 8
                    beginTimer = 1
                    story2count = 1
            elif storyLevel == 3:
                if story3count == 1:
                    gameWindow.blit(pygame.image.load('images/story/story3a.png'), (0, 0))
                elif story3count == 2:
                    gameWindow.blit(pygame.image.load('images/story/story3b.png'), (0, 0))
                elif story3count == 3:
                    backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel3.jpg')
                    gameLevel = Level(3, "Moving Up")
                    gameLevel.constructLevel()
                    startTime = pygame.time.get_ticks()
                    menuControl = 8
                    beginTimer = 1
                    story3count = 1
            elif storyLevel == 4:
                if story4count == 1:
                    gameWindow.blit(pygame.image.load('images/story/story4a.png'), (0, 0))
                elif story4count == 2:
                    gameWindow.blit(pygame.image.load('images/story/story4b.png'), (0, 0))
                elif story4count == 3:
                    gameWindow.blit(pygame.image.load('images/story/story4c.png'), (0, 0))
                elif story4count == 4:
                    gameWindow.blit(pygame.image.load('images/story/story4d.png'), (0, 0))
                elif story4count == 5:
                    backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel4.jpg')
                    gameLevel = Level(4, "Fun and Games")
                    gameLevel.constructLevel()
                    startTime = pygame.time.get_ticks()
                    menuControl = 8
                    beginTimer = 1
                    story4count = 1
            elif storyLevel == 5:
                if story5count == 1:
                    gameWindow.blit(pygame.image.load('images/story/story5a.png'), (0, 0))
                elif story5count == 2:
                    gameWindow.blit(pygame.image.load('images/story/story5b.png'), (0, 0))
                elif story5count == 3:
                    gameWindow.blit(pygame.image.load('images/story/story5c.png'), (0, 0))
                elif story5count == 4:
                    backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel5.jpg')
                    gameLevel = Level(5, "Into the Pit")
                    gameLevel.constructLevel()
                    startTime = pygame.time.get_ticks()
                    menuControl = 8
                    beginTimer = 1
                    story5count = 1
            elif storyLevel == 6:
                if story6count == 1:
                    gameWindow.blit(pygame.image.load('images/story/story6a.png'), (0, 0))
                elif story6count == 2:
                    gameWindow.blit(pygame.image.load('images/story/story6b.png'), (0, 0))
                elif story6count == 3:
                    backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel6.jpg')
                    gameLevel = Level(6, "Ambush")
                    gameLevel.constructLevel()
                    startTime = pygame.time.get_ticks()
                    menuControl = 8
                    beginTimer = 1
                    story6count = 1
            elif storyLevel == 7:
                if story7count == 1:
                    gameWindow.blit(pygame.image.load('images/story/story7a.png'), (0, 0))
                elif story7count == 2:
                    backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel7.jpg')
                    gameLevel = Level(7, "Stronghold")
                    gameLevel.constructLevel()
                    startTime = pygame.time.get_ticks()
                    menuControl = 8
                    beginTimer = 1
                    story7count = 1
            elif storyLevel == 8:
                if story8count == 1:
                    gameWindow.blit(pygame.image.load('images/story/story8a.png'), (0, 0))
                elif story8count == 2:
                    gameWindow.blit(pygame.image.load('images/story/story8b.png'), (0, 0))
                elif story8count == 3:
                    gameWindow.blit(pygame.image.load('images/story/story8c.png'), (0, 0))
                elif story8count == 4:
                    backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel8.jpg')
                    gameLevel = Level(8, "No Mercy")
                    gameLevel.constructLevel()
                    startTime = pygame.time.get_ticks()
                    menuControl = 8
                    beginTimer = 1
                    story8count = 1
            elif storyLevel == 9:
                if story9count == 1:
                    gameWindow.blit(pygame.image.load('images/story/story9a.png'), (0, 0))
                elif story9count == 2:
                    gameWindow.blit(pygame.image.load('images/story/story9b.png'), (0, 0))
                elif story9count == 3:
                    gameWindow.blit(pygame.image.load('images/story/story9c.png'), (0, 0))
                elif story9count == 4:
                    backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel9.jpg')
                    gameLevel = Level(9, "Take Over")
                    gameLevel.constructLevel()
                    startTime = pygame.time.get_ticks()
                    menuControl = 8
                    beginTimer = 1
                    story9count = 1
            elif storyLevel == 10:
                if story10count == 1:
                    gameWindow.blit(pygame.image.load('images/story/story10a.png'), (0, 0))
                elif story10count == 2:
                    gameWindow.blit(pygame.image.load('images/story/story10b.png'), (0, 0))
                elif story10count == 3:
                    gameWindow.blit(pygame.image.load('images/story/story10c.png'), (0, 0))
                elif story10count == 4:
                    gameWindow.blit(pygame.image.load('images/story/story10d.png'), (0, 0))
                elif story10count == 5:
                    backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel10.jpg')
                    gameLevel = Level(10, "Apocalypse")
                    gameLevel.constructLevel()
                    startTime = pygame.time.get_ticks()
                    menuControl = 8
                    beginTimer = 1
                    story10count = 1
            elif storyLevel == 11:
                if story11count == 1:
                    gameWindow.blit(pygame.image.load('images/story/story11a.png'), (0, 0))
                elif story11count == 2:
                    gameWindow.blit(pygame.image.load('images/story/story11b.png'), (0, 0))
                elif story11count == 3:
                    gameWindow.blit(pygame.image.load('images/story/story11c.png'), (0, 0))
                elif story11count == 4:
                    gameWindow.blit(pygame.image.load('images/story/story11d.png'), (0, 0))
                elif story11count == 5:
                    story11count = 1
                    menuControl = 1
                    storyActive = 0
        pygame.display.update()

    def freeplayMenu(self):
        global gameRunning, menuControl, storyActive, gameLevel, backgroundGame, startTime, beginTimer, menuMusic, endMusic

        gameWindow.blit(pygame.image.load('images/backgrounds/backgroundLevelSelection.png'), (0, 0))
        self.returnButton.constructButton(gameWindow)
        self.level1Button.constructButton(gameWindow)
        self.level2Button.constructButton(gameWindow)
        self.level3Button.constructButton(gameWindow)
        self.level4Button.constructButton(gameWindow)
        self.level5Button.constructButton(gameWindow)
        self.level6Button.constructButton(gameWindow)
        self.level7Button.constructButton(gameWindow)
        self.level8Button.constructButton(gameWindow)
        self.level9Button.constructButton(gameWindow)
        self.level10Button.constructButton(gameWindow)

        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.returnButton.constructButton(gameWindow):
                menuControl = 1
            elif self.level1Button.constructButton(gameWindow):
                backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel1.jpg')
                gameLevel = Level(1, "No Talk")
                gameLevel.constructLevel()
                startTime = pygame.time.get_ticks()
                menuControl = 8
                beginTimer = 1
                storyActive = 0
            elif self.level2Button.constructButton(gameWindow):
                backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel2.jpg')
                gameLevel = Level(2, "Down Under")
                gameLevel.constructLevel()
                startTime = pygame.time.get_ticks()
                menuControl = 8
                beginTimer = 1
                storyActive = 0
            elif self.level3Button.constructButton(gameWindow):
                backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel3.jpg')
                gameLevel = Level(3, "Moving Up")
                gameLevel.constructLevel()
                startTime = pygame.time.get_ticks()
                menuControl = 8
                beginTimer = 1
                storyActive = 0
            elif self.level4Button.constructButton(gameWindow):
                backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel4.jpg')
                gameLevel = Level(4, "Fun and Games")
                gameLevel.constructLevel()
                startTime = pygame.time.get_ticks()
                menuControl = 8
                beginTimer = 1
                storyActive = 0
            elif self.level5Button.constructButton(gameWindow):
                backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel5.jpg')
                gameLevel = Level(5, "Into the Pit")
                gameLevel.constructLevel()
                startTime = pygame.time.get_ticks()
                menuControl = 8
                beginTimer = 1
                storyActive = 0
            elif self.level6Button.constructButton(gameWindow):
                backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel6.jpg')
                gameLevel = Level(6, "Ambush")
                gameLevel.constructLevel()
                startTime = pygame.time.get_ticks()
                menuControl = 8
                beginTimer = 1
                storyActive = 0
            elif self.level7Button.constructButton(gameWindow):
                backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel7.jpg')
                gameLevel = Level(7, "Stronghold")
                gameLevel.constructLevel()
                startTime = pygame.time.get_ticks()
                menuControl = 8
                beginTimer = 1
                storyActive = 0
            elif self.level8Button.constructButton(gameWindow):
                backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel8.jpg')
                gameLevel = Level(8, "No Mercy")
                gameLevel.constructLevel()
                startTime = pygame.time.get_ticks()
                menuControl = 8
                beginTimer = 1
                storyActive = 0
            elif self.level9Button.constructButton(gameWindow):
                backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel9.jpg')
                gameLevel = Level(9, "Take Over")
                gameLevel.constructLevel()
                startTime = pygame.time.get_ticks()
                menuControl = 8
                beginTimer = 1
                storyActive = 0
            elif self.level10Button.constructButton(gameWindow):
                backgroundGame = pygame.image.load('images/backgrounds/backgroundLevel10.jpg')
                gameLevel = Level(10, "Apocalypse")
                gameLevel.constructLevel()
                startTime = pygame.time.get_ticks()
                menuControl = 8
                beginTimer = 1
                storyActive = 0
        elif event.type == pygame.QUIT:
            gameRunning = False

        pygame.display.update()

    def instructionsMenu(self):
        global gameRunning, menuControl, instructionsPause

        gameWindow.blit(pygame.image.load('images/backgrounds/backgroundInstructions.jpg'), (0, 0))
        # constroi o botao de retorno
        self.returnButton.constructButton(gameWindow)
        # retorna pro menu inicial caso clicado
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.returnButton.constructButton(gameWindow):
                if instructionsPause == 1:
                    menuControl = 6
                    instructionsPause = 0
                else:
                    menuControl = 1
        elif event.type == pygame.QUIT:
            gameRunning = False

        # atualiza a tela pra mostrar as modificacoes
        pygame.display.update()

    def highscoresMenu(self):
        global gameRunning, menuControl

        saveFile = shelve.open('data/saves/savedGameState')
        playerOnePoints = saveFile["playerOnePoints"]
        playerTwoPoints = saveFile["playerTwoPoints"]
        playerThreePoints = saveFile["playerThreePoints"]
        playerFourPoints = saveFile["playerFourPoints"]
        playerFivePoints = saveFile["playerFivePoints"]
        saveFile.close()

        highscores = [playerOnePoints, playerTwoPoints, playerThreePoints, playerFourPoints, playerFivePoints]
        highscoresSupport = np.array(highscores)
        playerNames = np.array(["Manivela", "Da", "Silva", "Junior", "Junior"])
        highscoresSupportSort = highscoresSupport.argsort()
        playerNamesSort = playerNames[highscoresSupportSort]
        highscores.sort()

        # retorna pro menu inicial caso clicado
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.returnButton.constructButton(gameWindow):
                menuControl = 1
        elif event.type == pygame.QUIT:
            gameRunning = False

        # ordem das pontuacoes
        firstPlaceUnder = gameFont.render(("1: " + str(playerNamesSort[4]) + " - " + str(highscores[4])), True, (195, 195, 195))
        firstPlaceAbove = gameFont.render(("1: " + str(playerNamesSort[4]) + " - " + str(highscores[4])), True, (0, 0, 0))
        secondPlaceUnder = gameFont.render(("2: " + str(playerNamesSort[3]) + " - " + str(highscores[3])), True, (195, 195, 195))
        secondPlaceAbove = gameFont.render(("2: " + str(playerNamesSort[3]) + " - " + str(highscores[3])), True, (0, 0, 0))
        thirdPlaceUnder = gameFont.render(("3: " + str(playerNamesSort[2]) + " - " + str(highscores[2])), True, (195, 195, 195))
        thirdPlaceAbove = gameFont.render(("3: " + str(playerNamesSort[2]) + " - " + str(highscores[2])), True, (0, 0, 0))
        fourthPlaceUnder = gameFont.render(("4: " + str(playerNamesSort[1]) + " - " + str(highscores[1])), True, (195, 195, 195))
        fourthPlaceAbove = gameFont.render(("4: " + str(playerNamesSort[1]) + " - " + str(highscores[1])), True, (0, 0, 0))
        fifthPlaceUnder = gameFont.render(("5: " + str(playerNamesSort[0]) + " - " + str(highscores[0])), True, (195, 195, 195))
        fifthPlaceAbove = gameFont.render(("5: " + str(playerNamesSort[0]) + " - " + str(highscores[0])), True, (0, 0, 0))

        # bota na tela o fundo e as pontuacoes com o respectivo jogador
        gameWindow.blit(pygame.image.load('images/backgrounds/backgroundHighscores.jpg'), (0, 0))
        gameWindow.blit(firstPlaceUnder, (174, 250))
        gameWindow.blit(firstPlaceAbove, (170, 246))
        gameWindow.blit(secondPlaceUnder, (174, 375))
        gameWindow.blit(secondPlaceAbove, (170, 371))
        gameWindow.blit(thirdPlaceUnder, (174, 495))
        gameWindow.blit(thirdPlaceAbove, (170, 491))
        gameWindow.blit(fourthPlaceUnder, (174, 615))
        gameWindow.blit(fourthPlaceAbove, (170, 611))
        gameWindow.blit(fifthPlaceUnder, (174, 735))
        gameWindow.blit(fifthPlaceAbove, (170, 731))

        # constroi o botao de retorno
        self.returnButton.constructButton(gameWindow)

        # atualiza a tela pra mostrar as modificacoes
        pygame.display.update()

    def pauseMenu(self):
        global gameRunning, menuControl, storyActive, gameLevel, beginTimer, musicSoundControl, effectsSoundControl, menuMusic, instructionsPause

        gameWindow.blit(pygame.image.load('images/backgrounds/backgroundPause.jpg'), (0, 0))
        self.resumeButton.constructButton(gameWindow)
        self.restartButton.constructButton(gameWindow)
        self.instructionsPausedButton.constructButton(gameWindow)
        self.menuButton.constructButton(gameWindow)
        if musicSoundControl == 1:
            self.musicOnButton.constructButton(gameWindow)
        else:
            self.musicOffButton.constructButton(gameWindow)
        if effectsSoundControl == 1:
            self.effectsOnButton.constructButton(gameWindow)
        else:
            self.effectsOffButton.constructButton(gameWindow)

        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.resumeButton.constructButton(gameWindow):
                menuControl = 8
            elif self.restartButton.constructButton(gameWindow):
                gameMenu.gameRestart()
                gameLevel = Level(gameLevel.levelNumber, gameLevel.levelName)
                gameLevel.constructLevel()
                menuControl = 8
            elif self.instructionsPausedButton.constructButton(gameWindow):
                menuControl = 4
                instructionsPause = 1
            elif self.menuButton.constructButton(gameWindow):
                gameMenu.gameRestart()
                menuMusic = 0
                storyActive = 0
                menuControl = 1

            if musicSoundControl == 1:
                if self.musicOnButton.constructButton(gameWindow):
                    pygame.mixer.music.pause()
                    musicSoundControl = 0
            elif musicSoundControl == 0:
                if self.musicOffButton.constructButton(gameWindow):
                    pygame.mixer.music.unpause()
                    musicSoundControl = 1

            if effectsSoundControl == 1:
                if self.effectsOnButton.constructButton(gameWindow):
                    effectsSoundControl = 0
            elif effectsSoundControl == 0:
                if self.effectsOffButton.constructButton(gameWindow):
                    effectsSoundControl = 1
        elif event.type == pygame.QUIT:
            gameRunning = False



        pygame.display.update()

    def postgameMenu(self):
        global gameRunning, menuControl, storyActive, storyLevel, storyLose, menuMusic, endMusic

        if endMusic == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/musics/Dust.mp3')
            if musicSoundControl == 1:
                pygame.mixer.music.play(-1)
            menuMusic = 0
            endMusic = 1

        gameWindow.blit(pygame.image.load('images/backgrounds/backgroundPostgame.jpg'), (0, 0))
        postgameFont = pygame.font.Font('data/fonts/True Lies.ttf', 36)
        scoreUnder = postgameFont.render(str(gameBall.accumulatedScore), True, (195, 195, 195))
        scoreAbove = postgameFont.render(str(gameBall.accumulatedScore), True, (0, 0, 0))

        saveFile = shelve.open('data/saves/savedGameState')
        if playerNumber == 1:
            playerName = playerNames[0]
            playerOnePoints = saveFile["playerOnePoints"]
            accumulatedScoreUnder = postgameFont.render(str(playerOnePoints), True, (195, 195, 195))
            accumulatedScoreAbove = postgameFont.render(str(playerOnePoints), True, (0, 0, 0))
        elif playerNumber == 2:
            playerName = playerNames[1]
            playerTwoPoints = saveFile["playerTwoPoints"]
            accumulatedScoreUnder = postgameFont.render(str(playerTwoPoints), True, (195, 195, 195))
            accumulatedScoreAbove = postgameFont.render(str(playerTwoPoints), True, (0, 0, 0))
        elif playerNumber == 3:
            playerName = playerNames[2]
            playerThreePoints = saveFile["playerThreePoints"]
            accumulatedScoreUnder = postgameFont.render(str(playerThreePoints), True, (195, 195, 195))
            accumulatedScoreAbove = postgameFont.render(str(playerThreePoints), True, (0, 0, 0))
        elif playerNumber == 4:
            playerName = playerNames[3]
            playerFourPoints = saveFile["playerFourPoints"]
            accumulatedScoreUnder = postgameFont.render(str(playerFourPoints), True, (195, 195, 195))
            accumulatedScoreAbove = postgameFont.render(str(playerFourPoints), True, (0, 0, 0))
        elif playerNumber == 5:
            playerName = playerNames[4]
            playerFivePoints = saveFile["playerFivePoints"]
            accumulatedScoreUnder = postgameFont.render(str(playerFivePoints), True, (195, 195, 195))
            accumulatedScoreAbove = postgameFont.render(str(playerFivePoints), True, (0, 0, 0))
        saveFile.close()

        playerNameUnder = postgameFont.render(playerName, True, (195, 195, 195))
        playerNameAbove = postgameFont.render(playerName, True, (0, 0, 0))
        gameWindow.blit(playerNameUnder, (250, 273))
        gameWindow.blit(playerNameAbove, (244, 269))
        gameWindow.blit(scoreUnder, (250, 425))
        gameWindow.blit(scoreAbove, (244, 421))
        gameWindow.blit(accumulatedScoreUnder, (250, 573))
        gameWindow.blit(accumulatedScoreAbove, (244, 569))
        self.menuButton.constructButton(gameWindow)

        if storyActive == 1:
            if storyLose == 1:
                self.retryButton.constructButton(gameWindow)
                if pygame.mouse.get_pressed()[0]:
                    if self.retryButton.constructButton(gameWindow):
                        menuControl = 2
                        gameMenu.gameRestart()
            else:
                self.continueButton.constructButton(gameWindow)
                if pygame.mouse.get_pressed()[0]:
                    if self.continueButton.constructButton(gameWindow):
                        storyLevel += 1
                        saveFile = shelve.open('data/saves/savedGameState')
                        saveFile["storyLevel"] = storyLevel
                        saveFile.close()
                        menuControl = 2
                        gameMenu.gameRestart()

        if pygame.mouse.get_pressed()[0]:
            if self.menuButton.constructButton(gameWindow):
                storyLevel += 1
                saveFile = shelve.open('data/saves/savedGameState')
                saveFile["storyLevel"] = storyLevel
                saveFile.close()
                storyActive = 0
                menuControl = 1
                gameMenu.gameRestart()

        pygame.display.update()

    def gameRestart(self):
        global storyLose, powerupBlock

        storyLose = 0
        powerupBlock = 0
        gameBall.ballsRemaining = 3
        gameBall.brokenBricks = 0
        gameBall.accumulatedScore = 0
        gameBricks.clear()

    def reset(self):
        countdownSeconds = 3
        for timeCountdown in range(countdownSeconds):
            countdownTextUnder = countdownFont.render(str(countdownSeconds - timeCountdown), True, (140, 255, 251))
            countdownTextAbove = countdownFont.render(str(countdownSeconds - timeCountdown), True, (255, 242, 0))
            gameWindow.blit(backgroundGame, (0, 0))
            gameWindow.blit(levelTextUnder, (25, 25))
            gameWindow.blit(levelTextAbove, (21, 21))
            gameWindow.blit(pointsTextUnder, (415, 25))
            gameWindow.blit(pointsTextAbove, (411, 21))
            gameWindow.blit(ballsRemainingTextUnder, (25, 950))
            gameWindow.blit(ballsRemainingTextAbove, (21, 946))
            gameWindow.blit(ballDamageUnder, (230, 950))
            gameWindow.blit(ballDamageAbove, (226, 946))
            gameWindow.blit(timeElapsedTextUnder, (450, 950))
            gameWindow.blit(timeElapsedTextAbove, (446, 946))
            gameWindow.blit(countdownTextUnder, (((screenWidth // 2) - 60), ((screenHeight // 2) - 60)))
            gameWindow.blit(countdownTextAbove, (((screenWidth // 2) - 64), ((screenHeight // 2) - 64)))
            pygame.display.update()
            time.sleep(1)

        gamePlatform1.xAxisPos = (screenWidth // 2) - (gamePlatform1.spriteWidth // 2)
        gamePlatform2.xAxisPos = (screenWidth // 2) - (gamePlatform2.spriteWidth // 2)
        gamePlatform1.speed = 13
        gamePlatform2.speed = 13
        gameBall.xAxisPos = (screenWidth // 2) - gameBall.radius
        gameBall.yAxisPos = screenHeight - 240
        gameBall.speed = np.array(([10], [10]))
        gameBall.brickDamage = 1
        gameBall.special = 1
        gameBall.ballType = 1

        gameBall.ballDirection = np.random.randint(1, 3)
        if gameBall.ballDirection == 2:
            gameBall.speed[0, 0] *= -1


class Powerups:
    def __init__(self):
        yAxisSpaces = np.array([np.random.randint(150, 350), np.random.randint(600, 850)])
        self.powerupType = np.random.randint(1, 4)
        self.xAxisPos = np.random.randint(20, 556)
        self.yAxisPos = np.random.choice(yAxisSpaces)
        self.spriteWidth = 54
        self.spriteHeight = 54
        self.powerupBlock = 0
        self.rect = pygame.Rect(self.xAxisPos, self.yAxisPos, self.spriteWidth, self.spriteHeight)

    def spawnPowerup(self, gameWindow):
        global powerupBlock

        if self.powerupType == 1:
            powerupSprite = pygame.image.load('images/sprites/powerupSpeed.png')
            hitPowerupSound = pygame.mixer.Sound('sounds/effects/Metroid_Door-Brandino.wav')
        elif self.powerupType == 2:
            powerupSprite = pygame.image.load('images/sprites/powerupDamage.png')
            hitPowerupSound = pygame.mixer.Sound('sounds/effects/Power_Up_Ray-Mike_Koenig-800933783.wav')
        elif self.powerupType == 3:
            powerupSprite = pygame.image.load('images/sprites/powerupExtraball.png')
            hitPowerupSound = pygame.mixer.Sound('sounds/effects/Elevator Ding-SoundBible.wav')

        if 0 < self.powerupType < 4:
            gameWindow.blit(powerupSprite, (self.xAxisPos, self.yAxisPos))

        if self.rect.colliderect(gameBall.rect):
            powerupBlock = 0
            self.powerupBoost(self.powerupType)
            if effectsSoundControl == 1:
                hitPowerupSound.play()

    def powerupBoost(self, powerupType):
        if powerupType == 1:
            if gameBall.speed[0, 0] == 10 or gameBall.speed[0, 0] == -10:
                gameBall.accumulatedScore += 100
                gameBall.special = 2
            elif gameBall.speed[0, 0] == 15 or gameBall.speed[0, 0] == -15:
                gameBall.accumulatedScore += 200
                gameBall.special = 3
            elif gameBall.speed[0, 0] == 20 or gameBall.speed[0, 0] == -20:
                gameBall.accumulatedScore += 300
                gameBall.special = 3
            elif gameBall.speed[0, 0] == 25 or gameBall.speed[0, 0] == -25:
                gameBall.accumulatedScore += 400
                gameBall.special = 4

            if 10 <= gameBall.speed[0, 0] <= 25 or -10 >= gameBall.speed[0, 0] >= -25:
                if gameBall.speed[0, 0] < 0:
                    gameBall.speed[0, 0] += -5
                else:
                    gameBall.speed[0, 0] += 5
                if gameBall.speed[1, 0] < 0:
                    gameBall.speed[1, 0] += -5
                else:
                    gameBall.speed[1, 0] += 5
            if gamePlatform1.speed <= 33:
                gamePlatform1.speed += 5
                gamePlatform2.speed += 5
            gameBall.ballType = 2

        elif powerupType == 2:
            if gameBall.brickDamage == 1:
                gameBall.brickDamage = 2
                gameBall.accumulatedScore += 200
                gameBall.special = 2
            elif gameBall.brickDamage == 2:
                gameBall.brickDamage = 3
                gameBall.accumulatedScore += 400
                gameBall.special = 3

            gameBall.ballType = 3

        elif powerupType == 3:
            gameBall.ballsRemaining += 1
            gameBall.accumulatedScore += 200


gameFont = pygame.font.Font('data/fonts/True Lies.ttf', 28)
countdownFont = pygame.font.Font('data/fonts/True Lies.ttf', 128)
zapbreakerFont = pygame.font.Font('data/fonts/Cyberpunk-Regular.ttf', 56)
rebootingTextUnder = gameFont.render("rebooting the simulation", True, (140, 255, 251))
rebootingTextAbove = gameFont.render("rebooting the simulation", True, (255, 242, 0))
breakTextUnder = zapbreakerFont.render("ZAPBREAKED", True, (140, 255, 251))
breakTextAbove = zapbreakerFont.render("ZAPBREAKED", True, (255, 242, 0))
endGameTextUnder = zapbreakerFont.render('Game Over', True, (140, 255, 251))
endGameTextAbove = zapbreakerFont.render('Game Over', True, (255, 242, 0))

menuControl, storyActive, storyLose, powerupBlock, musicSoundControl, effectsSoundControl, menuMusic, storyMusic, endMusic, beginTimer, instructionsPause = 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0
story1count, story2count, story3count, story4count, story5count, story6count, story7count, story8count, story9count, story10count, story11count = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1

gamePlatform1 = Paddle((screenWidth // 2), screenHeight - 110, 1)
gamePlatform2 = Paddle((screenWidth // 2), 110, 2)
gameBall = Ball()
gameBricks = []


# playerNumber = 1
#
# saveFile = shelve.open('data/saves/savedGameState')
# saveFile["storyLevel"] = 1
# saveFile["playerNumber"] = playerNumber
# saveFile["playerOnePoints"] = 0
# saveFile["playerTwoPoints"] = 0
# saveFile["playerThreePoints"] = 0
# saveFile["playerFourPoints"] = 0
# saveFile["playerFivePoints"] = 0
# saveFile.close()


saveFile = shelve.open('data/saves/savedGameState')
storyLevel = saveFile["storyLevel"]
playerNumber = saveFile["playerNumber"]
playerOnePoints = saveFile["playerOnePoints"]
playerTwoPoints = saveFile["playerTwoPoints"]
playerThreePoints = saveFile["playerThreePoints"]
playerFourPoints = saveFile["playerFourPoints"]
playerFivePoints = saveFile["playerFivePoints"]
saveFile.close()

playerNames = np.array(["Manivela", "Da", "Silva", "Junior", "Junior"])

# faz a musica comecar a tocar assim que abrir o jogo
pygame.mixer.music.load('sounds/musics/Interlude.mp3')
if musicSoundControl == 1:
    pygame.mixer.music.play(-1)

# main loop // ve se eu nao quitei do jogo
gameRunning = True
while gameRunning:
    fps.tick(27)

    # controla se eu fechei o jogo
    for finish in pygame.event.get():
        if finish.type == pygame.QUIT:
            gameRunning = False

    gameMenu = Menu()

    # menuControl 1 e a tela inicial
    if menuControl == 1:
        gameMenu.mainMenu()
    # menuControl 2 inicia o modo historia
    elif menuControl == 2:
        gameMenu.storyMenu()
    # menuControl 3 e a tela de selecao de fases
    elif menuControl == 3:
        gameMenu.freeplayMenu()
    # menuControl 4 e a tela com as intrucoes do jogo
    elif menuControl == 4:
        gameMenu.instructionsMenu()
    # menuControl 5 e a tela de pontuacoes
    elif menuControl == 5:
        gameMenu.highscoresMenu()
    # menuControl 6 e a tela de pause
    elif menuControl == 6:
        gameMenu.pauseMenu()
    # menuControl 7 e a tela de gameover
    elif menuControl == 7:
        gameMenu.postgameMenu()
    # menuControl 8 e o jogo
    elif menuControl == 8:
        # se apertar a tecla ESCAPE o jogo pausa
        if pygame.key.get_pressed()[pygame.K_j]:
            gameBall.brokenBricks = gameLevel.totalBricks

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            menuControl = 6

        else:
            gameTime = int((pygame.time.get_ticks() - startTime) / 1000)  # calculate how many seconds
            powerupsTime = (pygame.time.get_ticks() - startTime) / 1000

            # controla movimentacao atraves do teclado
            # para a plataforma de baixo
            if pygame.key.get_pressed()[pygame.K_RIGHT] and gamePlatform1.xAxisPos < screenWidth - (gamePlatform1.spriteWidth + gamePlatform1.speed):
                gamePlatform1.xAxisPos += gamePlatform1.speed
            elif pygame.key.get_pressed()[pygame.K_LEFT] and gamePlatform1.xAxisPos > gamePlatform1.speed:
                gamePlatform1.xAxisPos -= gamePlatform1.speed
            # para a plataforma de cima
            if pygame.key.get_pressed()[pygame.K_RIGHT] and gamePlatform2.xAxisPos > gamePlatform2.speed:
                gamePlatform2.xAxisPos -= gamePlatform2.speed
            elif pygame.key.get_pressed()[pygame.K_LEFT] and gamePlatform2.xAxisPos < screenWidth - (gamePlatform2.spriteWidth + gamePlatform2.speed):
                gamePlatform2.xAxisPos += gamePlatform2.speed

        levelTextUnder = gameFont.render(("Level: " + str(gameLevel.levelNumber) + " - " + gameLevel.levelName), True, (195, 195, 195))
        levelTextAbove = gameFont.render(("Level: " + str(gameLevel.levelNumber) + " - " + gameLevel.levelName), True, (0, 0, 0))
        pointsTextUnder = gameFont.render(("Points: " + str(gameBall.accumulatedScore)), True, (195, 195, 195))
        pointsTextAbove = gameFont.render(("Points: " + str(gameBall.accumulatedScore)), True, (0, 0, 0))
        ballsRemainingTextUnder = gameFont.render(("Balls: " + str(gameBall.ballsRemaining)), True, (195, 195, 195))
        ballsRemainingTextAbove = gameFont.render(("Balls: " + str(gameBall.ballsRemaining)), True, (0, 0, 0))
        ballDamageUnder = gameFont.render(("Damage: " + str(gameBall.brickDamage)), True, (195, 195, 195))
        ballDamageAbove = gameFont.render(("Damage: " + str(gameBall.brickDamage)), True, (0, 0, 0))
        timeElapsedTextUnder = gameFont.render(("Time: " + str(gameTime) + "s"), True, (195, 195, 195))
        timeElapsedTextAbove = gameFont.render(("Time: " + str(gameTime) + "s"), True, (0, 0, 0))

        if beginTimer == 1:
            gameMenu.reset()
            beginTimer = 0

        # bota imagens
        gameWindow.blit(backgroundGame, (0, 0))
        gameWindow.blit(levelTextUnder, (25, 25))
        gameWindow.blit(levelTextAbove, (21, 21))
        gameWindow.blit(pointsTextUnder, (415, 25))
        gameWindow.blit(pointsTextAbove, (411, 21))
        gameWindow.blit(ballsRemainingTextUnder, (25, 950))
        gameWindow.blit(ballsRemainingTextAbove, (21, 946))
        gameWindow.blit(ballDamageUnder, (230, 950))
        gameWindow.blit(ballDamageAbove, (226, 946))
        gameWindow.blit(timeElapsedTextUnder, (450, 950))
        gameWindow.blit(timeElapsedTextAbove, (446, 946))
        gamePlatform1.constructPaddle(gameWindow)
        gamePlatform2.constructPaddle(gameWindow)
        gameBall.constructBall(gameWindow, gameLevel)

        if (np.round(powerupsTime % 10) == 0) and powerupsTime > 9.999:
            gamePowerup = Powerups()
            powerupBlock = 1
        if powerupBlock == 1:
            gamePowerup.spawnPowerup(gameWindow)

        for blocks in gameBricks:
            if blocks.resistance != 0:
                blocks.constructBrick(gameWindow, gameLevel)

        # faz as coisas aparecerem na tela, atualiza tudo
        pygame.display.update()

saveFile = shelve.open('data/saves/savedGameState')
saveFile["playerNumber"] += 1
if playerNumber == 5:
    saveFile["playerNumber"] = 1
    saveFile["playerOnePoints"] = 0
else:
    if playerNumber == 2:
        if playerOnePoints != 0 and playerThreePoints != 0:
            saveFile["playerTwoPoints"] = 0
    if playerNumber == 3:
        if playerTwoPoints != 0 and playerFourPoints != 0:
            saveFile["playerThreePoints"] = 0
    if playerNumber == 4:
        if playerThreePoints != 0 and playerFivePoints != 0:
            saveFile["playerFourPoints"] = 0
    if playerNumber == 5:
        if playerFourPoints != 0 and playerOnePoints != 0:
            saveFile["playerFivePoints"] = 0
saveFile["storyLevel"] = storyLevel
saveFile.close()

# fecha o pygame
pygame.quit()
