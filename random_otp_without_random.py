from datetime import datetime


def generate_otp(digits=4):
    
    if digits > 10 or digits != round(digits):
        return 'Enter valid number under 11'
    
    values = [2,1,3,0,4,9,8,6,5,7]
    otp = ""
    
    current_time = datetime.now()
    current_second = round(current_time.second)
    
    for i in range(digits):
        otp += str( (current_second + values[i]) % 10 ) 
    return int(otp)


def generate_unique_otp(digits=4):
    
    if digits > 10 or digits != round(digits):
        return 'Enter valid number under 11'

    otp = ""
    
    current_time = datetime.now()
    current_second = round(current_time.second)
    
    for i in range(digits):
        otp += str((i + current_second) % 10)
        
    return int(otp)
    
    
print(generate_otp(4))
print(generate_unique_otp(4))
    