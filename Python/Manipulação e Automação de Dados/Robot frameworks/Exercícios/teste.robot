*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${input_first_name}    name:first_name
${input_last_name}     name:last_name
${input_email}         name:email
${input_phone}         name:phone
${input_address}       name:address
${input_city}          name:city
${select_states}       name:state
${select_state}        //option[6]
${input_zip}           name:zip
${input_website}       name:website
${input_hosting}       name:hosting
${textarea_description}  name:comment
${button_submit}         //button[@class='btn btn-default']


*** Keywords ***
Abrir Navegador e Acessar o Site
    Open Browser    https://demo.seleniumeasy.com/input-form-demo.html    chrome

Preencher os Campos
    Input Text    ${input_first_name}    Carlens
    Sleep  1s
    Input Text    ${input_last_name}    OSlin
    Sleep  1s
    Input Text    ${input_email}    Carlensoslin@gmail.com
    Sleep  1s
    Input Text    ${input_phone}    (123) 456-7890
    Sleep  1s
    Input Text    ${input_address}    Prado Velho
    Sleep  1s
    Input Text    ${input_city}    Curitiba
    Sleep  1s
    Input Text    ${input_zip}    96162
    Sleep  1s
    Input Text    ${input_website}    www.carlens.darley.com.br
    Sleep  1s
    Input Text    ${textarea_description}    Olá, Mundo
    Sleep  1s

Clicar nos Elementos
    Click Element    ${select_states}
    Sleep  1s
    Click Element    ${select_state}
    Sleep  1s
    Click Element    ${input_hosting}
    Sleep  1s
    Click Element    ${select_states}
    Sleep  1s
    Click Element    ${button_submit}
    Sleep  1s

Fechar o Navegador
    Close Browser

*** Test Cases ***
Case 01: Preencher o Formulário
    Abrir Navegador e Acessar o Site
    Preencher os Campos
    Clicar nos Elementos
    Fechar o Navegador
