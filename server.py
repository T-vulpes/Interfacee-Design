import csv
import socket
import threading

# Sabitler
PORT = 37256
IP = '192.168.77.218'
ADDR = (IP, PORT)

SIZE = 1024
FORMAT = "utf-8"


class ServerSide:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = set()
        self.connected = False

    def connect(self):
        self.server.bind(ADDR)
        self.server.listen(2)  # Max 2 cihaz bağlanabilir
        print(f"[LISTENING] Server {IP}:{PORT} dinlemede...")
        while True:
            client_socket, client_address = self.server.accept()
            self.clients.add(client_socket)
            print(f"[CLIENT CONNECTED] {client_address} bağlandı.")
            self.start_threads(client_socket)
            self.connected = True


    def start_threads(self, client_socket):
            get_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            get_thread.start()
        

    def handle_client(self, client_socket):
        #Ağ sorunları nedeniyle bağlantı kesildiğinde bile soketin açık kalmasına yardımcı olur.
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)  # Keep-alive ayarı
        while True:
            msg = client_socket.recv(SIZE).decode(FORMAT)
            flag = 0
            if msg=="":
                continue

            # Check message
            msg_sp = msg.split(";")
            if msg_sp[0]=="TELE" or msg_sp[0]=="INFO" or msg_sp[0]=="ERROR":               
                flag = 1
                #print("OK", msg)
            #else :
                #print("hata",msg)
                
            if not msg:
                # Mesaj yoksa, müşteri bağlantısı kesilir ve döngü sonlanır.
                print(f"[CLIENT DISCONNECTED] {client_socket.getpeername()} bağlantısı kesildi.")
                self.clients.remove(client_socket)
                client_socket.close()
                break
            #print(f"[MESSAGE RECEIVED] {msg}")
            # CSV dosyasına veriyi ekleyen fonksiyona giden iş parçacığı başlatılır.
            if flag == 1:
                self.add_data_csv(msg)
            

    # Verileri CSV dosyasına ekleme.
    def add_data_csv(self, newData):
        try:
            with open("verii.csv", "a", newline="") as dosya_csv:
                # CSV dosyasına yazmak için bir yazıcı nesnesi oluşturulur
                yazici = csv.writer(dosya_csv, delimiter=";")
                yazici.writerow([newData])
                print([newData])

                    
                    
        except Exception as e:
            print(f"Hata: {e}")

    def send_message(self, message):
        #print(message)
        # Eğer 'clients' listesinde bağlı müşteri varsa mesajı göndermeye çalış.
        if self.clients:
            for client in self.clients:
                try:
                    client.sendall(message.encode())
                    print("Mesaj Gönderildi: ", message)
                # Eğer bağlantı kesilirse hatayı göster
                except ConnectionResetError:
                    print("Bağlantı kesildi, mesaj gönderilemedi.")
        # Eğer 'clients' listesi boşsa hata ver
        else:
            print("Bağlantı yok, mesaj gönderilemedi.")

    def is_connected(self):
        return self.connected


if __name__ == "__main__":
    server = ServerSide()
    server.connect()
