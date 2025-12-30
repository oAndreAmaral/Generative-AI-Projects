from dotenv import load_dotenv
from crew import stock_crew

load_dotenv()

def run(query:str):
    result = stock_crew.kickoff(inputs={"topic":query})
    print(result)

if __name__ == "__main__":
    
    run("Latest trends in generative AI")