import pandas as pd
import random 
import  os

START_PROMPT = "なつき:1  ちひろ:2   番号を選んでください"
ERROR_PROMPT = "半角数値で入力してください"
print(START_PROMPT)
user_choice = input('>>> ')

try:
    colors = ['R','Y','BL','BK','G','O','P']
    if user_choice == "2":
        colors.append('W')


    df=pd.DataFrame({1:random.choices(colors,k=20)})
    for i in range(2,46):    
        df_add = pd.DataFrame({i:random.choices(colors,k=20)})
        df = pd.concat([df, df_add], axis=1)
        i+=1

except:
   print(ERROR_PROMPT)

output_dir = 'output'
os.makedirs(output_dir, exist_ok=True) 

output_file = 'onkan.xlsx'
df.to_excel(os.path.join(output_dir, output_file),index=False, header= None)