# Definindo perguntas
def coletar_respostas():
    respostas = {}

    print("Bem-vindo ao sistema especialista de escolha de carreira em TI!")

    respostas['gosta_programar'] = input("Você gosta de programar? (sim/nao): ").strip().lower()
    respostas['interesse_negocios'] = input("Você tem interesse em negócios? (sim/nao): ").strip().lower()
    respostas['interesse_sistemas'] = input("Você gosta de desenhar e gerenciar sistemas? (sim/nao): ").strip().lower()
    respostas['habilidade_analitica'] = input("Você se considera uma pessoa analítica? (sim/nao): ").strip().lower()
    respostas['interesse_hardware'] = input("Você tem interesse em hardware? (sim/nao): ").strip().lower()
    respostas['interesse_redes'] = input("Você tem interesse em redes de computadores? (sim/nao): ").strip().lower()
    respostas['interesse_dados'] = input("Você tem interesse em trabalhar com dados e estatísticas? (sim/nao): ").strip().lower()
    respostas['interesse_seguranca'] = input("Você tem interesse em segurança da informação? (sim/nao): ").strip().lower()
    respostas['interesse_ia'] = input("Você tem interesse em Inteligência Artificial? (sim/nao): ").strip().lower()
    respostas['interesse_web'] = input("Você tem interesse em desenvolvimento web? (sim/nao): ").strip().lower()
    respostas['interesse_mobile'] = input("Você tem interesse em desenvolvimento mobile? (sim/nao): ").strip().lower()
    respostas['interesse_gestao'] = input("Você tem interesse em gestão de projetos de TI? (sim/nao): ").strip().lower()
    respostas['interesse_arquitetura'] = input("Você tem interesse em arquitetura de software? (sim/nao): ").strip().lower()
    respostas['interesse_banco_dados'] = input("Você tem interesse em administração de banco de dados? (sim/nao): ").strip().lower()

    return respostas

# Motor de regras para determinar a área mais adequada
def recomendar_area(respostas):
    if respostas['gosta_programar'] == 'sim':
        if respostas['interesse_web'] == 'sim':
            return "Desenvolvimento Web (DW)"
        elif respostas['interesse_mobile'] == 'sim':
            return "Desenvolvimento Mobile (DM)"
        elif respostas['interesse_ia'] == 'sim':
            return "Inteligência Artificial (IA)"
        elif respostas['interesse_arquitetura'] == 'sim':
            return "Arquitetura de Software (AS)"
        elif respostas['interesse_seguranca'] == 'sim':
            return "Segurança da Informação (SI)"
        elif respostas['habilidade_analitica'] == 'sim':
            if respostas['interesse_negocios'] == 'sim':
                return "Sistemas da Informação (SI)"
            elif respostas['interesse_dados'] == 'sim':
                return "Ciência de Dados (CD)"
            else:
                return "Ciência da Computação (CC) ou Análise e Desenvolvimento de Sistemas (ADS)"
    elif respostas['interesse_hardware'] == 'sim':
        return "Engenharia da Computação (EC)"
    elif respostas['interesse_redes'] == 'sim':
        return "Redes de Computadores (RC)"
    elif respostas['interesse_negocios'] == 'sim' and respostas['interesse_gestao'] == 'sim':
        return "Gestão de Projetos de TI (GP)"
    elif respostas['interesse_banco_dados'] == 'sim':
        return "Administração de Banco de Dados (DBA)"
    elif respostas['interesse_negocios'] == 'sim':
        return "Tecnologia da Informação (TI)"
    else:
        return "Tecnologia da Informação (TI) ou outra área geral de TI"

# Função principal para executar o sistema especialista
def sistema_especialista():
    respostas = coletar_respostas()
    area_recomendada = recomendar_area(respostas)
    print(f"\nBaseado nas suas respostas, a área recomendada para você é: {area_recomendada}")

# Executando o sistema especialista
sistema_especialista()
