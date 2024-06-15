** Settings **
Library  SeleniumLibrary

** Variables **
${Musica}    Mount everest
${URL}    https://www.youtube.com/
${browser}    chrome
${barra_pesquisa}    //input[@name='search_query']
${botao_de_pesquisa}    //button[@id='search-icon-legacy']
${video}    (//yt-formatted-string[@class='style-scope ytd-video-renderer'])[3]   
${prova}    (//div[@class='yt-spec-touch-feedback-shape__fill'])[4]

*** Tasks ***
    

** Keywords **
Given Acessar o site e a url
    Open Browser    ${URL}     ${browser}

When clicar na barra da pesquisa
    Input Text    ${barra_pesquisa}    Mount Everest

And Clicar no botão de pesquisa
    Click Element    ${botao_de_pesquisa}

And clicar na primeira opção de video
    Wait Until Element Is Visible    ${video}    10
    Click Element    ${video}

Then o vídeo será executado e clicara no botão de login
    Sleep    3
    Click Element     ${prova}
    Sleep    5
    Close Browser 


** Test Cases **
Cenário 1: Abrir um Vídeo no youtube pra assistir
    Given Acessar o site e a url
    When clicar na barra da pesquisa
    And Clicar no botão de pesquisa
    And clicar na primeira opção de video
    Then o vídeo será executado e clicara no botão de login
