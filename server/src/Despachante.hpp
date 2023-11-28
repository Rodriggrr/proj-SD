struct Despachante {

    /**
     * @brief Empacota uma mensagem para ser enviada ao cliente
     * @param message Mensagem de referência, para pegar o id, objref e methodid
     * @param args Argumentos da mensagem (retorno do método)
     * @param error Se a mensagem é de erro ou não
     */ 
    static Gerenciador::Message empacotaMensagem(Gerenciador::Message message, std::string args, bool error = false) {
        Gerenciador::Message response;
        response.set_error(error);
        response.set_id(message.id());
        response.set_objref(message.objref());
        response.set_methodid(message.methodid());
        response.set_args(args);
        return response;
    }

    /**
     * @brief Invoca o método correto do esqueleto de uma classe e envia a mensagem de resposta, ou de erro, para o cliente.
     * @param request Mensagem recebida do cliente
     * @return Gerenciador::Message com a resposta do método, ou de erro.
     */
    static Gerenciador::Message invoke(Gerenciador::Message request){
        auto objref = request.objref();
        auto arg = request.methodid();

        // Se o objeto for "Campeonato", invoca o método correto do esqueleto e retorna a mensagem de resposta.
        if(objref == "Campeonato") {

            if(arg == "getAtleta") {
                Gerenciador::Atleta atleta;
                atleta.ParseFromString(request.args());
                return empacotaMensagem(request, Campeonato::Esqueleto::getAtleta(atleta.nome()).SerializeAsString());
            }
            
            if(arg == "addAtleta") {
                Gerenciador::Atleta atleta;
                atleta.ParseFromString(request.args());
                return empacotaMensagem(request, Campeonato::Esqueleto::addAtleta(atleta).SerializeAsString());
            }

            if(arg == "getTime") {
                Gerenciador::Time time;
                time.ParseFromString(request.args());
                return empacotaMensagem(request, Campeonato::Esqueleto::getTime(time.nome()).SerializeAsString());
            }

            if(arg == "addTime") {
                Gerenciador::Time time;
                time.ParseFromString(request.args());
                return empacotaMensagem(request, Campeonato::Esqueleto::addTime(time).SerializeAsString());
            }

            return empacotaMensagem(request, "Método não encontrado, revise seu código.", true);
        }

        return empacotaMensagem(request, "Objeto não encontrado, revise seu código.", true);
    }
};