from turtle import title
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window


class TelaPrincipal(MDBoxLayout):

    def __init__(self, **kwargs):
        super(TelaPrincipal, self).__init__(**kwargs)

    def calcular_imc(self):
        peso = self.ids['txt_peso'].text
        peso = peso.replace(',', '.')
        altura = self.ids['txt_altura'].text
        altura = altura.replace(',', '.')
        if peso == '':
            self.ids['lbl_resultado'].text = ('O campo peso é obrigatório')
        elif altura == '':
            self.ids['lbl_resultado'].text = ('O campo altura é obrigatório')
        else:
            self.ids['lbl_resultado'].text = ('')
            peso = float(peso)
            altura = float(altura)
            imc = peso / (altura * altura)
            self.exibir_status(imc)

    def exibir_status(self, imc):
        if imc < 18.5:
            self.ids['lbl_resultado'].text = (
                f'Com {imc:.1f} kg/m² sua classificação é MAGREZA OBESIDADE GRAU 0')
        elif imc >= 18.5 and imc < 25.0:
            self.ids['lbl_resultado'].text = (
                f'Com {imc:.1f} kg/m² sua classificação é NORMAL OBESIDADE GRAU 0')
        elif imc >= 25.0 and imc < 30.0:
            self.ids['lbl_resultado'].text = (
                f'Com {imc:.1f} kg/m² sua classificação é SOBREPESO OBESIDADE GRAU I')
        elif imc >= 30.0 and imc <= 40.0:
            self.ids['lbl_resultado'].text = (
                f'Com {imc:.1f} kg/m² sua classificação é OBESIDADE GRAU II')
        elif imc > 40.0:
            self.ids['lbl_resultado'].text = (
                f'Com {imc:.1f} kg/m² sua classificação é OBESIDADE GRAU III')
        else:
            self.ids['lbl_resultado'].text = ''


class Imc(MDApp):
    def build(self):
        Window.size = (300, 500)
        return TelaPrincipal()


if __name__ == '__main__':
    Imc().run()
