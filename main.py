from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel

# ! TIPE DATA
class ThreatData(BaseModel):
    ThreatID: int
    ThreatName: str
    ThreatType: str
    ThreatSeverity: int
    ThreatDescription: str
    ThreatSource: str

class DataUser(BaseModel):
    UserID: int
    Password : str

class ThreatLog(BaseModel): 
    LogID: int
    ThreatID: int
    SourceID: int
    LogDescription: str

# ! READ FILE
json_filename = "data.json"
with open(json_filename, "r") as read_file: 
    data = json.load(read_file)

# ! FAST API
app = FastAPI()

#! ROUTING ThreatData
# GET: Mendapatkan semua data ThreatData
@app.get("/threatdata")
async def get_threat_data():
    return data['threat_data']

# GET: Mendapatkan data ThreatData berdasarkan ThreatID
@app.get("/threatdata/{threat_id}", response_model=ThreatData)
def read_threatdata(threat_id: int):
    threat_data = data.get("threat_data")
    for threat in threat_data:
        if threat["ThreatID"] == threat_id:
            return threat
    raise HTTPException(status_code=404, detail="ThreatData not found")

# POST: Menambahkan data ThreatData
@app.post("/threatdata")
async def create_threatdata(threat: ThreatData):
    threat_data = data.get("threat_data")
    threat_data.append(threat.dict())
    with open(json_filename, "w") as write_file:
        json.dump(data, write_file, indent=4)
    return threat  

# PUT: Mengupdate data ThreatData berdasarkan ThreatID
@app.put("/threatdata/{threat_id}", response_model=ThreatData)
def update_threatdata(threat_id: int, updated_threat: ThreatData):
    threat_data = data.get("threat_data")
    for i, threat in enumerate(threat_data):
        if threat.get("ThreatID") == threat_id:
            threat_data[i] = updated_threat.dict()
            with open(json_filename, "w") as write_file:
                json.dump(data, write_file, indent=4)
            return updated_threat
    raise HTTPException(status_code=404, detail="ThreatData not found")

# DELETE: Menghapus data ThreatData berdasarkan ThreatID
@app.delete("/threatdata/{threat_id}", response_model=ThreatData)
def delete_threatdata(threat_id: int):
    threat_data = data.get("threat_data")
    for i, threat in enumerate(threat_data):
        if threat.get("ThreatID") == threat_id:
            deleted_threat = threat_data.pop(i)
            with open(json_filename, "w") as write_file:
                json.dump(data, write_file, indent=4)
            return deleted_threat
    raise HTTPException(status_code=404, detail="ThreatData not found")


# GET: Mendapatkan semua data ThreatLog
@app.get("/threatlog/")
def read_all_threatlog():
    return data.get("threat_log")

# GET: Mendapatkan data ThreatLog berdasarkan LogID
@app.get("/threatlog/{log_id}", response_model=ThreatLog)
def read_threatlog(log_id: int):
    threat_log = data.get("threat_log")
    for log in threat_log:
        if log.get("LogID") == log_id:
            return log
    raise HTTPException(status_code=404, detail="ThreatLog not found")

# POST: Menambahkan data ThreatLog
@app.post("/threatlog")
def create_threatlog(log: ThreatLog):
    threat_log = data.get("threat_log")
    log_id = max([log.get("LogID") for log in threat_log]) + 1
    log.LogID = log_id
    threat_log.append(log.dict())
    with open(json_filename, "w") as write_file:
        json.dump(data, write_file, indent=4)
    return log

# PUT: Mengupdate data ThreatLog berdasarkan LogID
@app.put("/threatlog/{log_id}", response_model=ThreatLog)
def update_threatlog(log_id: int, updated_log: ThreatLog):
    threat_log = data.get("threat_log")
    for i, log in enumerate(threat_log):
        if log.get("LogID") == log_id:
            updated_log.LogID = log_id
            threat_log[i] = updated_log.dict()
            with open(json_filename, "w") as write_file:
                json.dump(data, write_file, indent=4)
            return updated_log
    raise HTTPException(status_code=404, detail="ThreatLog not found")

# DELETE: Menghapus data ThreatLog berdasarkan LogID
@app.delete("/threatlog/{log_id}", response_model=ThreatLog)
def delete_threatlog(log_id: int):
    threat_log = data.get("threat_log")
    for i, log in enumerate(threat_log):
        if log.get("LogID") == log_id:
            deleted_log = threat_log.pop(i)
            with open(json_filename, "w") as write_file:
                json.dump(data, write_file, indent=4)
            return deleted_log
    raise HTTPException(status_code=404, detail="ThreatLog not found")


# GET: Mendapatkan semua data DataUser
@app.get("/datauser/")
def read_all_datauser():
    return data.get("data_user")

# GET: Mendapatkan data DataUser berdasarkan UserID
@app.get("/datauser/{user_id}", response_model=DataUser)
def read_datauser(user_id: int):
    data_user = data.get("data_user")
    for user in data_user:
        if user.get("UserID") == user_id:
            return user
    raise HTTPException(status_code=404, detail="DataUser not found")

# POST: Menambahkan data DataUser
@app.post("/datauser")
def create_datauser(user: DataUser):
    data_user = data.get("data_user")
    user_id = max([user.get("UserID") for user in data_user]) + 1
    user.UserID = user_id
    data_user.append(user.dict())
    with open(json_filename, "w") as write_file:
        json.dump(data, write_file, indent=4)
    return user

# PUT: Mengupdate data DataUser berdasarkan UserID
@app.put("/datauser/{user_id}")
def update_datauser(user_id: int, updated_user: DataUser):
    data_user = data.get("data_user")
    for i, user in enumerate(data_user):
        if user.get("UserID") == user_id:
            updated_user.UserID = user_id
            data_user[i] = updated_user.dict()
            with open(json_filename, "w") as write_file:
                json.dump(data, write_file, indent=4)
            return updated_user
    raise HTTPException(status_code=404, detail="DataUser not found")

# DELETE: Menghapus data DataUser berdasarkan UserID
@app.delete("/datauser/{user_id}", response_model=DataUser)
def delete_datauser(user_id: int):
    data_user = data.get("data_user")
    for i, user in enumerate(data_user):
        if user.get("UserID") == user_id:
            deleted_user = data_user.pop(i)
            with open(json_filename, "w") as write_file:
                json.dump(data, write_file, indent=4)
            return deleted_user
    raise HTTPException(status_code=404, detail="DataUser not found")




