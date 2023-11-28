#include <vector>
#include "Classes.pb.h"


// Nameapce para guardar a classe campeonato e o esqueleto.
namespace Campeonato {

/**
 * @brief Classe que representa um campeonato de futsal.
 * @note A classe Campeonato é responsável por armazenar os times e atletas do campeonato.
*/
class Campeonato {
    std::vector<Gerenciador::Time> times;

public:

    // Retorna o atleta com o nome passado por parâmetro
    Gerenciador::Atleta getAtleta(std::string nome){
        for (auto time : times){
            for (auto atleta : time.atletas()){
                if (atleta.first == nome){
                    return atleta.second;
                }
            }
        }
        throw std::runtime_error("Atleta não encontrado");
    }

    // Adiciona um atleta à lista de atletas do time passado por parâmetro
    void addAtleta(std::string time, Gerenciador::Atleta atleta){
        for(int i = 0; i < times.size(); i++){
            if (times[i].nome() == time){
                times[i].mutable_atletas()->insert({atleta.nome(), atleta});
                return;
            }
        }
        throw std::runtime_error("Time não encontrado");
    }
    // Adiciona um time à lista de times do campeonato
    void addTime(Gerenciador::Time time){
        times.push_back(time);
    }

    Gerenciador::Time getTime(std::string nome) {
        for(auto a : times) {
            if(a.nome() == nome)
                return a;
        }
        throw std::runtime_error("Time não encontrado");
    }

    Gerenciador::Time::Tecnico getTecnico(std::string nomeTime) {
        for(int i = 0; i < times.size(); i++){
            if (times[i].nome() == nomeTime){
                Gerenciador::Time::Tecnico tecnico;
                tecnico.ParseFromString(times[i].tecnico());
                return tecnico;
            }
        }
        throw std::runtime_error("Time não encontrado"); 
    }

    // Retorna todos os atletas do campeonato
    std::vector<Gerenciador::Atleta> getAllAtletas() {
        std::vector<Gerenciador::Atleta> atletas;
        for (auto time : times){
            for (auto atleta : time.atletas()){
                atletas.push_back(atleta.second);
            }
        }
        return atletas;
    }

    

};

}