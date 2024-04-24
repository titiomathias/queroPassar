import flet as ft


def main(page: ft.Page):
    page.title = "Home"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Row(
            [
                ft.TextField(label="Adicionar Matéria", hint_text="Digite o nome da matéria aqui..."), ft.FilledButton(text="Adicionar", icon="add")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
   )

    page.horizontal_alignment = ft.MainAxisAlignment.CENTER


ft.app(main)
