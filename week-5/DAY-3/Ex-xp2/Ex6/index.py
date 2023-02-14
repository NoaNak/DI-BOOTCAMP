from datetime import datetime

def calculate_lifespan_in_minutes(birthdate):
    birthdate_datetime = datetime.strptime(birthdate, "24-08-2002")
    
    time_delta = datetime.now() - birthdate_datetime
    minutes_lived = int(time_delta.total_seconds() // 60)
    
    print (f"You have lived for {minutes_lived} minutes.")

calculate_lifespan_in_minutes("24-08-2002")
