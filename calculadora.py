from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

# Configuración del tamaño de la ventana
Window.size = (399, 500)

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # 1. Pantalla de resultados (TextInput)
        self.result = TextInput(
            multiline=False,
            size_hint_y=0.2,
            halign='right',
            font_size=55,
            readonly=True,
            background_color=[0.1, 0.1, 0.1, 1], # Fondo oscuro
            foreground_color=[1, 1, 1, 1]        # Texto blanco
        )
        self.add_widget(self.result)

        # 2. Definición de botones
        buttons = [
            ['C', '+/-', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '00', '.', '='],
        ]

        # 3. Rejilla de botones (GridLayout)
        grid = GridLayout(cols=4, spacing=5, padding=10)
        
        for row in buttons:
            for item in row:
                button = Button(
                    text=item,
                    font_size=32,
                    on_press=self.button_click,
                    # Aplicamos el color según el tipo de botón
                    background_color=self.get_button_color(item),
                    # Quitamos la textura gris por defecto para que el color sea real
                    background_normal='',
                    color=[1, 1, 1, 1] # Texto blanco
                )
                grid.add_widget(button)
        
        self.add_widget(grid)

    def get_button_color(self, label):
        """Devuelve el color RGBA según el texto del botón"""
        if label in {'C', '+/-', '%'}:
            return [0.6, 0.6, 0.6, 1]  # Gris claro
        elif label in {'/', '*', '-', '+', '='}:
            return [1, 0.65, 0, 1]     # NARANJA brillante
        return [0.3, 0.3, 0.3, 1]      # Gris oscuro para números

    def button_click(self, instance):
        current_text = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ""
        
        elif button_text == '=':
            if current_text:
                try:
                    # eval() evalúa el string como una operación matemática
                    self.result.text = str(eval(current_text))
                except Exception:
                    self.result.text = "Error"
        
        elif button_text == '+/-':
            if current_text.startswith('-'):
                self.result.text = current_text[1:]
            elif current_text:
                self.result.text = '-' + current_text
        
        elif button_text == '%':
            if current_text:
                try:
                    self.result.text = str(float(current_text) / 100)
                except:
                    self.result.text = "Error"
        
        else:
            # Añadir el número o el operador a la pantalla
            self.result.text += button_text

class CalculatorApp(App):
    def build(self):
        self.title = "Calculadora Kivy"
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()