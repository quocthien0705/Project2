import pandas as pd

df = pd.read_excel(r'C:\Users\ADMIN\Downloads\merge20212023\merge20212023.xlsx')
df = df.dropna(subset=['Emails'])

# Tạo một hàm kiểm tra xem một list email có chứa ít nhất một email không chứa @vn, @cp hoặc @jp hay không
def check_emails(email_list):
    for email in email_list:
        if not(('@vn' in email) or ('@cp' in email) or ('@jp' in email) or ('@bcn' in email)):
            return True
    return False

# Tách các email và áp dụng hàm kiểm tra
emails = df['Emails'].str.split('\n')
df = df[emails.apply(check_emails)]
df.to_excel(r'C:\Users\ADMIN\Downloads\merge20212023\merge20212023_new.xlsx',index= False)