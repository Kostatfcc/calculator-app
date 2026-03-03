import flet as ft

def main(page: ft.Page):
    page.title = "Калькулятор оплаты"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 400

    # Поле для ввода тарифа
    tariff_field = ft.TextField(label="Тариф (руб)", value="5.50", width=200)
    # Поле для начальных показаний
    start_field = ft.TextField(label="Начальные", value="1000", width=200)
    # Поле для конечных показаний
    end_field = ft.TextField(label="Конечные", value="1050", width=200)
    # Текст для вывода результата
    result_text = ft.Text("К оплате: 0.00 рублей", size=20)

    def calculate(e):
        try:
            T = float(tariff_field.value)
            V = int(start_field.value)
            v = int(end_field.value)
            U = v - V
            P = T * U
            result_text.value = f"К оплате: {P:.2f} рублей"
        except ValueError:
            result_text.value = "Ошибка ввода!"
        page.update()

    # Кнопка для расчета
    calculate_button = ft.ElevatedButton("Рассчитать", on_click=calculate)

    # Добавляем все элементы на страницу
    page.add(
        ft.Column(
            [
                tariff_field,
                start_field,
                end_field,
                calculate_button,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
