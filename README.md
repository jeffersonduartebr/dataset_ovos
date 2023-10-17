# Projeto Final - Modelos Preditivos Conexionistas

### Jefferson Igor Duarte Silva

|**Classificação de Imagens**|**Finalizado**|**Tensorflow**|


## Performance

O modelo treinado possui performance de **84,09%**.
O modelo se baseia na rede [EfficientNetV2B1](https://keras.io/api/applications/efficientnet_v2/), mas treina novamente as últimas 150 camadas do modelo. Obtendo assim um modelo mais direcionado para o problema em questão.

A opção por esta CNN foi devido a sua (1) maior eficiência computacional; (2) ter sido proposta recentemente, logo, incorpora novas inovações; (3) ser pequena. Assim, pudemos retreiná-la parcialmente em GPUs com 16Gb de VRAM.

### Output do bloco de treinamento

<details>
  <summary>Mais detalhes</summary>
  
  ```
Epoch 1/10
26/26 [==============================] - 214s 5s/step - loss: 0.5558 - accuracy: 0.7677 - val_loss: 0.7581 - val_accuracy: 0.7490
Epoch 2/10
26/26 [==============================] - 22s 638ms/step - loss: 0.2046 - accuracy: 0.9282 - val_loss: 0.8612 - val_accuracy: 0.8107
Epoch 3/10
26/26 [==============================] - 22s 636ms/step - loss: 0.1043 - accuracy: 0.9625 - val_loss: 0.6183 - val_accuracy: 0.8313
Epoch 4/10
26/26 [==============================] - 22s 644ms/step - loss: 0.1340 - accuracy: 0.9557 - val_loss: 0.5210 - val_accuracy: 0.8368
Epoch 5/10
26/26 [==============================] - 22s 634ms/step - loss: 0.0898 - accuracy: 0.9691 - val_loss: 0.5595 - val_accuracy: 0.8450
Epoch 6/10
26/26 [==============================] - 22s 635ms/step - loss: 0.1337 - accuracy: 0.9591 - val_loss: 0.4501 - val_accuracy: 0.8711
Epoch 7/10
26/26 [==============================] - 22s 634ms/step - loss: 0.0617 - accuracy: 0.9794 - val_loss: 0.5362 - val_accuracy: 0.8340
Epoch 8/10
26/26 [==============================] - 22s 630ms/step - loss: 0.1319 - accuracy: 0.9550 - val_loss: 0.5478 - val_accuracy: 0.8532
Epoch 9/10
26/26 [==============================] - 22s 654ms/step - loss: 0.0387 - accuracy: 0.9860 - val_loss: 0.6505 - val_accuracy: 0.8409
  ```
</details>

### Evidências do treinamento

Acurácia e erro do modelo:
![Acurácia e erro do modelo](https://github.com/jeffersonduartebr/dataset_ovos/blob/main/assets/train_val_acc_los_EfficientNetV2B1-150l.png)

No diretório assets estão os notebooks. Tem dois, foram dois resultados obtidos - 83 e 84% de acurácia. Um retreinou 5 camadas e o outro 150 camadas da EfficientNetV2B1.


## Roboflow

Nessa seção deve colocar o link para acessar o dataset no Roboflow

Link para o [dataset](https://universe.roboflow.com/projetos-egvuo/deteccao_ovos).

## Dataset

No diretório dataset nós temos o diretório já com ampliação dos dados. A ampliação foi realizada utilizando o próprio keras.

