from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.core.window import Window


class TelaPrincipal(MDBoxLayout):

    def __init__(self, **kwargs):
        super(TelaPrincipal, self).__init__(**kwargs)

    def calcular_imc(self):
        peso = self.ids['txt_peso'].text
        altura = self.ids['txt_altura'].text
        peso = float(peso)
        altura = float(altura)
        imc = peso / (altura * altura)
        self.ids['lbl_resultado'].text = (
            f'O IMC calculado é de {imc:.1f} kg/m²')


class Imc(MDApp):
    def build(self):
        Window.size = (300, 500)
        return TelaPrincipal()


if __name__ == '__main__':
    Imc().run()
