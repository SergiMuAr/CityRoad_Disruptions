# @source code: example/exapmle.py
import csv
import llda

tlist = []
with open('TrainingDataSet/stemmed.csv') as f:
  reader = csv.reader(f)
  for row in reader:
    tlist.append((','.join(row), ['TI']))

# data
labeled_documents = [("encara,embus,ap7,sant,cugat,santa,perpetua,gt,girona,topada,,camio,turismes,carril,tallat,aturats,santa,perpetua,gt,sud,afecta,b30,equipviari", ["TI"]),
                     ("aturats,ap7,altura,barbera,sentit,girona,accident,santa,perpetua,girona,equipviari", ["TI"]),
                     ("nii,tallada,agullana,emporda,2,sentits,causa,accident,desviaments,ap7,precaucio,equipviari", ["TI"])]

# new a Labeled LDA model
llda_model = llda.LldaModel(labeled_documents=tlist)
# print llda_model

# trainingass
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
document = "accident,tarragona,talla,carril,sentit,nord,provoca,2km"
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