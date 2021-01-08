# -*- coding: utf-8 -*-
tracado_via = {
  'Reta': 0,
  'Curva': 1,
  'Cruzamento': 2,
  'Intersecao de vias': 3,
  'Desvio Temporario': 6,
  'Viaduto': 4,
  'Rotatoria': 5,
  'Ponte': 8,
  'Retorno Regulamentado': 7,
  'Tunel': 9
}

uso_solo = {
  'Rural': 0,
  'Urbano': 1,
}

causa_acidente = {'Agressão Externa': 25,
 'Animais na Pista': 1,
 'Avarias e/ou desgaste excessivo no pneu': 16,
 'Carga excessiva e/ou mal acondicionada': 19,
 'Condutor Dormindo': 13,
 'Defeito Mecânico no Veículo': 9,
 'Defeito na Via': 8,
 'Deficiência ou não Acionamento do Sistema de Iluminação/Sinalização do Veículo': 22,
 'Desobediência à sinalização': 4,
 'Desobediência às normas de trânsito pelo condutor': 12,
 'Desobediência às normas de trânsito pelo pedestre': 26,
 'Dormindo': 5,
 'Falta de Atenção do Pedestre': 14,
 'Falta de Atenção à Condução': 11,
 'Falta de atenção': 2,
 'Fenômenos da Natureza': 23,
 'Ingestão de Substâncias Psicoativas': 24,
 'Ingestão de Álcool': 6,
 'Ingestão de álcool e/ou substâncias psicoativas pelo pedestre': 27,
 'Mal Súbito': 18,
 'Não guardar distância de segurança': 7,
 'Objeto estático sobre o leito carroçável': 21,
 'Outras': 0,
 'Pista Escorregadia': 15,
 'Restrição de Visibilidade': 20,
 'Sinalização da via insuficiente ou inadequada': 17,
 'Ultrapassagem Indevida': 10,
 'Velocidade Incompatível': 3}

tipo_pista = {
  'Simples':0,
  'Dupla':1,
  'Múltipla':2
}
tipo_acidente = {
   'Atropelamento de animal': 3,
 'Atropelamento de pessoa': 8,
 'Capotamento': 10,
 'Colisão Transversal': 4,
 'Colisão com bicicleta': 11,
 'Colisão com objeto em movimento': 20,
 'Colisão com objeto estático': 17,
 'Colisão com objeto fixo': 6,
 'Colisão com objeto móvel': 12,
 'Colisão frontal': 0,
 'Colisão lateral': 2,
 'Colisão transversal': 19,
 'Colisão traseira': 7,
 'Danos eventuais': 9,
 'Derramamento de carga': 15,
 'Engavetamento': 21,
 'Incêndio': 14,
 'Queda de motocicleta / bicicleta / veículo': 13,
 'Queda de ocupante de veículo': 16,
 'Saída de Pista': 1,
 'Saída de leito carroçável': 18,
 'Tombamento': 5
}
condicao_metereologica = {
  'Ceu Claro':0,
  'Chuva':1,
  'Nublado':2,
  'Sol':3,
  'Nevoeiro/neblina':4,
  'Granizo':5,
  'Vento':6,
  'Neve':7,
  'Garoa/Chuvisco':8,
}
fase_dia = {
  'Pleno dia':0,
  'Plena noite':1,
  'Anoitecer':3,
  'Amanhecer':2,
}
sentido_via = {
  'Crescente':1,
  'Decrescente':0
  }