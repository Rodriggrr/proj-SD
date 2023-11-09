#include "src/DatagramSocket.hpp"
#include "src/Campeonato.hpp"
Campeonato campeonato;

#include "src/Despachante.hpp"
using namespace Gerenciador;
#include "src/fn.hpp"
#include <iostream>

Message getRequest(std::pair<int, char*> request){
    Message message;
    char* buffer = request.second;
    int messageSize = request.first;

    char* fixedBuffer = new char[messageSize];
    for(int i = 0; i < messageSize; i++){
        fixedBuffer[i] = buffer[i];
    }

    if(!message.ParseFromArray(buffer, messageSize)){
        throw std::runtime_error("Failed to parse message");
    }
    return message;
}

int main(){
    DatagramSocket socket(49110);

    Time time;
    time.set_nome("Sao Paulo");
    time.set_pontos(6);
    time.set_qtdjogos(2);
    campeonato.addTime(time);
    Atleta atleta;
    atleta.set_nome("Hernanes");
    atleta.set_idade(35);
    atleta.set_time("Sao Paulo");

    campeonato.addAtleta(atleta.time(), atleta);

    while(true){
        try{
            Message message;
            Despachante despachante;
            message = getRequest(socket.recv());
            std::cout << "Received message: " << message.DebugString() << std::endl;
            Message sendMsg = despachante.invoke(message);
            std::cout << "Sending message: " << sendMsg.DebugString() << std::endl;
            socket.sendTo(*socket.getAddress(), sendMsg.SerializeAsString());

        } catch(std::runtime_error& e){
            std::cout << e.what() << std::endl;
        }
    }
}