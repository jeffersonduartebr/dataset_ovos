# Projeto Final - Modelos Preditivos Conexionistas

### Jefferson Igor Duarte Silva

|**Classificação de Imagens**|**Finalizado**|**Tensorflow**|


## Performance

O modelo treinado possui performance de **83,13%**.
O modelo se baseia na rede EfficientNetV2B1, mas treina novamente as últimas 05 camadas do modelo. Obtendo assim um modelo mais direcionado para o problema em questão.

### Output do bloco de treinamento

<details>
  <summary>Mais detalhes</summary>
  
  ```
Epoch 1/10
26/26 [==============================] - 211s 5s/step - loss: 0.9392 - accuracy: 0.6122 - val_loss: 0.8656 - val_accuracy: 0.6228
Epoch 2/10
26/26 [==============================] - 191s 5s/step - loss: 0.5459 - accuracy: 0.7958 - val_loss: 0.6099 - val_accuracy: 0.7682
Epoch 3/10
26/26 [==============================] - 189s 6s/step - loss: 0.4713 - accuracy: 0.8161 - val_loss: 0.5772 - val_accuracy: 0.7613
Epoch 4/10
26/26 [==============================] - 189s 5s/step - loss: 0.3542 - accuracy: 0.8770 - val_loss: 0.5743 - val_accuracy: 0.7833
Epoch 5/10
26/26 [==============================] - 191s 5s/step - loss: 0.3310 - accuracy: 0.8770 - val_loss: 0.5487 - val_accuracy: 0.7805
Epoch 6/10
26/26 [==============================] - 189s 5s/step - loss: 0.3038 - accuracy: 0.8926 - val_loss: 0.5600 - val_accuracy: 0.7819
Epoch 7/10
26/26 [==============================] - 196s 6s/step - loss: 0.2133 - accuracy: 0.9254 - val_loss: 0.4853 - val_accuracy: 0.8230
Epoch 8/10
26/26 [==============================] - 190s 5s/step - loss: 0.2291 - accuracy: 0.9154 - val_loss: 0.5258 - val_accuracy: 0.7874
Epoch 9/10
26/26 [==============================] - 191s 5s/step - loss: 0.1611 - accuracy: 0.9485 - val_loss: 0.4943 - val_accuracy: 0.8107
Epoch 10/10
26/26 [==============================] - 198s 6s/step - loss: 0.1505 - accuracy: 0.9494 - val_loss: 0.4462 - val_accuracy: 0.8313
  ```
</details>

### Evidências do treinamento

Nessa seção você deve colocar qualquer evidência do treinamento, como por exemplo gráficos de perda, performance, matriz de confusão etc.

Exemplo de adição de imagem:
![Acurácia e erro do modelo](https://github.com/jeffersonduartebr/dataset_ovos/blob/main/assets/train_val_acc_los_EfficientNetV2B1-5l.png)

## Roboflow

Nessa seção deve colocar o link para acessar o dataset no Roboflow

Link para o [dataset](https://universe.roboflow.com/projetos-egvuo/deteccao_ovos).

