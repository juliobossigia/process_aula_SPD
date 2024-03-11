import datetime
import subprocess

def executar_multiplos_processos(comando_original, num_processos):
    processos = []

    
    for _ in range(num_processos):
        processo = subprocess.Popen(comando_original, stdout=subprocess.PIPE)
        # A execução sequencial de subprocessos usando subprocess.Popen() é, por padrão, síncrona, 
        # o que significa que o próximo subprocesso só é iniciado após o término do anterior.
        processos.append(processo)

    
    for processo in processos:
        processo.wait()

    print(f"{num_processos} processos foram concluídos.")


num_processos = int(input("Quantos processos deseja executar? "))
comando = ["python3", "scanner.py"]

start_time = datetime.datetime.now()

executar_multiplos_processos(comando, num_processos)

end_time = datetime.datetime.now()
tempo_execucao = end_time - start_time
print(f"Tempo de execução: {tempo_execucao.total_seconds()} segundos")
