#include "src/DatagramSocket.hpp"

#include "src/Campeonato.hpp"
Campeonato campeonato;

#include "src/Despachante.hpp"

using namespace Gerenciador;
#include "src/fn.hpp"
#include <iostream>

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

int main(){
    DatagramSocket socket(49110);

    // Inicialização do campeonato, com um time e um atleta. (Para testes)
    Time time;
    time.set_nome("Sao Paulo");
    time.set_pontos(6);
    time.set_qtdjogos(2);
    campeonato.addTime(time);
    Atleta atleta;
    atleta.set_nome("Hernanes");
    atleta.set_idade(38);
    atleta.set_time("Sao Paulo");
    atleta.set_posicao(Gerenciador::Atleta_Posicao_ATACANTE);

    campeonato.addAtleta(atleta.time(), atleta);

    // Loop básico de recebimento de mensagens
    while(true){
        Message message;
        try{
            
            // Recebe a mensagem e a parseia para um objeto Message e a imprime
            message = getRequest(socket.recv());
            std::cout << "Received message: " << message.DebugString() << std::endl;

            // Invoca o método correto e envia a mensagem de resposta, ou de erro, para o cliente.
            Message sendMsg = Despachante::invoke(message);
            std::cout << "Sending message: " << sendMsg.DebugString() << std::endl;
            socket.sendTo(*socket.getAddress(), sendMsg.SerializeAsString());

        // Caso ocorra algum erro, envia uma mensagem de erro para o cliente.
        } catch(std::runtime_error& e){
            std::cout << "Sending error message: " << e.what() << std::endl;
            socket.sendTo(*socket.getAddress(), Despachante::empacotaMensagem(message, e.what(), true).SerializeAsString());
        }
    }
}