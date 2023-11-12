namespace Campeonato {

struct Esqueleto {
    static Gerenciador::Atleta getAtleta(std::string nome) {
        return campeonato.getAtleta(nome);
    }

    static Gerenciador::Atleta addAtleta(Gerenciador::Atleta atleta) {
        campeonato.addAtleta(atleta.time(), atleta);
        return atleta;
    }
};

}