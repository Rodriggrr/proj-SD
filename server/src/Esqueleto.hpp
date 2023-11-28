namespace Campeonato {

struct Esqueleto {
    static Gerenciador::Atleta getAtleta(std::string nome) {
        return campeonato.getAtleta(nome);
    }

    static Gerenciador::Atleta addAtleta(Gerenciador::Atleta atleta) {
        campeonato.addAtleta(atleta.time(), atleta);
        return atleta;
    }

    static Gerenciador::Time getTime(std::string nome) {
        return campeonato.getTime(nome);
    }

    static Gerenciador::Time addTime(Gerenciador::Time time) {
        campeonato.addTime(time);
        return time;
    }

    static Gerenciador::Time::Tecnico getTecnico(std::string nomeTime) {
        return campeonato.getTecnico(nomeTime);
    }
};

}