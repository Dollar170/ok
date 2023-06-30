from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class SummationApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)

        self.num1 = TextInput(hint_text='Введите первое число', multiline=False)
        layout.add_widget(self.num1)

        self.num2 = TextInput(hint_text='Введите второе число', multiline=False)
        layout.add_widget(self.num2)

        btn = Button(text='Сложить')
        btn.bind(on_press=self.calculate_sum)
        layout.add_widget(btn)

        self.sum_label = Label(text='Сумма: ')
        layout.add_widget(self.sum_label)


        return layout

    def calculate_sum(self, instance):
        num1 = int(self.num1.text)
        num2 = int(self.num2.text)
        sum_result = num1 + num2
        self.sum_label.text = f'Сумма: {sum_result}'


if __name__ == '__main__':
    SummationApp().run()