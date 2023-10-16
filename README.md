# Projeto Final - Modelos Preditivos Conexionistas

### Jefferson Igor Duarte Silva

|**Classificação de Imagens**|**Finalizado**|**Tensorflow**|


## Performance

O modelo treinado possui performance de **82,6%**.
O modelo se baseia na rede EfficientNetB0, mas treina novamente as últimas 20 camadas do modelo. Obtendo assim um modelo mais direcionado para o problema em questão.

### Output do bloco de treinamento

<details>
  <summary>Mais detalhes</summary>
  
  ```
Epoch 1/20
3/3 [==============================] - 34s 4s/step - loss: 1.2417 - accuracy: 0.4177 - val_loss: 1.2568 - val_accuracy: 0.4130
Epoch 2/20
3/3 [==============================] - 11s 3s/step - loss: 0.5461 - accuracy: 0.8228 - val_loss: 1.2891 - val_accuracy: 0.3913
Epoch 3/20
3/3 [==============================] - 10s 1s/step - loss: 0.2823 - accuracy: 0.9177 - val_loss: 1.3320 - val_accuracy: 0.5000
Epoch 4/20
3/3 [==============================] - 9s 949ms/step - loss: 0.0953 - accuracy: 0.9810 - val_loss: 1.1074 - val_accuracy: 0.5217
Epoch 5/20
3/3 [==============================] - 11s 961ms/step - loss: 0.0479 - accuracy: 0.9937 - val_loss: 0.8252 - val_accuracy: 0.5652
Epoch 6/20
3/3 [==============================] - 9s 2s/step - loss: 0.0531 - accuracy: 0.9810 - val_loss: 0.4858 - val_accuracy: 0.7826
Epoch 7/20
3/3 [==============================] - 9s 991ms/step - loss: 0.0102 - accuracy: 1.0000 - val_loss: 0.3462 - val_accuracy: 0.8696
Epoch 8/20
3/3 [==============================] - 10s 959ms/step - loss: 0.0159 - accuracy: 1.0000 - val_loss: 0.3748 - val_accuracy: 0.8261
Epoch 9/20
3/3 [==============================] - 10s 951ms/step - loss: 0.0212 - accuracy: 0.9873 - val_loss: 0.4678 - val_accuracy: 0.8478
Epoch 10/20
3/3 [==============================] - 10s 2s/step - loss: 0.0048 - accuracy: 1.0000 - val_loss: 0.4653 - val_accuracy: 0.8478
Epoch 11/20
3/3 [==============================] - 8s 935ms/step - loss: 0.0072 - accuracy: 1.0000 - val_loss: 0.5015 - val_accuracy: 0.8261
Epoch 12/20
3/3 [==============================] - 10s 1s/step - loss: 0.0036 - accuracy: 1.0000 - val_loss: 0.4885 - val_accuracy: 0.8261
  ```
</details>

### Evidências do treinamento

Nessa seção você deve colocar qualquer evidência do treinamento, como por exemplo gráficos de perda, performance, matriz de confusão etc.

Exemplo de adição de imagem:
![Descrição](https://picsum.photos/seed/picsum/500/300)

## Roboflow

Nessa seção deve colocar o link para acessar o dataset no Roboflow

Link para o [dataset](https://universe.roboflow.com/projetos-egvuo/deteccao_ovos).

## HuggingFace

O modelo proposto não foi adicionado ao HuggingFace
