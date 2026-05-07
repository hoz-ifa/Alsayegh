from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

# ضبط ألوان الواجهة لتكون سينمائية (أسود وذهبي)
Window.clearcolor = get_color_from_hex('#121212') 

class AlsayeghPro(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20

        # العنوان الرئيسي
        self.add_widget(Label(
            text='الصايغ برو - ALSAYEGH PRO',
            font_size='32sp',
            color=get_color_from_hex('#D4AF37'), # لون ذهبي
            bold=True
        ))

        # مدخلات البيانات
        self.weight = TextInput(hint_text='الوزن (جرام)', multiline=False, input_filter='float', halign='center', font_size='25sp')
        self.price_per_gram = TextInput(hint_text='سعر الجرام اليوم', multiline=False, input_filter='float', halign='center', font_size='25sp')
        
        self.add_widget(self.weight)
        self.add_widget(self.price_per_gram)

        # زر الحساب
        calc_btn = Button(
            text='احسب القيمة',
            background_color=get_color_from_hex('#D4AF37'),
            color=(1, 1, 1, 1),
            font_size='25sp',
            bold=True
        )
        calc_btn.bind(on_press=self.calculate)
        self.add_widget(calc_btn)

        # النتيجة
        self.result = Label(text='إجمالي الذهب: 0.00', font_size='28sp', color=(1, 1, 1, 1))
        self.add_widget(self.result)

    def calculate(self, instance):
        try:
            w = float(self.weight.text)
            p = float(self.price_per_gram.text)
            total = w * p
            self.result.text = f'الإجمالي: {total:,.2f}'
        except ValueError:
            self.result.text = 'يرجى إدخال أرقام صحيحة'

class SayeghApp(App):
    def build(self):
        self.title = 'Alsayegh Pro'
        return AlsayeghPro()

if __name__ == '__main__':
    SayeghApp().run()

                

