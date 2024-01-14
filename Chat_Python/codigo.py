
import flet as ft
import datetime


def main(pag):
    texto = ft.Text("Fluchat", size=60, color="green")
    chat = ft.Column()
    hora = datetime.datetime.now()
    hora_mensagem = hora.strftime("%A %d %B - %I: %M")


    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_men = mensagem["texto"]
            usuario_men = mensagem["usuario"]
            hora_men = mensagem["hora"]
            chat.controls.append(ft.Text(f"{hora_men}", size=8, italic=True))
            chat.controls.append(ft.Text(f"{usuario_men}: {texto_men}"))

        else:
            usuario_men = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_men} Entrou no chat...",
                                         size=10, italic=True, color="red"
                                         ))

        pag.update()

    #função PUBSUB

    pag.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pag.pubsub.send_all({
            "texto": campo_mensagem.value,
            "usuario": nome_usuario.value,
            "hora": hora_mensagem,
            "tipo": "mensagem"})
        campo_mensagem.value = ""

        pag.update()


    #variaveis do popup
    nome_usuario = ft.TextField(label="Escreva seu Nome:")
    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_men = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)


    def entrar_popup(evento):
        pag.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        pag.add(chat)
        popup.open =False
        pag.remove(botao_iniciar)
        pag.remove(texto)
        pag.add(ft.Row(
            [campo_mensagem, botao_enviar_men]
        ))


        pag.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindos ao Chat do Fluzão"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
       )

    def entrarChat(evento):
        pag.dialog = popup
        popup.open = True
        pag.update()


    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrarChat)

#Area de Adds

    pag.add(texto)
    pag.add(botao_iniciar)





ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
