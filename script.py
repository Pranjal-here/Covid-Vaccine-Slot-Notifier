    import requests
    import smtplib
    from email.message import EmailMessage
    from datetime import datetime, timedelta
    import time
    import json
    def email_alert(subject,body,to):
        msg=EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to
       
        user="xyz@gmail.com"  #sender email
        msg['from']=user
        password="ujhxvojiordztisq" #sender password please refer readme for password setup
  
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user,password)
        server.send_message(msg)
        
        server.quit()
        print("success")
        return
      
    age = 60
    pinCodes = ["221101"]
    num_days = 3
 
    print_flag = 'Y'
   
  
  
    actual = datetime.today()
    list_format = [actual + timedelta(days=i) for i in range(num_days)]
    actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]
    
    while True:
        counter = 0   
    
        for pinCode in pinCodes:   
            for given_date in actual_dates:
    
                URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pinCode, given_date)
                header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
                
                result = requests.get( URL, headers=header )
                
                if result.ok:
                    response_json = result.json()
    
                    if response_json["centers"]:        
                        if(print_flag.lower() =='y'):
    
                            for center in response_json["centers"]:
                
                                for session in center["sessions"]:
                                
                                    s=" "
                                    if (session["min_age_limit"] <= age and session["available_capacity"] > 0 ) :
                                        s+="Pincode"
                                        s+=str(pinCode)
                                        s+=" Available on: "
                                        s+=str(given_date)
                                        s+=" center: "
                                        s+=str(center["name"])
                                        s+=" ,"
                                        s+=str(center["block_name"])
                                        s+=" Available Slots: "
                                        s+=str(session["available_capacity"])
                                        if(session["vaccine"] != ''):
                                          s+=" Vaccine: "
                                          s+=str(session["vaccine"])
  
    
                                        counter = counter + 1
                                        email_alert("Vaccine SLOTS",s,"abc@gmail.com") #receiver email address
                                    else:
                                        pass                                    
                    else:
                        pass        
                              
                else:
                    print("No Response!")
    
                    
        if(counter == 0):
            email_alert("Vaccine Slot","No Vaccination slot avaliable!","abc@gmail.com")
            break
        else:
            break



#no use of this comment
#testing code reviewer for python
