import flet as ft


def main(page: ft.Page):
    page.title = "Minha primeira página!"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(ft.SafeArea(ft.Text("Olá, moça.")))


ft.app(main)
