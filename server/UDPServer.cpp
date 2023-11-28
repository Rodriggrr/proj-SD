#include "src/Campeonato.hpp"
Campeonato::Campeonato campeonato;

#include "src/Esqueleto.hpp"

#include "src/DatagramSocket.hpp"
#include "src/Despachante.hpp"

#include <iostream>
#include <thread>

using namespace Gerenciador;

Message getRequest(std::pair<int, char*> request);
void sendReply(Message message, sockaddr_in address, int port, DatagramSocket socket);
void inicializarTimes();

int main(){
    bool duped = false;

    DatagramSocket socket(49110);

    // Inicialização do Brasileirão
    inicializarTimes();

    Despachante dispatcher;

    //Inicializa o simulador de reflexão.
    dispatcher.inicializarMapaDeFuncoes();

    std::thread t([&]() {
        while(true) {
            std::cout << "Debug:\n"
                    << "1 - Enviar pacotes duplicados" << ((duped) ? " (ON)" : "") << "\n"
                    << "2 - Desligar o servidor\n";
            int choice;
            std::cin >> choice;
            std::cin.ignore();
            if(choice == 1) {
                duped = (duped) ? false : true;
            }
            else if (choice == 2) exit(0);
        }
    });
    t.detach();

    // Loop básico de recebimento de mensagens
    while(true){
        Message message;

        try{ 
            // Recebe a mensagem e a parseia para um objeto Message e a imprime.
            message = getRequest(socket.recv());

            // Invoca o método correto e envia a mensagem de resposta, ou de erro, para o cliente.
            Message sendMsg = dispatcher.invoke(message);
            sendReply(sendMsg, *socket.getAddress(), socket.getPort(), socket);

            // Caso a opção de pacotes duplicados esteja ligada, envia uma cópia da mensagem para o cliente.
            if (duped) {
                std::cout << "Enviando pacote duplicado\n";
                Message sendMsg = dispatcher.invoke(message);
                sendReply(sendMsg, *socket.getAddress(), socket.getPort(), socket);
            }

        // Caso ocorra algum erro, envia uma mensagem de erro para o cliente.
        } catch(std::runtime_error& e){
            socket.sendTo(*socket.getAddress(), Despachante::empacotaMensagem(message, e.what(), true).SerializeAsString());
        }
    }
}

/**
 * @brief Recebe uma mensagem e retorna um objeto Message
 * @param request pair<int, char*> com o tamanho (primeiro) e o buffer da mensagem recebida pelo socket.
 * @return Gerenciador::Message com a mensagem parseada
 * @exception std::runtime_error caso a mensagem não seja parseável pelo protobuf
*/
Message getRequest(std::pair<int, char*> request){
    Message message;

    char* buffer = request.second;
    int messageSize = request.first;

    // Copia o buffer para um buffer corrigido com o tamanho correto da mensagem recebida.
    char* fixedBuffer = new char[messageSize];
    for(int i = 0; i < messageSize; i++){
        fixedBuffer[i] = buffer[i];
    }

    // Lançamento de exceção caso a mensagem não seja parseável pelo protobuf
    if(!message.ParseFromArray(buffer, messageSize)){
        throw std::runtime_error("Failed to parse message");
    }
    return message;
}

/**
 * @brief Envia uma mensagem para o cliente
 * @param message Mensagem a ser enviada
 * @param address Endereço do cliente
 * @param port Porta do cliente
*/
void sendReply(Message message, sockaddr_in address, int port, DatagramSocket socket){
    socket.sendTo(address, message.SerializeAsString());
}

/**
 * @brief Inicializa os times do campeonato
*/
void inicializarTimes(){
    Time time;
    Time::Tecnico tecnico;
    Atleta atleta;

    time.set_nome("Sao Paulo");
    time.set_pontos(6);
    time.set_qtdjogos(2);
    tecnico.set_nome("Dorival");
    tecnico.set_idade(61);
    tecnico.set_qtdtitulos(6);
    time.set_tecnico(tecnico.SerializeAsString().c_str());
    campeonato.addTime(time);
    atleta.set_nome("Hernanes");
    atleta.set_idade(38);
    atleta.set_numcamisa(15);
    atleta.set_time("Sao Paulo");
    atleta.set_posicao(Gerenciador::Atleta_Posicao_ATACANTE);
    campeonato.addAtleta(atleta.time(), atleta);

    time.set_nome("Corinthians");
    time.set_pontos(6);
    time.set_qtdjogos(2);
    tecnico.set_nome("Carille");
    tecnico.set_idade(44);
    tecnico.set_qtdtitulos(2);
    time.set_tecnico(tecnico.SerializeAsString().c_str());
    campeonato.addTime(time);
    atleta.set_nome("Jô");
    atleta.set_idade(30);
    atleta.set_numcamisa(7);
}
    

    