from datetime import datetime
from instagram import instagram
import os
import glob
from time import sleep

class GerenciadorDoInstagram:

    def __init__(self, caminho_raiz=None, semana=1, carrocel=1):
        self.caminho_raiz = caminho_raiz
        self.semana_da_postagem = semana
        self.carrocel_da_postagem = carrocel
        self.nome_do_arquivo = f'{self.semana_da_postagem} - *'
        self.dia_da_semana = datetime.today().weekday()
        self.geckodriver = r'\geckodriver.exe'

        #----Perfil: default-release----
        #Escreva "about:profiles" no firefox e descubra qual é seu perfil profile.
        self.perfil_firefox = r'C:\Users\NomeDoUsuario\AppData\Roaming\Mozilla\Firefox\Profiles\dfasfadsf.default-release'

        self.CALENDARIO_DAS_POSTAGENS = {
            'segunda_feira': os.path.join(self.caminho_raiz, 'Dicas', f'{self.nome_do_arquivo}.png'),
            'terça_feira': os.path.join(self.caminho_raiz, 'Vídeos', f'{self.nome_do_arquivo}.mp4'),
            'quarta_feira': os.path.join(self.caminho_raiz, 'Curiosidades', f'{self.nome_do_arquivo}.png'),
            'quinta_feira': os.path.join(self.caminho_raiz, 'Django', f'{self.nome_do_arquivo}.png'),
            'sexta_feira': os.path.join(self.caminho_raiz, 'Código', f'{self.nome_do_arquivo}.png'),
            'sábado': os.path.join(self.caminho_raiz, 'Memes\Img Memes', f'{self.nome_do_arquivo}.png'),
            'domingo': os.path.join(self.caminho_raiz, 'Quiz', f'{self.nome_do_arquivo}.png'),
        }

        self.interações = r'C:\Users\NomeDoUsuario\Pictures\Rede Sociais\Instagram\Interações\Publicação Python, Interações 0.png'

    def iniciar_bot_do_instagram(self, caminho_da_postagem=None, comentário=None):
        arquivo, extensao = os.path.splitext(caminho_da_postagem)
        path = list(glob.glob(caminho_da_postagem))

        self.robo = instagram(
            caminho_do_geckodriver=self.geckodriver,
            caminho_do_perfil_firefox=self.perfil_firefox)

        self.robo.abrir_o_site()
        self.robo.criar_postagem()
        self.robo.selecionar_postagem(caminho_da_postagem=path[0])

        if extensao == ".mp4":
            self.robo.selecionar_tamanho_do_vídeo()

        else:
            self.robo.adicionar_o_carrocel()

            for indice in range(len(path)):
                if indice > 1:
                    carrocel = caminho_da_postagem.replace('*', str(indice))
                    self.robo.selecionar_imagem_do_carrocel(
                        caminho_do_carrocel=carrocel)

            if not len(path) >= 10:
                self.robo.selecionar_imagem_do_carrocel(
                    caminho_do_carrocel=self.interações)

        self.robo.avançar_para_o_filtro()
        self.robo.avançar_para_o_comentario()
        self.robo.comentário(comentário=comentário)
        self.robo.compatilhar()
        # sleep(10)
        # self.robo.compatilhar()

    def obter_dia_da_semana(self):
        calendário = {
            0: self.CALENDARIO_DAS_POSTAGENS['segunda_feira'],
            1: self.CALENDARIO_DAS_POSTAGENS['terça_feira'],
            2: self.CALENDARIO_DAS_POSTAGENS['quarta_feira'],
            3: self.CALENDARIO_DAS_POSTAGENS['quinta_feira'],
            4: self.CALENDARIO_DAS_POSTAGENS['sexta_feira'],
            5: self.CALENDARIO_DAS_POSTAGENS['sábado'],
            6: self.CALENDARIO_DAS_POSTAGENS['domingo'],
        }

        comentários = {
            0: '😎 DICA 😎',
            1: '🤖 <SCRIPT> 🤖',
            2: '🤓 CURIOSIDADES 🤓',
            3: '👾 DJANGO 👾',
            4: '👽 CÓDIGO 👽',
            5: '😆 :) 😆',
            6: '🤔 QUIZ 🤔',
        }

        comentário_completo = f"""
            {comentários[self.dia_da_semana]}

            #python #pythonbasico #programador #programação
            #codigo #aprendapython #instatech #tecnologiadainformação
            #engenhariadacomputação #cienciadacomputacao #finanças #investimento #investimentos #informatica #automacao #developer #dev
            #backend #frontend #pythonparafinanças
            #powerbi #excel #computação #dicasdeprogramação
            #dicasdepython #computador #tecnologia #desenvolvedor #desenvolvedores #freelance
        """

        self.iniciar_bot_do_instagram(
            calendário[self.dia_da_semana], comentário=comentário_completo)

if __name__ == '__main__':
    teste = GerenciadorDoInstagram(
        caminho_raiz=r'C:\Users\NomeDoUsuario\Pictures\Rede Sociais\Instagram\Publicações',
        semana=1,
        carrocel=1,
    )
    teste.obter_dia_da_semana()