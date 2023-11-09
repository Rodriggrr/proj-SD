struct Esqueleto {
    Gerenciador::Atleta getAtleta(std::string nome) {
        return campeonato.getAtleta(nome);
    }

    Gerenciador::Atleta addAtleta(Gerenciador::Atleta atleta) {
        campeonato.addAtleta(atleta.time(), atleta);
        return atleta;
    }
};