#BIBLIOTECAS

import pygame
import random
 
pygame.init()
 
#----------------------------------------------------------------------------#

#CORES
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#----------------------------------------------------------------------------#

#JANELA + FPS +FONTE 
xjanela = 800
yjanela = 480

dis = pygame.display.set_mode((xjanela, yjanela), pygame.FULLSCREEN)
pygame.display.set_caption('Jogo da Cobrinha')
 
clock = pygame.time.Clock()
 
cobraCorpo = 10
velocidade = 10
 
fonteEstilo = pygame.font.SysFont("bahnschrift", 25)
pontosFonte = pygame.font.SysFont("timesnewroman", 25)
 
#----------------------------------------------------------------------------#

#PONTOS
#FUNÇÃO QUE SERVE PARA RENDENIZAR A PONTUAÇÃO ATUAL NA TELA
def pontuacao(pontos):
    valor = pontosFonte.render("Pontos: " + str(pontos), True, green)
    dis.blit(valor, [0, 0])
 
#----------------------------------------------------------------------------#
 
#COBRA
#FUNÇÃO QUE SERVE PARA DESENHAR A COBRA NA TELA USANDO UMA LISTA DE COORDENADAS
def cobrinha(cobraCorpo, cobraLista):
    for x in cobraLista:
        pygame.draw.rect(dis, green, [x[0], x[1], cobraCorpo, cobraCorpo])
 
#----------------------------------------------------------------------------#
 
#OPÇÃO DE JOGO 
#FUNÇÃO QUE SERVE PARA RENDENIZAR UMA MENSAGEM NA TELA PARA CONTINUAR OU SAIR DO JOGO
def opcao(opc, color):
    op = fonteEstilo.render(opc, True, color)
    dis.blit(op, [xjanela / 6,yjanela / 3])
 
#----------------------------------------------------------------------------#    
 
#JOGO DA COBRINHA 
#FUNÇAO QUE SERVE PARA IMPLEMENTAR A LÓGICA DO JOGO
#INICIANDO UM LOOP PRINCIPAL ATÉ O TÉRMINO DO JOGO
def jogo():
    gameOver = False
    fecharJogo = False
 
    x1 = xjanela / 2
    y1 = yjanela / 2
 
    x1Troca = 0
    y1Troca = 0
 
    cobraLista = []
    cobraTamanho = 1
 
    frutax = round(random.randrange(0, xjanela - cobraCorpo) / 10.0) * 10.0
    frutay = round(random.randrange(0, yjanela - cobraCorpo) / 10.0) * 10.0
 
    while not gameOver:
        
        #LOOP QUE SERVE PARA GERENCIAR EVENTOS
        while fecharJogo == True:
            dis.fill(blue)
            opcao("Você Perdeu!! C-Continuar jogando S-Sair", green)
            pontuacao(cobraTamanho - 1)
            pygame.display.update()
 
            for clique in pygame.event.get():
                if clique.type == pygame.KEYDOWN:
                    if clique.key == pygame.K_s:
                        gameOver = True
                        fecharJogo = False
                    if clique.key == pygame.K_c:
                        jogo()
                   
                    #------------------------------#  
                   
        #FOR QUE FAZ A COBRA SE MOVER PELA MUDANÇA DE X E DE DA CABEÇA DA COBRA
        for clique in pygame.event.get():
            if clique.type == pygame.QUIT:
                gameOver = True
            if clique.type == pygame.KEYDOWN:
                if clique.key == pygame.K_LEFT:
                    x1Troca = - cobraCorpo
                    y1Troca = 0
                elif clique.key == pygame.K_RIGHT:
                    x1Troca = cobraCorpo
                    y1Troca = 0
                elif clique.key == pygame.K_UP:
                    y1Troca = - cobraCorpo
                    x1Troca = 0
                elif clique.key == pygame.K_DOWN:
                    y1Troca = cobraCorpo
                    x1Troca = 0
                    
                    #------------------------------#
        
        #COLISÕES COM O PRÓPRIO CORPO E COM AS FRUTAS
        #EM QUE VOCÊ PERDE O JOGO, OU, O TAMANHO DA COBRINHA É INCREMENTADO RESPECTIVAMENTE
        if x1 >= xjanela or x1 < 0 or y1 >= yjanela or y1 < 0:
            fecharJogo = True
        x1 += x1Troca
        y1 += y1Troca
        dis.fill(blue)
        pygame.draw.rect(dis, red, [frutax, frutay, cobraCorpo, cobraCorpo])
        cobraCabeca = []
        cobraCabeca.append(x1)
        cobraCabeca.append(y1)
        cobraLista.append(cobraCabeca)
        if len(cobraLista) > cobraTamanho:
            del cobraLista[0]
 
        for x in cobraLista[:-1]:
            if x == cobraCabeca:
                fecharJogo = True
 
        cobrinha(cobraCorpo, cobraLista)
        pontuacao(cobraTamanho - 1)
 
        pygame.display.update()
 
        if x1 == frutax and y1 == frutay:
            frutax = round(random.randrange(0, xjanela - cobraCorpo) / 10.0) * 10.0
            frutay = round(random.randrange(0, yjanela - cobraCorpo) / 10.0) * 10.0
            cobraTamanho += 1
 
        clock.tick(20)
 
    pygame.quit()
    quit()
 
jogo()