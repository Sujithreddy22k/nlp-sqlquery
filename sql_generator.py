# sql_generator.py
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from schema import SCHEMA_TEXT

load_dotenv()

def generate_sql_with_table_selection_azure(user_query: str, tenant_id: str):
    """
    Generates tenant-filtered SQL using GPT and ESS schema.
    Ensures TEN_ID = {tenant_id} is always present.
    """

    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")

    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version=api_version
    )

    prompt = f"""
You are an expert in T-SQL for the Employee Self-Service (ESS) System.
You will generate a single valid SQL query based on the schema below.
Make sure to include TEN_ID = {tenant_id} in the WHERE clause for every query.

Rules:
- Do NOT use markdown, explanation, or comments.
- Only return the SQL statement.
- If the question doesn’t require filtering, still ensure TEN_ID = {tenant_id} is used.
- Provide the query in one line.
- Make note of the ID columns in each table for joins. For eg, the Employee ID column in ESS_EMPLOYEES table is just ID, and not
EMP_ID. Likewise, Tenant ID column in ESS_TENANT table is ID, and not TEN_ID. Ensure correct column names are used for joins.

SCHEMA:
{SCHEMA_TEXT}

USER QUESTION:
{user_query}

Ensure results are only for TEN_ID = {tenant_id}.
"""

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
        temperature=0,
        top_p=1.0,
        model=deployment
    )

    sql_query = response.choices[0].message.content.strip()

    return sql_query
