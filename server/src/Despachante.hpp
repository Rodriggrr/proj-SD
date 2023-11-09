#include "Esqueleto.hpp"

struct Despachante : Esqueleto {
    Gerenciador::Message empacotaMensagem(Gerenciador::Message message, std::string args, bool error = false) {
        Gerenciador::Message response;
        if (error) {
            response.set_error(1);
        } else {
            response.set_error(0);
        }
        response.set_id(message.id());
        response.set_objref(message.objref());
        response.set_methodid(message.methodid());
        response.set_args(args);
        return response;
    }

    Gerenciador::Message invoke(Gerenciador::Message request){
        auto arg = request.methodid();
        if(arg == "getAtleta") {
            Gerenciador::Atleta atleta;
            atleta.ParseFromString(request.args());
            return empacotaMensagem(request, getAtleta(atleta.nome()).SerializeAsString());
        }
        
        if(arg == "addAtleta") {
            Gerenciador::Atleta atleta;
            atleta.ParseFromString(request.args());
            return empacotaMensagem(request, addAtleta(atleta).SerializeAsString());
        }

        return empacotaMensagem(request, "Método não encontrado", true);
    }
};