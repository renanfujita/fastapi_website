import time

def fazer_pedido_sincrono (id_pedido):
    print (f"[Sync] Começando pedido {id_pedido}...")
    time.sleep(2) 
    print(f"[Sync] Pedido {id_pedido} pronto!")

def executar_sincrono():
    print ("-----INICANDO MODO SINCRONO--------")
    inicio = time.time()

    fazer_pedido_sincrono(1)
    fazer_pedido_sincrono(2)
    fazer_pedido_sincrono(3)

    fim = time.time()
    print(f"----Tempo total Sincrono: {fim - inicio:.2f} segundos ----- \n")

if __name__ == "__main__":
    executar_sincrono()