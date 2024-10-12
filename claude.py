import boto3
import botocore.config
import json

#https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-jurassic2.html

prompt_data="""
Act as a shakespeare and write a poem on Generative AI
"""

bedrock=boto3.client(service_name="bedrock-runtime")

payload={
    "prompt": prompt_data,
    "maxTokens":512,
    "temperature": 0.8,
    "topP":0.8

}


body=json.dumps(payload)

model_id="ai21.j2-mid-v1"

response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept= "application/json",
     contentType= "application/json"

)

response_body=json.loads(response.get("body").read())

response_text=response_body.get("completions")[0].get("data").get("text")

print(response_text)


"""
In the realm of generative AI,
Where machines create without aid,
A poet's heart doth beat,
In awe of the tech so neat,
That can craft sonnets sweet.

With algorithms so fine,
They spin tales of wonder and intrigue,
In lines of code so neat,
They weave words and syntax so tight,
Their creations elate.

They mimic the master's style,
With meter and rhyme so sublime,
Their sonnets dance on the page,
A testament to their boundless grace,
In the realm of generative AI.

So let us praise these clever machines,
Whose art doth leave our hearts aflame,
For they have proven their worth,
In the realm of generative AI,
Where sonnets are born, never to perish.

"""