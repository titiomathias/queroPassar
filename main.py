import flet as ft


def main(page: ft.Page):
    page.title = "Home"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def add_course(e):
        courses_view.controls.append(ft.TextField(label=new_course.value))
        new_course.value = ''
        view.update()

    new_course = ft.TextField(label="Adicionar Matéria", hint_text="Digite o nome da matéria aqui...", expand=True)
    courses_view = ft.Column()
    view = ft.Column(
        width=600,
        controls=[
            ft.Row(controls=[
                new_course,
                ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_course)
            ],
            ),
            courses_view,
        ],
    )

    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.add(view)


ft.app(main)
