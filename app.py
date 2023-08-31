import PySimpleGUI as sg
import pyautogui as bot
import math

sg.theme_background_color("white")

cabecalho = [
    [
        sg.Text(
            "Cálculo do Índice de Massa Corporal (IMC)",
            font="Doppio  14 bold",
            justification="center",
            background_color="white",
            text_color="#595959",
            pad=(12, (15, 0)),
        )
    ],
    [sg.HSep(pad=(0, (0, 0)))],
]

subtitulo = [
    sg.Text(
        "Descubra seu índice de massa corporal",
        font="Dopio 12 ",
        justification="center",
        background_color="white",
        text_color="#595959",
        pad=(60, (22, 0)),
    )
]

sexo = [
    sg.Text(
        "Sexo",
        font="Dopio 14 bold",
        justification="center",
        background_color="white",
        text_color="#595959",
        pad=(170, (18, 0)),
    )
]

sexo_2 = [
    [
        sg.Text(
            "Feminino",
            font="Dopio 11 bold",
            justification="left",
            background_color="white",
            text_color="#595959",
            pad=(70, (22, 0)),
        ),
        sg.Text(
            "Masculino",
            font="Dopio 11 bold",
            justification="right",
            background_color="white",
            text_color="#595959",
            pad=(55, (21, 0)),
        ),
    ],
    [
        sg.Button(
            "",
            key="btn_feminino",
            image_filename="img\\Female.png",
            button_color="#D9D9D9",
            image_size=(132, 85),
            pad=(35, (22, 0)),
        ),
        sg.VSep(pad=(0, (22, 0)), color="Black"),
        sg.Text(
            "",
            background_color="white",
            pad=(15, (0, 0)),
        ),
        sg.Button(
            "",
            key="btn_masculino",
            image_filename="img\\Male.png",
            button_color="#D9D9D9",
            image_size=(132, 85),
            pad=(10, (22, 0)),
        ),
    ],
]

altura = [
    [
        sg.Text(
            "Altura e peso",
            font="Dopio 13 bold",
            justification="center",
            background_color="white",
            text_color="gray",
            expand_x=True,
            pad=(0, (45, 0)),
        )
    ],
    [
        sg.Text("", pad=(50, (5, 0)), background_color="white"),
        sg.Image(
            filename="Sewing Tape Measure.png",
            background_color="white",
            pad=(5, (5, 0)),
        ),
        sg.Input("",
            
            background_color="#D9D9D9",
            text_color="White",
            font="Dopio 9 bold",
            justification="c",
            key='input_altura',
            size=(20, 5),
            pad=(0, (5, 0)),
        ),
    ],
]

peso = [
    [
        sg.Text("", pad=(47, (5, 0)), background_color="white"),
        sg.Image(
            filename="img\peso.png",
            background_color="white",
            pad=(5, (5, 0)),
        ),
        sg.Input( "",
            
            background_color="#D9D9D9",
            text_color="White",
            font="Dopio 9 bold",
            justification="c",
            key='input_peso',
            size=(20, 5),
            pad=(0, (5, 0)),
        ),
    ],
    [
        sg.Button(
            "OK",
            key="btn_ok",
            mouseover_colors="grey",
            pad=(195, (0, 0)),
            size=(15, 1),
        )
    ],
]

imagem = [
    sg.Image(
        filename="img\\People working out in a gym.png",
        background_color="white",
        size=(190, 178),
        pad=(
            95,
            (0, 0),
        ),
    ),
]

layout = [cabecalho, subtitulo, sexo, sexo_2, altura, peso, imagem]

window = sg.Window("Cálculo de IMC", layout=layout, size=(423, 624), margins=(0, 0))

while True:
    event, values = window.read()

    altura = values["input_altura"]
    peso = values["input_peso"]
    
    
    if event is sg.WIN_CLOSED:
        break
    
    if event == "btn_feminino" or event == "btn_masculino":
        bot.confirm(title="", text="Prossiga inserindo seus dados")
    
    if event == "btn_ok":
        if bool(altura) and bool(peso):
            try:
                calculo_imc = float(peso) / math.pow(float(altura),2)
                calculo_imc_formatado = format(calculo_imc, ".2f")
                if float(altura) <= 2.50 and float(peso) <= 280:
                    if calculo_imc < 18.5:
                        bot.confirm(title="Resultado", text=f"Seu Imc é {(calculo_imc_formatado)}. Verifique, você está abaixo do seu peso ideal.") 
                    elif calculo_imc >= 18.5 or calculo_imc <= 24.9:
                        bot.confirm(title="Resultado", text=f"Seu Imc é {(calculo_imc_formatado)}. Você está no seu peso ideal.")
                    elif calculo_imc >= 25.0 or calculo_imc <= 29.9:
                        bot.confirm(title="Resultado", text=f"Seu Imc é {(calculo_imc_formatado)}. Você está acima do peso.")
                    elif calculo_imc >= 30.0 or calculo_imc <= 34.1:
                        bot.confirm(title="Resultado", text=f"Seu Imc é {(calculo_imc_formatado)}. Você está com obesidade grau I.")
                    elif calculo_imc >= 35.0 or calculo_imc <= 39.9:
                        bot.confirm(title="Resultado", text=f"Seu Imc é {(calculo_imc_formatado)}. Você está com obesidade grau II.")
                    elif calculo_imc >=40:
                        bot.confirm(title="Resultado", text=f"Seu Imc é {(calculo_imc_formatado)}. Você está com obesidade grau III.")
                else:
                    bot.confirm(title="ERRO", text=f"Insira dados válidos",buttons=["OK"]) 
            except:
                bot.confirm(title="ERRO", text=f"Insira dados válidos",buttons=["OK"]) 
        else:
            bot.confirm(title="ERRO", text=f"POR FAVOR PREENCHA",buttons=["OK"]) 
            
        
        
        
