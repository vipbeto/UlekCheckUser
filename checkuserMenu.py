
import os
import subprocess
import sys
import socket
import json

cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_amarela = "\033[93m"
cor_azul = "\033[94m"
cor_reset = "\033[0m"

def adicionar_ao_cache(chave, valor):
    cache = carregar_cache()  
    cache[chave] = valor
    salvar_cache(cache)  

def remover_do_cache(chave):
    cache = carregar_cache()  
    if chave in cache:
        del cache[chave]
        salvar_cache(cache) 

def obter_do_cache(chave):
    cache = carregar_cache()  
    return cache.get(chave)

def carregar_cache():
    try:
        with open('/root/UlekCheckuser/cache.json', 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {} 
    
def salvar_cache(cache):
    with open('/root/UlekCheckuser/cache.json', 'w') as arquivo:
        json.dump(cache, arquivo)


def get_network_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        network_ip = s.getsockname()[0]

        return network_ip
    except Exception as e:
        print("Não foi possível obter o endereço IP da rede:", str(e))
        return None


def verificar_processo(nome_processo):
    try:
        resultado = subprocess.check_output(["ps", "aux"]).decode()
        linhas = resultado.split('\n')
        for linha in linhas:
            if nome_processo in linha and "python" in linha:
                return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao verificar o processo: {e}")
    return False


nome_do_script = "/root/UlekCheckuser/checkuser.py"




if __name__ == "__main__":
    while True:
        os.system('clear')


        if verificar_processo(nome_do_script):
            status = f'{cor_verde}ativo{cor_reset} - porta em uso: {obter_do_cache("porta")}'
        else:
            status = f'{cor_vermelha}parado{cor_reset} - porta que será usada: {obter_do_cache("porta")}'
       
        print(f"Status: {status}")

        print(f"")

        print(f"Selecione uma opção:")
        print(f" 1 - Iniciar checkuser")
        print(f" 2 - Parar checkuser")
        print(f" 3 - Verificar links")
        print(f" 4 - Sobre")
        print(f" 0 - Sair do menu")

        option = input("Digite a opção: ")

        if option == "1":
            
            adicionar_ao_cache('porta', input("Digite a porta que deseja usar !"))

            os.system('clear')
            print(f'Porta escolhida: {obter_do_cache("porta")}')

            os.system(f'nohup python3 {nome_do_script} --port {obter_do_cache("porta")} & ')

            input(f"\nPressione a tecla enter para voltar ao menu\n\n")
        elif option == "2":
            if verificar_processo(nome_do_script):
                comando = f'fuser -n tcp {obter_do_cache("porta")} 2>/dev/null'

                try:
                    saida_bytes = subprocess.check_output(comando, shell=True)
                    pid = saida_bytes.decode('utf-8').strip()

                    print(pid)

                    if pid.isdigit():
                        subprocess.run(f"kill -9 {pid}", shell=True)
                    else:
                        print("O processo não foi encontrado.")
                        
                except subprocess.CalledProcessError:
                    print("Erro ao executar o comando.")
                remover_do_cache("porta")
            else: 
                print("O Checkuser não está ativo.")
            


            input(f"Pressione a tecla enter para voltar ao menu")
        elif option == "3":
            os.system('clear')
            if verificar_processo(nome_do_script):
                print("Abaixo os apps, e os links para cada um: ")
                print("")
                ip = get_network_ip()
                porta = obter_do_cache("porta")
                print(f" DtunnelMod - http://{ip}:{porta}/dtmod  ")
                print(f" GltunnelMod - http://{ip}:{porta}/gl ")
                print(f" AnyVpnMod - http://{ip}:{porta}/anymod ")
                print(f" Conecta4g - http://{ip}:{porta}/checkUser ")
                print("")

            else:
                print("\nInicie o serviço primeiro\n")
            input(f"Pressione a tecla enter para voltar ao menu")
                  

        elif option == "4":
            os.system('clear')
            print(f"Olá, esse é um multi-checkuser criado por @UlekBR")
            print(f"Com esse checkuser venho trazendo a possibilidade de usar em diversos apps")
            print(f"Apps como: ")
            print(f" - DtunnelMod")
            print(f" - GlTunnelMod")
            print(f" - AnyVpnMod")
            print(f" - Conecta4g")
            print(f"")
            input(f"Pressione a tecla enter para voltar ao menu")
        elif option == "0":
            sys.exit(0)
        else:
            os.system('clear')
            print(f"Selecionado uma opção invalida, tente novamente !")
            input(f"Pressione a tecla enter para voltar ao menu")