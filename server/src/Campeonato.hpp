#include <vector>
#include "Classes.pb.h"

class Campeonato {
    std::vector<Gerenciador::Time> times;

public:
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
    void addTime(Gerenciador::Time time){
        times.push_back(time);
    }
    void addAtleta(std::string time, Gerenciador::Atleta atleta){
        for(int i = 0; i < times.size(); i++){
            if (times[i].nome() == time){
                times[i].mutable_atletas()->insert({atleta.nome(), atleta});
                return;
            }
        }
        throw std::runtime_error("Time não encontrado");
    }
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