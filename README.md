# FL_PCB_Defect_Detection_AI_Model
- Project Title : AI 영상 기술을 활용하여 PCB 표면 불량 판단
- Project Name : 연합학습을 활용한 PCB 표면 불량 판단 시스템
- Corp : ㈜보아스SE
- Period : 2023.07 ~ 2023.10.26

## 학습 · 배포를 위한 SW 및 HW
- 필요 SW    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;모델 학습 및 추론: Python, Jupyter Notebook, Flask    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;연합학습 서버 배포: Flask, MongoDB, AWS, Docker   
- 필요 패키지 – numpy, pandas, tensorflow, pytorch, matplotlib, sklearn, flask, requests, socketio, ultralytics   
- 분석 환경 – [OS]Linux #86 -Ubuntu SMP   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GPU] CUDA 11.3,    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PYTHON] 3.8,    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Tensorflow] 2.7   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RAM] 32GB

## Result 
- ./Inference(Final) : 모델 시연(Test) Flow
- ./result_clf_img/images : Image Classification 결과; "불량"으로 판정된 PCB
- ./result_clf_img/inference : Object Detection 결과; ./result_clf_img/images 경로에 있는 PCB의 불량 위치 검출
- ./Image_Classification : Image Classification 결과 (Client 설정 가능; Client1, Client2, or All)
- ./Object_Detection_C1 : (Client1) FL Object Detection
- ./Object_Detection_C2 : (Client2) FL Object Detection
- ./Object_Detection_Central : 중앙집중형 Object Detection (All)
- ./yolov5/runs : 각 Client에 따른 Object Detection Result
- ./model_save_C1_PCB_CLF : (Client 1) Image Classification Model
- ./model_save_C2_PCB_CLF : (Client 2) Image Classification Model
- ./model_save_PCB_CLF : (All) Image Classification Model


## PPT
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-0](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/698008f2-b4bb-4c31-be1f-381a8a79a2fd)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-1](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/ca132c48-cf90-4a76-8a3d-76b5819c886e)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-2](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/5242654d-8e96-44f6-829e-c6a37cda24b1)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-3](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/8c9c091a-058f-4e1d-a3d7-3a1f2f9a8731)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-4](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/7fc47d2c-7c8b-4b39-841f-9943d3a29915)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-5](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/35e1ecf9-12b5-4874-b382-27635d3525d4)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-6](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/8d35af6c-301f-44a0-abdd-9772cefaa087)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-7](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/5c0710d6-bc6e-4029-8fbe-6e6c2b5346ea)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-8](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/1ac8100c-70ba-46a5-924c-92f9840cc51a)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-9](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/80a44d16-d0ee-4ed3-9b3c-28bcc458d5f3)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-10](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/39ac3726-6fa1-4038-b781-c7be815f61ee)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-11](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/ea002323-4555-44b5-afbc-b2f972b294ce)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-12](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/c2da66b5-c430-4e57-8ac5-42f70adf1db1)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-13](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/e2f23144-40c0-4c68-93fa-0b872c0a8321)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-14](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/86f4af0c-4c42-4160-a5c9-445e89ab5337)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-15](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/9f76b718-4631-4c89-84c4-6274986ff2a1)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-16](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/8c3ee8ed-0ac6-4739-9902-e5129e5dce01)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-17](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/dab0c350-3c50-417b-a262-63c6ce78a921)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-18](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/7461f0d8-cf17-40c3-b019-e2b7ce6ebab5)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-19](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/67509bf7-12a5-4018-8ca3-f81ad77432d8)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-20](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/d645b457-9dcb-46ae-a481-57341b0ed466)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-21](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/939ad62a-dc33-45c0-a362-adf24be5bb81)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-22](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/d61149da-c165-41e8-bd96-aa96bc2a7d45)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-23](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/590a2a2c-2f09-40e6-8f26-5dc36dcf349c)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-24](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/3f2a41b8-9e81-4ccc-885d-3aff4cf6293a)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-25](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/fb6e77cb-4fd9-4b2f-a285-a29cbe5ada7e)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-26](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/1cc64cef-e357-4c7b-8002-e7b8b43caa2c)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-27](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/5f9e006d-0fe4-4dc2-8921-0ab49d6befab)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-28](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/9b5d1c28-a729-4493-96cd-2f233c895f66)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-29](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/004c7377-7fa5-4549-9861-97effd6e6cc5)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-30](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/aceade5d-4179-4f7d-adf5-793e17f053e5)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-31](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/043dc7a4-2e08-42d9-ba6e-d6ec358f21aa)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-32](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/1e9345b0-cc90-4cde-892b-3b802dd461db)
![27afa1356d934015d535914e44a11e32tO5tKATV6cM7cnli-33](https://github.com/SS-yong/FL_PCB_Defect_Detection_AI_Model/assets/108441950/9af82876-ac9c-49fa-8654-fb02530074a2)
