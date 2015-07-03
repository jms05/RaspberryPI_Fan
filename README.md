# RaspberryPI_Fan

No Openelec é necessário extrair RPi.zip para o lugar onde está o fanRPi.py
Ex:

-Pasta
----RPi
----fanRPi.py

Ir à pasta RPi cd RPi
Executar os seguintes comandos:
    rm __init__.py
    touch __init__.py

No raspbian não é necessário os passos anteriores, apenas executar o fanRPi.py, como sudo e comentar a linha:
    #GPIO.setwarnings(False)