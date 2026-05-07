from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import datetime

# تصميم الخلفية - أسود ملكي فخم
Window.clearcolor = get_color_from_hex('#050505')

class AlsayeghProApp(App):
    def build(self):
        self.title = "AL-SAYEGH PRO | الصايغ برو"
        root = BoxLayout(orientation='vertical', padding=25, spacing=15)
        
        # الهيدر السينمائي
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=120)
        title = Label(text="AL-SAYEGH PRO", font_size='32sp', bold=True, color=get_color_from_hex('#FFD700'))
        subtitle = Label(text="نظام إدارة وتعدين الذهب الذكي", font_size='14sp', color=get_color_from_hex('#BBBBBB'))
        header.add_widget(title)
        header.add_widget(subtitle)
        root.add_widget(header)

        # منطقة المدخلات الاحترافية
        scroll = ScrollView()
        inputs_layout = BoxLayout(orientation='vertical', spacing=12, size_hint_y=None)
        inputs_layout.bind(minimum_height=inputs_layout.setter('height'))

        def styled_input(hint):
            return TextInput(
                hint_text=hint, multiline=False, size_hint_y=None, height=55,
                background_normal='', background_color=get_color_from_hex('#151515'),
                foreground_color=(1, 1, 1, 1), hint_text_color=get_color_from_hex('#555555'),
                padding=[15, 15], font_size='18sp', cursor_color=get_color_from_hex('#FFD700')
            )

        self.ounce_in = styled_input("سعر الأونصة العالمي ($)")
        self.rate_in = styled_input("سعر الصرف (SDG)")
        self.weight_in = styled_input("الوزن (جرام)")
        self.karat_in = styled_input("العيار (مثلاً 21)")
        self.profit_in = styled_input("نسبة الربح %")

        for inp in [self.ounce_in, self.rate_in, self.weight_in, self.karat_in, self.profit_in]:
            inputs_layout.add_widget(inp)
        
        scroll.add_widget(inputs_layout)
        root.add_widget(scroll)

        # زر توليد الفاتورة
        calc_btn = Button(
            text="توليد فاتورة احترافية", size_hint_y=None, height=70,
            background_normal='', background_color=get_color_from_hex('#FFD700'),
            color=(0, 0, 0, 1), font_size='20sp', bold=True
        )
        calc_btn.bind(on_press=self.generate_invoice)
        root.add_widget(calc_btn)

        # منطقة عرض النتيجة (الفاتورة)
        self.invoice_box = Label(text="بانتظار العمليات...", font_size='15sp', markup=True, halign='center')
        root.add_widget(self.invoice_box)

        return root

    def generate_invoice(self, instance):
        try:
            ounce = float(self.ounce_in.text)
            rate = float(self.rate_in.text)
            weight = float(self.weight_in.text)
            karat = float(self.karat_in.text)
            profit_pct = float(self.profit_in.text)

            gram_price = (ounce / 31.1034) * (karat / 24) * rate
            cost = gram_price * weight
            final = cost * (1 + profit_pct / 100)
            
            now = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M")
            self.invoice_box.text = (
                f"[b][color=#FFD700]─── فاتورة الصايغ برو ───[/color][/b]\n"
                f"[color=#888888]{now}[/color]\n"
                f"سعر الجرام: [b]{gram_price:,.2f}[/b]\n"
                f"التكلفة: [b]{cost:,.2f}[/b]\n"
                f"[color=#FFD700]سعر البيع: {final:,.2f}[/color]\n"
                f"---------------------------\n"
                f"تمت العملية بنجاح"
            )
        except:
            self.invoice_box.text = "[color=#FF0000]خطأ في إدخال البيانات[/color]"

if __name__ == "__main__":
    AlsayeghProApp().run()

