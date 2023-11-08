#include "src/DatagramSocket.hpp"
#include "src/Campeonato.hpp"
Campeonato campeonato;

#include "src/Despachante.hpp"
using namespace Gerenciador;
#include "src/fn.hpp"
#include <iostream>

Message getRequest(char* buffer){
    Message message;
    int messageSize = message.ByteSizeLong();
    if(!message.ParseFromArray(buffer, messageSize)){
        throw std::runtime_error("Failed to parse message");
    }
    return message;
}

int main(){
    DatagramSocket socket(8080);

    Time time;
    time.set_nome("Flamengo");
    time.set_pontos(6);
    time.set_qtdjogos(2);

    while(true){
        Message message;
        Despachante despachante;
        message = getRequest(socket.recv());
        Message sendMsg = despachante.invoke(message);
        socket.sendTo(*socket.getAddress(), sendMsg.SerializeAsString());
    }
}