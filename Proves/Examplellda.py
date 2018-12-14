# @source code: example/exapmle.py

import llda

# data
labeled_documents = [("encara,embus,ap7,sant,cugat,santa,perpetua,girona,topada,camio,turismes,carril,tallada,aturats,santa,perpetua,sud,afecta,b30,equipviari", ["TI"]),
                     ("aturats,ap7,altura,barbera,sentit,girona,accident,santa,perpetua,girona,equipviari", ["TI"]),
                     ("hija,yo,recordamos,hoy,hay,naidesabenada,laser,las,1300,esperamos", ["NTI"]),
                     ("desde,tarde,hasta,domingo,mis,posters,estaran,utopiamarkets,ilustracion,parada,thefolioclub,que,ilusien", ["NTI"])]

# new a Labeled LDA model
llda_model = llda.LldaModel(labeled_documents=labeled_documents)
# print llda_model

# training
llda_model.training(iteration=10, log=True)

# update
# print "before updating: ", llda_model
# update_labeled_documents = [("good perfect good good perfect good good perfect good ", ["positive"]),
#                             ("bad bad down down bad", ["negative"]),
#                             ("new example test example test example test example test", ["example", "test"])]
# llda_model.update(labeled_documents=update_labeled_documents)
# print "after updating: ", llda_model

# train again
# llda_model.training(iteration=10, log=True)

# inference
# note: the result topics may be different for difference training, because gibbs sampling is a random algorithm
document = "nii,tallada,agullana,emporda,2,sentits,causa,accident,desviaments,ap7,precaucio,equipviari"
topics = llda_model.inference(document=document, iteration=10, times=10)
print "Mirem topics: ", topics

# # save to disk
# save_model_dir = "../data/model"
# llda_model.save_model_to_dir(save_model_dir)

# # load from disk
# llda_model_new = llda.LldaModel()
# llda_model_new.load_model_from_dir(save_model_dir)
# print "llda_model_new", llda_model_new
# print "llda_model", llda_model