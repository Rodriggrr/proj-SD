#include <functional>
#include <map>

struct Despachante {

    using FuncaoEsqueleto = std::function<std::string(const std::string&)>;

    /**
     * @brief Inicializa o mapa de funções do esqueleto. Feito para imitar a reflexão.
     * @note Para adicionar uma nova função, basta adicionar uma nova entrada no mapaDeFuncoes.
     */
    void inicializarMapaDeFuncoes() {
        mapaDeFuncoes[{"Campeonato", "getAtleta"}] = [](const std::string& args) {
            Gerenciador::Atleta atleta;
            atleta.ParseFromString(args);
            return Campeonato::Esqueleto::getAtleta(atleta.nome()).SerializeAsString();
        };

        mapaDeFuncoes[{"Campeonato", "addAtleta"}] = [](const std::string& args) {
            Gerenciador::Atleta atleta;
            atleta.ParseFromString(args);
            return Campeonato::Esqueleto::addAtleta(atleta).SerializeAsString();
        };

        mapaDeFuncoes[{"Campeonato", "getTime"}] = [](const std::string& args) {
            Gerenciador::Time time;
            time.ParseFromString(args);
            return Campeonato::Esqueleto::getTime(time.nome()).SerializeAsString();
        };

        mapaDeFuncoes[{"Campeonato", "addTime"}] = [](const std::string& args) {
            Gerenciador::Time time;
            time.ParseFromString(args);
            return Campeonato::Esqueleto::addTime(time).SerializeAsString();
        };

        mapaDeFuncoes[{"Campeonato", "getTecnico"}] = [](const std::string& args) {
            Gerenciador::Time time;
            time.ParseFromString(args);
            return Campeonato::Esqueleto::getTecnico(time.nome()).SerializeAsString();
        };
    }

    // Mapeia pares (objref, methodid) para funções do esqueleto
    std::map<std::pair<std::string, std::string>, FuncaoEsqueleto> mapaDeFuncoes;

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
    Gerenciador::Message invoke(Gerenciador::Message request){
            auto objref = request.objref();
            auto methodid = request.methodid();
            auto args = request.args();

            auto it = mapaDeFuncoes.find({objref, methodid});
            if (it != mapaDeFuncoes.end()) {
                // Chama a função do esqueleto associada ao par (objref, methodid)
                std::string resultado = it->second(args);
                return empacotaMensagem(request, resultado);
            } else {
                return empacotaMensagem(request, "Método não encontrado, revise seu código.", true);
            }
    }
};
