# -*- coding: utf-8 -*-
from colunas import *
from joblib import load
import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

clf = load('Mlp_classificador.joblib')
reg = load('Mlp_regressao.joblib')

st.sidebar.header("Parâmetros do acidente")

causa = st.sidebar.selectbox(
    'Causa do Acidente',
    ('Agressão Externa',
 'Animais na Pista',
 'Avarias e/ou desgaste excessivo no pneu',
 'Carga excessiva e/ou mal acondicionada',
 'Condutor Dormindo',
 'Defeito Mecânico no Veículo',
 'Defeito na Via',
 'Deficiência ou não Acionamento do Sistema de Iluminação/Sinalização do Veículo',
 'Desobediência à sinalização',
 'Desobediência às normas de trânsito pelo condutor',
 'Desobediência às normas de trânsito pelo pedestre',
 'Dormindo',
 'Falta de Atenção do Pedestre',
 'Falta de Atenção à Condução',
 'Falta de atenção',
 'Fenômenos da Natureza',
 'Ingestão de Substâncias Psicoativas',
 'Ingestão de Álcool',
 'Ingestão de álcool e/ou substâncias psicoativas pelo pedestre',
 'Mal Súbito',
 'Não guardar distância de segurança',
 'Objeto estático sobre o leito carroçável',
 'Pista Escorregadia',
 'Restrição de Visibilidade',
 'Sinalização da via insuficiente ou inadequada',
 'Ultrapassagem Indevida',
 'Velocidade Incompatível',
 'Outras')
)

tipoacidente = st.sidebar.selectbox(
    'Tipo do Acidente',
    ('Atropelamento de animal',
 'Atropelamento de pessoa',
 'Capotamento',
 'Colisão Transversal',
 'Colisão com bicicleta',
 'Colisão com objeto em movimento',
 'Colisão com objeto estático',
 'Colisão com objeto fixo',
 'Colisão com objeto móvel',
 'Colisão frontal',
 'Colisão lateral',
 'Colisão transversal',
 'Colisão traseira',
 'Danos eventuais',
 'Derramamento de carga',
 'Engavetamento',
 'Incêndio',
 'Queda de motocicleta / bicicleta / veículo',
 'Queda de ocupante de veículo',
 'Saída de Pista',
 'Saída de leito carroçável',
 'Tombamento')
        )

metereologica = st.sidebar.selectbox(
    'Condição Metereologica',
    ('Ceu Claro',
      'Chuva',
      'Nublado',
      'Sol',
      'Nevoeiro/neblina',
      'Granizo',
      'Vento',
      'Neve',
      'Garoa/Chuvisco'
      )
)


fasedia = st.sidebar.selectbox(
    'Fase do dia',
    ('Pleno dia',
      'Plena noite',
      'Anoitecer',
      'Amanhecer'
    )
)


sentidovia = st.sidebar.selectbox(
    'Sentido da Via',
    ('Crescente',
    'Decrescente')
)

tipopista = st.sidebar.selectbox(
    'Tipo da Pista',
    ('Simples',
      'Dupla',
      'Múltipla')
)


tracado = st.sidebar.selectbox(
    'Traçado da Via',
    (
        'Reta',
        'Curva',
        'Cruzamento',
        'Intersecao de vias',
        'Desvio Temporario',
        'Viaduto',
        'Rotatoria',
        'Ponte',
        'Retorno Regulamentado',
        'Tunel'
     )
)

solo = st.sidebar.selectbox(
    'Área',
    (
        'Rural',
        'Urbano',
    )
)
quant_pessoas = st.sidebar.number_input(
    'Pessoas',
    0,
    100,
    0
)

quant_veiculos = st.sidebar.number_input(
    'Quantidade de Veículos',
    0,
    100,
    0
)

tipos_veiculos = st.sidebar.multiselect(
    'Tipos de Veículos',
    (
        'Automóvel',
        'Bicicleta',            'Caminhonete',
            'Caminhão',        'Caminhão-Tanque',
    'Caminhão-Trator',        'Caminhão-trator',
        'Camioneta',           'Carro-de-mao',
    'Carroça-charrete',      'Chassi-plataforma',
        'Ciclomotor',            'Microônibus',
        'Motocicletas',               'Motoneta',
        'Motor-Casa',                 'Ônibus',
        'Quadriciclo',                'Reboque',
        'Semi-Reboque',               'Side-car',
'Trator de esteira',     'Trator de esteiras',
    'Trator de rodas',           'Trator misto',
        'Trem-bonde',               'Triciclo',
        'Utilitário',                 'Outros'
     )
)
if (len(tipos_veiculos) > quant_veiculos):
    st.sidebar.warning('Selecione a mesma quantidade dos veiculos envolvidos, caso selecione um numero maior somente os '+ str(quant_veiculos) +' primeiros seram contabilizados.')

def tp_automoveis(tipos_veiculos):
    tpv = np.zeros(29, dtype='int')

    tpv2 = ['Automóvel',
                    'Bicicleta',            'Caminhonete',
                     'Caminhão',        'Caminhão-Tanque',
              'Caminhão-Trator',        'Caminhão-trator',
                    'Camioneta',           'Carro-de-mao',
             'Carroça-charrete',      'Chassi-plataforma',
                   'Ciclomotor',            'Microônibus',
                 'Motocicletas',               'Motoneta',
                   'Motor-Casa',                 'Outros',
                  'Quadriciclo',                'Reboque',
                 'Semi-Reboque',               'Side-car',
            'Trator de esteira',     'Trator de esteiras',
              'Trator de rodas',           'Trator misto',
                   'Trem-bonde',               'Triciclo',
                   'Utilitário',                 'Ônibus']


    for i in range(len(tipos_veiculos)):
        for j in range(len(tpv2)):
            if(tipos_veiculos[i] == tpv2[j]):
                tpv[j] = 1;
                print(tipos_veiculos[i])

    return tpv

tpv = tp_automoveis(tipos_veiculos)



data_classificacao = {
    'causa_acidente': causa_acidente[causa],
    'tipo_acidente': tipo_acidente[tipoacidente],
    'fase_dia': fase_dia[fasedia],
    'sentido_via': sentido_via[sentidovia],
    'condicao_metereologica': condicao_metereologica[metereologica],
    'tipo_pista': tipo_pista[tipopista],
    'tracado_via': tracado_via[tracado],
    'uso_solo': uso_solo[solo],
    'pessoas': quant_pessoas,
    'veiculos': quant_veiculos,
    '0':1,
    'Automóvel': tpv[0],
    'Bicicleta': tpv[1],
    'Caminhonete': tpv[2],
    'Caminhão': tpv[3],  
    'Caminhão-Tanque': tpv[4],
    'Caminhão-Trator': tpv[5],
    'Caminhão-trator': tpv[6],
    'Camioneta': tpv[7], 
    'Carro-de-mao': tpv[8],
    'Carroça-charrete': tpv[9], 
    'Chassi-plataforma': tpv[10],
    'Ciclomotor': tpv[11],
    'Microônibus': tpv[12],
    'Motocicletas': tpv[13],
    'Motoneta': tpv[14],
    'Motor-Casa': tpv[15],
    'Outros': tpv[16],
    'Quadriciclo': tpv[17],
    'Reboque': tpv[18],
    'Semi-Reboque': tpv[19],
    'Side-car': tpv[20],
    'Trator de esteira': tpv[21],
    'Trator de esteiras': tpv[22],
    'Trator de rodas': tpv[23],
    'Trator misto': tpv[24],
    'Trem-bonde': tpv[25],
    'Triciclo': tpv[26],
    'Utilitário': tpv[27],
    'Ônibus': tpv[28] 
}
data_regressao = {
    'tipo_acidente': tipo_acidente[tipoacidente],
    'fase_dia': fase_dia[fasedia],
    'sentido_via': sentido_via[sentidovia],
    'condicao_metereologica': condicao_metereologica[metereologica],
    'tipo_pista': tipo_pista[tipopista],
    'tracado_via': tracado_via[tracado],
    'uso_solo': uso_solo[solo],
    'veiculos': quant_veiculos,
}

features_classificacao = pd.DataFrame(data_classificacao,index=[0])
features_regressao = pd.DataFrame(data_regressao,index=[0])


st.markdown('# Classificador')
st.markdown('### Caracteristicas usadas para predição:')
st.warning('> Causa do Acidente, Tipo do Acidente, Fase do dia, Sentido da Via, Condição Metereológica, Tipo da Pista,	Traçado da Via, Área, Pessoas, Quantidade de Veiculos,	Tipos de Veiculos.')

prediction = clf.predict(features_classificacao)
prediction_proba = clf.predict_proba(features_classificacao)
print(prediction)
print(prediction_proba)
st.subheader("Previsão")
st.write(pd.DataFrame({'Conclusao': prediction}))
st.subheader("Previsão probabilística")
st.write(pd.DataFrame(
    {
        'Com Vítimas Fatais': prediction_proba[0][0],
        'Com Vítimas Feridas': prediction_proba[0][1],
        'Sem Vítimas': prediction_proba[0][2],
    }, index=[0]))

st.markdown('# Regressão')
st.markdown('### Caracteristicas usadas para predição:')
st.warning('> Tipo do Acidente, Fase do dia, Sentido da Via, Condição Metereológica, Tipo da Pista, Traçado da Via, Área, Quantidade de Veiculos.')

prediction2 = reg.predict(features_regressao)
print(prediction2)
st.subheader("Previsão")
st.write(pd.DataFrame({'Quantidade de pessoas estimada': prediction2}))


