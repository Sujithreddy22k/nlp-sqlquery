# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sql_generator import generate_sql_with_table_selection_azure

app = FastAPI(title="SQL Generator API")

class QueryRequest(BaseModel):
    tenant_id: str
    user_query: str

@app.post("/generate-sql")
def generate_sql(request: QueryRequest):
    tenant_id = request.tenant_id.strip()
    user_query = request.user_query.strip()

    try:
        sql_query = generate_sql_with_table_selection_azure(user_query, tenant_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"SQL Generation Error: {str(e)}")

    return {
        "tenant_id": tenant_id,
        "generated_sql": sql_query
    }
