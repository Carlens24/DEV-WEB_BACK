*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${var01}  Olá
${var02}  Mundo

*** Keywords ***
Abrir o site do google
    Open Browser    https://www.google.com.br/    chrome

Fechar navegador    
    Close Browser

Abrir site da globo
    Open Browser    https://globoplay.globo.com/    chrome

*** Test Cases ***
cenário 1: abrir o site do google
    Abrir o site do google
    Fechar Navegador

cenário 2: abrir o site da globo  
    Abrir site da globo 
    Fechar Navegador