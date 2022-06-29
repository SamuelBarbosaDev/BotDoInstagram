from selenium import webdriver
from time import sleep
import pyperclip as pc
import pyautogui as py


class instagram:

    def __init__(self, caminho_do_geckodriver=None, caminho_do_perfil_firefox=None):
        self.SITE_LINK = 'https://www.instagram.com/'
        self.SITE_MAP = {
            'instagram': {
                'popup': {
                    'notificações': '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]'
                },
                'postagem': {
                    'criar_postagem': '//div[@class="_acub"]/button[@class="_abl- _abm2"]',
                    'selecionar_postagem': '//div[@class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _ab9x _aba7"]/button[@class="_acan _acap _acas"]',
                    'adicionar_o_carrocel': '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/button',
                    'selecionar_imagem_do_carrocel': '//div[@class="_aab3 _aab7"]/div[@class="_aaef"]',
                    'selecionar_tamanho_do_vídeo': '//div[@class="_abfz _abg1"]/button[@class="_acan _acao _acas"]',
                    'selecionar_tamanho_original_do_vídeo': '//div[@class="_ac36 _ac38"]/button[@class="_acan _acao _acas"]',
                    'avança_para_selecionar_frame_do_vídeo': '//div[@class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _ab9- _abaa"]/button[@class="_acan _acao _acas"]',
                    'avançar_para_o_filtro': '//div[@class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _ab9- _abaa"]/button[@class="_acan _acao _acas"]',
                    'avançar_para_o_comentario': '//div[@class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _ab9- _abaa"]/button[@class="_acan _acao _acas"]',
                    'comentário': '//div[@class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p"]/textarea[@class="_ablz _aaeg"]',
                    'compatilhar': '//div[@class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _ab9- _abaa"]/button[@class="_acan _acao _acas"]',
                }
            }
        }
        # options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Firefox(
            firefox_profile=caminho_do_perfil_firefox,
            executable_path=caminho_do_geckodriver,
            # options=options,
        )

    def abrir_o_site(self):
        self.driver.get(self.SITE_LINK)

    def pop_up_notificações(self, dormi=5):
        sleep(dormi)
        self.driver.find_element_by_xpath(
            self.SITE_MAP['instagram']['popup']['notificações']
        ).click()

    def criar_postagem(self, dormi=5):
        sleep(dormi)
        self.driver.find_element_by_xpath(
            self.SITE_MAP['instagram']['postagem']['criar_postagem']
        ).click()

    def selecionar_postagem(self, caminho_da_postagem=None, dormi=5):
        sleep(dormi)
        self.driver.find_element_by_xpath(
            self.SITE_MAP['instagram']['postagem']['selecionar_postagem']
        ).click()

        pc.copy(
            caminho_da_postagem
        )
        sleep(dormi)
        py.hotkey('ctrl', 'v')
        sleep(dormi)
        py.hotkey('enter')

    def adicionar_o_carrocel(self, dormi=5):
        sleep(dormi)
        self.driver.find_element_by_xpath(
            self.SITE_MAP['instagram']['postagem']['adicionar_o_carrocel']
        ).click()

    def selecionar_imagem_do_carrocel(self, caminho_do_carrocel=None, dormi=5):
        sleep(dormi)
        self.driver.find_element_by_xpath(
            self.SITE_MAP['instagram']['postagem']['selecionar_imagem_do_carrocel']
        ).click()

        sleep(dormi)
        pc.copy(
            caminho_do_carrocel
        )
        sleep(dormi)
        py.hotkey('ctrl', 'v')
        sleep(dormi)
        py.hotkey('enter')

    def selecionar_tamanho_do_vídeo(self, dormi=5):
        sleep(dormi)
        self.driver.find_element_by_xpath(
            self.SITE_MAP['instagram']['postagem']['selecionar_tamanho_do_vídeo']
        ).click()

        self.driver.find_element_by_xpath(
            self.SITE_MAP['instagram']['postagem']['selecionar_tamanho_original_do_vídeo']
        ).click()

    def avançar_para_o_filtro(self, dormi=5):
        sleep(dormi)
        self.driver.find_element_by_xpath(
            self.SITE_MAP['instagram']['postagem']['avançar_para_o_filtro']
        ).click()

    def avançar_para_o_comentario(self, dormi=5):
        sleep(dormi)
        self.driver.find_element_by_xpath(
            self.SITE_MAP['instagram']['postagem']['avançar_para_o_comentario']
        ).click()

    def comentário(self, comentário=None, dormi=5):
        sleep(dormi)

        self.driver.find_element_by_xpath(
            self.SITE_MAP['instagram']['postagem']['comentário']
        ).send_keys(comentário)

    def compatilhar(self, dormi=5):
        sleep(dormi)
        self.driver.find_element_by_xpath(
            self.SITE_MAP['instagram']['postagem']['compatilhar']
        ).click()
        sleep(10)

    def unfollow(self, dormi=5):
        #ainda não é funcional
        self.driver.get(self.SITE_LINK+'samuelbarbosa_dev/following/')
        unfollow = {
            'unfollow': {
                'deixar_de_segui': 3,
            }
        }
        sleep(5)
        print('-'*100)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/ul/div/li[1]/div/div[2]/button').click()
        sleep(10)
        # for número in range(51):
        #     if número == 0:
        #         continue
        #     deixar_de_segui = f'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/ul/div/li[1]/div/div[2]/button'

        #     print(deixar_de_segui)
        #     sleep(3)


if __name__ == '__main__':
    comentário = """comentário."""
    postagem = r'Vídeos\1 - 1.mp4' #caminho da postagem
    carrocel = r'Publicação Python, Interações 0.png' #caminho do carrocel
    geckodriver = r'\geckodriver.exe'
    
    #----Perfil: default-release----
    #Escreva "about:profiles" no firefox e descubra qual é seu perfil profile.
    perfil_firefox = r'C:\Users\NomeDoUsuario\AppData\Roaming\Mozilla\Firefox\Profiles\dfasfadsf.default-release' 

    robo = instagram(caminho_do_geckodriver=geckodriver,
                     caminho_do_perfil_firefox=perfil_firefox)
    robo.abrir_o_site()
    robo.criar_postagem()
    robo.selecionar_postagem(caminho_da_postagem=postagem)
    robo.selecionar_tamanho_do_vídeo()
    robo.avançar_para_o_filtro()
    robo.avançar_para_o_comentario()
    robo.comentário(comentário=comentário)
    robo.compatilhar()
