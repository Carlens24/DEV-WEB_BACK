import re

def contar_palavras(texto, palavra):
    padrao = r'\b' + palavra + r'\b'
    matches = re.findall(padrao, texto, re.IGNORECASE)
    return len(matches)

texto = """O Censo Escolar da Educação Básica é um levantamento estatístico anual coordenado pelo Instituto 
Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep) e realizado em parceria com secretarias 
estaduais e municipais de educação, escolas públicas e privadas de todo o País. A declaração das informações 
ao Censo Escolar é obrigatória para todos os estabelecimentos públicos e privados de educação básica e deve 
ser feita com base nos documentos administrativos das escolas e redes de ensino, tendo por parâmetro a 
situação observada na data de referência da pesquisa, definida como a última quarta-feira do mês de maio de 
2022 (Portaria Inep nº 89/2022).
A pesquisa permite a produção e avaliação de estatísticas das condições de oferta e atendimento 
do sistema educacional brasileiro na educação básica, reunindo informações sobre todas as suas etapas e 
modalidades de ensino e compondo um quadro detalhado sobre os alunos, as turmas, os profissionais 
escolares em sala de aula, os gestores e as escolas. Os dados apurados subsidiam a operacionalização de 
políticas públicas, programas governamentais e ações setoriais nas três esferas de governo (federal, estadual 
e municipal).
As notas estatísticas têm por objetivo ser um instrumento inicial de divulgação com destaques relativos 
às informações de alunos (matrículas), docentes, escolas e gestores coletadas no Censo Escolar da Educação 
Básica 2022. Para ampliar o potencial de análise, o Inep também disponibiliza os microdados da pesquisa, a 
sinopse estatística e o resumo técnico com resultados mais detalhados."""

palavra = "Federal"
contagem = contar_palavras(texto, palavra)

print(f"A palavra '{palavra}' aparece {contagem} vezes no texto.")
