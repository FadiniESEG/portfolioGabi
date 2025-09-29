import streamlit as st
from PIL import Image

# --- CONFIGURAÇÕES GERAIS DA PÁGINA ---
st.set_page_config(
    page_title="Gabrielle Carpejane | Portfólio",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS CUSTOMIZADO PARA ESTILOS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# (Opcional) Crie um arquivo style.css para mais customização ou use o markdown abaixo
st.markdown("""
<style>
    /* Esconde o menu e o rodapé padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* Estilo para os botões/links na página inicial */
    .stButton>button {
        border: 2px solid #4F8BF9;
        border-radius:10px;
        color: #4F8BF9;
        background-color: transparent;
    }
    .stButton>button:hover {
        border-color: #0B45A9;
        color: #0B45A9;
    }
</style>
""", unsafe_allow_html=True)


# --- BARRA LATERAL (MENU DE NAVEGAÇÃO) ---
with st.sidebar:
    try:
        # IMPORTANTE: Troque 'profile_pic.png' pelo nome do seu arquivo de imagem
        profile_pic = Image.open('profile_pic.png')
        st.image(profile_pic, width=200)
    except FileNotFoundError:
        st.warning("Adicione uma foto chamada 'profile_pic.png' na mesma pasta do script.")

    st.title("Gabrielle Borgatto Carpejane")
    st.markdown("[E-mail: gabrielleborgatto@gmail.com](mailto:gabrielleborgatto@gmail.com)")
    st.markdown("[LinkedIn: in/gabrielle-carpejane](https://www.linkedin.com/in/gabrielle-carpejane)")

    st.markdown("---")

    page = st.radio(
        "Navegue pelas seções:",
        ("Início", "Trajetória Profissional", "Portfólio Acadêmico", "Habilidades", "Contato"),
        label_visibility="collapsed"
    )
    st.markdown("---")


# --- CONTEÚDO DAS PÁGINAS ---

# Página: Início
if page == "Início":
    st.title("Bem-vindo(a) ao meu Portfólio Profissional")
    st.subheader("Objetivo: Estagiária Jurídica II")
    
    st.markdown(
        """
        Estou à procura de uma oportunidade de estágio onde possa mostrar meus conhecimentos em Direito, aplicando na prática o que em sua grande maioria apenas experienciei na teoria.
        
        Dedicada a aprender as diversas facetas do Direito brasileiro, estou motivada para me integrar a uma equipe dinâmica, contribuindo ativamente enquanto aprimoro minhas habilidades através de experiências práticas.
        """
    )
    st.markdown("---")
    st.subheader("Principais Experiências")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("##### **Jurídico Corporativo (Energias Renováveis)**")
        st.markdown("Atuação no setor de energias renováveis na **Recurrent Energy**, com análise de contratos em português e inglês e suporte a projetos de usinas solares.")
    with col2:
        st.markdown("##### **Compliance Global e Direito Internacional**")
        st.markdown("Experiência em Compliance Global na **CEVA Logistics**, analisando licenças de exportação e sanções internacionais (OFAC e ITAR).")
    with col3:
        st.markdown("##### **Advocacia Estratégica**")
        st.markdown("Vivência na rotina de escritório no contencioso estratégico, com redação de petições e gestão de processos em Recuperação Judicial, Tributário e Cível.")

# Página: Trajetória Profissional
elif page == "Trajetória Profissional":
    st.header("Trajetória Profissional e Acadêmica")

    st.subheader("Experiência Profissional")

    with st.expander("**Estagiária Jurídica | Recurrent Energy** (Junho de 2025 - Atual)"):
        st.markdown(
            """
            - Análise e revisão de contratos diversos, aditivos e NDAs, em português e inglês.
            - Suporte jurídico em projetos de usinas solares, incluindo a fase greenfield.
            - Auxílio em tarefas relacionadas a fusões, aquisições e gestão societária.
            - Trabalho diário em equipe com membros de diversos países da América Latina, utilizando o inglês avançado.
            """
        )

    with st.expander("**Estagiária Jurídica | NDN Advogados** (Setembro de 2024 - Junho de 2025)"):
        st.markdown(
            """
            - Redação de petições simples e de média complexidade.
            - Experiência ativa com o sistema "PROJURIS" e controle de prazos internos da equipe.
            - Contato com rotina agitada de escritório, atuando sob pressão.
            - Atuação em Recuperação Judicial, Tributário e Consultivo Cível-Estratégico (Despejo e Execução).
            """
        )

    with st.expander("**Estagiária de Compliance Global | CEVA Logistics** (Setembro de 2023 - Setembro de 2024)"):
        st.markdown(
            """
            - Análise de licenças de exportações internacionais (Military Goods) e obediência a leis internacionais e americanas.
            - Aprovação ou negação de embargos que descumpriam com o OFAC e ITAR.
            - Auditoria de aprovações de exportações e obediência a sanções internacionais.
            - Apoio aos contratos globais, verificando acordo com políticas internas e de direitos humanos.
            - Contato com o mundo global corporativo e experiência focada no Direito Internacional e no Compliance Global.
            - Uso diário do inglês em reuniões, tornando-o fluente.
            """
        )

    st.subheader("Educação")
    st.markdown("**Direito** - Faculdade Eseg - Grupo Etapa (Conclusão em 2027)")
    st.markdown(
        """
        *Disciplinas cursadas abrangem tópicos como Obrigações e Contratos, Direito Processual Civil, Direito Empresarial e Direito Administrativo, além de disciplinas não-dogmáticas para aplicação prática do Direito.*
        """
    )


# Página: Portfólio Acadêmico
elif page == "Portfólio Acadêmico":
    st.header("Liderança Acadêmica e Produções Relevantes")

    st.subheader("Publicações")
    st.markdown(
        """
        > **Artigo Completo | Dossiê Internacional de Direitos Humanos de Campinas (Setembro de 2024)**
        >
        > *Tema: "Intersseccionalidade e Injustiça: Um olhar crítico sobre os direitos da mulher preta no Brasil - Uma abordagem à partir do movimento feminista branco-liberal".*
        """
    )
    st.markdown(
        """
        > **Resumo Acadêmico | Simpósio de Direitos Humanos de Coimbra (Junho de 2023)**
        >
        > *Tema: "A inexequibilidade do capitalismo verde e a exploração contemporânea do trabalhador".*
        """
    )

    st.subheader("Atividades de Liderança")
    st.markdown(
        """
        > **Monitora de Direito Civil (Fevereiro de 2025 - Junho de 2025)**
        >
        > *Responsável por oferecer suporte acadêmico aos estudantes, auxiliar o professor, pesquisar jurisprudência relevante, curar exercícios da OAB e realizar plantões de dúvidas.*
        """
    )
    st.markdown(
        """
        > **Monitora de Direitos Humanos e Minorias (Julho de 2024 - Dezembro de 2024)**
        >
        > *Auxílio a alunos com dificuldades em Direitos Humanos Internacionais e suporte ao docente em assuntos do tema.*
        """
    )

# Página: Habilidades
elif page == "Habilidades":
    st.header("Habilidades Técnicas e Interpessoais")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Idiomas e Hard Skills")
        st.markdown(
            """
            - **Inglês:** Fluente (com Experiência Internacional)
            - **Espanhol:** Intermediário
            - **Francês:** Básico
            - **Pacote Office:** Avançado
            - **Análise de Dados:** Power BI
            - **Cursos:** Comércio Global e Varejo Japonês
            """
        )

    with col2:
        st.subheader("Soft Skills")
        st.markdown(
            """
            - Trabalho em Equipe
            - Comunicação
            - Resolução de problemas
            - Proatividade
            - Aprendizado Ativo
            - Pensamento analítico
            - Inovação
            """
        )

# Página: Contato
elif page == "Contato":
    st.header("Contato")
    st.markdown("Estou aberta a novas oportunidades de estágio e conexões profissionais. Sinta-se à vontade para entrar em contato através dos canais abaixo.")
    st.markdown("---")
    st.subheader("Informações de Contato:")
    st.markdown(f"""
    - **Localização:** Guarulhos, São Paulo
    - **Celular:** (11) 9 8986-3988
    - **E-mail:** [gabrielleborgatto@gmail.com](mailto:gabrielleborgatto@gmail.com)
    - **LinkedIn:** [www.linkedin.com/in/gabrielle-carpejane](https://www.linkedin.com/in/gabrielle-carpejane)
    """)