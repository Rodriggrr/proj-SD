#include "src/Campeonato.hpp"
Campeonato::Campeonato campeonato;

#include "src/Esqueleto.hpp"

#include "src/DatagramSocket.hpp"
#include "src/Despachante.hpp"
#include "src/fn.hpp"

#include <iostream>
#include <thread>

using namespace Gerenciador;

Message getRequest(std::pair<int, char*> request);

int main(){
    bool duped = false;

    DatagramSocket socket(49110);

    // Inicialização do campeonato, com um time, um tecnico e um atleta. (Para testes)
    Time time;
    time.set_nome("Sao Paulo");
    time.set_pontos(6);
    time.set_qtdjogos(2);
    Time::Tecnico tecnico;
    tecnico.set_nome("Dorival");
    tecnico.set_idade(61);
    tecnico.set_qtdtitulos(6);
    time.set_tecnico(tecnico.SerializeAsString().c_str());
    campeonato.addTime(time);
    Atleta atleta;
    atleta.set_nome("Hernanes");
    atleta.set_idade(38);
    atleta.set_numcamisa(15);
    atleta.set_time("Sao Paulo");
    atleta.set_posicao(Gerenciador::Atleta_Posicao_ATACANTE);
    campeonato.addAtleta(atleta.time(), atleta);


    Despachante dispatcher;

    //Inicializa o simulador de reflexão.
    dispatcher.inicializarMapaDeFuncoes();

    // Loop básico de recebimento de mensagens
    while(true){
        Message message;

        std::thread t([&]() {
            while(true) {
                std::cout << "Debug:\n"
                        << "1 - Enviar pacotes duplicados" << ((duped) ? " (ON)" : "") << "\n"
                        << "2 - Desligar o servidor\n";
                int choice;
                std::cin >> choice;
                if(choice == 1) {
                    duped = (duped) ? false : true;
                }
                else if (choice == 2) exit(0);
            }
        });

        t.detach();

        try{
            
            // Recebe a mensagem e a parseia para um objeto Message e a imprime.
            message = getRequest(socket.recv());

            std::cout << message.DebugString();

            // Invoca o método correto e envia a mensagem de resposta, ou de erro, para o cliente.
            Message sendMsg = dispatcher.invoke(message);
            socket.sendTo(*socket.getAddress(), sendMsg.SerializeAsString());


            if (duped) {
                Message sendMsg = dispatcher.invoke(message);
                socket.sendTo(*socket.getAddress(), sendMsg.SerializeAsString());
            }

        // Caso ocorra algum erro, envia uma mensagem de erro para o cliente.
        } catch(std::runtime_error& e){
            std::cout << "Sending error message: " << e.what() << std::endl;
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