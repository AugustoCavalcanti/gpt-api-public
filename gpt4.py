import openai

#To generate a file in the right format to fine-tune the model, you need to use the following code: 
#Cli comand: openai tools fine_tunes.prepare_data -f <LOCAL_FILE>
#The above command will generate a file in the jsonl format, which is the format that the API expects for fine-tuning.
#The comand wil acept diferent formats off files, CSV, TSV, XLSX, JSON or JSONL
#Remeber that the file must have a column called "prompt" and another called "completion" and only those two columns. Otherwise, the comand will return an error.

#To fine-tune the model, you need to use the following code:
class GPT4:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    #Send a request to the OpenAI API to generate text
    def generate_text(self, prompt, length=100, temperature=0.5, model="text-davinci-003"):
        response = openai.Completion.create(
            #The name of the model you wish to use. The default is text-davinci-003.
            engine=model,
            #The prompt is the text that the model will use to generate the response.
            prompt=prompt,
            #The maximum number of tokens to generate the response. The default is 64.
            max_tokens=length,
            #The temperature is a number between 0 and 1 that controls the randomness of the model. The lower the temperature, the less random the text. The default is 0.5.
            temperature=temperature
        )
        return response.choices[0].text
       
    #Send a request to the OpenAI API to get the model information
    def get_model_info(self, model_name="text-davinci-003"):
        response = openai.Model.retrieve(model_name)
        return response
        
    #Send a request to the OpenAI API to get the models list
    def get_models_list(self):
        response = openai.Model.list()
        return response

    #Send a request to the OpenAI API to generate a new fine-tuning
    def fine_tune(self, training_data, model_name="text-davinci-003", steps=1000, learning_rate=1e-5, batch_size=1):
        response = openai.FineTune.create(
            #The id of the training file you wish to use for fine-tuning.
            prompt=training_data,
            #The name of the model you wish to fine-tune. The default is text-davinci-003.
            model=model_name,
            #The number of steps to fine-tune the model. The default is 1000.
            n_epochs=steps,
            #The learning rate to use for fine-tuning. The default is 1e-5.
            learning_rate=learning_rate,
            #The batch size to use for fine-tuning. The default is 1.
            batch_size=batch_size
        )
        return response
    
    #Send a request to the OpenAI API to get the fine-tuning information
    def retrive_fine_tuning(self, fine_tuning_id):
        response = openai.FineTune.retrieve(id=fine_tuning_id)
        return response
    
    #Send a request to the OpenAI API to get your fine-tunings list
    def list_fine_tunings(self):
        response = openai.FineTune.list()
        return response
    
    #Send a request to the OpenAI API to delete a fine-tuning
    def delete_fine_tuning(self, fine_tuning_id):
        response = openai.FineTune.delete(id=fine_tuning_id)
        return response

    #Send a request to the OpenAI API to get the list of checkpoints for the especified model
    def list_checkpoints(self, model_name="text-davinci-003"):
        response = openai.Checkpoint.list(model=model_name)
        return response
    
    #Send a training file to the OpenAI API
    def send_file(self, file_path, purpose="fine-tune"):
        response = openai.File.create(
            file=open(file_path, "rb"),
            purpose=purpose
        )
        return response
    
    #Send a request to the OpenAI API to get your files list
    def list_files(self):
        response = openai.File.list()
        return response
    
    #Send a request to the OpenAI API to delete a file
    def delete_file(self, file_id):
        response = openai.File.delete(id=file_id)
        return response
    
    #Send a request to the OpenAI API to get a file information
    def get_file(self, file_id):
        response = openai.File.retrieve(id=file_id)
        return response
    
    #Send a request to the OpenAI API to get a file contents
    def get_file_contents(self, file_id):
        response = openai.File.download(file_id)
        return response.contents