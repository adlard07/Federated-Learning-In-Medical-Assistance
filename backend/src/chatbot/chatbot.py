import openai
from src.chatbot.config import api_key

client = openai.OpenAI(api_key=api_key)

class Prompt:
    def disease_description(self, disease, disease_class):
        query = f'''A PATIENT IS DOUBTFUL OF HAVING {disease}, 
        AFTER PREDICTION THE OUTPUT CLASS IS {disease_class}. 
        GIVE ME SOME ADVICE WHAT THE PATIENT SHOULD DO IN SUCH SITUATION IN BELOW FORMAT. 
        
        1. SUMMARY OF THE DISEASE: 
        2. HOW DEADLY IT IS:
        3. TREATMENT:
        4. MEASURES AND PRECAUSIONS TO TAKE:
        5. OUTCOME OF NOT TREATING PROPERLY:
        '''         
                    
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query}
        ])

        return completion.choices[0].message.content
    
    def doubt(self, prompt):
        query = f'''
        I HAVE A DOUBT. {prompt}?
        ANSWER THE ABOVE QUESTION IN 50-100 WORDS AND START DIRECTLY WITH THE ANSWER NO NEED OF INTRODUCTRY SENTENCES. 
        '''
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a an expert in diseases like alzheimers, brain tumor, breast cancer, fracture, kidney, pneumonia."},
            {"role":"user", 'content': query}
        ])

        return completion.choices[0].message.content


if __name__=='__main__':
    disease = 'alzheimers'
    disease_class = 'Very Mild Dementia'
    # gen_text = Prompt().disease_description(disease, disease_class)
    answer = Prompt().doubt('What are the symptoms of breast cancer')
    print(answer)