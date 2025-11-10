import requests
from tabulate import tabulate
from db_connector import get_connection

API_URL = "http://127.0.0.1:8000/generate-sql"

def exec_query(cxn, query):
    cursor = cxn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def print_rows(rows):

    if not rows:
        print("No results found.")
        return

    print("\n📊 Query Results:")
    print(tabulate(rows, tablefmt="grid"))  

def main():
    tenant_id = input("Enter Tenant ID: ").strip()
    user_query = input("Enter your question: ").strip()

    payload = {"tenant_id": tenant_id, "user_query": user_query}

  
    print("\n🔄 Generating SQL from API...")
    response = requests.post(API_URL, json=payload)

    if response.status_code != 200:
        print("\n❌ Error:", response.status_code, response.text)
        return

    data = response.json()
    generated_sql = data.get("generated_sql")

    print("\n✅ SQL Generated Successfully!")
    print(generated_sql)
  
    # Step 2: Execute SQL and show results
    print("\n🔄 Executing SQL on database...")
    connection = get_connection()

    try:
        rows = exec_query(connection, generated_sql)
        print_rows(rows)
    except Exception as e:
        print("\n❌ Error executing SQL:", str(e))
    finally:
        connection.close()

if __name__ == "__main__":
    main()
