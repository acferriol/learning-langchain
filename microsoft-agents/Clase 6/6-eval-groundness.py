import os

import azure.identity
import rich
from azure.ai.evaluation import (
    AzureOpenAIModelConfiguration,
    GroundednessEvaluator,
    OpenAIModelConfiguration,
)

model_config: OpenAIModelConfiguration = {
    "api_key": "",
    "base_url": "http://localhost:11434/v1",
    "model": "llama3.2:3b",
    "type": "openai",
}

query = "Dada la especificación del producto para la Silla de Comedor de Contoso Home Furnishings, proporciona una descripción de marketing atractiva."
context = 'Silla de comedor. Asiento de madera. Cuatro patas. Respaldo. Marrón. 18" de ancho, 20" de profundidad, 35" de alto. Soporta 250 lbs.'
response = 'Presentamos nuestra atemporal silla de comedor de madera, diseñada tanto para la comodidad como para la durabilidad. Fabricada con un asiento de teca maciza y una base robusta de cuatro patas, esta silla ofrece un soporte confiable de hasta 250 lbs. El acabado caoba liso añade un toque de elegancia rústica, mientras que el respaldo de forma ergonómica garantiza una experiencia de comedor cómoda. Con unas dimensiones de 18" de ancho, 20" de profundidad y 35" de alto, es la combinación perfecta de forma y función, convirtiéndola en una adición versátil a cualquier espacio de comedor. Eleva tu hogar con esta opción de asiento, bella en su sencillez pero sofisticada.'

groundedness_eval = GroundednessEvaluator(model_config)
groundedness_score = groundedness_eval(query=query, response=response, context=context)

rich.print(groundedness_score)


"""
Category                              |	Evaluator class
Performance and quality (AI-assisted) |	GroundednessEvaluator, RelevanceEvaluator, CoherenceEvaluator, FluencyEvaluator, SimilarityEvaluator, RetrievalEvaluator
Performance and quality (NLP)	      | F1ScoreEvaluator, RougeScoreEvaluator, GleuScoreEvaluator, BleuScoreEvaluator, MeteorScoreEvaluator
Risk and safety (AI-assisted)	      | ViolenceEvaluator, SexualEvaluator, SelfHarmEvaluator, HateUnfairnessEvaluator, IndirectAttackEvaluator, ProtectedMaterialEvaluator
Composite	                          | QAEvaluator, ContentSafetyEvaluator
"""
